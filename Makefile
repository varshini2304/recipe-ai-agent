.PHONY: setup ingest test test-all run-api run-web eval
setup:
	python -m pip install -e ".[dev]"
ingest:
	python scripts/ingest.py
test:
	python -m pytest -m "not slow"
test-all:
	python -m pytest -m "slow or not slow"
run-api:
	python -m recipelens.api
run-web:
	python -m recipelens.web
eval:
	python scripts/inspect_data.py
