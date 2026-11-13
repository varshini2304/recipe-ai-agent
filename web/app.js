"use strict";
const $ = (s) => document.querySelector(s);
const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const nf = (n) => Number(n).toLocaleString();
let sid = null, lastTrace = null, busy = false;
try { sid = localStorage.getItem("rl_sid"); } catch (_) {}

const SUGGESTIONS = [
  "penne pasta",
  "I have eggs, onions, tomatoes, rice, no peanuts, at most 6 steps",
  "How many recipes have garlic AND onion?",
  "Show me tomato recipes with fewest steps",
  "What are the most common ingredients?",
];

async function api(path, body) {
  const opt = body ? { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) } : {};
  const r = await fetch(path, opt);
  if (!r.ok) throw new Error((await r.json().catch(() => ({}))).detail || r.statusText);
  return r.json();
}

/* ---------- markdown-lite (escape first, then format) ---------- */
function md(text) {
  const lines = esc(text).split("\n").map((l) => {
    l = l.replace(/^###\s+(.*)$/, "<h4>$1</h4>");
    l = l.replace(/\*\*(.+?)\*\*/g, "<b>$1</b>").replace(/`([^`]+)`/g, "<code>$1</code>");
    return l;
  });
  return lines.join("\n");
}

/* ---------- chat ---------- */
function addMsg(role, html) {
  const d = document.createElement("div");
  d.className = "msg " + role;
  d.innerHTML = html;
  $("#log").appendChild(d);
  $("#log").scrollTop = 1e9;
  return d;
}

function summaryLine(p) {
  if (!p) return "";
  if (p.kind === "search") return `Found ${p.items.length} recipes.`;
  if (p.kind === "match") return p.status === "no_eligible_match"
    ? "No recipe satisfies every hard constraint." : `${p.results.length} recipes satisfy your constraints.`;
  if (p.kind === "analytics") return "Computed from the database — see the panel for the formula and denominators.";
  if (p.kind === "substitution") return `Evidence grade: ${p.report.evidence_grade}.`;
  return "";
}

function botBubble(res) {
  const g = res.verification;
  const badge = g.grounded
    ? '<span class="badge ok" title="Every recipe ID and number in this answer was matched to tool output">✓ grounded</span>'
    : `<span class="badge bad" title="${esc((g.ungrounded_ids.concat(g.ungrounded_numbers)).join(", "))}">⚠ ungrounded</span>`;
  const sum = summaryLine(res.payload);
  const long = sum && res.answer.length > 240;
  const body = long
    ? `${esc(sum)}<details><summary>Full text answer</summary>${md(res.answer)}</details>`
    : md(res.answer);
  const tag = res.payload && res.payload.kind === "unsupported" ? '<span class="badge warn">refused</span>' : "";
  return `${body}<span class="src">${badge}${tag}<span class="badge">${esc(res.intent)}</span></span>`;
}

async function send(text) {
  if (busy || !text.trim()) return;
  busy = true; $("#send").disabled = true;
  addMsg("user", esc(text));
  const t = addMsg("bot", '<span class="typing">thinking…</span>');
  try {
    const res = await api("/api/chat", { message: text, session_id: sid });
    t.innerHTML = botBubble(res);
    onResult(res);
  } catch (e) {
    t.innerHTML = `<span class="badge bad">error</span> ${esc(e.message)}`;
  } finally { busy = false; $("#send").disabled = false; $("#input").focus(); }
}

function onResult(res) {
  sid = res.session_id;
  try { localStorage.setItem("rl_sid", sid); } catch (_) {}
  lastTrace = res.trace ? { ...res.trace, verification: res.verification, state: res.state } : lastTrace;
  renderChips(res.state);
  if (res.payload) renderPanel(res.payload);
  $("#suggest").style.display = "none";
}

/* ---------- constraint chips ---------- */
const CHIP_LABEL = { query: "query", include: "include", exclude: "exclude", group: "excluded", max_steps: "limit", pantry: "pantry" };
function renderChips(state) {
  const box = $("#chips"); box.innerHTML = "";
  for (const c of state.chip_items || []) {
    const el = document.createElement("span");
    el.className = "chip " + (["group", "exclude", "max_steps"].includes(c.kind) ? "hard" : c.kind === "pantry" ? "pantry" : "");
    el.innerHTML = `<b>${CHIP_LABEL[c.kind] || c.kind}</b>${esc(c.label)}<button title="Remove" aria-label="Remove ${esc(c.label)}">✕</button>`;
    el.querySelector("button").onclick = () => removeChip(c);
    box.appendChild(el);
  }
}
async function removeChip(c) {
  try {
    const res = await api("/api/chip/remove", { session_id: sid, kind: c.kind, value: c.value });
    renderChips(res.state);
    if (res.answer) { addMsg("bot", `Removed <b>${esc(c.label)}</b> and re-ran the query.`); onResult(res); }
  } catch (e) { addMsg("bot", `<span class="badge bad">error</span> ${esc(e.message)}`); }
}

/* ---------- result panel ---------- */
function renderPanel(p) {
  const el = $("#panel");
  const fn = { search: viewSearch, match: viewMatch, analytics: viewAnalytics, substitution: viewSub, recipe_detail: viewDetail }[p.kind];
  if (!fn) return;
  el.innerHTML = fn(p);
  el.scrollTop = 0;
  el.querySelectorAll("[data-recipe]").forEach((b) => (b.onclick = () => openRecipe(b.dataset.recipe)));
}

function bars(breakdown) {
  return Object.entries(breakdown || {}).map(([k, v]) => {
    const w = Math.max(0, Math.min(100, Math.abs(Number(v)) * 100));
    return `<div class="bar"><span style="width:96px">${esc(k)}</span><span class="track"><i style="width:${w}%"></i></span><span>${Number(v).toFixed(3)}</span></div>`;
  }).join("");
}

function viewSearch(p) {
  if (!p.items.length) return '<div class="empty"><h2>No matches</h2><p>Nothing satisfied the query together with every active constraint.</p></div>';
  return `<h3>Search results</h3><div class="sub">Hybrid retrieval (keyword + semantic), hard constraints applied before ranking.</div>` +
    p.items.map((r) => `<div class="card"><div class="row"><span><span class="rank">${r.rank}</span><button class="title" data-recipe="${esc(r.recipe_id)}">${esc(r.title)}</button></span><span class="id">${esc(r.recipe_id)}</span></div>
    ${r.matched_terms.length ? `<div class="pills">${r.matched_terms.map((t) => `<span class="pill have">${esc(t)}</span>`).join("")}</div>` : ""}
    <details><summary class="sub">Why this ranked here</summary>${bars(r.score_breakdown)}</details></div>`).join("");
}

function viewMatch(p) {
  const head = `<h3>Pantry matches</h3><div class="sub">${nf(p.candidates_scored)} candidates scored of ${nf(p.candidates_total)}${p.truncated ? " (candidate cap applied)" : ""}. Hard constraints are never relaxed.</div>`;
  const notes = (p.notes || []).map((n) => `<div class="note">${esc(n)}</div>`).join("");
  const card = (m, alt) => `<div class="card"><div class="row"><span><span class="rank">${alt ? "—" : m.rank}</span><button class="title" data-recipe="${esc(m.recipe_id)}">${esc(m.title)}</button></span><span class="id">score ${Number(m.score).toFixed(2)}</span></div>
    <div class="pills">${m.matched.map((x) => `<span class="pill have" title="${esc((x.recipe_lines || []).join(" | "))}${x.quantity_note ? " — " + esc(x.quantity_note) : ""}">✓ ${esc(x.pantry_name)}${x.quantity_check === "insufficient" ? " (not enough)" : ""}</span>`).join("")}${m.missing.map((x) => `<span class="pill miss">✗ ${esc(x)}</span>`).join("")}${m.assumed_staples.map((x) => `<span class="pill stp">assumed ${esc(x)}</span>`).join("")}</div>
    <div class="sub">${esc(m.why)}</div><div class="sub">${m.step_count} steps · ${m.ingredient_count} ingredients${m.instructions_low_confidence ? " · ⚠ instructions low-confidence" : ""}${(m.unused_pantry || []).length ? " · unused: " + esc(m.unused_pantry.join(", ")) : ""}</div>
    ${alt && m.violations ? `<div class="warnbox">${m.violations.map((v) => `<div><b>${esc(v.kind.replace(/_/g, " "))}</b>: ${esc(v.detail)}</div>`).join("")}</div>` : ""}
    <details><summary class="sub">Score breakdown</summary>${bars(m.score_breakdown)}</details></div>`;
  if (p.status === "no_eligible_match") {
    return head + `<div class="warnbox"><b>No recipe satisfies every hard constraint.</b> I will not quietly relax them. The nearest recipes that break a constraint are shown below, clearly marked.</div>` +
      notes + (p.violating_alternatives || []).map((m) => card(m, true)).join("");
  }
  return head + notes + p.results.map((m) => card(m, false)).join("");
}

function chart(rows, labelKey, valueKey, fmt) {
  const max = Math.max(...rows.map((r) => r[valueKey]), 1), h = 26, w = 520, lw = 150;
  const svg = rows.map((r, i) => {
    const bw = ((w - lw - 70) * r[valueKey]) / max;
    return `<g transform="translate(0,${i * h})"><text x="0" y="17">${esc(String(r[labelKey]).slice(0, 22))}</text><rect class="bg" x="${lw}" y="5" width="${w - lw - 70}" height="14" rx="4"/><rect class="fg" x="${lw}" y="5" width="${bw}" height="14" rx="4"/><text x="${lw + (w - lw - 70) + 6}" y="17">${esc(fmt(r))}</text></g>`;
  }).join("");
  return `<svg class="chart" viewBox="0 0 ${w} ${rows.length * h}" width="100%" role="img" aria-label="Bar chart">${svg}</svg>`;
}

function viewAnalytics(p) {
  const r0 = p.rows[0] || {};
  let main = "";
  if ("count" in r0 && "percentage" in r0 && !("canonical" in r0)) {
    main = `<div class="kpi">${nf(r0.count)}</div><div class="sub">recipes match — ${Number(r0.percentage).toFixed(2)}% of usable-ingredient recipes${r0.percentage_all_recipes != null ? `, ${Number(r0.percentage_all_recipes).toFixed(2)}% of all recipes` : ""}</div>`;
  } else if ("canonical" in r0) {
    main = chart(p.rows, "canonical", "count", (r) => `${nf(r.count)} (${Number(r.percentage).toFixed(1)}%)`);
  } else if ("mean" in r0) {
    main = `<dl class="kv"><dt>Mean</dt><dd>${Number(r0.mean).toFixed(2)}</dd><dt>Median</dt><dd>${r0.median}</dd><dt>Range</dt><dd>${r0.min} – ${r0.max}</dd></dl>`;
  } else if ("metric_value" in r0 || "step_count" in r0) {
    main = `<table><tr><th>#</th><th>Recipe</th><th class="n">${esc(p.metric)}</th><th class="n">Ingredients</th></tr>${p.rows.map((r, i) => `<tr><td>${i + 1}</td><td><button class="title" data-recipe="${esc(r.recipe_id)}">${esc(r.title)}</button></td><td class="n">${r.metric_value}</td><td class="n">${r.ingredient_count}</td></tr>`).join("")}</table>` +
      (p.cutoff_tie_count > 1 ? `<div class="note">${p.cutoff_tie_count} recipes are tied at the cutoff value.</div>` : "");
  }
  return `<h3>Analytics</h3>${main}
    <dl class="kv"><dt>Analyzed</dt><dd>${nf(p.n_analyzed)} recipes</dd><dt>Denominator</dt><dd>${esc(p.denominator_label)}</dd>${p.secondary_denominator_label ? `<dt>Secondary</dt><dd>${esc(p.secondary_denominator_label)}</dd>` : ""}<dt>Formula</dt><dd><code>${esc(p.formula)}</code></dd></dl>
    <details><summary class="sub">Normalization notes</summary><div class="note">${esc(p.normalization_notes)}</div></details>`;
}

function viewSub(p) {
  const r = p.report;
  const cands = r.candidates.length
    ? `<table><tr><th>Candidate</th><th class="n">With ${esc(r.remove)}</th><th class="n">Without</th><th class="n">Lift</th><th>Evidence</th></tr>${r.candidates.map((c) => `<tr><td>${esc(c.canonical)}</td><td class="n">${(c.with_rate * 100).toFixed(0)}%</td><td class="n">${(c.without_rate * 100).toFixed(0)}%</td><td class="n">${Number(c.lift).toFixed(1)}×</td><td><span class="grade ${esc(c.evidence_grade)}">${esc(c.evidence_grade)}</span></td></tr>`).join("")}</table>`
    : '<div class="note">No ingredient appears more often in peer recipes without it — no substitution is claimed.</div>';
  const changed = new Set((p.changes || []).filter((c) => c.original_line).map((c) => c.original_line));
  const li = (arr, mark) => arr.map((x) => `<li class="${mark && changed.has(x) ? "chg" : ""}">${esc(x)}</li>`).join("");
  return `<h3>Substitution — ${esc(r.target_title)}</h3>
    <div class="sub">Remove <b>${esc(r.remove)}</b>${r.remove_group ? ` (group: ${esc(r.remove_group)})` : ""} · overall evidence <span class="grade ${esc(r.evidence_grade)}">${esc(r.evidence_grade)}</span> · ${r.n_peers} peer recipes (${r.with_x_count} with / ${r.without_x_count} without) · ${esc(r.retrieval_mode)}</div>
    ${cands}
    <div class="diff"><div><b>Original</b><ul>${li(p.original_ingredients, true)}</ul></div><div><b>Adapted</b><ul>${li(p.updated_ingredients, false)}</ul></div></div>
    ${(p.predicted_effects || []).length ? `<div class="note"><b>Predicted effects</b> (rule-based, not from the dataset):<ul>${p.predicted_effects.map((x) => `<li>${esc(x)}</li>`).join("")}</ul></div>` : ""}
    ${(p.uncertainty || []).length ? `<div class="warnbox"><b>Uncertainty</b><ul>${p.uncertainty.map((x) => `<li>${esc(x)}</li>`).join("")}</ul></div>` : ""}
    <details><summary class="sub">Revised instructions</summary><pre>${esc(p.revised_instructions)}</pre></details>
    <div class="note">${esc(p.disclaimer)}</div>
    <details><summary class="sub">Formula & thresholds</summary><div class="note"><code>${esc(r.formula)}</code></div></details>`;
}

function viewDetail(p) { return recipeHtml(p.recipe); }
function recipeHtml(r) {
  return `<h3>${esc(r.title)}</h3><div class="sub"><span class="id">${esc(r.recipe_id)}</span> · ${r.step_count} steps · ${r.ingredient_count} ingredients${r.instructions_low_confidence ? " · ⚠ instruction splitting low-confidence" : ""}</div>
    <b>Ingredients</b><ul>${r.ingredients.map((x) => `<li>${esc(x)}</li>`).join("")}</ul><b>Instructions</b><pre>${esc(r.instructions)}</pre>`;
}
async function openRecipe(id) {
  try {
    const r = await api("/api/recipe?id=" + encodeURIComponent(id) + (sid ? "&session_id=" + sid : ""));
    $("#modalBody").innerHTML = recipeHtml(r); $("#modal").showModal();
  } catch (e) { addMsg("bot", `<span class="badge bad">error</span> ${esc(e.message)}`); }
}

/* ---------- header stats, trace, reset ---------- */
async function loadStats() {
  try {
    const s = await api("/api/stats");
    const c = s.counts, bits = [`${nf(c.all_recipes)} recipes`, `${nf(c.usable_ingredients)} with ingredients`];
    if (s.index_coverage && s.index_coverage.searchable) bits.push(`semantic index ${nf(s.index_coverage.indexed)}/${nf(s.index_coverage.searchable)}`);
    $("#stats").innerHTML = bits.map((b) => `<span>${esc(b)}</span>`).join("");
  } catch (_) { $("#stats").innerHTML = '<span>backend not reachable</span>'; }
}
$("#traceBtn").onclick = () => {
  $("#traceBody").innerHTML = lastTrace
    ? `<h3>How the last answer was produced</h3><pre>${esc(JSON.stringify(lastTrace, null, 2))}</pre>`
    : "<p>Send a message first.</p>";
  $("#trace").showModal();
};
$("#resetBtn").onclick = async () => {
  if (sid) await api("/api/reset", { session_id: sid }).catch(() => {});
  $("#log").innerHTML = ""; $("#chips").innerHTML = ""; $("#suggest").style.display = "";
  $("#panel").innerHTML = '<div class="empty"><h2>Results appear here</h2></div>'; lastTrace = null; greet();
};
$("#form").onsubmit = (e) => { e.preventDefault(); const v = $("#input").value; $("#input").value = ""; send(v); };

function greet() {
  addMsg("bot", "Hi! Search recipes, tell me your pantry and limits, ask exact dataset questions, or ask me to adapt a recipe. Add constraints in follow-ups — they stack and never get dropped silently.");
  const box = $("#suggest"); box.innerHTML = "";
  SUGGESTIONS.forEach((s) => { const b = document.createElement("button"); b.textContent = s; b.onclick = () => send(s); box.appendChild(b); });
}
greet(); loadStats();
