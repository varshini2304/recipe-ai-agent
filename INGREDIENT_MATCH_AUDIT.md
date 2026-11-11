# Ingredient match audit

Canonical counts use `ingredient_lines`; raw regex counts search the JSON-decoded original `ingredients_raw` lines directly.
Primary denominator: recipes with usable ingredients. Secondary denominator: all recipe rows.

| Term | Exact canonical | Canonical token family | Raw-text regex (usable) | Gap: raw minus exact | Raw-text regex (all recipes) |
|---|---:|---:|---:|---:|---:|
| tomato | 1,205 | 19,278 | 19,391 | +18,186 | 19,391 |
| garlic | 13,475 | 37,327 | 37,344 | +23,869 | 37,344 |
| onion | 5,309 | 37,961 | 36,905 | +31,596 | 36,905 |

## Garlic AND onion

Exact canonical AND: **1,731** recipes; raw regex AND among usable-ingredient recipes: **20,245**; gap: **+18,514**.
Raw regex AND among all recipes: **20,245**. Usable denominator: **122,971**; all-recipes denominator: **125,164**.
## Reviewed family rules: canonical results vs raw-line regex

Rules come from owner-approved `config/families.yaml`.
| Term | Canonical family recipes | Raw-line regex recipes | Canonical minus raw |
|---|---:|---:|---:|
| tomato | 13,656 | 12,011 | +1,645 |
| garlic | 32,434 | 30,357 | +2,077 |
| onion | 34,980 | 30,311 | +4,669 |

Family garlic AND onion: canonical **17,190**; raw-line regex **14,821**.

## Every canonical variant containing the token

### tomato

| Canonical value | Recipes |
|---|---:|
| "-slices tomato | 1 |
| #10 can tomato sauce* | 1 |
| (6-ounce can tomato paste | 1 |
| (7.75 oz.) dole® extra veggie™ with grape tomato | 2 |
| * can tomato sauce | 1 |
| ***tomatillos are often referred to as "green tomatoes," but are members of the gooseberry family. to prepare tomatillos for the salsa, remove their papery husks and rinse away their sticky outer coating. or, canned whole tomatillos are available under the san marcos brand | 1 |
| **a green tomato-like vegetable with a paper-thin husk. available at latin american markets and some supermarkets | 1 |
| **tomatillos are often referred to as "green tomatoes," but are members of the gooseberry family. to prepare tomatillos for the salsa, remove their papery husks and rinse away their sticky outer coating. or, canned whole tomatillos are available under the san marcos brand | 1 |
| *a green tomato-like vegetable with a paper-thin husk. available at latin american markets and some supermarkets | 1 |
| *dried, smoked jalapeos canned in a spicy tomato sauce called adobo; sold at some supermarkets and at specialty foods stores and latin markets | 1 |
| *note: if you use dehydrated tomatoes ? add a little water to them and allow them to rehydrate slightly | 1 |
| *tiny pickled green tomatoes; available at specialty foods stores and online from oldsouth.com and igourmet | 1 |
| - 28 oz cans chopped plum tomatoes, no salt added | 1 |
| - ounce sun-dried tomato | 1 |
| - to 16-ounce can whole tomatoes, including juice | 1 |
| - to 32-ounce can whole tomatoes, drained, seeded, and chopped | 1 |
| -1/2 oz tomato | 1 |
| -1/2 pounds vine ripened tomato | 2 |
| -1/2 pounds vine-ripened tomatoes, cored | 3 |
| -1/4 lb fresh, ripe roma tomatoes, or 2 c. crushed tomato | 1 |
| -10 cherry tomatoes, halved | 1 |
| -10 plum tomato | 1 |
| -15 beefsteak tomato | 1 |
| -20 mixed, large, ripe tomatoes (beef, roma, vine, etc.) | 1 |
| -24 ounce can tomato sauce | 1 |
| -28 ounce cans whole peeled italian plum tomato | 1 |
| -28-ounce can italian-style tomatoes with juices | 1 |
| -3 large heirloom tomato | 1 |
| -3 plum tomato | 1 |
| -3 plum tomatoes, thinly sliced | 1 |
| -4 roma tomatoes cut into cubes | 1 |
| -8 oz. chilled tomato soup | 1 |
| -cup fresh diced tomato | 1 |
| -cup smoked tomato vinaigrette | 1 |
| -inch-thick heirloom tomato slices (from 2 very large tomatoes) | 1 |
| -inch-thick slices from large red or orange heirloom tomato | 1 |
| -ounce box strained tomatoes (recommended: pomi) | 1 |
| -ounce can (or 2 cups) canned plum tomato | 1 |
| -ounce can chopped tomato | 1 |
| -ounce can crushed tomato | 1 |
| -ounce can crushed tomatoes (about 2 cups) | 1 |
| -ounce can crushed tomatoes, with juices | 1 |
| -ounce can diced tomato | 2 |
| -ounce can diced tomatoes in juice | 1 |
| -ounce can diced tomatoes with green chiles | 2 |
| -ounce can italian plum tomatoes including the juice | 1 |
| -ounce can italian plum tomatoes, crushed by hand | 1 |
| -ounce can italian plum tomatoes, drained in a colander | 1 |
| -ounce can italian plum tomatoes, seeds removed | 1 |
| -ounce can italian plum tomatoes, undrained | 1 |
| -ounce can of roma tomatoes, drained | 1 |
| -ounce can plum tomatoes including the juice | 2 |
| -ounce can plum tomatoes, drained and chopped | 1 |
| -ounce can plum tomatoes, drained and coarsely chopped | 1 |
| -ounce can pureed tomato | 1 |
| -ounce can tomato paste | 1 |
| -ounce can whole napoli tomatoes, strained and roughly chopped | 1 |
| -ounce can whole peeled tomato | 1 |
| -ounce can whole san marzano tomatoes, crushed by hand | 1 |
| -ounce can whole tomato | 2 |
| -ounce cans diced tomatoes in juice | 1 |
| -ounce chopped tomato | 1 |
| -ounce diced tomato | 1 |
| -ounce jar of tomato sauce | 1 |
| -ounce minced roasted tomato | 1 |
| -ounce sun-dried tomato | 1 |
| -ounce tomato | 2 |
| -ounce tomato concasse | 1 |
| -ounce tomato paste | 1 |
| -ounces water (fill the crushed tomato can 1 1/2 times) | 1 |
| -oz can crushed tomato | 1 |
| -oz. jar sun-dried tomato halves, drained and cut in 1/4" slices | 1 |
| -pint cherry tomatoes, cut in half | 1 |
| -pint containers small red and/or yellow cherry tomato | 1 |
| -pints red and/or yellow cherry tomatoes, cut in half | 1 |
| -pound can tomato | 1 |
| -pound can tomatoes, drained well and chopped | 1 |
| / 2 cup chopped drained oil-packed sun-dried tomatoes (2 tablespoons oil reserved) | 1 |
| /1.8 kg tomato | 1 |
| /125 ml tomato ketchup | 1 |
| /14 oz canned chopped tomato | 1 |
| /2 cup crushed tomato | 1 |
| /200 g red cherry tomatoes, cut into 1/4-inch/5-mm dice | 1 |
| /200 g ripe cherry tomato | 1 |
| /200 g tiger or plum tomatoes, cut into 1/4-inch/5-mm dice | 1 |
| /200 g yellow cherry tomatoes, cut into 1/4-inch/5-mm dice | 1 |
| /250 ml sun-dried tomato | 2 |
| /28 g chopped sun-dried tomatoes in olive oil (oil reserved for later use) | 1 |
| /28 g tomato paste | 1 |
| /30 ml reserved sun-dried tomato oil (or extra-virgin olive oil) | 1 |
| /300 g tomato puree | 1 |
| /400 g cherry tomato | 1 |
| /45 ml tomato paste | 1 |
| /500 g medium slicing tomatoes (about 5), cut into 1/4-inch/5-mm dice | 1 |
| /500 g tomatoes, seeded and quartered or chopped | 1 |
| /500 ml plum tomato | 1 |
| /500g cherry tomato | 1 |
| /500ml canned tomato | 1 |
| /500ml cherry tomato | 1 |
| /700 g tomato puree | 1 |
| /about 800 g tomato puree | 1 |
| 1 /2 to 2 cups tomato | 1 |
| 1-inch cubed red heirloom tomato | 1 |
| 1-pint basket cherry or teardrop tomatoes, halved | 1 |
| 1-pint basket cherry tomatoes, halved | 2 |
| 1-pint baskets cherry tomato | 1 |
| 1-pint container cherry tomato | 1 |
| 1-pint container grape tomato | 1 |
| 1-pint container multicolored baby heirloom tomatoes, halved (2 1/2 cups) | 1 |
| 1-pound (450 grams) can peeled tomatoes, drained | 1 |
| 1-pound container baby heirloom tomatoes or cherry tomato | 1 |
| 1//2 cups tomato puree | 1 |
| 1/2-inch diced tomato | 1 |
| 1/4 inch dice tomato | 1 |
| 1/4-inch diced tomato | 1 |
| 10 1/2- or 11-ounce can condensed tomato soup | 1 |
| 10 3/4-ounce can tomato soup | 1 |
| 10- to 12-ounce container grape tomato | 1 |
| 10-ounce can diced tomatoes and green chiles | 2 |
| 10-ounce can mexican-style diced tomatoes with green chiles | 1 |
| 10-ounce cans diced tomatoes and green chiles | 1 |
| 10-ounce cans diced tomatoes with green chiles | 1 |
| 10-ounce cans fire-roasted diced tomatoes with green chiles (1 3/4 cups) | 1 |
| 10-ounce container grape tomato | 1 |
| 10-ounce container yellow and/or red cocktail tomatoes, quartered | 1 |
| 10-ounce package grape tomato | 1 |
| 10-ounce package grape tomatoes, halved lengthwise | 1 |
| 10oz/280g jar of sun-dried tomatoes, drained and finely chopped | 1 |
| 12 1/2-ounce container refrigerated fire-roasted tomato salsa | 1 |
| 12 ounce tomato | 1 |
| 12-ounce bag cherry tomatoes, halved (2 cups) | 1 |
| 12-ounce bag cherry tomatoes, stemmed | 1 |
| 12-ounce bags cherry tomato | 2 |
| 12-ounce bags or baskets cherry tomatoes, stemmed | 1 |
| 12-ounce baskets cherry tomatoes, stemmed, halved | 1 |
| 12-ounce bottle tomato-based chili sauce (such as heinz) | 1 |
| 12-ounce can diced tomato | 1 |
| 12-ounce can tomato paste | 1 |
| 12-ounce can tomato sauce | 1 |
| 12-ounce can whole peeled tomato | 1 |
| 12-ounce cans tomato sauce | 1 |
| 12-ounce container cherry tomato | 2 |
| 12-ounce container cherry tomatoes or grape tomato | 1 |
| 12-ounce container cherry tomatoes, halved | 1 |
| 12-ounce container cherry tomatoes, halved or quartered if large | 1 |
| 12-ounce container grape or cherry tomatoes, quartered lengthwise | 1 |
| 12-ounce container grape tomato | 2 |
| 12-ounce container grape tomatoes or cherry tomatoes, halved | 1 |
| 12-ounce container grape tomatoes, halved | 1 |
| 12-ounce container yellow and red cherry tomatoes, halved | 1 |
| 12-ounce containers cherry tomato | 1 |
| 12-ounce containers cherry tomatoes (about 4 1/2 cups) | 1 |
| 12-ounce containers grape tomato | 1 |
| 12-ounce package cherry tomato | 1 |
| 12-ounce package grape tomato | 1 |
| 12-ounce packages cherry tomato | 1 |
| 12ounce can plum tomatoes with juices | 1 |
| 14 -ounce can diced tomatoes with chiles | 1 |
| 14 -ounce can peeled tomatoes, halved | 1 |
| 14 .5-ounce can diced tomatoes, drained | 1 |
| 14 1/2 ounce can diced tomato | 1 |
| 14 1/2 ounce cans whole tomato | 1 |
| 14 1/2- to 16-ounce can diced peeled tomato | 1 |
| 14 1/2- to 16-ounce can diced tomatoes in juice | 1 |
| 14 1/2- to 16-ounce can diced tomatoes with liquid | 1 |
| 14 1/2-ounce can (1 3/4 cups) crushed tomatoes with added puree | 1 |
| 14 1/2-ounce can chopped seeded peeled tomatoes with juices | 1 |
| 14 1/2-ounce can diced peeled tomatoes in juice | 1 |
| 14 1/2-ounce can diced peeled tomatoes with juices | 1 |
| 14 1/2-ounce can diced ready-cut tomato | 1 |
| 14 1/2-ounce can diced tomatoes in juice | 24 |
| 14 1/2-ounce can diced tomatoes in juice (preferably fire-roasted) | 2 |
| 14 1/2-ounce can diced tomatoes in juice with italian herbs | 1 |
| 14 1/2-ounce can diced tomatoes in juice, drained | 2 |
| 14 1/2-ounce can diced tomatoes in puree | 1 |
| 14 1/2-ounce can diced tomatoes with balsamic vinegar, basil, and olive oil | 1 |
| 14 1/2-ounce can diced tomatoes with green pepper and onion | 1 |
| 14 1/2-ounce can diced tomatoes with italian seasonings in juice | 1 |
| 14 1/2-ounce can diced tomatoes with italian seasonings, drained | 1 |
| 14 1/2-ounce can diced tomatoes with juice | 1 |
| 14 1/2-ounce can diced tomatoes with mild green chilies, undrained | 1 |
| 14 1/2-ounce can diced tomatoes with roasted garlic | 1 |
| 14 1/2-ounce can diced tomatoes with roasted garlic in juice | 1 |
| 14 1/2-ounce can diced tomatoes, drained | 4 |
| 14 1/2-ounce can italian plum tomatoes, drained | 1 |
| 14 1/2-ounce can italian stewed tomato | 1 |
| 14 1/2-ounce can italian-style stewed tomato | 3 |
| 14 1/2-ounce can mexican recipe stewed tomatoes with juices | 1 |
| 14 1/2-ounce can mexican-style or regular stewed tomato | 1 |
| 14 1/2-ounce can mexican-style stewed tomato | 3 |
| 14 1/2-ounce can peeled tomatoes (undrained) | 1 |
| 14 1/2-ounce can petite diced tomatoes in juice | 2 |
| 14 1/2-ounce can ready-cut peeled tomato | 1 |
| 14 1/2-ounce can seasoned pasta-style tomatoes, well drained | 1 |
| 14 1/2-ounce can stewed tomato | 2 |
| 14 1/2-ounce can tomatoes, drained | 1 |
| 14 1/2-ounce can whole peeled tomatoes in juice, puréed in blender with juices | 1 |
| 14 1/2-ounce can whole tomatoes, drained (juices reserved) | 1 |
| 14 1/2-ounce cans diced peeled tomatoes in juice | 1 |
| 14 1/2-ounce cans diced tomatoes in juice | 5 |
| 14 1/2-ounce cans diced tomatoes in juice with garlic, oregano, and basil | 1 |
| 14 1/2-ounce cans diced tomatoes in juice, drained | 1 |
| 14 1/2-ounce cans diced tomatoes with balsamic vinegar, basil, and olive oil in juice | 1 |
| 14 1/2-ounce cans diced tomatoes with caramelized onion, in juice | 1 |
| 14 1/2-ounce cans diced tomatoes with garlic, basil, and oregano in juice | 1 |
| 14 1/2-ounce cans diced tomatoes with green pepper and garlic or italian-recipe tomato | 1 |
| 14 1/2-ounce cans diced tomatoes with roasted garlic | 1 |
| 14 1/2-ounce cans fire-roasted tomatoes in juice | 1 |
| 14 1/2-ounce cans italian-style diced tomato | 1 |
| 14 1/2-ounce cans mexican-style stewed tomato | 3 |
| 14 1/2-ounce cans petite diced tomatoes in juice | 2 |
| 14 1/2-ounce cans stewed tomato | 2 |
| 14 1/2-to 16-ounce can diced tomato | 1 |
| 14 1/2–ounce can diced tomatoes in juice | 1 |
| 14 1/4-ounce can diced tomato | 1 |
| 14 ounce can whole peeled tomato | 1 |
| 14 oz, san marzano tomato | 1 |
| 14- to 14 1/2-ounce can ready-for-pasta chunky tomato | 1 |
| 14- to 15-ounce can diced tomatoes in juice | 1 |
| 14- to 16-ounce can diced organic tomatoes in juice | 1 |
| 14- to 16-ounce can tomatoes including the juice | 1 |
| 14- to 16-ounce cans stewed tomato | 1 |
| 14-ounce can cherry tomato | 1 |
| 14-ounce can cherry tomatoes kosher salt | 1 |
| 14-ounce can crushed tomato | 4 |
| 14-ounce can diced fire-roasted tomato | 4 |
| 14-ounce can diced tomato | 3 |
| 14-ounce can diced tomatoes in juice | 1 |
| 14-ounce can diced tomatoes with chiles | 1 |
| 14-ounce can fire-roasted diced tomato | 1 |
| 14-ounce can low-sodium diced tomato | 1 |
| 14-ounce can no-salt-added diced tomato | 4 |
| 14-ounce can no-salt-added tomato sauce | 1 |
| 14-ounce can plum tomatoes including-the juice | 1 |
| 14-ounce can whole peeled tomato | 2 |
| 14-ounce can whole plum tomato | 1 |
| 14-ounce can whole san marzano tomatoes, crushed | 1 |
| 14-ounce can whole tomato | 2 |
| 14-ounce can whole tomatoes with juice | 1 |
| 14-ounce cans cherry tomatoes, drained, or three cups fresh | 1 |
| 14-ounce cans diced fire-roasted tomatoes with green chiles | 1 |
| 14-ounce cans diced tomato | 1 |
| 14-ounce cans diced tomatoes in juice | 2 |
| 14-ounce cans low-sodium diced fire-roasted tomato | 1 |
| 14-ounce cans mexican-style diced tomatoes with green chiles | 1 |
| 14-ounce cans of good-quality chopped plum tomatoes, or 2 cups passata | 1 |
| 14-ounce cans whole peeled tomato | 1 |
| 14-ounces can whole peeled tomato | 1 |
| 14-to 15-ounce can plum tomatoes in juice; tomatoes chopped, juice reserved | 1 |
| 14.5- to 16-ounce can whole tomatoes in juice | 1 |
| 14.5-ounce can cherry tomato | 1 |
| 14.5-ounce can crushed fire-roasted tomato | 1 |
| 14.5-ounce can crushed tomato | 3 |
| 14.5-ounce can diced fire-roasted tomato | 2 |
| 14.5-ounce can diced fireroasted tomatoes in juice | 1 |
| 14.5-ounce can diced tomato | 8 |
| 14.5-ounce can diced tomatoes (preferably fire-roasted) | 1 |
| 14.5-ounce can diced tomatoes in juice | 8 |
| 14.5-ounce can diced tomatoes with green chiles | 1 |
| 14.5-ounce can diced tomatoes with italian herbs, drained well | 1 |
| 14.5-ounce can diced tomatoes with italian herbs, undrained | 1 |
| 14.5-ounce can fire-roasted or plain diced tomato | 1 |
| 14.5-ounce can no-salt-added diced tomato | 3 |
| 14.5-ounce can petite diced tomato | 1 |
| 14.5-ounce can whole peeled tomato | 1 |
| 14.5-ounce can whole peeled tomatoes, drained | 1 |
| 14.5-ounce cans diced tomatoes in juice | 4 |
| 14.5-ounce cans petite diced tomatoes with green chiles | 1 |
| 15 -ounce can crushed tomato | 1 |
| 15 -ounce can tomato sauce | 1 |
| 15 -ounce cans diced fire-roasted tomato | 1 |
| 15 1/2 ounce cans whole tomatoes with juice | 1 |
| 15 ounce can whole peeled tomatoes, drained | 1 |
| 15 oz can tomato | 1 |
| 15 oz can unsalted diced tomato | 1 |
| 15 oz. can diced tomato | 1 |
| 15 oz. can tomato sauce | 1 |
| 15- to 16-ounce can diced tomato | 1 |
| 15- to 16-ounce can mexican-style stewed tomatoes, coarsely mashed | 1 |
| 15- to 16-ounce can tomato sauce | 1 |
| 15-ounce can cherry tomato | 5 |
| 15-ounce can cherry tomatoes, drained (juices reserved) | 1 |
| 15-ounce can crushed tomato | 11 |
| 15-ounce can diced fire-roasted tomato | 3 |
| 15-ounce can diced fire-roasted tomatoes with chiles | 1 |
| 15-ounce can diced fire-roasted tomatoes with green chiles | 1 |
| 15-ounce can diced tomato | 9 |
| 15-ounce can diced tomatoes in juice | 1 |
| 15-ounce can diced tomatoes in juice, drained | 1 |
| 15-ounce can diced tomatoes with green chiles | 2 |
| 15-ounce can diced tomatoes, drained, juices reserved | 1 |
| 15-ounce can no-salt-added crushed tomato | 1 |
| 15-ounce can no-salt-added diced fire-roasted tomato | 1 |
| 15-ounce can no-salt-added diced tomato | 3 |
| 15-ounce can no-salt-added diced tomatoes, drained | 1 |
| 15-ounce can no-salt-added fire-roasted tomato | 1 |
| 15-ounce can no-salt-added petite diced tomato | 1 |
| 15-ounce can no-salt-added tomato puree | 1 |
| 15-ounce can no-salt-added whole peeled tomatoes, crushed by hand (about 2 cups) | 1 |
| 15-ounce can petite diced tomato | 2 |
| 15-ounce can plum tomato | 4 |
| 15-ounce can tomato puree | 1 |
| 15-ounce can tomato sauce | 9 |
| 15-ounce can whole peeled tomato | 1 |
| 15-ounce can whole peeled tomatoes, crushed by hand | 1 |
| 15-ounce can whole san marzano tomatoes, crushed by hand | 1 |
| 15-ounce can whole tomatoes, crushed by hand | 1 |
| 15-ounce cans chopped tomatoes in juice | 1 |
| 15-ounce cans diced fire-roasted tomato | 1 |
| 15-ounce cans diced tomato | 1 |
| 15-ounce cans diced tomatoes in juice | 1 |
| 15-oz. can tomato puree | 1 |
| 15-to 16-ounce can stewed tomato | 1 |
| 15–ounce can tomato sauce | 1 |
| 16 ounce can stewed tomato | 1 |
| 16 ounce can whole peeled tomatoes, drained | 1 |
| 16-ounce can crushed tomato | 1 |
| 16-ounce can italian plum tomatoes, drained | 1 |
| 16-ounce can plum tomatoes, drained and chopped | 1 |
| 16-ounce can stewed tomato | 1 |
| 16-ounce can tomato puree | 1 |
| 16-ounce can tomato sauce or 6 large fresh tomatoes chopped and stewed for 1hour | 1 |
| 16-ounce can tomato sauce, low sodium | 1 |
| 16-ounce can tomatoes, drained and de-seeded | 2 |
| 16-ounce container campari or other small vine-ripened tomatoes, quartered | 1 |
| 2.5 ounces, slivered dry-packed sun-dried tomato | 1 |
| 20 ounce can crushed tomato | 1 |
| 20 ounce can whole tomato | 1 |
| 26-ounce box chopped tomatoes (such as pomi) or two 14 1/2-ounce cans diced tomato | 1 |
| 26-ounce jar prepared tomato pasta sauce (about 3 1/4 cups) | 1 |
| 26-ounce jar purchased tomato pasta sauce (such as spicy red pepper or tomato-basil) | 1 |
| 28 -ounce can crushed tomato | 1 |
| 28 -ounce can diced tomato | 1 |
| 28 -ounce can diced tomatoes, drained well | 1 |
| 28 -ounce can san marzano plum tomato | 2 |
| 28 -ounce can whole peeled tomatoes with juices, broken up | 1 |
| 28 -ounce can whole peeled tomatoes, crushed slightly, liquid reserved | 1 |
| 28 -ounce can whole san marzano tomatoes, crushed by hand | 1 |
| 28 ounce can of tomatoes, crushed | 1 |
| 28 ounce can peeled tomatoes with juices, crushed by hand | 1 |
| 28 ounce can peeled tomatoes, puréed in a food processor | 1 |
| 28 oz can tomato | 1 |
| 28-ounce can chopped tomato | 1 |
| 28-ounce can chopped tomatoes, lightly drained | 1 |
| 28-ounce can crushed italian tomato | 1 |
| 28-ounce can crushed san marzano tomato | 1 |
| 28-ounce can crushed tomato | 13 |
| 28-ounce can crushed tomatoes in puree | 1 |
| 28-ounce can crushed tomatoes in purée | 1 |
| 28-ounce can crushed tomatoes with added puree | 11 |
| 28-ounce can diced fire-roasted tomato | 3 |
| 28-ounce can diced peeled tomato | 1 |
| 28-ounce can diced peeled tomatoes with juices | 1 |
| 28-ounce can diced tomato | 8 |
| 28-ounce can diced tomatoes in juice | 21 |
| 28-ounce can diced tomatoes in juice (preferably fire-roasted) | 1 |
| 28-ounce can diced tomatoes in juice, drained | 1 |
| 28-ounce can diced tomatoes in juice, drained, juice reserved | 1 |
| 28-ounce can diced tomatoes in juice, well drained, juices reserved | 1 |
| 28-ounce can diced tomatoes with juices | 1 |
| 28-ounce can diced tomatoes with juices, puréed in blender until smooth | 1 |
| 28-ounce can italian plum tomato | 3 |
| 28-ounce can italian plum tomatoes with juices | 1 |
| 28-ounce can italian plum tomatoes, drained | 3 |
| 28-ounce can italian plum tomatoes, drained, juices reserved | 1 |
| 28-ounce can italian plum tomatoes, undrained | 1 |
| 28-ounce can italian tomato | 1 |
| 28-ounce can italian-style peeled tomato | 1 |
| 28-ounce can italian-style plum tomato | 1 |
| 28-ounce can italian-style tomato | 2 |
| 28-ounce can italian-style tomatoes in juice, tomatoes chopped, juice reserved | 1 |
| 28-ounce can italian-style tomatoes with juices | 1 |
| 28-ounce can italian-style tomatoes, drained | 1 |
| 28-ounce can italian-style tomatoes, drained, crushed | 1 |
| 28-ounce can italian-style tomatoes, drained, juices reserved | 2 |
| 28-ounce can italian-style tomatoes, tomatoes chopped, juices reserved | 1 |
| 28-ounce can no-salt-added diced tomato | 2 |
| 28-ounce can no-salt-added tomatoes, crushed by hand | 1 |
| 28-ounce can no-salt-added whole peeled tomatoes in puree, crushed by hand | 1 |
| 28-ounce can no-salt-added whole plum tomatoes, crushed by hand | 1 |
| 28-ounce can of tomatoes with liquid, crushing the tomatoes by hand | 1 |
| 28-ounce can peeled san marzano tomatoes, crushed by hand | 1 |
| 28-ounce can plum tomato | 7 |
| 28-ounce can plum tomato, drained and chopped coarse | 1 |
| 28-ounce can plum tomatoes in juice, tomatoes coarsely chopped | 1 |
| 28-ounce can plum tomatoes in puree | 1 |
| 28-ounce can plum tomatoes, crushed by hand | 1 |
| 28-ounce can plum tomatoes, drained | 1 |
| 28-ounce can pureed tomato | 1 |
| 28-ounce can ready-cut tomato | 1 |
| 28-ounce can san marzano plum tomatoes, drained | 1 |
| 28-ounce can san marzano plum tomatoes, drained, juices reserved | 1 |
| 28-ounce can san marzano tomatoes in juice | 1 |
| 28-ounce can san marzano tomatoes, crushed by hand | 2 |
| 28-ounce can seasoned crushed tomatoes with italian herbs | 1 |
| 28-ounce can tomato | 1 |
| 28-ounce can tomato puree (preferably san marzano) | 1 |
| 28-ounce can tomato sauce | 1 |
| 28-ounce can whole fire-roasted tomato | 1 |
| 28-ounce can whole italian-style tomatoes, drained, juices reserved, tomatoes chopped | 1 |
| 28-ounce can whole peeled san marzano tomato | 1 |
| 28-ounce can whole peeled san marzano tomatoes, crushed by hand | 1 |
| 28-ounce can whole peeled tomato | 16 |
| 28-ounce can whole peeled tomatoes (preferably san marzano) | 1 |
| 28-ounce can whole peeled tomatoes (preferably san marzano) kosher salt | 1 |
| 28-ounce can whole peeled tomatoes and their juices, coarsely puréed | 1 |
| 28-ounce can whole peeled tomatoes, crushed by hand | 1 |
| 28-ounce can whole peeled tomatoes, crushed by hand, juices reserved | 2 |
| 28-ounce can whole peeled tomatoes, crushed well by hand | 1 |
| 28-ounce can whole peeled tomatoes, drained | 3 |
| 28-ounce can whole plum tomato | 3 |
| 28-ounce can whole plum tomatoes in juice (preferably san marzano), tomatoes chopped, juice reserved | 1 |
| 28-ounce can whole plum tomatoes, coarsely crushed with your hands | 1 |
| 28-ounce can whole plum tomatoes, crushed by hand | 10 |
| 28-ounce can whole plum tomatoes, preferably fire-roasted | 2 |
| 28-ounce can whole plum tomatoes, pureed with their juices | 1 |
| 28-ounce can whole san marzano tomato | 5 |
| 28-ounce can whole san marzano tomatoes, crushed by hand | 5 |
| 28-ounce can whole san marzano tomatoes, drained, juice reserved | 1 |
| 28-ounce can whole tomato | 1 |
| 28-ounce can whole tomatoes in juice | 2 |
| 28-ounce can whole tomatoes with juice | 1 |
| 28-ounce can whole tomatoes, crushed by hand | 1 |
| 28-ounce can whole tomatoes, drained | 1 |
| 28-ounce can whole tomatoes, drained and roughly chopped | 2 |
| 28-ounce can whole tomatoes, drained, crushed with your hands | 1 |
| 28-ounce can whole tomatoes, well drained | 1 |
| 28-ounce cans chopped diced tomatoes in juice, drained | 1 |
| 28-ounce cans crushed tomato | 1 |
| 28-ounce cans crushed tomatoes or whole canned tomatoes, gently crushed with your hands | 1 |
| 28-ounce cans crushed tomatoes with added puree | 2 |
| 28-ounce cans diced tomatoes in juice | 4 |
| 28-ounce cans diced tomatoes in juice (preferably san marzano) | 1 |
| 28-ounce cans diced tomatoes with juice | 1 |
| 28-ounce cans diced tomatoes with juices | 1 |
| 28-ounce cans fire-roasted peeled whole tomato | 1 |
| 28-ounce cans italian plum tomatoes, drained | 1 |
| 28-ounce cans italian plum tomatoes, drained in a colander | 1 |
| 28-ounce cans italian-style tomato | 2 |
| 28-ounce cans italian-style tomatoes, drained | 1 |
| 28-ounce cans of tomatoes, crushed and mixed | 2 |
| 28-ounce cans peeled whole tomato | 1 |
| 28-ounce cans peeled whole tomatoes with basil in juice, tomatoes diced, all juice reserved | 1 |
| 28-ounce cans plum tomatoes in juice, pureed with juice in blender in batches until smooth | 1 |
| 28-ounce cans plum tomatoes, crushed | 1 |
| 28-ounce cans plum tomatoes, drained | 1 |
| 28-ounce cans plum tomatoes, with their juice | 1 |
| 28-ounce cans san marzano plum tomato | 2 |
| 28-ounce cans tomato | 1 |
| 28-ounce cans whole italian-style tomato | 1 |
| 28-ounce cans whole peeled tomato | 1 |
| 28-ounce cans whole peeled tomatoes (pelati) | 1 |
| 28-ounce cans whole peeled tomatoes in juice, drained, juice reserved, tomatoes finely chopped | 1 |
| 28-ounce cans whole peeled tomatoes with juices | 1 |
| 28-ounce cans whole peeled tomatoes, drained, seeded and halved, with 1/2 cup juice reserved | 1 |
| 28-ounce cans whole san marzano tomato | 2 |
| 28-ounce cans whole san marzano tomatoes, crushed by hand | 3 |
| 28-ounce cans whole tomato | 1 |
| 28-ounce cans whole tomatoes (preferably muir glen from california) | 1 |
| 28-ounce container strained tomatoes or tomato puree | 1 |
| 28-ounces can italian-style tomato | 1 |
| 28-ounces cans whole peeled italian plum tomato | 1 |
| 28-ounces cans whole peeled tomato | 1 |
| 28.2-ounce can peeled tomatoes in puree with basil | 1 |
| 28–ounce cans italian tomatoes (such as san marzano) with juice | 1 |
| 29-ounce can ready-cut tomato | 1 |
| 32-ounce can crushed tomato | 1 |
| 32-ounce jar prepared tomato sauce | 1 |
| 35 -ounce can whole peeled tomatoes, crushed, juices reserved | 1 |
| 35-ounce can whole san marzano tomato | 1 |
| 46-ounce can tomato juice | 1 |
| 5-ounce container sun-dried tomato- and basil-flavored feta cheese spread or 1 1/2 cups crumbled flavored feta cheese | 1 |
| 6- to 7-ounce jars oil-packed sun-dried tomatoes with herbs, drained well, oil reserved | 1 |
| 6-ounce can tomato paste | 10 |
| 6-ounce cans tomato paste | 3 |
| 6-ounce container assorted bab tomatoes, large ones halved | 1 |
| 6-ounce container cherry tomatoes, halved if large | 1 |
| 8 oz cans of tomato sauce | 1 |
| 8- ounce can tomato sauce | 1 |
| 8-ounce can no-salt added tomato sauce | 1 |
| 8-ounce can tomato sauce | 15 |
| 8-ounce cans tomato sauce | 5 |
| 8-ounce tomato | 2 |
| 8-ounce tomato sauce | 1 |
| 8.5-ounce jar sun-dried tomatoes in olive oil with herbs, drained, 1 tablespoon oil reserved | 1 |
| 8oz. can tomato sauce | 1 |
| a 1-pound can whole peeled tomatoes with juice | 1 |
| a 1-pound can whole tomatoes in purée, drained, reserving 2 tablespoons purée, and chopped fine | 1 |
| a 13 1/2- to 14 1/2-ounce can tomatoes, drained in a sieve | 1 |
| a 14 1/2- to 16-ounce can chopped tomatoes including juice | 1 |
| a 14 1/2-ounce can diced tomatoes including juice | 1 |
| a 14 1/2-ounce can diced tomatoes with juice | 1 |
| a 14 1/2-ounce can stewed tomatoes including liquid | 1 |
| a 14- to 16-ounce can peeled whole tomatoes including their juice | 1 |
| a 14- to 16-ounce can peeled whole tomatoes, drained and chopped | 1 |
| a 14- to 16-ounce can tomatoes, drained | 1 |
| a 14- to 16-ounce can tomatoes, drained, reserving the juice, and chopped fine | 1 |
| a 14- to 16-ounce can whole tomatoes including the juice | 1 |
| a 14- to 16-ounce can whole tomatoes, drained, reserving juice, and chopped | 2 |
| a 14-ounce can italian tomatoes, drained | 1 |
| a 14-ounce can plum tomatoes, drained, seeded, and chopped | 1 |
| a 14-ounce can tomatoes including the juice | 1 |
| a 14-ounce can tomatoes, drained well in a colander | 1 |
| a 14-to-16 ounce can tomato | 1 |
| a 16-ounce can tomato sauce | 1 |
| a 16-ounce can tomatoes, drained and chopped | 1 |
| a 16-ounce can whole tomatoes including juice | 1 |
| a 26- to 32-ounce container chopped tomato | 1 |
| a 28- to 32-ounce can organic tomato | 1 |
| a 28- to 32-ounce can tomatoes, drained and chopped | 1 |
| a 28- to 32-ounce can whole italian tomatoes, drained, reserving 1 1/4 cups juice, and chopped fine | 1 |
| a 28- to 32-ounce can whole tomato | 2 |
| a 28- to 32-ounce can whole tomatoes including juice | 2 |
| a 28- to 32-ounce can whole tomatoes including liquid coarsely puréed in a blender | 1 |
| a 28- to 32-ounce can whole tomatoes with juice | 2 |
| a 28- to 32-ounce can whole tomatoes with thick purée | 1 |
| a 28- to 32-ounce can whole tomatoes, drained, seeded, and chopped | 1 |
| a 28-ounce can crushed tomatoes in puree (preferably italian; about 3 1/2 cups) | 1 |
| a 28-ounce can italian tomatoes, drained and chopped | 1 |
| a 28-ounce can italian tomatoes, drained, reserving the juice, and chopped | 1 |
| a 28-ounce can peeled whole tomatoes, seeded, drained, reserving 1/4 cup juice, and chopped | 1 |
| a 28-ounce can plum tomatoes including the juice | 1 |
| a 28-ounce can plum tomatoes, drained and chopped | 1 |
| a 28-ounce can plum tomatoes, drained well and chopped fine | 1 |
| a 28-ounce can plum tomatoes, the juice discarded and the tomatoes chopped and drained well | 1 |
| a 28-ounce can tomatoes including the juice | 1 |
| a 28-ounce can tomatoes including the juice, puréed coarse | 1 |
| a 28-ounce can whole italian plum tomatoes, seeded and drained well | 1 |
| a 28-ounce can whole tomato | 1 |
| a 28-ounce to 32-ounce can plum tomatoes, drained and chopped | 1 |
| a 28-to 32-ounce can whole tomatoes including juice, puréed coarse | 1 |
| a 28-to 32-ounce can whole tomatoes, drained and puréed coarse | 1 |
| a 28-to-32 ounce can whole tomatoes including juice | 2 |
| a 28-to-32 ounce can whole tomatoes, drained and chopped | 1 |
| a 32- to 35-ounce can tomatoes, drained, reserving the juice, and chopped | 1 |
| a 35-ounce can italian plum tomatoes, drained, reserving 1 cup of the juice, and chopped | 1 |
| a 35-ounce can plum tomatoes, drained | 1 |
| a 35-ounce can plum tomatoes, drained well | 1 |
| a 6-ounce can tomato paste | 2 |
| a few grape tomato | 1 |
| a few sun-dried tomatoes packed short shape in oil | 1 |
| a handful sun-dried tomatoes packed in oil | 1 |
| a tablespoon tomato, brunoised | 1 |
| about 1/2 cup very thinly sliced mushrooms or chopped fresh tomatoes, or roasted eggplant slices | 1 |
| about 1/3 cup tomato powder or 1 to 2 plum tomatoes, seeded and finely diced | 1 |
| about 1/4 cup chopped tomato | 1 |
| about 10 cherry tomatoes, halved | 1 |
| about 10 roma tomatoes, cored and chopped | 1 |
| about 12 medium roma tomatoes (2 pounds) | 1 |
| about 2 cups spicy tomato sauce, heated | 1 |
| about 2 cups tomato sauce (see recipe below), warmed | 1 |
| about 2 cupsfresh tomato salsa | 1 |
| about 2 tablespoons chopped tomato | 1 |
| about 20 cherry tomatoes, halved | 1 |
| about 3 cups of your favorite tomato sauce | 1 |
| about 30 grape tomato | 1 |
| about 4 1/2 pounds tomatoes (2kg), halved | 1 |
| about 5 grape tomato | 1 |
| about 6 cups winter tomato sauce | 1 |
| accompaniment, if desired: tomatoes provencale, recipe follows | 1 |
| accompaniment: charred tomato mint salsa | 1 |
| accompaniment: chilled tomato soups | 1 |
| accompaniment: fresh tomato salsa | 1 |
| accompaniment: mixed cherry tomatoes with tamarind dressing | 1 |
| accompaniment: roasted tomato and arugula salad | 1 |
| accompaniment: spicy tomato cranberry preserves | 1 |
| accompaniment: tomato ginger jam | 1 |
| accompaniment: tomato relish, chutney, or ketchup | 1 |
| accompaniment: tomato salsa | 2 |
| accompaniment: tomato salsa if desired | 1 |
| accompaniment: tomato sauce | 1 |
| accompaniment: tomato-rubbed bruschetta | 1 |
| accompaniment: warm homemade or bottled spicy tomato sauce | 1 |
| accompaniments: fresh cilantro leaves; chopped plum tomato; finely chopped white onion; tortilla chips | 1 |
| accompaniments: homemade burger buns ; homemade ketchup ; homemade mustard ; homemade pickle relish ; lettuce and tomato | 1 |
| accompaniments: homemade tomato ketchup | 1 |
| accompaniments: lettuce, tomato, mustard, and pickles | 1 |
| accompaniments: lettuce; sliced tomato | 1 |
| accompaniments: mayonnaise; mustard; iceberg lettuce; sliced tomatoes; dill pickles | 1 |
| accompaniments: sandwich bread; lettuce leaves; sliced tomato | 1 |
| accompaniments:guacamole orfresh tomato salsa | 1 |
| adriana's tomato basil sauce, recipe follows | 1 |
| amazing cherry or plum tomatoes, halved plus 1 pound canned plum tomato | 1 |
| an 8-ounce can tomato sauce (about 3/4 cup) | 1 |
| and 1 (14-ounce) can whole tomatoes, both thoroughly drained | 1 |
| any or all of the following, cut into large chunks if necessary: 1/2 peeled onion, 1 small peeled carrot, 1 celery rib, a garlic clove, a bay leaf, a small tomato, a thyme sprig or two, parsley stems | 1 |
| arugula and sliced tomatoes, for serving | 1 |
| assorted additional toppings (such as tomato and grilled onion slices) | 1 |
| assorted baby tomatoes (red, yellow, and orange) | 1 |
| assorted cherry and/or grape tomato | 1 |
| assorted cherry or grape tomatoes, halved | 1 |
| assorted cherry tomatoes (red, yellow, orange, pear-shaped, grape-sized, etc.) | 1 |
| assorted cherry tomatoes, halved | 3 |
| assorted cherry tomatoes, halved or quartered if large | 2 |
| assorted cherry tomatoes, some halved | 1 |
| assorted cherry, grape, and teardrop tomatoes, halved (or quartered if large) | 1 |
| assorted color heirloom tomato | 1 |
| assorted crudite such as baby carrots, fennel, celery and cherry tomatoes, for serving | 1 |
| assorted cut-up vegetables (broccoli, carrots, tomatoes, bell peppers, cauliflower, onions and mushrooms) | 1 |
| assorted cut-up vegetables (such as carrots, cucumbers, red bell peppers, yellow bell peppers, cherry tomatoes, fennel bulbs, green onions and radishes) | 1 |
| assorted heirloom or vine-ripened red tomatoes, cut into 1/2-inch thick slices | 1 |
| assorted heirloom tomato | 6 |
| assorted heirloom tomatoes (3 to 4), cored and chopped | 1 |
| assorted heirloom tomatoes, cut in halves or quarters (cherry tomato varieties left whole) | 1 |
| assorted heirloom tomatoes, cut into chunks | 1 |
| assorted heirloom tomatoes, or substitute plum tomato | 1 |
| assorted large and small heirloom tomato | 1 |
| assorted large heirloom tomato | 1 |
| assorted medium heirloom tomatoes (2 lb total), cut into 1/4- to 1/3-inch-thick slices | 1 |
| assorted mixed baby heirloom tomato | 1 |
| assorted raw vegetables, such as: cherry tomatoes, trimmed radishes, cucumber spears, celery sticks | 1 |
| assorted ripe green heirloom tomatoes (such as green zebras), cut into wedges | 1 |
| assorted ripe heirloom tomatoes, halved or quartered, depending on size and shape | 1 |
| assorted small heirloom tomato | 1 |
| assorted small heirloom tomatoes, halved | 1 |
| assorted small heirloom tomatoes, halved (larger ones quartered) | 1 |
| assorted small tomatoes (such as cherry, grape, and teardrop; preferably mix of red and yellow) | 1 |
| assorted small tomatoes (such as cherry, sun gold, or green), halved, quartered if large | 1 |
| assorted small tomatoes, halved, quartered if large | 1 |
| assorted small vine-ripened cherry or currant tomato | 1 |
| assorted tomatoes (heirloom, vine and plum) | 2 |
| assorted tomatoes (heirlooms, etc.), cut into wedges | 1 |
| assorted tomatoes, halved or cut into wedges if large | 1 |
| assorted vegetables (bell peppers, zucchini, eggplant, tomatoes, asparagus, potatoes, fennel, onions) cleaned and if necessary cut or skewered | 1 |
| assorted vegetables (such as carrot sticks, yellow bell pepper strips, cherry tomatoes and boiled baby potatoes) | 1 |
| assorted vegetables, such as green or red bell pepper, cherry tomatoes, zucchini, and onion, all cubed except tomatoes, for the kabobs, as desired | 1 |
| assorted vine-ripened heirloom tomatoes, cored and cut into 1/2-inch wedges | 1 |
| baby heirloom tomato | 1 |
| baby heirloom tomatoes, halved | 2 |
| baby or teardrop tomato | 1 |
| baby red pear tomato | 1 |
| baby tomato | 2 |
| baby tomatoes (cherry or grape), cut in half | 1 |
| baby yellow pear tomato | 1 |
| bacon and tomato twist mayonnaise | 1 |
| bacon and tomato twist mayonnaise (recommended: best foods) | 1 |
| bag or box of cherry tomato | 1 |
| balls fresh mozzarella in water, cherry tomato size | 1 |
| barilla® tomato & basil sauce | 2 |
| basic tomato sauce | 7 |
| basic tomato sauce (recipe follows) | 2 |
| basic tomato sauce, for serving | 1 |
| basic tomato sauce, pureed in a blender | 1 |
| basic tomato sauce, pureed, recipe follows | 1 |
| basic tomato sauce, recipe follows | 13 |
| basic tomato sauce, recipe follows, diluted with 1/2 cup boiling water | 1 |
| basil and garlic tomato pasta sauce (from 16 ounce jar) | 1 |
| basket assorted cherry tomato | 1 |
| basket cherry or grape tomato | 1 |
| basket cherry tomato | 2 |
| basket cherry tomatoes, halved | 3 |
| basket cherry tomatoes, red, yellow or both, washed and stemmed | 1 |
| basket grape or cherry tomato | 1 |
| basket grape tomatoes, halved | 1 |
| basket grape tomatoes, halved lengthwise | 1 |
| basket sweet 100 tomatoes, or cherry tomato | 1 |
| baskets cherry tomatoes, halved | 1 |
| baskets cherry tomatoes, quartered and seeded | 1 |
| basque tomato sauce | 1 |
| beef and tomato base, recipe follows | 2 |
| beef base stirred into 1 cup water (part of which should be the soaking liquid if re-hydrating the sun-dried tomatoes) | 1 |
| beef steak tomato | 2 |
| beef tomato | 1 |
| beef, chicken or tomato bouillon cube | 2 |
| beef, chicken or tomato bouillon cubes | 1 |
| beefsteak or heirloom tomato | 3 |
| beefsteak or heirloom tomatoes (about 1 pound), cut into 1-inch wedges | 1 |
| beefsteak or heirloom tomatoes, cut into 1/4-inch slices | 1 |
| beefsteak or jersey tomato | 1 |
| beefsteak tomato | 42 |
| beefsteak tomato or in-season yellow/red heirloom tomato | 1 |
| beefsteak tomato, cut in thick slices | 1 |
| beefsteak tomato, cut into 4 thick slices | 1 |
| beefsteak tomato, thinly sliced | 3 |
| beefsteak tomatoes (about 12 ounces) | 1 |
| beefsteak tomatoes (about 2 pounds) | 1 |
| beefsteak tomatoes (about 3) | 1 |
| beefsteak tomatoes (about 4 large tomatoes) | 1 |
| beefsteak tomatoes (about 4), quartered | 1 |
| beefsteak tomatoes (cut into 1/2 inch pieces) | 1 |
| beefsteak tomatoes (or 6 plum) | 1 |
| beefsteak tomatoes (slightly under ripe is best) | 1 |
| beefsteak tomatoes sliced 1/2-inch thick | 1 |
| beefsteak tomatoes, cap removed, cored and hollowed out | 1 |
| beefsteak tomatoes, cut 1/3-inch thick | 1 |
| beefsteak tomatoes, cut into 1-inch wedges | 2 |
| beefsteak tomatoes, cut into 1-inch-thick wedges | 1 |
| beefsteak tomatoes, cut into 1/2-inch dice, reserve the seeds and juices | 1 |
| beefsteak tomatoes, cut into 1/2-inch slices | 2 |
| beefsteak tomatoes, cut into 1/2-inch wedges | 1 |
| beefsteak tomatoes, cut into 1/3-inch thick slices | 1 |
| beefsteak tomatoes, cut into 1/4-inch-thick rounds | 1 |
| beefsteak tomatoes, cut into 2-inch wedges | 1 |
| beefsteak tomatoes, cut into wedges | 3 |
| beefsteak tomatoes, halved | 2 |
| beefsteak tomatoes, halved and seeded | 1 |
| beefsteak tomatoes, halved lengthwise and sliced crosswise 1/4 inch thick | 1 |
| beefsteak tomatoes, quartered | 1 |
| beefsteak tomatoes, seeded and cut into 1/2-inch dice | 1 |
| beefsteak tomatoes, thinly sliced | 1 |
| beefsteak tomatoes, trimmed and cut into 1-inch thick slices | 1 |
| bertolli® vineyard premium collections fire roasted tomato with cabernet sauvignon sauce | 1 |
| best quality italian chopped tomato | 1 |
| best quality tomato juice | 1 |
| bibb lettuce and sliced tomato, for topping | 3 |
| big beautiful ripe red tomato | 1 |
| big beefsteak tomato | 1 |
| bite-size pieces assorted vegetables (such as radishes, tomatoes, peas, summer squash) or carrot ribbons | 1 |
| blanched plum tomatoes or 1 (15 ounce) can crushed tomato | 1 |
| blistered baby zucchini, baby pattypan squash, and grilled tomato | 1 |
| blue cheese-crusted tomato | 1 |
| bolognese meat sauce, marinara tomato sauce, or store-bought pasta sauce | 1 |
| bottle clam-tomato cocktail (recommended: clamato) | 1 |
| bottle sun-dried tomato pesto | 1 |
| bottle tomato and clam juice cocktail | 1 |
| bottle tomato and clam juice cocktail (such as clamato®) | 2 |
| bottle tomato juice | 2 |
| bottle tomato juice (recommended: sacramanto) | 2 |
| bottle tomato ketchup, or combination tomato paste and sauce | 1 |
| bottle tomato-based chili sauce | 4 |
| bottle tomato-based chili sauce (such as heinz®) | 2 |
| bottle tomato-vegetable juice cocktail | 5 |
| bottle tomato-vegetable juice cocktail (such as v8®) | 3 |
| bottle vegetable or tomato juice, preferably organic | 1 |
| bottled mild tomato chili sauce (such as homade brand) | 1 |
| bottled tomato juice | 1 |
| bottled tomato salsa | 1 |
| bottled tomato salsa (about 9 ounces) | 3 |
| bottled tomato-based barbecue sauce | 1 |
| bottles tomato-based chili sauce | 1 |
| branch cherry tomato | 1 |
| broiled tomato crostini, for serving, recipe follows | 1 |
| broiled tomato sauce with roasted garlic | 1 |
| broiled tomatoes, recipe follows | 1 |
| broth (vegetable, chicken, tomato juice or water) | 1 |
| brown butter-tomato vinaigrette, recipe follows | 1 |
| brown, orange, green, or yellow ripe tomatoes, mixed | 1 |
| brunoise of tomato (small dice) | 1 |
| cabot tomato basil cheddar, cabot garlic & herb cheddar and cabot sharp, or cabot horseradish cheddar, cabot smoky bacon cheddar and cabot seriously sharp, or cabot pepper jack, cabot habanero cheddar and cabot mozzarella shredded | 1 |
| campari or other small vine-ripened tomato | 4 |
| campari or other small vine-ripened tomatoes (about 10 ounces), quartered | 1 |
| campari or other small vine-ripened tomatoes, quartered | 2 |
| campari or plum tomato | 1 |
| campari tomatoes, halved | 1 |
| campari tomatoes, seeded and minced | 1 |
| campbell's® condensed tomato soup | 3 |
| campbell's® condensed tomato soup (regular or healthy request®) | 3 |
| campbell's® tomato juice tomato juice | 1 |
| can "petite" diced tomatoes in juice | 1 |
| can (2 cups) plum tomato | 1 |
| can (3/4 cup) tomato paste | 1 |
| can (796 ml) diced tomato | 1 |
| can aylmer® accents® garlic and olive oil petite cut tomato | 1 |
| can aylmer® accents® italian seasonings chunky stewed tomato | 1 |
| can campbell's® condensed tomato soup | 2 |
| can campbell's® condensed tomato soup (regular or 25% less sodium) | 2 |
| can campbell's® condensed tomato, chipotle & olive oil soup | 2 |
| can canned crushed tomato | 2 |
| can canned diced tomato | 11 |
| can canned diced tomatoes and green chiles, drained | 1 |
| can canned diced tomatoes with their juice | 2 |
| can canned diced tomatoes, undrained | 1 |
| can canned peeled and diced tomato | 4 |
| can canned stewed tomato | 1 |
| can canned tomato | 4 |
| can canned tomato sauce | 4 |
| can canned tomatoes, drained and chopped | 2 |
| can cherry or diced tomato | 1 |
| can cherry tomato | 2 |
| can chili-style diced tomato | 1 |
| can chopped fire roasted tomatoes (recommended: muir glen) | 1 |
| can chopped fire-roasted tomato | 1 |
| can chopped plum tomato | 1 |
| can chopped plum tomatoes in puree | 1 |
| can chopped plum tomatoes plus their liquid | 1 |
| can chopped plum tomatoes with juice | 1 |
| can chopped stewed tomato | 3 |
| can chopped stewed tomatoes, with juice | 1 |
| can chopped tomato | 33 |
| can chopped tomatoes and green chiles | 1 |
| can chopped tomatoes in juice | 1 |
| can chopped tomatoes in puree | 1 |
| can chopped tomatoes or 2 diced fresh tomato | 1 |
| can chopped tomatoes with diced green chiles | 1 |
| can chopped tomatoes with juice | 4 |
| can chopped tomatoes with liquid | 2 |
| can chopped tomatoes with onions, drained | 1 |
| can chopped tomatoes, drained | 9 |
| can chopped tomatoes, drained and pureed | 2 |
| can chopped tomatoes, in juice | 1 |
| can chopped tomatoes, strained, juice reserved | 1 |
| can chopped tomatoes, with juice | 1 |
| can chopped tomatoes, with liquid | 1 |
| can chopped tomatoes, with their juice | 1 |
| can chunky style crushed tomato | 6 |
| can chunky style crushed tomatoes or diced tomatoes in puree | 1 |
| can chunky tomato sauce | 3 |
| can chunky-style crushed tomato | 1 |
| can chunky-style crushed tomatoes or diced tomatoes in puree | 2 |
| can condensed cream of tomato soup | 3 |
| can condensed tomato soup | 81 |
| can condensed tomato soup (such as campbell's®) | 2 |
| can condensed tomato soup (such as campbell's®) (optional) | 1 |
| can condensed tomato soup with basil and oregano | 1 |
| can condensed tomato soup, plus | 1 |
| can contadina® crushed tomato | 1 |
| can contadina® petite diced tomatoes, drained | 1 |
| can contadina® tomato paste | 1 |
| can contadina® tomato puree | 1 |
| can contadina® tomato sauce | 4 |
| can crushed fire roasted tomato | 4 |
| can crushed fire roasted tomatoes (recommended: muir glen) | 1 |
| can crushed fire roasted tomatoes, about 2 cups | 1 |
| can crushed fire roasted tomatoes, liquid included | 1 |
| can crushed italian tomato | 4 |
| can crushed italian tomatoes, any brand | 1 |
| can crushed or diced tomato | 2 |
| can crushed or diced tomatoes with juice | 1 |
| can crushed or pureed italian tomatoes (recommended: san marzano) | 1 |
| can crushed organic tomatoes, undrained | 1 |
| can crushed plum tomato | 2 |
| can crushed red tomatoes in puree | 2 |
| can crushed roma or plum tomato | 1 |
| can crushed san marzano (italian imported) tomato | 1 |
| can crushed san marzano tomato | 7 |
| can crushed san marzano tomatoes, or other high-quality plum tomato | 1 |
| can crushed tomato | 260 |
| can crushed tomatoes (best quality) | 1 |
| can crushed tomatoes (preferably italian) | 1 |
| can crushed tomatoes (quality varies dramatically; i prefer redpack, progresso and muir glen brands) | 1 |
| can crushed tomatoes (recommended: san marzano) | 1 |
| can crushed tomatoes (recommended: san marzano), plus 1 (14-ounce) can | 1 |
| can crushed tomatoes (such as contadina®) | 1 |
| can crushed tomatoes (such as hunt's®) | 1 |
| can crushed tomatoes (such as san marzano®) | 1 |
| can crushed tomatoes in juice | 1 |
| can crushed tomatoes in puree | 3 |
| can crushed tomatoes in purée | 1 |
| can crushed tomatoes in thick purée | 1 |
| can crushed tomatoes in tomato puree | 1 |
| can crushed tomatoes with added purée | 1 |
| can crushed tomatoes with basil | 2 |
| can crushed tomatoes with basil (i like hunt's) | 1 |
| can crushed tomatoes with garlic | 1 |
| can crushed tomatoes with juices | 1 |
| can crushed tomatoes with puree | 3 |
| can crushed tomatoes, (recommended: san marzano) | 2 |
| can crushed tomatoes, (recommended: san marzano)* if san marzanos are not available, add a teaspoon sugar to your sauce | 1 |
| can crushed tomatoes, drained | 2 |
| can crushed tomatoes, in puree | 2 |
| can crushed tomatoes, in thick puree | 1 |
| can crushed tomatoes, including liquid | 1 |
| can crushed tomatoes, or coarsely chopped tomatoes packed in puree | 1 |
| can crushed tomatoes, or plum tomatoes in puree | 2 |
| can crushed tomatoes, preferably san marzano | 5 |
| can crushed tomatoes, sam marzano if available | 1 |
| can crushed tomatoes, see cook's notes | 1 |
| can crushed tomatoes, such as san marzano | 1 |
| can crushed tomatoes, undrained | 1 |
| can crushed tomatoes, with juice | 2 |
| can crushed tomatoes, with juices | 1 |
| can crushed tomatoes, with liquid | 4 |
| can del monte® original recipe stewed tomatoes, not drained | 1 |
| can del monte® petite diced tomatoes, drained | 1 |
| can diced (or crushed) tomatoes (do not drain) | 1 |
| can diced fire roasted tomato | 2 |
| can diced fire roasted tomatoes, drained | 1 |
| can diced fire-roasted tomato | 8 |
| can diced fire-roasted tomatoes or diced tomato | 1 |
| can diced italian paste tomatoes (such as san marzano) | 1 |
| can diced italian plum tomatoes, juices reserved | 1 |
| can diced italian tomato | 2 |
| can diced italian tomatoes, undrained | 1 |
| can diced italian-style tomatoes, drained | 1 |
| can diced mexican style tomato | 1 |
| can diced or crushed tomato | 1 |
| can diced or stewed tomato | 1 |
| can diced plum tomato | 3 |
| can diced san marzano tomatoes with juice | 1 |
| can diced stewed tomatoes, or more to taste | 1 |
| can diced tomato | 448 |
| can diced tomato in juices | 2 |
| can diced tomatoes (about 3 1/2 cups) | 1 |
| can diced tomatoes (no salt added) | 1 |
| can diced tomatoes (or tomato puree) | 1 |
| can diced tomatoes (recommended: hunt's) | 1 |
| can diced tomatoes (recommended: muir glen) | 1 |
| can diced tomatoes (recommended: ro-tel) | 1 |
| can diced tomatoes and green chiles | 9 |
| can diced tomatoes and green chiles (recommended: ro'tel) | 3 |
| can diced tomatoes and green chiles (such as ro*tel® mexican lime & cilantro) | 1 |
| can diced tomatoes and green chiles (such as ro*tel® mild) | 2 |
| can diced tomatoes and green chiles (such as ro*tel®) | 4 |
| can diced tomatoes and green chiles (such as ro*tel®), drained (optional) | 1 |
| can diced tomatoes and green chiles (such as ro*tel®), undrained | 1 |
| can diced tomatoes and green chiles, drained | 2 |
| can diced tomatoes and green chiles, undrained | 2 |
| can diced tomatoes and green chilies | 2 |
| can diced tomatoes and green chilies, undrained | 1 |
| can diced tomatoes and green chilies, with liquid | 1 |
| can diced tomatoes and their juices | 1 |
| can diced tomatoes in juice | 26 |
| can diced tomatoes in juice with italian seasonings | 1 |
| can diced tomatoes in juice, drained | 2 |
| can diced tomatoes in juice, drained, reserving juice | 1 |
| can diced tomatoes in puree | 1 |
| can diced tomatoes in puree or coarsely ground tomato | 1 |
| can diced tomatoes including juice | 4 |
| can diced tomatoes or chunky-style crushed tomato | 1 |
| can diced tomatoes or coarsely ground tomato | 1 |
| can diced tomatoes or diced tomatoes with chiles | 1 |
| can diced tomatoes or fire roasted diced tomato | 1 |
| can diced tomatoes with balsamic vinegar, basil and olive oil | 1 |
| can diced tomatoes with basil | 1 |
| can diced tomatoes with basil and garlic | 1 |
| can diced tomatoes with basil and oregano | 1 |
| can diced tomatoes with basil, garlic and oregano | 2 |
| can diced tomatoes with basil, garlic, and oregano | 2 |
| can diced tomatoes with basil, garlic, and oregano - drained | 1 |
| can diced tomatoes with basil, garlic, and oregano, drained | 1 |
| can diced tomatoes with chiles | 2 |
| can diced tomatoes with chiles (see chef's tip, below) | 1 |
| can diced tomatoes with chiles in sauce (recommended: ro'tel) | 1 |
| can diced tomatoes with chiles or stewed tomato | 1 |
| can diced tomatoes with chiles, drained | 1 |
| can diced tomatoes with garlic | 3 |
| can diced tomatoes with garlic and herbs | 1 |
| can diced tomatoes with garlic and olive oil | 1 |
| can diced tomatoes with garlic and onion | 6 |
| can diced tomatoes with garlic and onion, drained | 1 |
| can diced tomatoes with garlic, onion, and peppers, drained | 1 |
| can diced tomatoes with green chile pepper | 72 |
| can diced tomatoes with green chile peppers (optional) | 2 |
| can diced tomatoes with green chile peppers (such as hatch®) | 1 |
| can diced tomatoes with green chile peppers (such as ro*tel®) | 37 |
| can diced tomatoes with green chile peppers (such as ro*tel®), drained | 5 |
| can diced tomatoes with green chile peppers (such as ro*tel®), undrained | 5 |
| can diced tomatoes with green chile peppers, drain and reserve liquid | 1 |
| can diced tomatoes with green chile peppers, drained | 18 |
| can diced tomatoes with green chile peppers, partially drained | 2 |
| can diced tomatoes with green chile peppers, with liquid | 6 |
| can diced tomatoes with green chiles | 6 |
| can diced tomatoes with green chiles (recommended: rotel) | 1 |
| can diced tomatoes with green chiles (such as ro*tel) | 1 |
| can diced tomatoes with green chiles (such as ro*tel® original), drained | 1 |
| can diced tomatoes with green chiles (such as rotel®), drained slightly | 1 |
| can diced tomatoes with green chiles, drained (i like rotel) | 1 |
| can diced tomatoes with green chili (such as rotel®) | 1 |
| can diced tomatoes with green chilies (such as ro*tel®) | 1 |
| can diced tomatoes with green chilies (such as ro*tel®), undrained | 1 |
| can diced tomatoes with green chilies, drained | 3 |
| can diced tomatoes with green chilies, undrained | 2 |
| can diced tomatoes with green chilies, well drained | 1 |
| can diced tomatoes with green pepper and onion, drained | 1 |
| can diced tomatoes with green pepper, celery, and onion | 1 |
| can diced tomatoes with green peppers and onion | 2 |
| can diced tomatoes with green peppers, celery, and onion (recommended: hunt's) | 1 |
| can diced tomatoes with habaneros (such as ro*tel® hot), drained | 1 |
| can diced tomatoes with italian herbs, with juices | 1 |
| can diced tomatoes with italian seasonings | 1 |
| can diced tomatoes with jalapeno peppers, drained | 1 |
| can diced tomatoes with jalapenos | 1 |
| can diced tomatoes with juice | 59 |
| can diced tomatoes with juices | 7 |
| can diced tomatoes with lime juice and cilantro | 1 |
| can diced tomatoes with lime juice and cilantro (such as ro*tel®) | 1 |
| can diced tomatoes with liquid | 1 |
| can diced tomatoes with mild green chiles | 1 |
| can diced tomatoes with mild green chilies, undrained | 2 |
| can diced tomatoes with onion and celery, drained | 1 |
| can diced tomatoes with onion, celery, and green pepper | 1 |
| can diced tomatoes with roasted garlic | 1 |
| can diced tomatoes with their juice | 1 |
| can diced tomatoes, drained | 72 |
| can diced tomatoes, drained and juice reserved | 3 |
| can diced tomatoes, drained and rinsed | 1 |
| can diced tomatoes, drained or 3 roma tomato | 1 |
| can diced tomatoes, drained well | 1 |
| can diced tomatoes, in juice | 3 |
| can diced tomatoes, in puree | 1 |
| can diced tomatoes, in thick puree | 1 |
| can diced tomatoes, including juice | 2 |
| can diced tomatoes, including the liquid | 1 |
| can diced tomatoes, juices drained | 1 |
| can diced tomatoes, or more to taste | 1 |
| can diced tomatoes, preferably "no salt added" | 1 |
| can diced tomatoes, preferably fire roasted (recommended: muir glen) | 1 |
| can diced tomatoes, strained | 1 |
| can diced tomatoes, such as san marzano | 1 |
| can diced tomatoes, undrained | 36 |
| can diced tomatoes, undrained or use tomato sauce for a thicker sauce | 1 |
| can diced tomatoes, well drained | 2 |
| can diced tomatoes, with juice | 5 |
| can diced tomatoes, with juices | 2 |
| can diced tomatoes, with liquid | 2 |
| can diced tomatoes, with their juice | 2 |
| can diced tomatoes, with their juices | 1 |
| can fire roasted chopped tomatoes (recommended: muir glen) | 1 |
| can fire roasted chopped tomatoes (such as hunts®) | 1 |
| can fire roasted chopped tomatoes, such as muir glenn or, regular diced tomato | 1 |
| can fire roasted crushed tomato | 2 |
| can fire roasted diced tomato | 5 |
| can fire roasted diced tomatoes (recommended: muir glen) | 1 |
| can fire roasted diced tomatoes, drained | 1 |
| can fire roasted diced tomatoes, drained well | 1 |
| can fire roasted diced tomatoes, such as muir glenn brand | 1 |
| can fire roasted tomato | 4 |
| can fire roasted tomatoes, drained, about 1 1/3 cups | 1 |
| can fire-roasted crushed tomato | 7 |
| can fire-roasted diced or crushed tomato | 2 |
| can fire-roasted diced or crushed tomatoes or 1 (15-ounce) can diced tomatoes with green chilies | 1 |
| can fire-roasted diced tomato | 13 |
| can fire-roasted diced tomatoes with garlic | 1 |
| can fire-roasted diced tomatoes with juice | 1 |
| can fire-roasted diced tomatoes, lightly drained | 1 |
| can fire-roasted diced tomatoes, partially drained | 1 |
| can fire-roasted diced tomatoes, undrained | 2 |
| can fire-roasted diced tomatoes, with juice | 6 |
| can fire-roasted tomato | 3 |
| can fire-roasted tomatoes (such as hunt's®) | 1 |
| can fire-roasted tomatoes with green chiles | 1 |
| can fire-roasted whole tomatoes, crushed by hand | 1 |
| can good-quality whole tomato | 1 |
| can good-quality whole tomatoes in juice, drained and chopped or 2 cups chopped ripe tomato | 1 |
| can heinz tomato paste | 1 |
| can hunt's® crushed tomato | 1 |
| can hunt's® diced tomato | 4 |
| can hunt's® diced tomatoes, drained | 9 |
| can hunt's® diced tomatoes, undrained | 4 |
| can hunt's® fire roasted diced tomatoes, undrained | 1 |
| can hunt's® petite diced tomatoes, drained | 2 |
| can hunt's® petite diced tomatoes, undrained | 1 |
| can hunt's® tomato paste | 2 |
| can hunt's® tomato sauce | 3 |
| can hunt’s® diced tomatoes with basil, garlic and oregano, undrained | 1 |
| can imported italian plum tomatoes, drained, seeded and slightly crushed with juices reserved | 1 |
| can italian diced tomatoes, drained | 1 |
| can italian diced tomatoes, undrained | 1 |
| can italian plum tomato | 7 |
| can italian plum tomatoes and their juice | 1 |
| can italian plum tomatoes in juice, drained | 1 |
| can italian plum tomatoes in juice, drained and chopped | 2 |
| can italian plum tomatoes in puree | 1 |
| can italian plum tomatoes, passed through a food mill | 1 |
| can italian plum tomatoes, passed through the food mill | 1 |
| can italian plum tomatoes, pureed | 1 |
| can italian plum tomatoes, seeded | 1 |
| can italian san marzano tomato | 1 |
| can italian stewed tomato | 1 |
| can italian style stewed tomato | 1 |
| can italian tomato | 6 |
| can italian-seasoned diced tomato | 1 |
| can italian-style crushed tomato | 2 |
| can italian-style crushed tomatoes, undrained | 1 |
| can italian-style diced tomato | 19 |
| can italian-style diced tomatoes (such as hunt's® diced tomatoes with basil, garlic and oregano) | 1 |
| can italian-style diced tomatoes, drained | 9 |
| can italian-style diced tomatoes, undrained | 9 |
| can italian-style plum tomatoes, drained and coarsely chopped | 1 |
| can italian-style stewed tomato | 12 |
| can italian-style stewed tomatoes, drained and diced | 1 |
| can italian-style tomato paste | 1 |
| can italian-style tomatoes, undrained and chopped | 1 |
| can italian-style whole peeled tomato | 2 |
| can low-sodium crushed tomato | 1 |
| can low-sodium diced tomatoes and green chilies | 1 |
| can low-sodium diced tomatoes, juice included | 1 |
| can low-sodium tomato sauce | 5 |
| can low-sodium, tomato-vegetable juice cocktail | 1 |
| can mackerel in tomato sauce | 1 |
| can mexican or chili-style stewed tomatoes, undrained | 1 |
| can mexican stewed tomatoes, unrinsed and chopped into 1/2-inch pieces | 1 |
| can mexican style hot tomato sauce (such as el pato salsa de chile fresco®) | 1 |
| can mexican-style diced tomatoes, undrained | 1 |
| can mexican-style hot tomato sauce | 3 |
| can mexican-style hot tomato sauce (such as el pato®) | 1 |
| can mexican-style stewed tomato | 4 |
| can mexican-style stewed tomatoes with chiles, undrained | 1 |
| can mexican-style stewed tomatoes with jalapeno peppers and spices, undrained | 1 |
| can mexican-style tomato sauce | 1 |
| can no salt added diced tomato | 1 |
| can no salt added diced tomatoes with juice | 1 |
| can no salt added diced tomatoes, with their juices | 1 |
| can no salt-added diced tomatoes with italian herbs | 2 |
| can no salt-added diced tomatoes, drained, juice reserved | 1 |
| can no-salt tomato sauce | 1 |
| can no-salt-added diced tomato | 7 |
| can no-salt-added diced tomatoes with basil, garlic, and oregano | 1 |
| can no-salt-added diced tomatoes, strained and juice reserved (about 3/4 to 1 cup juice) | 1 |
| can no-salt-added diced tomatoes, undrained | 2 |
| can no-salt-added tomato | 1 |
| can no-salt-added tomato paste (such as hunt's®) | 1 |
| can no-salt-added tomato sauce | 3 |
| can no-salt-added whole tomatoes, undrained and chopped | 1 |
| can no-sugar-added diced tomato | 2 |
| can no-sugar-added tomato sauce | 1 |
| can of crushed tomatoes or tomato puree | 2 |
| can of diced tomato | 1 |
| can of tomato sauce | 2 |
| can of whole tomatoes, crushed (save juice) | 2 |
| can or 2 (14-ounce) cans fire roasted diced tomatoes, lightly drained (recommended: muir glenn brand) | 1 |
| can or 2 (15-ounce) cans fire roasted diced tomato | 1 |
| can or 4 (18-ounce) cans whole italian tomato | 1 |
| can organic fire-roasted diced tomatoes (such as muir glen®) | 1 |
| can organic italian diced tomato | 1 |
| can organic plum tomatoes with juice | 1 |
| can peeled and crushed tomato | 2 |
| can peeled and crushed tomatoes, with liquid | 1 |
| can peeled and crushed, or diced tomato | 1 |
| can peeled and diced tomato | 26 |
| can peeled and diced tomatoes with juice | 15 |
| can peeled and diced tomatoes, drained | 6 |
| can peeled diced tomato | 1 |
| can peeled plum tomato | 6 |
| can peeled plum tomatoes, drained, crushed | 1 |
| can peeled plum tomatoes, pureed | 8 |
| can peeled plum tomatoes, with juice | 1 |
| can peeled plum tomatoes, with juices | 2 |
| can peeled san marzano tomatoes, crushed by hand | 1 |
| can peeled tomato | 4 |
| can peeled tomatoes in juice, drained, liquid reserved | 1 |
| can peeled tomatoes, crushed by hand | 1 |
| can peeled tomatoes, drained | 1 |
| can peeled tomatoes, drained and crushed by hand | 1 |
| can peeled whole plum tomato | 1 |
| can peeled whole tomato | 2 |
| can peeled, whole tomatoes, drained and chopped | 1 |
| can pelati tomatoes* | 1 |
| can pelati tomatoes, blended smooth | 1 |
| can petite diced or chunky style crushed tomato | 1 |
| can petite diced tomato | 16 |
| can petite diced tomatoes in juice | 2 |
| can petite diced tomatoes with chipotle | 1 |
| can petite diced tomatoes with green chiles | 1 |
| can petite diced tomatoes, drained | 4 |
| can petite diced tomatoes, drained and rinsed | 1 |
| can petite diced tomatoes, preferably fire roasted | 3 |
| can petite diced tomatoes, undrained | 2 |
| can petite diced tomatoes, well drained | 1 |
| can petite diced, crushed or stewed tomato | 1 |
| can petite tomatoes in juice | 1 |
| can petite-cut diced tomatoes with garlic and olive oil | 1 |
| can plain crushed tomato | 1 |
| can plain tomato | 1 |
| can plain tomato sauce | 1 |
| can plum tomato | 15 |
| can plum tomatoes (about 1 3/4 cups) | 1 |
| can plum tomatoes coarsely chopped, no juice | 1 |
| can plum tomatoes in juice | 1 |
| can plum tomatoes or 2 pounds fresh tomatoes (about 4 to 6), medium diced | 1 |
| can plum tomatoes with juices, crushed | 1 |
| can plum tomatoes, crushed | 1 |
| can plum tomatoes, crushed fine | 1 |
| can plum tomatoes, drained | 4 |
| can plum tomatoes, drained and chopped | 1 |
| can plum tomatoes, drained and chopped (or 8 vine ripened tomato | 3 |
| can plum tomatoes, drained and chopped juices reserved | 1 |
| can plum tomatoes, drained and diced | 1 |
| can plum tomatoes, drained well and coarsely chopped | 1 |
| can plum tomatoes, drained, (reserve 1/2 cup juice) and chopped | 1 |
| can plum tomatoes, including liquid | 1 |
| can plum tomatoes, juice discarded and tomatoes chopped and drained well | 1 |
| can plum tomatoes, juice strained | 1 |
| can plum tomatoes, not drained | 1 |
| can plum tomatoes, preferably san marzano | 1 |
| can plum tomatoes, pureed | 1 |
| can plum tomatoes, pureed until smooth | 1 |
| can plum tomatoes, the juice discarded and the tomatoes chopped and drained well | 1 |
| can plum tomatoes, undrained | 1 |
| can plum tomatoes, unsalted and crushed | 1 |
| can plum tomatoes, with their juice | 1 |
| can plus 1 (14 1/2-ounce) can diced tomatoes, with their juice | 1 |
| can pork and beans in tomato sauce | 1 |
| can pureed tomato | 3 |
| can red gold® crushed tomato | 5 |
| can red gold® diced tomato | 5 |
| can red gold® diced tomatoes chili ready | 1 |
| can red gold® diced tomatoes, drained | 2 |
| can red gold® petite diced tomatoes & green chilies | 2 |
| can red gold® petite diced tomatoes with chipotle | 1 |
| can red gold® petite diced tomatoes with garlic & olive oil, well drained | 1 |
| can red gold® petite diced tomatoes with lime juice & cilantro | 1 |
| can red gold® petite diced tomatoes with onion, celery & green pepper | 1 |
| can red gold® petite diced tomatoes, drained | 1 |
| can ro*tel diced tomatoes and green chilies, drained | 1 |
| can ro*tel diced tomatoes and green chilies, undrained | 3 |
| can ro*tel® hot diced tomatoes with habaneros, undrained | 1 |
| can ro*tel® original diced tomatoes & green chilies, drained | 2 |
| can ro*tel® original diced tomatoes & green chilies, undrained | 5 |
| can roasted garlic tomato paste | 1 |
| can roma tomatoes (crushed) | 1 |
| can roma tomatoes, with juice | 3 |
| can rotel diced tomatoes and green chiles, drained, squeezed dry | 1 |
| can sacramento tomato juice | 1 |
| can san marzano tomato | 8 |
| can san marzano tomatoes for sweeter stew, or diced fire roasted tomatoes, for smokier stew | 1 |
| can san marzano tomatoes with juices | 2 |
| can san marzano tomatoes, drained, hand-crushed with juice reserved | 1 |
| can san marzano tomatoes, passed through a food mill | 1 |
| can san marzano tomatoes, passed through the food mill | 1 |
| can san marzano tomatoes, with their juice | 1 |
| can san marzano whole tomato | 1 |
| can seasoned tomato sauce | 1 |
| can spiced tomatoes with green chiles | 1 |
| can stewed diced tomato | 1 |
| can stewed tomato | 95 |
| can stewed tomatoes (optional) | 1 |
| can stewed tomatoes (such as del monte® stewed tomatoes with onions, celery, and green peppers) | 1 |
| can stewed tomatoes (with garlic and herbs) | 1 |
| can stewed tomatoes (with juice) | 1 |
| can stewed tomatoes including juice | 3 |
| can stewed tomatoes or diced tomatoes with chiles | 1 |
| can stewed tomatoes with juice | 3 |
| can stewed tomatoes with peppers, onions and celery | 1 |
| can stewed tomatoes, blended | 1 |
| can stewed tomatoes, crushed | 1 |
| can stewed tomatoes, cut in half and drained | 1 |
| can stewed tomatoes, cut small | 1 |
| can stewed tomatoes, cut up | 1 |
| can stewed tomatoes, cut up in juice | 1 |
| can stewed tomatoes, drained | 8 |
| can stewed tomatoes, drained and sliced | 2 |
| can stewed tomatoes, drained, reserving juice, and coarsely chopped | 1 |
| can stewed tomatoes, lightly drained | 2 |
| can stewed tomatoes, not drained | 1 |
| can stewed tomatoes, puréed in a blender or food processor | 1 |
| can stewed tomatoes, undrained | 10 |
| can stewed tomatoes, with juice | 4 |
| can stewed tomatoes, with liquid | 8 |
| can stewed tomatoes, with their juices | 1 |
| can tex mex-style diced tomato | 1 |
| can tomato | 13 |
| can tomato bisque | 1 |
| can tomato juice | 32 |
| can tomato juice (optional) | 1 |
| can tomato juice, or more to taste | 1 |
| can tomato paste | 313 |
| can tomato paste (such as contadina®) | 1 |
| can tomato paste with roasted garlic | 1 |
| can tomato paste, for sauce and ribs | 1 |
| can tomato paste, or more as needed | 1 |
| can tomato paste, or more to taste | 1 |
| can tomato paste, or to taste | 2 |
| can tomato paste, or to taste (optional) | 1 |
| can tomato puree | 53 |
| can tomato puree (no salt added) | 1 |
| can tomato puree (such as contadina® tomato puree) | 1 |
| can tomato salsa | 1 |
| can tomato sauce | 540 |
| can tomato sauce (recommended: hunt's) | 4 |
| can tomato sauce (such as dei fratelli®) | 1 |
| can tomato sauce (such as del monte®) | 1 |
| can tomato sauce (such as goya®) | 1 |
| can tomato sauce (such as hunt's®) | 3 |
| can tomato sauce or tomato puree | 2 |
| can tomato sauce plus 1 can water | 1 |
| can tomato sauce with garlic and onion | 1 |
| can tomato sauce, or more if needed | 1 |
| can tomato sauce, or to taste | 1 |
| can tomato soup | 18 |
| can tomato soup (not condensed) (optional) | 1 |
| can tomato soup (optional) | 1 |
| can tomato soup (such as campbell's®) | 4 |
| can tomato soup, undiluted | 1 |
| can tomato-vegetable juice cocktail | 6 |
| can tomato-vegetable juice cocktail (such as v8®) | 3 |
| can tomatoes (recommended: san marzano) | 7 |
| can tomatoes (whole or diced) | 1 |
| can tomatoes or 3 to 4 fresh tomato | 1 |
| can tomatoes with green chiles | 1 |
| can tomatoes with green chiles, mild version | 1 |
| can tomatoes with green chiles, not drained | 1 |
| can tomatoes with juice | 1 |
| can tomatoes with liquid | 1 |
| can tomatoes with their juices | 1 |
| can tomatoes, drained (recommended: ro-tel) | 1 |
| can tomatoes, drained and chopped | 2 |
| can tomatoes, drained, hand-crushed with juice reserved (recommended: san marzano) | 1 |
| can tomatoes, including liquid | 1 |
| can tomatoes, preferably san marzano | 1 |
| can tomatoes, whole | 1 |
| can water-packed tomatoes (do not drain) | 1 |
| can whole italian paste tomatoes (such as san marzano), drained and torn into large chunks | 1 |
| can whole italian peeled plum tomato | 1 |
| can whole italian plum tomatoes (such as san marzano) | 1 |
| can whole italian plum tomatoes (such as san marzano), crushed | 1 |
| can whole italian tomato | 5 |
| can whole or chopped tomato | 1 |
| can whole or crushed san marzano tomato | 1 |
| can whole or diced tomatoes (recommended: san marzano) | 2 |
| can whole peeled or diced tomato | 1 |
| can whole peeled organic tomatoes in juice | 1 |
| can whole peeled plum tomato | 1 |
| can whole peeled plum tomatoes with juice | 1 |
| can whole peeled tomato | 60 |
| can whole peeled tomatoes (pelati) | 1 |
| can whole peeled tomatoes (preferably san marzano) | 2 |
| can whole peeled tomatoes (preferably san marzano), crushed | 1 |
| can whole peeled tomatoes (recommended: muir glen) | 1 |
| can whole peeled tomatoes (recommended: san marzano) | 1 |
| can whole peeled tomatoes in juice | 1 |
| can whole peeled tomatoes in juice, crushed by hand | 1 |
| can whole peeled tomatoes in juice, cut into 1/2-inch dice | 1 |
| can whole peeled tomatoes in juice, drained (about 5 tomatoes) | 1 |
| can whole peeled tomatoes with basil, pureed (recommended: progresso) | 1 |
| can whole peeled tomatoes with juice | 6 |
| can whole peeled tomatoes with liquid | 5 |
| can whole peeled tomatoes with liquid, mashed | 1 |
| can whole peeled tomatoes, broken apart by hand | 1 |
| can whole peeled tomatoes, broken into smaller pieces, with their liquid | 1 |
| can whole peeled tomatoes, crushed | 3 |
| can whole peeled tomatoes, crushed, juice reserved | 1 |
| can whole peeled tomatoes, drained | 6 |
| can whole peeled tomatoes, drained and chopped | 7 |
| can whole peeled tomatoes, drained and chopped, liquid reserved | 1 |
| can whole peeled tomatoes, drained and hand crushed | 1 |
| can whole peeled tomatoes, drained and hand crushed (recommended: san marzano) | 1 |
| can whole peeled tomatoes, drained and hand crushed, liquid reserved | 1 |
| can whole peeled tomatoes, drained and mashed | 1 |
| can whole peeled tomatoes, hand crushed | 1 |
| can whole peeled tomatoes, hand-crushed | 1 |
| can whole peeled tomatoes, in juice | 1 |
| can whole peeled tomatoes, mashed | 3 |
| can whole peeled tomatoes, mashed, liquid reserved | 1 |
| can whole peeled tomatoes, preferably italian san marzano, drained | 1 |
| can whole peeled tomatoes, preferably san marzano, drained | 1 |
| can whole peeled tomatoes, pureed with their juice | 1 |
| can whole peeled tomatoes, quartered | 1 |
| can whole peeled tomatoes, smashed with hands | 1 |
| can whole peeled tomatoes, undrained | 2 |
| can whole peeled tomatoes, undrained and chopped | 2 |
| can whole peeled tomatoes, with liquid | 10 |
| can whole peeled tomatoes, with their juice | 3 |
| can whole peeled tomatoes, with their juices | 1 |
| can whole plum tomato | 1 |
| can whole plum tomatoes in juice | 1 |
| can whole plum tomatoes in puree | 1 |
| can whole plum tomatoes including juice | 1 |
| can whole plum tomatoes with juice (not in purée) | 1 |
| can whole plum tomatoes, drained and chopped | 1 |
| can whole plum tomatoes, drained, reserving juice, and chopped | 1 |
| can whole plum tomatoes, passed through a food mill | 1 |
| can whole plum tomatoes, undrained and quartered | 1 |
| can whole plum tomatoes, with their juices | 1 |
| can whole san marzano tomato | 1 |
| can whole san marzano tomatoes in juice | 1 |
| can whole san marzano tomatoes in juice, juice reserved and tomatoes coarsely chopped | 1 |
| can whole san marzano tomatoes in juice, puréed in a blender with juice | 1 |
| can whole san marzano tomatoes, crushed by hand | 1 |
| can whole san marzano tomatoes, hand-crushed | 3 |
| can whole stewed tomato | 2 |
| can whole tomato | 24 |
| can whole tomatoes (recommended: san marzano) | 3 |
| can whole tomatoes in juice | 31 |
| can whole tomatoes in juice (preferably italian) | 3 |
| can whole tomatoes in juice (preferably san marzano), drained and chopped | 1 |
| can whole tomatoes in juice, drained | 1 |
| can whole tomatoes in juice, drained and chopped | 2 |
| can whole tomatoes in juice, drained and chopped (1 cup) | 1 |
| can whole tomatoes in juice, drained and coarsely chopped | 2 |
| can whole tomatoes in juice, drained and juices reserved | 1 |
| can whole tomatoes in juice, drained, juice reserved and tomatoes chopped, or 1 3/4 pounds fresh tomato | 1 |
| can whole tomatoes in juice, drained, reserving 2 tablespoons juice, and chopped | 1 |
| can whole tomatoes in juice, drained, reserving juice, and chopped | 5 |
| can whole tomatoes in juice, drained, reserving juice, and coarsely chopped | 1 |
| can whole tomatoes in juice, drained, seeded, and finely chopped | 1 |
| can whole tomatoes in juice, forced with juices through a food mill (1 1/2 cups) | 1 |
| can whole tomatoes in juice, including juice | 1 |
| can whole tomatoes in juice, juice reserved and tomatoes coarsely chopped | 1 |
| can whole tomatoes in juice, pulsed (including juice) in food processor until chopped | 1 |
| can whole tomatoes in juice, tomatoes chopped, reserving juice | 1 |
| can whole tomatoes in juice, with juice reserved | 1 |
| can whole tomatoes in puree | 2 |
| can whole tomatoes in puree, crushed | 1 |
| can whole tomatoes in purée | 4 |
| can whole tomatoes including juice | 1 |
| can whole tomatoes with basil | 1 |
| can whole tomatoes with juice | 4 |
| can whole tomatoes with juice, lightly crushed with hands and pulp removed | 1 |
| can whole tomatoes, crushed | 1 |
| can whole tomatoes, crushed by hand | 3 |
| can whole tomatoes, crushed in a bowl | 1 |
| can whole tomatoes, drained | 7 |
| can whole tomatoes, drained and chopped | 3 |
| can whole tomatoes, drained and crushed | 1 |
| can whole tomatoes, drained and hand crushed | 1 |
| can whole tomatoes, drained and hand-crushed | 5 |
| can whole tomatoes, drained and pureed | 2 |
| can whole tomatoes, drained, and juice reserved | 1 |
| can whole tomatoes, drained, and seeded | 1 |
| can whole tomatoes, drained, rinsed, patted dry | 1 |
| can whole tomatoes, hand-crushed | 1 |
| can whole tomatoes, hand-crushed (recommended: san marzano) | 1 |
| can whole tomatoes, in juice | 2 |
| can whole tomatoes, in thick puree | 1 |
| can whole tomatoes, including juice | 2 |
| can whole tomatoes, including liquid | 1 |
| can whole tomatoes, or 5 large fresh tomatoes chopped | 1 |
| can whole tomatoes, roughly pureed or crushed by hand | 1 |
| can whole tomatoes, such as san marzano, with half of the juice strained out, and crushed with your fingers | 1 |
| can whole tomatoes, undrained | 1 |
| can whole tomatoes, undrained and chopped | 1 |
| can whole tomatoes, with their juice, crushed | 1 |
| can, crushed tomato | 4 |
| can, tomato sauce | 1 |
| canned chopped san marzano tomato | 1 |
| canned chopped san marzano tomatoes, with juice | 1 |
| canned chopped tomato | 8 |
| canned chopped tomatoes and green chiles, such as ro*tel | 1 |
| canned chopped tomatoes in juice | 1 |
| canned chopped tomatoes with their juices | 1 |
| canned chopped tomatoes, drained | 1 |
| canned chopped tomatoes, such as bel aria | 1 |
| canned chopped tomatoes, undrained | 1 |
| canned crushed fire-roasted tomato | 1 |
| canned crushed plum tomatoes, with their juices | 1 |
| canned crushed roasted tomato | 1 |
| canned crushed tomato | 43 |
| canned crushed tomatoes (15-ounce can) | 1 |
| canned crushed tomatoes (from a 28-oz can) | 1 |
| canned crushed tomatoes (such as san marzano®) | 1 |
| canned crushed tomatoes in heavy purée | 1 |
| canned crushed tomatoes in puree | 1 |
| canned crushed tomatoes in puree (from one 28-ounce can) | 1 |
| canned crushed tomatoes in puree, such as redpack | 1 |
| canned crushed tomatoes in purée | 1 |
| canned crushed tomatoes or 1 (16-ounce) can diced tomatoes, drained very well | 2 |
| canned crushed tomatoes or 2 cups peeled | 1 |
| canned crushed tomatoes or tomato puree | 1 |
| canned crushed tomatoes with added puree | 15 |
| canned crushed tomatoes with added puree (from 28-ounce can) | 1 |
| canned crushed tomatoes with added puree (from two 28-ounce cans) | 1 |
| canned crushed tomatoes with added purée | 1 |
| canned crushed tomatoes with juice | 1 |
| canned crushed tomatoes with puree (14 ounces) | 2 |
| canned crushed tomatoes, drained | 1 |
| canned crushed tomatoes, with their juice | 1 |
| canned diced fire roasted tomatoes (or canned | 1 |
| canned diced fire-roasted tomatoes with green chiles | 1 |
| canned diced peeled tomatoes with juices | 1 |
| canned diced plum tomatoes, with the juices reserved | 1 |
| canned diced san marzano tomato | 4 |
| canned diced tomato | 19 |
| canned diced tomatoes in juice | 3 |
| canned diced tomatoes in juice (from two 14.5-ounce cans) | 1 |
| canned diced tomatoes including juice | 1 |
| canned diced tomatoes or diced fresh tomato | 1 |
| canned diced tomatoes with green chiles | 1 |
| canned diced tomatoes with juice | 1 |
| canned diced tomatoes with juices | 2 |
| canned diced tomatoes with their juice | 1 |
| canned diced tomatoes, drained | 5 |
| canned diced tomatoes, drained (15-ounce can) | 1 |
| canned diced tomatoes, drained and juices reserved | 1 |
| canned diced tomatoes, undrained | 3 |
| canned diced tomatoes, with juices | 1 |
| canned fire-roasted diced tomato | 3 |
| canned imported tomato | 1 |
| canned italian plum tomato | 3 |
| canned italian plum tomatoes, with juice | 1 |
| canned italian plum tomatoes, with their juices | 1 |
| canned italian tomatoes, passed through a food mill | 1 |
| canned italian-style tomatoes with juice | 1 |
| canned low-sodium diced tomatoes, with juice | 1 |
| canned no-salt-added tomato sauce | 1 |
| canned no-sodium stewed tomato | 1 |
| canned or fresh ripe tomato | 1 |
| canned or fresh tomato | 1 |
| canned or fresh tomatoes (pureed and passed through a strainer) | 1 |
| canned or jarred tomato sauce | 1 |
| canned organic low-sodium tomato sauce | 1 |
| canned peeled and diced tomato | 2 |
| canned peeled tomato | 5 |
| canned peeled tomatoes, plus their juices | 1 |
| canned peeled tomatoes, seeded and coarsely chopped | 1 |
| canned petite diced tomato | 1 |
| canned plum tomato | 13 |
| canned plum tomatoes and juices | 1 |
| canned plum tomatoes and juices, pureed | 5 |
| canned plum tomatoes and their juices | 2 |
| canned plum tomatoes and their juices, coarsely smashed | 1 |
| canned plum tomatoes and their juices, pureed | 1 |
| canned plum tomatoes and their juices, pureed until smooth and strained | 1 |
| canned plum tomatoes in thick puree, crushed up | 1 |
| canned plum tomatoes including the juice | 1 |
| canned plum tomatoes with juices | 1 |
| canned plum tomatoes with juices, pureed | 1 |
| canned plum tomatoes with their juices | 1 |
| canned plum tomatoes, crushed | 3 |
| canned plum tomatoes, crushed by hand, seeds removed | 2 |
| canned plum tomatoes, drained | 1 |
| canned plum tomatoes, drained and chopped | 3 |
| canned plum tomatoes, drained and coarsely chopped | 1 |
| canned plum tomatoes, drained and crushed | 2 |
| canned plum tomatoes, drained and cut with scissors or sliced into thin pieces | 2 |
| canned plum tomatoes, drained and diced | 1 |
| canned plum tomatoes, drained, seeded and diced | 1 |
| canned plum tomatoes, drained, seeded, and diced | 4 |
| canned plum tomatoes, halved and seeded | 1 |
| canned plum tomatoes, preferably san marzano | 1 |
| canned plum tomatoes, preferably san marzano, with their juices | 1 |
| canned plum tomatoes, pureed | 2 |
| canned plum tomatoes, seeded and chopped | 1 |
| canned plum tomatoes, seeds removed and roughly chopped | 1 |
| canned plum tomatoes, seeds removed and slightly crushed | 1 |
| canned plum tomatoes, undrained (about 1 cup) | 1 |
| canned plum tomatoes, well drained and coarsely chopped | 1 |
| canned plum tomatoes, with juice, pureed | 1 |
| canned plum tomatoes, with their juice | 1 |
| canned plum tomatoes, with their juices | 1 |
| canned plums tomatoes, drained and chopped (reserve 2/3 cup of the juice) | 1 |
| canned puree tomato | 2 |
| canned pureed peeled tomato | 1 |
| canned pureed tomato | 2 |
| canned pureed tomatoes, about five 15-ounce cans (recommended: di napoli, san marzano-style) | 1 |
| canned ready-cut italian-style tomatoes, with juices | 1 |
| canned roma (plum) tomatoes, seeded and diced | 1 |
| canned roma tomato | 1 |
| canned roma tomatoes, with liquid | 1 |
| canned san marzano peeled tomato | 1 |
| canned san marzano plum tomatoes, drained | 1 |
| canned san marzano tomato | 2 |
| canned san marzano tomato sauce | 1 |
| canned san marzano tomatoes, hand crushed | 1 |
| canned san marzano whole plum tomatoes, drained of their liquid and broken into small pieces | 1 |
| canned san marzano-style peeled plum tomato | 1 |
| canned stewed tomato | 4 |
| canned stewed tomatoes, strained and coarsely chopped | 1 |
| canned tomato | 18 |
| canned tomato juice | 8 |
| canned tomato paste | 2 |
| canned tomato puree | 12 |
| canned tomato puree or sauce | 1 |
| canned tomato purée | 8 |
| canned tomato purée (see cook's notes for a fresh-tomato alternative) | 1 |
| canned tomato sauce | 30 |
| canned tomato sauce or canned crushed tomato | 1 |
| canned tomato sauce, 8 ounces | 1 |
| canned tomato soup, undiluted | 2 |
| canned tomato-vegetable juice (such as v-8) | 1 |
| canned tomatoes ( recommended: san marzano), hand crushed | 1 |
| canned tomatoes (preferably home- canned), with their liquid | 1 |
| canned tomatoes and juices, crushed | 1 |
| canned tomatoes drained | 1 |
| canned tomatoes with juices, crushed | 1 |
| canned tomatoes, drained | 1 |
| canned tomatoes, drained and coarsely chopped | 1 |
| canned tomatoes, half-drained | 1 |
| canned tomatoes, rough chopped | 1 |
| canned unsalted diced tomato | 1 |
| canned whole or crushed plum tomato | 1 |
| canned whole peeled plum tomatoes, crushed by hand | 1 |
| canned whole peeled tomato | 2 |
| canned whole peeled tomatoes (pelati) | 1 |
| canned whole peeled tomatoes with their juice | 1 |
| canned whole peeled tomatoes, crushed | 1 |
| canned whole peeled tomatoes, crushed by hand | 1 |
| canned whole peeled tomatoes, with their juices | 1 |
| canned whole plum tomato | 3 |
| canned whole plum tomatoes (about one 35-ounce can) | 1 |
| canned whole plum tomatoes, drained, seeded, and coarsely chopped | 1 |
| canned whole plum tomatoes, drained, seeded, and diced | 1 |
| canned whole plum tomatoes, pulsed in a food processor to puree | 1 |
| canned whole plum tomatoes, salsa marinara, or your own favorite tomato sauce | 1 |
| canned whole roma tomatoes, hand crushed | 1 |
| canned whole san marzano tomato | 1 |
| canned whole san marzano tomatoes (with liquid from the can) | 1 |
| canned whole san marzano tomatoes, crushed by hand | 2 |
| canned whole san marzano tomatoes, plus liquid from the can | 3 |
| canned whole tomato | 13 |
| canned whole tomatoes (crushed with juice) | 1 |
| canned whole tomatoes (preferably san marzano) | 1 |
| canned whole tomatoes in juice | 1 |
| canned whole tomatoes in juice (from a 28-ounce can), cut into 1/2-inch diced (measured with their juice) | 1 |
| canned whole tomatoes with basil | 1 |
| canned whole tomatoes with juice | 1 |
| canned whole tomatoes, crushed | 2 |
| canned whole tomatoes, crushed by hands | 1 |
| canned whole tomatoes, crushed, reserving juices | 1 |
| canned whole tomatoes, drained and chopped | 1 |
| canned, crushed tomato | 2 |
| canned, whole peeled tomato | 1 |
| canola oil (if roasting tomato) | 1 |
| canola oil, plus more for brushing on the tomato | 1 |
| canola oil, plus more for brushing tomato | 1 |
| cans canned diced tomatoes with their juice | 2 |
| cans canned diced tomatoes, drained | 1 |
| cans canned tomato | 2 |
| cans canned tomato sauce | 1 |
| cans canned tomatoes, flavored with garlic | 1 |
| cans chopped canned tomato | 1 |
| cans chopped plum tomato | 1 |
| cans chopped stewed tomatoes, with juice | 1 |
| cans chopped tomato | 13 |
| cans chopped tomatoes in their juice | 1 |
| cans chopped tomatoes with juice | 1 |
| cans chopped tomatoes, undrained | 1 |
| cans chunky style crushed tomato | 2 |
| cans condensed tomato soup | 31 |
| cans contadina® diced tomatoes with roasted garlic, undrained | 1 |
| cans contadina® diced tomatoes, undrained | 2 |
| cans contadina® tomato sauce | 1 |
| cans crushed diced tomato | 1 |
| cans crushed italian (plum) tomatoes (such as san marzano) | 1 |
| cans crushed plum tomato | 1 |
| cans crushed plum tomatoes with basil (recommended: redpack brand) | 1 |
| cans crushed tomato | 68 |
| cans crushed tomatoes (recommended: san marzano) | 2 |
| cans crushed tomatoes and their juice | 1 |
| cans crushed tomatoes or vegetable tomato juice | 1 |
| cans crushed tomatoes with juice | 1 |
| cans crushed tomatoes with juice (such as hunt's®) | 1 |
| cans crushed tomatoes, preferably san marzanos | 1 |
| cans crushed tomatoes, with liquid | 1 |
| cans crushed tomatoes, with their liquid | 1 |
| cans diced chili-style tomato | 1 |
| cans diced stewed tomato | 1 |
| cans diced stewed tomatoes with chili seasonings | 2 |
| cans diced tomato | 82 |
| cans diced tomatoes (28 ounces each) | 1 |
| cans diced tomatoes (i use hunt's petite diced) | 1 |
| cans diced tomatoes (italian style preferred, not required) | 1 |
| cans diced tomatoes (no salt added) | 1 |
| cans diced tomatoes and green chiles | 3 |
| cans diced tomatoes and green chiles, undrained | 1 |
| cans diced tomatoes and green chilies, drained | 1 |
| cans diced tomatoes in juice | 6 |
| cans diced tomatoes in puree | 1 |
| cans diced tomatoes including juice | 1 |
| cans diced tomatoes with basil, garlic and oregano | 1 |
| cans diced tomatoes with garlic and basil, drained | 1 |
| cans diced tomatoes with green chile pepper | 22 |
| cans diced tomatoes with green chile peppers (such as ro*tel®) | 8 |
| cans diced tomatoes with green chile peppers (such as ro*tel®), drained | 1 |
| cans diced tomatoes with green chile peppers (such as ro*tel®), undrained | 2 |
| cans diced tomatoes with green chile peppers, drained | 3 |
| cans diced tomatoes with green chile peppers, liquid drained and reserved | 1 |
| cans diced tomatoes with green chile peppers, partially drained | 1 |
| cans diced tomatoes with green chiles drained | 1 |
| cans diced tomatoes with green chilies, drained | 1 |
| cans diced tomatoes with green chilies, undrained | 3 |
| cans diced tomatoes with green chilies, with their liquid | 1 |
| cans diced tomatoes with green peppers, celery and onion | 1 |
| cans diced tomatoes with jalapeno pepper | 1 |
| cans diced tomatoes with jalapenos | 1 |
| cans diced tomatoes with juice | 11 |
| cans diced tomatoes with juices | 1 |
| cans diced tomatoes with seasonings (green pepper and onion or garlic and oregano, or any flavor you want) | 1 |
| cans diced tomatoes, drained | 14 |
| cans diced tomatoes, drained and crushed with your hands | 1 |
| cans diced tomatoes, drained and juice reserved | 1 |
| cans diced tomatoes, drained and rinsed | 1 |
| cans diced tomatoes, in juice | 1 |
| cans diced tomatoes, or more to taste | 1 |
| cans diced tomatoes, undrained | 10 |
| cans diced tomatoes, with juice | 1 |
| cans diced tomatoes, with liquid | 1 |
| cans fire roasted diced tomatoes, drained | 1 |
| cans fire-roasted diced tomato | 8 |
| cans fire-roasted diced tomatoes with juice | 1 |
| cans fire-roasted diced tomatoes, drained | 1 |
| cans fire-roasted diced tomatoes, undrained | 1 |
| cans fire-roasted tomatoes with garlic (such as hunt's®), drained | 1 |
| cans good italian plum tomato | 1 |
| cans good quality plum tomato | 1 |
| cans good quality whole peeled tomatoes (recommended: tuttorosso brand) | 1 |
| cans good-quality peeled plum tomato | 1 |
| cans goya tomato sauce | 1 |
| cans hot tomato sauce | 1 |
| cans hunt's® diced tomato | 1 |
| cans hunt's® diced tomatoes, undrained | 3 |
| cans hunt's® fire roasted diced tomatoes, undrained | 1 |
| cans hunt's® no salt added petite diced tomatoes, drained | 1 |
| cans hunt's® petite diced tomatoes, undrained | 2 |
| cans hunt's® tomato sauce | 2 |
| cans imported crushed tomato | 2 |
| cans imported italian plum tomato | 1 |
| cans imported italian plum tomatoes with basil, preferably san marzano tomato | 1 |
| cans imported san marzano italian plum tomatoes, hand-crushed | 1 |
| cans imported san marzano tomato | 1 |
| cans italian diced tomatoes, drained | 1 |
| cans italian plum san marzano tomato | 3 |
| cans italian plum tomatoes in juice, drained, reserving juice, and finely chopped | 1 |
| cans italian plum tomatoes, drained and chopped, reserving liquid from one can | 1 |
| cans italian plum tomatoes, passed through the food mill or pureed | 1 |
| cans italian pureed tomato | 1 |
| cans italian stewed tomato | 1 |
| cans italian whole tomatoes, seeded and drained | 1 |
| cans italian-flavored crushed tomato | 1 |
| cans italian-style diced tomato | 6 |
| cans italian-style diced tomatoes with juice | 1 |
| cans italian-style diced tomatoes, drained | 2 |
| cans italian-style peeled tomatoes (such as cento® san marzano) | 1 |
| cans italian-style stewed tomato | 3 |
| cans low sodium tomato soup | 1 |
| cans low-sodium stewed tomato | 1 |
| cans mexican diced tomatoes (recommended: ro'tel) | 1 |
| cans mexican-style diced tomato | 1 |
| cans mexican-style diced tomatoes and green chilies with cilantro and lime juice (such as ro*tel®), drained | 1 |
| cans mexican-style diced tomatoes, undrained | 1 |
| cans mexican-style stewed tomato | 3 |
| cans no salt added diced tomatoes. with juice | 2 |
| cans no-salt-added diced tomato | 1 |
| cans no-salt-added tomato | 1 |
| cans no-salt-added tomato sauce | 1 |
| cans of good-quality plum tomato | 1 |
| cans of imported italian tomato | 1 |
| cans of no-salt-added diced tomatoes, with their juices | 1 |
| cans of peeled whole tomatoes (hand crushed with juice added) | 1 |
| cans of tomato paste | 1 |
| cans of tomatoes, crushed and mixed well with their juices | 2 |
| cans of whole tomato | 1 |
| cans or 1 (28-ounce) can crushed or diced fire roasted tomato | 1 |
| cans or 1 (28-ounce) can crushed tomato | 1 |
| cans peeled and diced tomato | 14 |
| cans peeled and diced tomatoes with juice | 5 |
| cans peeled and diced tomatoes, drained | 2 |
| cans peeled and diced tomatoes, juice reserved | 1 |
| cans peeled ground tomato | 1 |
| cans peeled pear tomato | 1 |
| cans peeled plum tomato | 1 |
| cans peeled tomato | 1 |
| cans peeled whole tomatoes (gently hand crushed, with juice reserved) | 1 |
| cans peeled whole tomatoes, crushed by hand and juices reserved | 3 |
| cans peeled whole tomatoes, crushed by hand, juices reserved | 1 |
| cans peeled whole tomatoes, pureed and strained | 1 |
| cans pelati tomatoes* (see cook's notes) | 1 |
| cans petite diced tomato | 6 |
| cans petite diced tomatoes in juice | 1 |
| cans petite diced tomatoes in juice, drained | 1 |
| cans petite-cut tomatoes with onions and roasted garlic, undrained | 1 |
| cans plum tomato | 2 |
| cans plum tomatoes (about 6 cups) | 1 |
| cans plum tomatoes and their juice, mashed up with a whisk | 1 |
| cans plum tomatoes and their juice, pureed in a blender | 1 |
| cans plum tomatoes and their juices, crushed with your hands | 2 |
| cans plum tomatoes with basil | 1 |
| cans plum tomatoes, drained | 1 |
| cans plum tomatoes, including juice | 1 |
| cans plum tomatoes, pureed in a blender | 1 |
| cans red gold® diced tomatoes with basil, garlic & oregano | 1 |
| cans red gold® fresh squeezed tomato juice | 1 |
| cans red gold® petite diced tomatoes & green chilies | 1 |
| cans red gold® petite diced tomatoes with garlic & olive oil | 1 |
| cans red gold® whole peeled tomato | 1 |
| cans reduced-sodium creamy tomato soup with 4g fat or less per serving (recommended: amy's organic light in sodium chunky tomato bisque) | 1 |
| cans ro*tel diced tomatoes & green chilies | 1 |
| cans ro*tel® original diced tomatoes & green chilies | 1 |
| cans ro*tel® original diced tomatoes & green chilies, drained | 1 |
| cans roasted diced tomato | 1 |
| cans roma tomatoes, with juice | 1 |
| cans san marzano plum tomato | 1 |
| cans san marzano tomato | 3 |
| cans san marzano tomatoes, passed through the food mill | 1 |
| cans san marzano-style peeled plum tomatoes with basil | 1 |
| cans seasoned tomato sauce | 1 |
| cans stewed italian tomato | 1 |
| cans stewed tomato | 53 |
| cans stewed tomatoes including liquid | 1 |
| cans stewed tomatoes with juice | 3 |
| cans stewed tomatoes with juices | 1 |
| cans stewed tomatoes, drained | 1 |
| cans stewed tomatoes, undrained | 2 |
| cans stewed tomatoes, undrained, crushed | 1 |
| cans stewed tomatoes, with juice | 1 |
| cans tomato | 3 |
| cans tomato juice | 5 |
| cans tomato juice, or as needed | 1 |
| cans tomato paste | 66 |
| cans tomato paste (such as hunt's®) | 1 |
| cans tomato paste with basil (such as hunt's®) | 1 |
| cans tomato paste, or as needed | 1 |
| cans tomato puree | 8 |
| cans tomato puree (28 ounces each) | 1 |
| cans tomato sauce | 139 |
| cans tomato sauce (such as hunt's®) | 2 |
| cans tomato sauce with mushrooms | 1 |
| cans tomato soup | 5 |
| cans tomato-vegetable juice cocktail | 1 |
| cans tomato-vegetable juice cocktail (such as v8®) | 1 |
| cans tomatoes (recommended: rotel brand) | 1 |
| cans tomatoes (recommended: san marzano) | 2 |
| cans tomatoes (recommended: san marzano), crushed by hand | 1 |
| cans tomatoes with chiles | 1 |
| cans tomatoes with green pepper, celery and onion | 1 |
| cans tomatoes, crushed by hand | 1 |
| cans tomatoes, drained and chopped | 1 |
| cans tomatoes, including juice, pureed course in a blender in 2 batches | 1 |
| cans tomatoes, undrained | 1 |
| cans unseasoned tomato sauce | 1 |
| cans whole italian plum tomato | 3 |
| cans whole italian tomatoes, drained, reserving juice, and chopped into 1/4 to 1/2-inch pieces | 1 |
| cans whole peeled italian tomatoes, undrained | 1 |
| cans whole peeled plum tomatoes in puree, undrained | 1 |
| cans whole peeled plum tomatoes, drained and roughly chopped (juice reserved) | 1 |
| cans whole peeled roma tomato | 1 |
| cans whole peeled san marzano tomato | 2 |
| cans whole peeled tomato | 30 |
| cans whole peeled tomatoes with liquid | 3 |
| cans whole peeled tomatoes, 2 whole tomatoes reserved and 1/4 cup liquid reserved for spanish rice | 1 |
| cans whole peeled tomatoes, crushed | 4 |
| cans whole peeled tomatoes, drained | 3 |
| cans whole peeled tomatoes, drained and crushed by hand | 1 |
| cans whole peeled tomatoes, drained and hand crushed | 3 |
| cans whole peeled tomatoes, drained and hand-crushed | 3 |
| cans whole peeled tomatoes, drained, juices reserved,and chopped | 1 |
| cans whole peeled tomatoes, drained, puréed in a blender | 1 |
| cans whole peeled tomatoes, mashed | 2 |
| cans whole peeled tomatoes, mashed, liquid reserved | 1 |
| cans whole peeled tomatoes, preferably san marzano, drained, puréed | 1 |
| cans whole peeled tomatoes, with juices (about 7 cups) | 1 |
| cans whole peeled tomatoes, with liquid | 2 |
| cans whole plum tomato | 2 |
| cans whole plum tomatoes (recommended: san marzano) | 1 |
| cans whole roma tomato | 1 |
| cans whole tomato | 11 |
| cans whole tomatoes in juice | 6 |
| cans whole tomatoes in juice (preferably italian) | 1 |
| cans whole tomatoes in juice (preferably organic) | 1 |
| cans whole tomatoes in juice (preferably san marzano) | 1 |
| cans whole tomatoes in juice, drained, reserving juice, and finely chopped | 1 |
| cans whole tomatoes in puree, pureed in a blender until smooth | 2 |
| cans whole tomatoes in purée, puréed in a blender until smooth | 1 |
| cans whole tomatoes including juice | 1 |
| cans whole tomatoes with juice | 1 |
| cans whole tomatoes with juice or crushed tomato | 1 |
| cans whole tomatoes, crushed by hand | 1 |
| cans whole tomatoes, cut into chunks | 1 |
| cans whole tomatoes, drained | 3 |
| cans whole tomatoes, drained and coarsely chopped* | 1 |
| cans whole tomatoes, hand crushed | 1 |
| cans whole tomatoes, undrained and chopped | 1 |
| cans) tomato paste | 1 |
| caper tomato relish, recipe follows | 1 |
| caramelized onion tomato jam, recipe follows | 1 |
| caramelized onion-tomato relish, recipe follows | 1 |
| carton campbell's® mexican style tomato soup | 2 |
| carton cherry tomato | 1 |
| center-cut slices from a small tomato | 1 |
| charred tomato coulis, recipe follows | 1 |
| charred tomato salsa, recipe follows, or your favorite green or red salsa | 1 |
| cheese, tomatoes, olives | 1 |
| cherokee purple tomatoes (about 12 ounces total) | 1 |
| cherry and/or pear tomatoes, halved | 1 |
| cherry and/or sun gold tomatoes, halved | 1 |
| cherry heirloom tomatoes, halved | 1 |
| cherry or grape tomato | 9 |
| cherry or grape tomatoes (1/4 pound), halved | 1 |
| cherry or grape tomatoes (3 cups), halved or, if large, quartered | 1 |
| cherry or grape tomatoes (3/4 lb), halved or quartered if large | 1 |
| cherry or grape tomatoes (about 40 tomatoes) | 1 |
| cherry or grape tomatoes, cut in 1/2 | 1 |
| cherry or grape tomatoes, halved | 20 |
| cherry or grape tomatoes, halved and tossed with some vinaigrette, for garnish | 1 |
| cherry or grape tomatoes, or more to taste | 1 |
| cherry or grape tomatoes, quartered | 3 |
| cherry or grape tomatoes, rinsed | 1 |
| cherry or grape tomatoes, rinsed and dried | 3 |
| cherry or pear red and yellow tomatoes, for garnish | 1 |
| cherry or pear tomato | 1 |
| cherry or pear tomatoes, cut in half | 1 |
| cherry or pear tomatoes, halved or quartered | 1 |
| cherry or pear, red and yellow tomatoes, for garnish | 1 |
| cherry tomato | 234 |
| cherry tomato half | 4 |
| cherry tomato sauce, recipe follows | 1 |
| cherry tomato vinaigrette (for serving) | 1 |
| cherry tomato, for garnish | 1 |
| cherry tomato, garnish | 1 |
| cherry tomato, halved | 1 |
| cherry tomatoes (1 pint), halved | 1 |
| cherry tomatoes (2 cups) | 1 |
| cherry tomatoes (20 large or 40 small) | 1 |
| cherry tomatoes (5 cups) | 1 |
| cherry tomatoes (about 1/2 pint) | 1 |
| cherry tomatoes (about 10 ounces), halved | 1 |
| cherry tomatoes (about 14) | 1 |
| cherry tomatoes (about 2 cups) | 1 |
| cherry tomatoes (about 28) | 1 |
| cherry tomatoes (about 3 1/2 cups) | 1 |
| cherry tomatoes (about 3 ounces), quartered | 1 |
| cherry tomatoes (about 3/4 pint) | 2 |
| cherry tomatoes (about 4 cups) | 1 |
| cherry tomatoes (about 4 cups), stemmed | 1 |
| cherry tomatoes (about 5 cups), trimmed if necessary | 1 |
| cherry tomatoes (about 6 cups) | 1 |
| cherry tomatoes (about 8 ounces), cut in half | 1 |
| cherry tomatoes (any color), halved | 1 |
| cherry tomatoes (optional) | 1 |
| cherry tomatoes (preferably assorted heirloom varieties), halved or quartered if large | 1 |
| cherry tomatoes (preferably heirloom) | 1 |
| cherry tomatoes (preferably mixed colors) | 1 |
| cherry tomatoes (preferably mixed colors), quartered if large | 1 |
| cherry tomatoes (preferably on the vine, cut into 4 bunches) | 1 |
| cherry tomatoes (such as sun gold) | 1 |
| cherry tomatoes and green cocktail olives each on sticks | 2 |
| cherry tomatoes cut in fourths | 1 |
| cherry tomatoes cut in half | 3 |
| cherry tomatoes for garnish | 1 |
| cherry tomatoes on the vine | 2 |
| cherry tomatoes or chopped plum tomato | 1 |
| cherry tomatoes or grape tomatoes, halved | 1 |
| cherry tomatoes or other small tomatoes on the vine | 1 |
| cherry tomatoes or small cocktail tomatoes, halved or quartered | 1 |
| cherry tomatoes sliced in half | 2 |
| cherry tomatoes, blanched and peeled | 1 |
| cherry tomatoes, cored | 1 |
| cherry tomatoes, cut in 1/2 | 6 |
| cherry tomatoes, cut in 1/4 | 1 |
| cherry tomatoes, cut in half | 23 |
| cherry tomatoes, cut in half (to serve) | 1 |
| cherry tomatoes, cut in half and salted | 1 |
| cherry tomatoes, cut in half on the diagonal | 1 |
| cherry tomatoes, cut in half, for garnish | 1 |
| cherry tomatoes, cut in half, for tossing with the greens | 1 |
| cherry tomatoes, cut into pieces | 1 |
| cherry tomatoes, cut into quarters | 3 |
| cherry tomatoes, different shapes and colors if you can find them | 1 |
| cherry tomatoes, each halved | 1 |
| cherry tomatoes, for garnish | 1 |
| cherry tomatoes, for garnish (optional) | 2 |
| cherry tomatoes, for garnishhalibut: | 1 |
| cherry tomatoes, for serving | 3 |
| cherry tomatoes, grape tomatoes, and/or pear tomato | 2 |
| cherry tomatoes, grape tomatoes, and/or pear tomatoes, halved | 1 |
| cherry tomatoes, halved | 255 |
| cherry tomatoes, halved (about 2/3 cup) | 1 |
| cherry tomatoes, halved (about 28) | 1 |
| cherry tomatoes, halved (optional) | 1 |
| cherry tomatoes, halved and lightly salted | 2 |
| cherry tomatoes, halved and seeded | 2 |
| cherry tomatoes, halved lengthwise | 3 |
| cherry tomatoes, halved lengthwise (2 2/3 cups) | 1 |
| cherry tomatoes, halved or 1 small tomato | 2 |
| cherry tomatoes, halved or quartered | 1 |
| cherry tomatoes, halved or quartered depending on size | 2 |
| cherry tomatoes, halved or quartered if large | 1 |
| cherry tomatoes, halved or quartered, depending on size | 1 |
| cherry tomatoes, halved through the stem | 1 |
| cherry tomatoes, halved, for garnish | 1 |
| cherry tomatoes, halved, or more to taste | 2 |
| cherry tomatoes, hulled | 1 |
| cherry tomatoes, left whole if small or halved | 1 |
| cherry tomatoes, on soaked skewers, for serving | 1 |
| cherry tomatoes, on the vine | 1 |
| cherry tomatoes, or 3 additional roma tomatoes, halved and seeded | 1 |
| cherry tomatoes, or as desired | 1 |
| cherry tomatoes, preferably on the vine | 1 |
| cherry tomatoes, quartered | 60 |
| cherry tomatoes, quartered (about 1 1/2 pints) | 1 |
| cherry tomatoes, quartered (about 1 cup) | 1 |
| cherry tomatoes, quartered (about 2 cups) | 1 |
| cherry tomatoes, quartered (optional) | 1 |
| cherry tomatoes, quartered and seeded | 1 |
| cherry tomatoes, quartered, or more as desired | 1 |
| cherry tomatoes, rinsed and halved | 1 |
| cherry tomatoes, roasted | 1 |
| cherry tomatoes, seeded and chopped | 1 |
| cherry tomatoes, seeded and minced | 1 |
| cherry tomatoes, skinned and seeded | 1 |
| cherry tomatoes, some quartered and the rest sliced in half | 1 |
| cherry tomatoes, stemmed | 1 |
| cherry tomatoes, stemmed and halved | 1 |
| cherry tomatoes, stemmed, halved | 2 |
| cherry tomatoes, stems removed and washed | 1 |
| cherry tomatoes, thinly sliced | 1 |
| cherry tomatoes, trimmed and halved | 1 |
| cherry tomatoes, very ripe and sweet | 1 |
| cherry tomatoes, whole | 1 |
| cherry tomatoes: 10 oz | 1 |
| chicken sausages, any flavors or brand, such as sun-dried tomato or garlic | 2 |
| chile relleno tomato sauce, for serving, recipe follows | 1 |
| chile-coconut tomato salad, recipe follows | 1 |
| chilled clamato juice, or 1 cup tomato juice and 1/2 cup bottled clam juice | 1 |
| chilled low-sodium tomato juice | 1 |
| chilled tomato and clam juice cocktail (such as clamato®) | 1 |
| chilled tomato juice | 4 |
| chilled tomato sauce | 1 |
| chipotle tomato sauce, recipe follows | 1 |
| chopped (or thinly sliced) sun-dried tomatoes (about 3 halves) | 1 |
| chopped and drained plum tomatoes from a can | 1 |
| chopped and drained ripe tomato | 1 |
| chopped and peeled tomato | 1 |
| chopped and seeded tomato | 1 |
| chopped canned chipotle chilies plus 1 tablespoon spicy tomato sauce reserved from can | 1 |
| chopped canned italian peeled tomato | 1 |
| chopped canned plum tomato | 6 |
| chopped canned plum tomatoes or leftover broth | 1 |
| chopped canned plum tomatoes, drained (4 ounces) | 1 |
| chopped canned plum tomatoes, with juices | 1 |
| chopped canned plum tomatoes, with some juice | 2 |
| chopped canned tomato | 14 |
| chopped canned tomato, seeds and juice removed | 1 |
| chopped canned tomatoes in heavy puree | 3 |
| chopped canned tomatoes with juice | 1 |
| chopped canned tomatoes, drained | 1 |
| chopped canned tomatoes, in heavy puree | 2 |
| chopped canned whole tomato | 1 |
| chopped cherry or grape tomato | 2 |
| chopped cherry tomato | 7 |
| chopped cherry tomatoes and pickled jalapenos, for topping (optional) | 1 |
| chopped cherry tomatoes, plus 1 cup halved cherry tomato | 1 |
| chopped cooked lobster or diced fresh plum tomato, and fresh tarragon, for garnish | 1 |
| chopped drained canned diced tomato | 1 |
| chopped drained canned italian plum tomato | 1 |
| chopped drained canned tomato | 6 |
| chopped drained oil-packed sun-dried tomato | 13 |
| chopped drained oil-packed sun-dried tomatoes (about one 7-1/2-ounce jar) | 1 |
| chopped drained oil-packed sun-dried tomatoes plus 2 tablespoons oil reserved from jar | 1 |
| chopped drained oil-packed sun-dried tomatoes, 1/4 cup oil reserved | 1 |
| chopped drained oil-packed sun-dried tomatoes, 2 tablespoons oil reserved | 1 |
| chopped drained sun-dried tomatoes (packed in oil) | 1 |
| chopped drained sun-dried tomatoes packed in oil | 1 |
| chopped drained sun-dried tomatoes packed in oil (about 1/4 pound) | 1 |
| chopped dried tomatoes packed in oil | 1 |
| chopped dry-pack sun-dried tomato | 1 |
| chopped fire-roasted tomatoes, drained | 1 |
| chopped fire-roasted tomatoes, with liquid | 1 |
| chopped fresh cilantro, halved cherry tomatoes, avocado wedges, queso fresco or mild feta | 1 |
| chopped fresh italian plum tomatoes, with juices | 1 |
| chopped fresh or canned tomato | 3 |
| chopped fresh plum tomato | 1 |
| chopped fresh tomato | 49 |
| chopped fresh tomato (optional) | 1 |
| chopped fresh tomatoes (3 medium tomatoes) or drained whole roma tomato | 2 |
| chopped fresh tomatoes (3 medium) | 1 |
| chopped fresh tomatoes, with their seeds, or 1 28‑ounce can diced tomatoes, undrained | 1 |
| chopped garlic and herb-marinated sun-dried tomato | 1 |
| chopped grape tomato | 1 |
| chopped green tomato | 4 |
| chopped herbs, spinach, or sun-dried tomato | 2 |
| chopped italian plum tomato | 1 |
| chopped low-sodium sun-dried tomato | 1 |
| chopped marinated sun-dried tomato | 1 |
| chopped mixed summer vegetables (such as bell peppers, eggplant, chiles, zucchini, summer squash, carrots, celery, radishes, and cherry tomatoes) | 1 |
| chopped oil-packed sun-dried tomato | 15 |
| chopped oil-packed sun-dried tomatoes (about 10 to 12 tomatoes) | 1 |
| chopped or julienned sun-dried tomatoes in oil, drained | 1 |
| chopped peeled and seeded tomatoes (see cooks' note, below) or 1 1/2 cups (from a 28-oz can) drained canned tomato | 1 |
| chopped peeled seeded tomato | 2 |
| chopped peeled seeded vine-ripened tomato (about 3/4 pound) | 1 |
| chopped peeled tomatoes, fresh or canned | 1 |
| chopped plum (roma) tomato | 1 |
| chopped plum tomato | 20 |
| chopped plum tomatoes (about 1 1/2 pounds) | 1 |
| chopped plum tomatoes (about 12 ounces) | 1 |
| chopped plum tomatoes (about 14 ounces) | 1 |
| chopped plum tomatoes (about 2 small) | 1 |
| chopped plum tomatoes (about 5 ounces) | 1 |
| chopped plum tomatoes san marzano type | 1 |
| chopped preserved sun-dried tomato | 1 |
| chopped purple cherokee tomato | 1 |
| chopped red onion, tomato, and lettuce, for serving | 1 |
| chopped red tomato and basil | 1 |
| chopped red tomatoes (about 1 1/2 pounds) | 1 |
| chopped ripe plum tomatoes (about 14 ounces) | 1 |
| chopped ripe roma tomato | 2 |
| chopped ripe tomato | 2 |
| chopped roasted tomato | 2 |
| chopped roma (plum) tomato | 5 |
| chopped roma tomato | 11 |
| chopped roma tomatoes or mild store-bought tomato salsa | 1 |
| chopped roma tomatoes with their juices | 1 |
| chopped roma tomatoes, with their juices | 1 |
| chopped salted tomatoes, for garnish | 1 |
| chopped seeded diced plum tomatoes (about 3/4 pound) | 1 |
| chopped seeded peeled red heirloom tomato | 1 |
| chopped seeded peeled tomato | 5 |
| chopped seeded plum or cherry tomato | 1 |
| chopped seeded plum tomato | 14 |
| chopped seeded plum tomatoes (about 8 ounces) | 1 |
| chopped seeded tomato | 26 |
| chopped seeded tomatoes (about 1 1/4 pounds) | 1 |
| chopped seeded vine-ripened tomato | 2 |
| chopped seeded vine-ripened tomatoes (about 7) | 1 |
| chopped seeded yellow tomato | 1 |
| chopped stewed tomato | 4 |
| chopped sun-dried tomato | 61 |
| chopped sun-dried tomato (in oil, drained) | 1 |
| chopped sun-dried tomato, packed in oil | 1 |
| chopped sun-dried tomatoes (not in oil) | 1 |
| chopped sun-dried tomatoes (not oil-packed) | 2 |
| chopped sun-dried tomatoes (not packed in oil) | 1 |
| chopped sun-dried tomatoes (not packed in oil; about 2 ounces) | 1 |
| chopped sun-dried tomatoes (optional) | 2 |
| chopped sun-dried tomatoes (packed in oil) | 1 |
| chopped sun-dried tomatoes (preferably oil-packed), drained | 1 |
| chopped sun-dried tomatoes in oil | 2 |
| chopped sun-dried tomatoes in oil, drained | 1 |
| chopped sun-dried tomatoes marinated in olive oil, drained | 1 |
| chopped sun-dried tomatoes packed in oil, drained | 1 |
| chopped sun-dried tomatoes, oil packed preferred | 1 |
| chopped sun-dried tomatoes, or to taste | 1 |
| chopped sun-dried tomatoes, packed without oil | 1 |
| chopped sundried tomato | 1 |
| chopped sundried tomatoes (1/4-inch pieces) | 1 |
| chopped sundried tomatoes, rehydrated for 15 minutes in about 1/4 cup white wine, beer or water | 1 |
| chopped sweet 100 tomatoes, or very small grape tomato | 1 |
| chopped tomato | 211 |
| chopped tomato (about 8 ounces) | 1 |
| chopped tomato (optional) | 4 |
| chopped tomato for garnish | 1 |
| chopped tomato or 10 cherry tomatoes, halved | 1 |
| chopped tomato or halved cherry or grape tomatoes, for garnish | 1 |
| chopped tomato with seeds (about 1 large tomato) | 1 |
| chopped tomato, for garnish | 3 |
| chopped tomato, plus 4 tablespoons peeled, seeded, large dice tomato | 1 |
| chopped tomato, seeds discarded | 1 |
| chopped tomatoes (about 2 large tomatoes) | 1 |
| chopped tomatoes (about 2 medium) | 1 |
| chopped tomatoes (about 3/4 pound) | 1 |
| chopped tomatoes (fresh is best, but you can use diced canned tomatoes) | 1 |
| chopped tomatoes (optional) | 4 |
| chopped tomatoes (tomato "guts" or canned or fresh) | 1 |
| chopped tomatoes and cilantro leaves, for garnish | 2 |
| chopped tomatoes with chiles | 1 |
| chopped tomatoes, as a garnish | 1 |
| chopped tomatoes, as an accompaniment | 1 |
| chopped tomatoes, for garnish | 3 |
| chopped tomatoes, ice burg lettuce, sour cream, salsa, guacamole (optional) | 1 |
| chopped tomatoes, pushed through a sieve | 1 |
| chopped tomatoes, seeded and peeled, fresh or canned (see cook's tip) | 1 |
| chopped tomatoes, with juice | 1 |
| chopped vine ripe tomato | 1 |
| chopped whole plum tomatoes with juices | 1 |
| chopped whole tomatoes, with juices | 1 |
| chopped yellow or beefsteak tomato | 1 |
| chopped yellow or orange tomatoes (8 to 9 ounces) | 1 |
| chopped yellow tomato | 1 |
| chopped, drained oil-packed sun-dried tomato | 1 |
| chopped, seeded tomato | 1 |
| chopped, well-drained canned tomato | 1 |
| chunky style crushed tomato | 1 |
| chunky style crushed tomatoes or diced tomato | 1 |
| chunky tomato salsa compote, recipe follows | 1 |
| chunky tomato sauce | 3 |
| chunky tomato sauce (such as prego®) | 1 |
| chunky tomato sauce, recipe follows | 1 |
| cilantro-tomato salsa | 1 |
| cinnamon-sage tomato sauce, recipe follows | 1 |
| clam and tomato juice, such as clamato | 1 |
| clam-tomato juice (recommended: clamato) | 2 |
| clam-tomato juice (such as clamato) | 3 |
| clam-tomato juice, such as clamato | 1 |
| clamato® tomato cocktail | 6 |
| classic tomato basil sauce, recipe follows | 2 |
| classic tomato sauce | 1 |
| clear tomato water, set aside from tomato puree, recipe follows, refrigerated* | 1 |
| coarsely chopped drained oil-packed sun-dried tomato | 2 |
| coarsely chopped fresh tomato | 2 |
| coarsely chopped fresh tomatoes or diced canned tomato | 1 |
| coarsely chopped fresh tomatoes, or 1/2 cup chopped drained sun-dried tomatoes in oil | 1 |
| coarsely chopped green tomatoes or unripe red tomato | 1 |
| coarsely chopped peeled fresh, ripe tomatoes, or 1 cup coarsely chopped canned whole peeled tomatoes with their juice | 1 |
| coarsely chopped peeled tomato | 1 |
| coarsely chopped plum tomato | 1 |
| coarsely chopped plum tomatoes (about 3 1/4 pounds) | 1 |
| coarsely chopped seeded tomato | 1 |
| coarsely chopped tomato confit | 1 |
| coarsely chopped tomatoes (about 6 medium) | 1 |
| coarsely chopped vine-ripened tomatoes (about 3/4 pound) freshly ground black pepper to taste | 1 |
| coarsely chopped yellow heirloom tomato | 1 |
| coarsely diced fresh tomato | 1 |
| cocktail tomatoes or 2 cups cherry tomato | 1 |
| cold smoked plum tomato | 1 |
| cold tomato juice | 1 |
| concentrated tomato paste | 1 |
| concentrated tomato puree | 1 |
| condensed crushed tomato | 1 |
| condensed tomato soup | 2 |
| confit cherry tomato | 1 |
| confit tomato | 1 |
| contadina® tomato paste | 1 |
| container cherry or grape tomatoes, halved | 1 |
| container cherry tomatoes, halved | 1 |
| container crushed tomato | 1 |
| container crushed tomatoes (such as hunt's®) | 1 |
| container grape tomatoes, halved | 1 |
| container small heirloom cherry tomatoes, halved | 1 |
| container tomato juice | 1 |
| containers grape tomato | 1 |
| containers mixed cherry tomato | 1 |
| containers whole peeled tomatoes, drained and crushed with your hands | 1 |
| cooked tomato | 2 |
| cored and chopped fresh or drained canned tomato | 1 |
| cored and chopped tomato | 1 |
| cored, seeded and diced ripe tomatoes (about 3 medium tomatoes) | 1 |
| couscous, steamed with tomato juice and 1 teaspoon ground cumin and 1 teaspoon ground coriander | 1 |
| cracker barrel crumbled feta cheese with oregano, sun dried tomatoes and black pepper | 1 |
| cream of tomato soup, not from concentrate | 1 |
| creamy spicy tomato sauce: | 1 |
| creamy tomato soup | 1 |
| creamy tomato soup with 4g fat or less per serving (recommended: amy's chunky tomato bisque) | 1 |
| creole or beefsteak tomato | 1 |
| creole tomatoes, seeded and diced | 1 |
| croutons and finely diced tomato, green bell pepper, and cucumber, for garnish | 1 |
| crumbled feta cheese with basil and sun-dried tomato | 3 |
| crumbled feta cheese with basil and tomato | 2 |
| crumbled seasoned feta cheese (such as basil and tomato; about 6 ounces) | 1 |
| crushed canned tomato | 3 |
| crushed canned tomatoes with juice (about one 28-ounce can) | 1 |
| crushed fresh or canned plum tomato | 1 |
| crushed italian (plum) tomatoes (such as san marzano) | 1 |
| crushed or chopped drained canned plum tomatoes, plus 1/4 cup of their juice | 1 |
| crushed peeled tomato | 1 |
| crushed plum tomato | 2 |
| crushed plum tomatoes (recommended: san marzano) | 1 |
| crushed plum tomatoes, drained | 1 |
| crushed red tomato | 1 |
| crushed san marzano tomato | 1 |
| crushed tomato | 57 |
| crushed tomatoes (32 ounces) | 1 |
| crushed tomatoes (canned are fine) | 1 |
| crushed tomatoes (recommended: machacado's) | 1 |
| crushed tomatoes in juice | 1 |
| crushed tomatoes in puree | 3 |
| crushed tomatoes in sauce | 1 |
| crushed tomatoes in thick tomato puree | 1 |
| crushed tomatoes in tomato puree | 1 |
| crushed tomatoes or 7 cups fresh tomato concasse (peeled, seeded and diced tomatoes) | 1 |
| crushed tomatoes or crushed tomatoes with added puree (from one 28-ounce can; preferably san marzano or muir glen) | 1 |
| crushed tomatoes with added puree | 3 |
| crushed tomatoes with added puree (from 28-ounce can) | 1 |
| crushed tomatoes with added puree (from two 28-ounce cans) | 1 |
| crushed tomatoes with added purée | 1 |
| crushed tomatoes with garlic | 1 |
| crushed tomatoes with juice | 3 |
| crushed tomatoes with oregano, basil, garlic | 1 |
| crushed tomatoes) | 1 |
| crushed tomatoes, 15 ounces | 1 |
| crushed tomatoes, 28 ounces | 1 |
| crushed tomatoes, preferably san marzano | 2 |
| crushed tomatoes, with puree | 1 |
| crushed vine ripe tomatoes, fresh or canned | 1 |
| crushed, canned whole tomatoes, undrained | 1 |
| cube chicken with tomato flavored bouillon | 1 |
| cube tomato-flavored bouillon | 1 |
| cubed (about 1-inch pieces) firm, ripe plum or other tomato | 1 |
| cubed seeded plum tomato | 1 |
| cubed tomato | 1 |
| cucumber and tomato tzatziki | 1 |
| cucumber/tomato salsa, (recipe follows) | 1 |
| cupoil-packed sun-dried tomato | 1 |
| cupsmexican-style tomato sauce | 1 |
| cupsrich winter tomato sauce | 1 |
| cupswinter tomato sauce | 1 |
| currant tomatoes (or cherry tomatoes cut in half) | 1 |
| currant, stemmed or yellow and red pear tomato | 2 |
| dead-ripe meaty tomatoes, cored, seeded, and cut into quarters | 1 |
| dehydrated sun-dried tomato | 3 |
| del monte® diced tomatoes-no salt added | 1 |
| del monte® petite diced tomatoes with chipotle chilies or del monte® petite diced tomatoes with zesty jalapenos | 1 |
| del monte® tomato sauce-no salt added | 1 |
| dessert spoons finely chopped tomato | 1 |
| diced (1/3 inch) plum tomato | 1 |
| diced (1/4 inch) ripe tomato | 2 |
| diced (1/4 inch) seeded ripe plum tomato | 1 |
| diced and drained tomato | 1 |
| diced and seeded tomato | 1 |
| diced and seeded tomatoes (drained if using canned) | 1 |
| diced and seeded tomatoes (with juices if using canned) | 1 |
| diced beefsteak tomato | 1 |
| diced beefsteak tomatoes (2 to 3 large tomatoes) | 1 |
| diced canned fire-roasted tomato | 1 |
| diced canned italian plum tomato | 6 |
| diced canned or fresh tomato | 1 |
| diced canned plum tomato | 1 |
| diced canned tomato | 4 |
| diced canned tomatoes in juice | 1 |
| diced canned tomatoes with juices | 1 |
| diced canned tomatoes, drained | 1 |
| diced cherry tomatoes, for serving | 1 |
| diced cherry tomatoes, or more to taste (optional) | 1 |
| diced chilis and tomatoes (recommended: ro'tel) | 1 |
| diced cored tomato | 1 |
| diced drained oil-packed sun-dried tomatoes (2 1/2 ounces) | 1 |
| diced fire roasted tomatoes, drained | 1 |
| diced fresh beefsteak tomato | 1 |
| diced fresh roma tomato | 1 |
| diced fresh seeded plum tomato | 1 |
| diced fresh tomato | 28 |
| diced fresh tomatoes (about 2 medium or 6 plum tomatoes) | 1 |
| diced fresh tomatoes (about 3 to 5) | 1 |
| diced fresh tomatoes (optional) | 1 |
| diced fresh tomatoes or one 15-ounce can diced tomato | 1 |
| diced grape tomato | 1 |
| diced green tomato | 2 |
| diced heirloom tomato | 2 |
| diced italian tomatoes in juice | 1 |
| diced oil packed sun-dried tomatoes, drained, oil reserved | 1 |
| diced oil-packed sun dried tomato | 1 |
| diced oil-packed sun-dried tomato | 2 |
| diced oil-packed sun-dried tomatoes, plus 1 tablespoon oil from jar | 1 |
| diced oil-packed sun-dried tomatoes, with 1 tablespoon oil from jar | 1 |
| diced oil-packed sundried tomato | 1 |
| diced peeled and seeded tomato | 1 |
| diced pickled green tomato | 1 |
| diced plum tomato | 14 |
| diced plum tomatoes (about 12 medium plum tomatoes) | 1 |
| diced plum tomatoes (preferably organic; about 14 ounces) | 1 |
| diced plum tomatoes or 1/2 cup thinly sliced sun-dried tomato | 1 |
| diced plum tomatoes or or parsley | 1 |
| diced plum tomatoes, seeded | 1 |
| diced red plum tomato | 1 |
| diced red tomato | 4 |
| diced rehydrated sun-dried tomato | 1 |
| diced ripe heirloom tomato, for serving | 1 |
| diced ripe tomato | 5 |
| diced ripe tomatoes, drained (optional) | 1 |
| diced roma tomato | 25 |
| diced roma tomato, for garnish | 2 |
| diced roma tomatoes, for garnish | 1 |
| diced roma tomatoes, for topping | 1 |
| diced san marzano tomato | 2 |
| diced seeded beefsteak tomato | 1 |
| diced seeded plum tomato | 12 |
| diced seeded plum tomatoes (about 10 ounces) | 1 |
| diced seeded plum tomatoes (about 4 ounces) | 1 |
| diced seeded red tomato | 1 |
| diced seeded red, yellow, and orange tomatoes (about 2 pounds) | 1 |
| diced seeded tomato | 3 |
| diced seeded tomato (1 small) | 1 |
| diced seeded tomatoes (about 3 medium) | 1 |
| diced seeded tomatoes (about 4 large) | 1 |
| diced seeded tomatoes, drained | 1 |
| diced sun dried tomato | 1 |
| diced sun-dried tomato | 8 |
| diced sun-dried tomatoes (from an 8-ounce jar) | 1 |
| diced tomato | 200 |
| diced tomato (excluding skin) | 1 |
| diced tomato with juice | 1 |
| diced tomato, as desired | 1 |
| diced tomato, for garnish | 2 |
| diced tomato, for topping | 2 |
| diced tomato, if desired | 1 |
| diced tomato, seeds removed | 1 |
| diced tomato, skin on, including seeds and juice | 1 |
| diced tomatoes (1-inch dice) | 1 |
| diced tomatoes (5 to 7 tomatoes, depending on size) | 1 |
| diced tomatoes (about 1 large tomato) | 1 |
| diced tomatoes (about 1 plum tomato) | 3 |
| diced tomatoes (about 3 medium tomatoes) | 1 |
| diced tomatoes (about 4 medium-large tomatoes) | 1 |
| diced tomatoes (approx. 2 seeded tomatoes) | 1 |
| diced tomatoes (optional) | 1 |
| diced tomatoes and green chiles (recommended: ro-tel brand) | 1 |
| diced tomatoes and green chiles, such as rotel | 1 |
| diced tomatoes and green chiles, undrained | 1 |
| diced tomatoes in assorted colors (about 2 1/2 pounds) | 1 |
| diced tomatoes in juice | 1 |
| diced tomatoes in juice (from two 14 1/2-ounce cans) | 1 |
| diced tomatoes in juice, 14 ounces | 1 |
| diced tomatoes in puree or chunky style crushed tomato | 1 |
| diced tomatoes or leftover tomato | 1 |
| diced tomatoes peeled and seeded | 1 |
| diced tomatoes with garlic and onion | 1 |
| diced tomatoes with green chiles, drained | 1 |
| diced tomatoes with green chiles, juice reserved | 1 |
| diced tomatoes with habaneros (such as ro*tel® hot) | 1 |
| diced tomatoes with italian herbs, hunt's | 1 |
| diced tomatoes with jalapeno chiles | 2 |
| diced tomatoes with juice | 3 |
| diced tomatoes with no-salt added | 1 |
| diced tomatoes with some juice (from a 14-oz can) | 1 |
| diced tomatoes, as needed | 1 |
| diced tomatoes, canned | 1 |
| diced tomatoes, cut up | 1 |
| diced tomatoes, drained | 9 |
| diced tomatoes, drained well | 1 |
| diced tomatoes, for garnish | 2 |
| diced tomatoes, for serving | 1 |
| diced tomatoes, for topping | 1 |
| diced tomatoes, including liquid | 1 |
| diced tomatoes, italian seasoned | 1 |
| diced tomatoes, mango, or quartered seedless grapes | 1 |
| diced tomatoes, or plum tomato | 1 |
| diced tomatoes, or to taste | 2 |
| diced tomatoes, usually canned | 1 |
| diced tomatoes, well drained | 1 |
| diced tomatoes, with juice | 2 |
| diced tomatoes, with liquid | 1 |
| diced vine-ripened tomato | 3 |
| diced vine-ripened tomato (optional) | 1 |
| diced yellow tomato | 1 |
| diced, seeded, tomato | 1 |
| divide tomato mixture among 4 plates. top each serving with an equal amount of the arugula. with a vegetable peeler, shave the parmesan over the salad. serve immediately | 1 |
| double concentrate tomato paste | 1 |
| double concentrate tomato paste (from a tube) | 1 |
| double concentrated tomato paste | 1 |
| double-concentrate tomato paste | 1 |
| double-concentrated italian tomato paste | 1 |
| dozen cherry tomato | 3 |
| dozen cherry tomatoes, washed with stems removed | 1 |
| dozen grape tomatoes, halved | 1 |
| drain the tomatoes in a sieve to remove excess liquid while you prepare the rest of the ingredients | 1 |
| drained and chopped canned plum tomato | 1 |
| drained and chopped canned whole tomato | 1 |
| drained and chopped oil packed sun-dried tomato | 1 |
| drained and chopped oil-packed dried tomato | 1 |
| drained and chopped sun dried tomatoes, packed in oil | 1 |
| drained and chopped sun-dried tomatoes (oil-packed) | 1 |
| drained and chopped sun-dried tomatoes halves, packed in oil | 1 |
| drained and chopped sun-dried tomatoes packed in oil | 1 |
| drained and chopped sun-dried tomatoes packed in oil (available at specialty foods shops and some supermarkets), reserving 2 tablespoons of the oil | 1 |
| drained and chopped sun-dried tomatoes packed in oil, reserving 2 tablespoons of the oil | 1 |
| drained and chopped sun-dried tomatoes, packed in oil | 1 |
| drained and chopped sundried tomatoes packed in oil | 1 |
| drained and coarsely chopped sun-dried tomato | 1 |
| drained and finely chopped oil-packed sundried tomato | 1 |
| drained and mushed whole plum tomatoes, plus 1/4 cup reserved roasting liquid or one 16-ounce can whole tomatoes with liquid | 1 |
| drained and seeded, canned whole tomatoes, halved | 1 |
| drained and thinly sliced oil-packed sun-dried tomato | 1 |
| drained bottled dried tomatoes packed in oil | 3 |
| drained canned chopped tomato | 1 |
| drained canned diced tomato | 4 |
| drained canned diced tomatoes (from a 14- to 15-oz can) | 1 |
| drained canned diced tomatoes in juice | 4 |
| drained canned italian plum tomatoes, crushed | 1 |
| drained canned mexican-style stewed tomato | 1 |
| drained canned plum tomatoes 12 ounces cheese filled ravioli | 1 |
| drained canned plum tomatoes, crushed, reserve tomato juice for recipe | 1 |
| drained canned san marzano tomatoes (about 8 tomatoes) | 1 |
| drained canned tomato | 7 |
| drained canned tomatoes chopped | 1 |
| drained canned whole tomato | 2 |
| drained chopped canned plum tomato | 1 |
| drained chopped canned tomato | 1 |
| drained chopped tomato | 1 |
| drained coarsely chopped sun dried tomatoes packed in oil | 1 |
| drained diced canned tomatoes (from 14.5-ounce can) | 1 |
| drained dried tomatoes packed in oil | 1 |
| drained marinated oil-packed sun-dried tomatoes (from 8.5-ounce jar), each halved | 1 |
| drained no-salt-added canned diced tomato | 1 |
| drained oil-packed julienned sun-dried tomato | 1 |
| drained oil-packed sun-dried tomato | 13 |
| drained oil-packed sun-dried tomatoes (about 6 ounces) | 1 |
| drained oil-packed sun-dried tomatoes, cut into thin strips | 1 |
| drained oil-packed sun-dried tomatoes, thinly sliced | 1 |
| drained stewed tomatoes (from a 14-oz can) | 1 |
| drained sun-dried tomatoes in oil | 2 |
| drained tomatoes from a 28-ounce can | 1 |
| drained, canned stewed tomato | 1 |
| drained, julienned oil-packed sun-dried tomato | 2 |
| dried sun-dried tomato | 1 |
| dried sun-dried tomato linguine | 1 |
| dried tomato | 2 |
| dried tomato and arugula pesto, or to taste | 1 |
| dried tomatoes (about 1/2 cup) | 1 |
| dried tomatoes (about 3 ounces) | 1 |
| dried tomatoes (about 3/4 cup), not packed in oil | 1 |
| dried tomatoes (not packed in oil) | 2 |
| dried tomatoes not packed in oil (about 2 ounces) | 1 |
| dried tomatoes packed in oil | 2 |
| dry pints (20 ounces/600 grams) grape or cherry tomato | 1 |
| dry red wine (or substitute broth or tomato juice) | 1 |
| dry-packed sun-dried tomatoes, halved | 1 |
| dry-packed sun-dried tomatoes, soaked for 1 to 4 hours in filtered water and drained | 1 |
| each 1/2-inch diced vegetables: yellow onion, green bell pepper, red bell pepper, and tomato | 1 |
| each diced carrot, celery, fresh-cooked beets, red peppers, yellow peppers, cucumbers, and tomato | 1 |
| each red and yellow cherry tomatoes, halved | 1 |
| each ripe mango and tomato, cut into 1/4-inch dice | 1 |
| each roasted zucchini, eggplant, potatoes, onions, carrots and tomato | 1 |
| each thin sliced roma tomato | 1 |
| each tomato | 1 |
| each tomatoes, vine-ripe | 1 |
| each yellow and red cherry tomatoes, halved | 1 |
| each: tomato paste and honey | 1 |
| early girl or other sweet red tomato | 1 |
| easy tomato sauce, recipe follows, or store-bought marinara sauce | 1 |
| eight 1/4-inch slices tomato | 2 |
| eight 3-inch-square pieces of tomato or plain focaccia bread, halved, or 8 hamburger buns, halved | 1 |
| eight 3/4-inch-thick slices heirloom tomato | 1 |
| equal parts vine ripe red and yellow tomatoes cut 1/4 dice | 1 |
| extra virgin olive oil, plus extra for basting tomato | 1 |
| extra-sweet grape tomato | 1 |
| extra-virgin olive oil for drizzling over the tomato | 1 |
| famous tomato sauce, recipe follows | 1 |
| farm fresh green tomato | 2 |
| fat-free tomato sauce | 1 |
| fava bean and tomato ragout, recipe follows | 1 |
| favorite burger toppings, such as raw onion, tomato slices and lettuce | 1 |
| favorite tomato based bbq sauce | 1 |
| favorite tomato sauce | 1 |
| finely chopped and seeded tomato | 1 |
| finely chopped assorted fresh vegetables (peppers, tomatoes and/or green onions) | 2 |
| finely chopped drained canned tomato | 1 |
| finely chopped drained oil-packed sun-dried tomato | 7 |
| finely chopped drained sun-dried tomatoes in oil | 1 |
| finely chopped drained sun-dried tomatoes packed in oil | 2 |
| finely chopped fresh plum tomato | 1 |
| finely chopped green tomato | 1 |
| finely chopped plum tomato | 3 |
| finely chopped plum tomato (1 large) | 1 |
| finely chopped seeded plum tomato | 1 |
| finely chopped seeded tomato | 2 |
| finely chopped seeded tomato for garnish | 1 |
| finely chopped seeded tomatoes (about 4 medium) | 1 |
| finely chopped seeded vine-ripened tomato or drained canned tomato | 1 |
| finely chopped sun-dried tomato | 5 |
| finely chopped sun-dried tomatoes in oil | 1 |
| finely chopped sun-dried tomatoes in olive oil | 1 |
| finely chopped sun-dried tomatoes — a nice handful from the jar | 1 |
| finely chopped sun-dried tomatoes, rehydrated | 2 |
| finely chopped sundried tomato | 1 |
| finely chopped sundried tomatoes in oil, drained | 1 |
| finely chopped tomato | 14 |
| finely chopped tomato confit | 1 |
| finely chopped tomatoes (about 11 ounces) | 1 |
| finely chopped tomatoes and chervil sprigs, for garnish | 1 |
| finely diced creole tomato | 1 |
| finely diced fresh tomato | 3 |
| finely diced plum tomatoes, juices reserved | 1 |
| finely diced seeded tomato | 2 |
| finely diced tomato | 8 |
| finely diced tomato (about 1 large or 30 grape tomatoes) | 1 |
| fire roasted diced tomatoes, drained | 1 |
| fire roasted eggplant and grilled tomatoes, recipe follows | 1 |
| fire roasted tomato sauce | 1 |
| fire roasted tomatoes, pureed | 1 |
| fire-roasted canned plum tomatoes, pureed | 1 |
| fire-roasted diced tomato | 1 |
| fire-roasted tomato | 1 |
| fire-roasted tomatoes, pureed | 1 |
| firm but almost ripe tomato | 1 |
| firm green heirloom tomatoes, cut into quarters | 1 |
| firm green tomato | 1 |
| firm green tomatoes (about 1 large), cored and cut into 1/4- to 1/2-inch dice | 1 |
| firm plum tomato, seeded and diced | 1 |
| firm plum tomatoes, halved lengthwise | 1 |
| firm plum tomatoes, seeded and finely chopped | 2 |
| firm red tomatoes, seeded and chopped | 1 |
| firm ripe tomato | 2 |
| firm ripe tomatoes, cored and cut into 1-inch pieces or two 28-ounce cans peeled, whole italian plum tomato | 1 |
| firm tomatoes, seeded and diced | 1 |
| firm tomatoes, thinly sliced into rounds | 1 |
| firm vine-ripened tomatoes (each about 3 inches in diameter) | 1 |
| firm, ripe medium tomato | 1 |
| firm, ripe roma tomato | 1 |
| firm, ripe tomato | 3 |
| firm, ripe tomatoes, cored and cut into 1-inch pieces | 1 |
| firm, ripe tomatoes, cut into 1-inch pieces | 3 |
| firm-ripe red tomato | 1 |
| firm-ripe roma tomato | 1 |
| firm-ripe tomato | 1 |
| firm-ripe tomatoes, cut into 1/4-inch dice (1 1/4 cups), then drained in a sieve about 20 minutes | 1 |
| firm-ripe tomatoes, seeded and chopped | 1 |
| fish stock, canned clam juice or clam and tomato juice | 1 |
| fluid ounces tomato and clam juice cocktail | 1 |
| fluid ounces tomato and clam juice cocktail (such as clamato®) | 1 |
| fluid ounces tomato juice | 5 |
| fluid ounces tomato-based chili sauce | 2 |
| fluid ounces tomato-vegetable juice cocktail (such as v8®), or more to taste | 1 |
| for famous tomato sauce: | 1 |
| for serving: tomato slices, lettuce leaves, red onion slices and dill pickle rounds | 1 |
| for sundried tomato butter: | 1 |
| for the tomato sauce: | 2 |
| for the tomatoes: | 1 |
| four 1/2-inch-thick slices tomato | 1 |
| four 1/2-pound tomato | 2 |
| four 10-inch tortillas, such as flour, spinach or sun-dried tomato | 1 |
| four 12-inch sun-dried tomato tortillas | 1 |
| four 12-inch sundried tomato tortillas, toasted with a little oil | 1 |
| four 14.5-ounce cans petite-diced tomato | 1 |
| four 16-ounce cans san marzano tomato | 1 |
| four 28-ounce cans hand crushed san marzano plum tomatoes, with juice | 1 |
| four 28-ounce cans whole peeled tomato | 1 |
| four 28-ounce cans whole peeled tomatoes, with liquid | 2 |
| four 28-ounce cans whole san marzano tomatoes, hand-crushed | 1 |
| four 28-ounce cans whole tomatoes, drained | 1 |
| four 6-inch tomato focaccia rolls, split and toasted (or your favorite focaccia bread) | 1 |
| fresh cherry tomato | 3 |
| fresh chopped tomato | 2 |
| fresh diced tomato | 3 |
| fresh diced tomatoes* | 1 |
| fresh finely chopped tomato | 1 |
| fresh heirloom tomatoes, cut into big chunks (variety of colors purple, yellow, bright red) | 1 |
| fresh italian plum tomato | 1 |
| fresh italian plum tomatoes, seeded if desired | 1 |
| fresh large diced tomato | 1 |
| fresh or canned peeled tomatoes, seeded and crushed, juices reserved | 1 |
| fresh or canned plum tomato | 2 |
| fresh or canned plum tomatoes, seeded and chopped | 1 |
| fresh or canned tomato | 1 |
| fresh peeled and chopped tomato | 1 |
| fresh plum or vine ripened tomato | 1 |
| fresh plum or vine tomato | 1 |
| fresh plum tomato | 6 |
| fresh plum tomato dice, seedless | 2 |
| fresh plum tomatoes or one 28-oz can whole tomatoes in juice | 1 |
| fresh plum tomatoes, cut into 1/8-inch thick rounds | 1 |
| fresh plum tomatoes, quartered | 1 |
| fresh plum tomatoes, seeded and chopped or 2 cans chopped tomato | 1 |
| fresh plum tomatoes, seeded and cut into bite-size pieces | 1 |
| fresh plum tomatoes, seeded and cut into fine dice | 1 |
| fresh plum tomatoes, seeded and diced | 1 |
| fresh red tomato | 2 |
| fresh ripe plum tomato | 1 |
| fresh ripe plum tomatoes, cut into eighths | 2 |
| fresh ripe tomato | 4 |
| fresh ripe tomatoes, seeded and roughly chopped (or one 28-oz can plum tomatoes) | 1 |
| fresh roma tomato | 2 |
| fresh roma tomato water (not canned juice), see cook's note | 1 |
| fresh roma tomato, seeded and diced | 1 |
| fresh spinach or tomato lasagne sheets (or half pound each) | 1 |
| fresh tamarillo (tree tomato) or small red tomato | 1 |
| fresh tamarillo or small red tomato | 1 |
| fresh tomato | 53 |
| fresh tomato and/or carrot juice (from about 1 lb vegetables) | 1 |
| fresh tomato from the garden or farmers' market | 1 |
| fresh tomato juice | 3 |
| fresh tomato puree | 3 |
| fresh tomato puree (peel, seed and puree one pound ripe tomatoes in a food processor) | 1 |
| fresh tomato puree (peel, seed, and puree 1 pound ripe tomatoes in a food processor) | 1 |
| fresh tomato salsa | 6 |
| fresh tomato salsa (recipe follows) | 1 |
| fresh tomato salsa, as an accompaniment | 1 |
| fresh tomato salsa, plus more for serving | 1 |
| fresh tomato salsa, recipe follows | 1 |
| fresh tomato sauce | 6 |
| fresh tomato sauce (recipe below) | 1 |
| fresh tomato sauce, recipe follows | 1 |
| fresh tomato sauce, recipe follows, for serving | 1 |
| fresh tomato slices, for garnish | 1 |
| fresh tomato slices, for topping each burger | 1 |
| fresh tomato wedges | 1 |
| fresh tomato, halved, or more to taste | 1 |
| fresh tomato-orange chutney (recipe follows) | 1 |
| fresh tomatoes (4 small) | 3 |
| fresh tomatoes (mix of fresh heirlooms, cherry, vine and plum tomatoes) | 1 |
| fresh tomatoes - peeled, seeded and chopped | 1 |
| fresh tomatoes or drained canned tomatoes, preferably imported italian | 1 |
| fresh tomatoes or one 16 ounce can of tomatoes in juice | 1 |
| fresh tomatoes, cored | 1 |
| fresh tomatoes, cut into wedges | 1 |
| fresh tomatoes, halved | 1 |
| fresh tomatoes, large dice | 1 |
| fresh tomatoes, quartered | 2 |
| fresh tomatoes, seeded and diced | 1 |
| fresh tomatoes, seeds removed and diced, or 1 large can (28-32 ounces) plum tomato | 1 |
| fresh tomatoes, skinned and diced | 1 |
| fresh tomatoes, unpeeled and cut in quarters, or one 28-ounce can tomato | 1 |
| fresh vine-ripened or heirloom tomatoes, cut into 1/2-inch pieces | 1 |
| fresh whole tomato | 1 |
| fresh, ripe tomato | 2 |
| fresh, ripe tomatoes or 1 cup canned imported italian plum tomatoes, cut up, and drained of juice | 1 |
| fresh-squeezed tomato juice | 1 |
| freshly diced tomato | 2 |
| freshly made tomato puree (water, tomatoes, and a dash of olive oil) | 1 |
| freshly pureed tomato | 1 |
| fried green tomatoes, recipe follows | 1 |
| fried tomato skins | 1 |
| fully cooked sun-dried-tomato chicken sausages, each cut into 6 pieces | 1 |
| gabriel's tomato sauce, recipe follows | 1 |
| gallon canned crushed tomato | 1 |
| gallon canned whole peeled tomato | 2 |
| gallon chopped tomatoes packed in juice | 1 |
| gallon crushed tomato | 1 |
| gallon green tomatoes, thinly sliced | 1 |
| gallon ground pear tomato | 1 |
| gallon premium diced tomatoes in juice | 1 |
| gallon tomato juice | 1 |
| gallon tomato sauce | 1 |
| gallon whole cooked plum tomatoes with juice | 2 |
| gallons canned tomatoes, stewed or whole peeled | 1 |
| gallons canned, crushed tomato | 1 |
| gallons tomato juice | 1 |
| gallons tomatoes, crushed | 1 |
| garden fresh tomato | 1 |
| garden tomatoes, medium diced | 1 |
| garden zucchini tomato sauce, recipe follows | 1 |
| garlic chili tomato butter, recipe follows | 1 |
| garlic powder, plus more for seasoning tomato | 1 |
| garlic roasted tomato spread (see footnote for recipe link) | 1 |
| garnish: 2 plum tomatoes, seeded and diced; finely chopped fresh chives | 1 |
| garnish: boston lettuce, tomato wedges and capers | 1 |
| garnish: celery sticks, trimmed green onions, and skewered cherry tomato | 1 |
| garnish: corn chips and chopped tomato | 1 |
| garnish: diced seeded tomato and finely chopped fresh parsley leaf | 1 |
| garnish: diced tomato; chopped chives | 1 |
| garnish: green or oilcured moroccan olives, lemon wedges, and tomato (optional | 1 |
| garnish: halved yellow pear or cherry tomato | 1 |
| garnish: julienne strips of tomato | 1 |
| garnish: olive, cherry tomato, and cocktail onion on a swizzle stick or toothpick | 1 |
| garnish: red and yellow cherry tomatoes, halved | 1 |
| garnish: sliced cucumber; sliced tomatoes; lime wedges; sambal oelek or sriracha (southeast asian chile sauce) | 1 |
| garnish: sliced ripe tomatoes, pickles, deviled potato salad, recipe follows | 2 |
| garnish: very small heirloom cherry or currant tomato | 1 |
| generous 1 pound tomatoes, cut into pieces | 1 |
| generous handfuls cherry tomato | 1 |
| generous handfuls sun-dried tomatoes, packed in oil | 1 |
| giant oxheart tomatoes (about 12 ounces total) | 1 |
| giant slices of field-grown tomato | 1 |
| ginger-tomato chutney | 1 |
| golden grape or cherry tomatoes (scant 4 cups), halved | 1 |
| golden tomato | 2 |
| golf ball-size tomato | 1 |
| good quality tomato sauce | 1 |
| good-quality jarred tomato sauce and 2 ounces feta cheese, for serving | 1 |
| good-quality tomato juice | 3 |
| goya tomato sauce | 1 |
| goya® tomato sauce | 1 |
| grain bread with sprouts, tomato and red onion | 2 |
| grape or cherry tomato | 8 |
| grape or cherry tomatoes (9 ounces) | 1 |
| grape or cherry tomatoes (9 oz) | 1 |
| grape or cherry tomatoes cut in 1/2 | 1 |
| grape or cherry tomatoes, cut in half | 2 |
| grape or cherry tomatoes, cut into 1/4-inch dice | 1 |
| grape or cherry tomatoes, halved | 22 |
| grape or cherry tomatoes, halved lengthwise | 1 |
| grape or cherry tomatoes, quartered | 1 |
| grape or pear tomatoes (preferably a mix of yellow and red), washed and dried | 1 |
| grape or small cherry tomato | 1 |
| grape or small cherry tomatoes (about 10 ounces) | 1 |
| grape or small vine tomatoes, halved | 1 |
| grape tomato | 62 |
| grape tomato halved | 1 |
| grape tomato, halved | 2 |
| grape tomatoes (2 cups) | 1 |
| grape tomatoes (2 cups), quartered | 1 |
| grape tomatoes (4 1/2 ounces), cut crosswise into 1/4-inch-thick slices | 1 |
| grape tomatoes (5 oz) | 1 |
| grape tomatoes (about 6 ounces) | 1 |
| grape tomatoes (preferably mixed colors), halved if large | 1 |
| grape tomatoes (yellow and red), halved lengthwise | 2 |
| grape tomatoes or cherry tomato | 1 |
| grape tomatoes or other | 1 |
| grape tomatoes or pear tomatoes in assorted colors, halved | 1 |
| grape tomatoes, cherry tomatoes, or baby heirloom tomatoes of assorted colors, halved (about 2 cups) | 1 |
| grape tomatoes, cored | 1 |
| grape tomatoes, cored and halved | 1 |
| grape tomatoes, cut in 1/2 | 1 |
| grape tomatoes, cut in half | 3 |
| grape tomatoes, cut into 1/4-inch dice (1/2 cup) | 1 |
| grape tomatoes, each pierced halfway through with a paring knife | 1 |
| grape tomatoes, for serving | 1 |
| grape tomatoes, halved | 93 |
| grape tomatoes, halved (about 1 pint) | 1 |
| grape tomatoes, halved (about 3 cups) | 1 |
| grape tomatoes, halved (preferably yellow and red) | 1 |
| grape tomatoes, halved lengthwise | 13 |
| grape tomatoes, halved or quartered | 2 |
| grape tomatoes, halved or quartered if large | 1 |
| grape tomatoes, halved, for garnish | 1 |
| grape tomatoes, mixed red and yellow if possible, rinsed and patted dry | 1 |
| grape tomatoes, quartered | 13 |
| grape tomatoes, quartered lengthwise | 2 |
| grape tomatoes, red and yellow | 1 |
| grape tomatoes, split | 1 |
| grape tomatoes, split down the middle | 1 |
| grape tomatoes, thinly sliced | 1 |
| grape, cherry, or sweet 100 tomatoes, halved (about 2 1/2 cups) | 1 |
| grated green tomato | 1 |
| grated peeled roma (plum) tomato | 1 |
| grated ripe tomatoes or canned diced tomatoes with their juice | 1 |
| grated tomato (see tips, below) | 1 |
| gravy or tomato sauce | 1 |
| green (unripe) tomatoes (about 4 medium) | 2 |
| green (unripe) tomatoes, cut into wedges | 1 |
| green cherry tomato | 1 |
| green cubanero peppers** (long green peppers), roasted and diced the same size as tomato | 1 |
| green tomato | 49 |
| green tomato jam, recipe follows | 1 |
| green tomato pulp | 1 |
| green tomato, cored and cut into 1/2-inch dice | 1 |
| green tomato, cut into 1/4-inch slices | 1 |
| green tomato, cut into 1/4-inch-thick slices | 1 |
| green tomatoes, 1/4-inch slices | 1 |
| green tomatoes, cut into 1/2 inch slices | 1 |
| green tomatoes, cut into 1/2-inch-thick slices | 1 |
| green tomatoes, cut into 1/4-inch rings | 1 |
| green tomatoes, cut into 1/4-inch slices | 1 |
| green tomatoes, cut into 1/4-inch thick slices | 1 |
| green tomatoes, cut into large dice (about 2 cups) | 1 |
| green tomatoes, cut into1/2-inch dice | 1 |
| green tomatoes, medium size | 1 |
| green tomatoes, quartered and cored | 1 |
| green tomatoes, seeded and chopped | 1 |
| green tomatoes, seeded and chopped (about 6 cups) | 1 |
| green tomatoes, seeded and diced | 1 |
| green tomatoes, stemmed | 1 |
| green tomatoes, thickly sliced | 1 |
| green unripe tomato | 1 |
| green zebra tomato | 1 |
| green zebra tomato, thinly sliced | 1 |
| green zebra tomatoes, cored and cut into quarters | 1 |
| grilled brie and tomato | 1 |
| grilled cherry tomato chutney, recipe follows | 1 |
| grilled or roasted tomatoes, see recipe | 1 |
| grilled plum tomato | 2 |
| grilled plum tomatoes, recipe follows | 1 |
| grilled red pepper-tomato sauce, recipe follows | 1 |
| grilled tomato | 3 |
| grilled tomato salsa, recipe follows | 1 |
| grilled tomato sauce | 1 |
| grilled tomatoes, recipe follows | 1 |
| ground pear tomato | 1 |
| ground peeled tomato | 1 |
| ground tomato | 1 |
| guacamole and tomato salsa as accompaniments | 2 |
| guacamole, tomato chutney, and sprouts (for serving; optional) | 1 |
| habanero-tomato salsa | 2 |
| half 14.5-ounce can diced tomato | 1 |
| half 15-ounce can crushed tomato | 1 |
| half 8-ounce can chopped stewed tomato | 1 |
| half-pint grape or cherry tomato | 2 |
| halved and thinly sliced tomato | 1 |
| halved assorted colored cherry or grape tomato | 1 |
| halved cherry or grape tomato | 3 |
| halved cherry or sugarplum tomato | 1 |
| halved cherry tomato | 64 |
| halved cherry tomatoes (about 1 pint) | 1 |
| halved cherry tomatoes (about 10 ounces) | 1 |
| halved cherry tomatoes (quartered if they're big) | 1 |
| halved cherry tomatoes, or more to taste | 1 |
| halved grape or cherry tomato | 3 |
| halved grape tomato | 24 |
| halved grape tomatoes (5 ounces) | 1 |
| halved grape tomatoes (about 1/2 pint) | 1 |
| halved heirloom tomato | 1 |
| halved red and yellow cherry tomato | 1 |
| halved red cherry or grape tomato | 1 |
| halved red grape tomato | 1 |
| halved sweet cherry tomato | 1 |
| halved teardrop or cherry tomatoes (red, yellow or a blend) | 1 |
| halved teardrop tomatoes or cherry tomato | 1 |
| halved vine-ripened cherry tomato | 1 |
| halved yellow and red grape tomatoes, or more to taste | 1 |
| halved yellow cherry tomato | 1 |
| halved yellow pear or cherry tomatoes, for garnish | 1 |
| halved yellow pear tomatoes or roughly chopped heirloom tomato | 1 |
| hand-chopped ripe roma tomato | 1 |
| handful grape tomato | 1 |
| handfuls (approx. 6 ounces) of cherry tomatoes, cut in half | 1 |
| handfuls cherry tomato | 1 |
| handfuls multi-colored (red and yellow) cherry tomatoes, halved | 1 |
| handfuls sun-dried tomatoes (preferably whole) | 1 |
| hardwood smoked tomato sauce, recipe follows | 1 |
| harissa paste (you can get it from most supermarkets) or 3 tablespoons tomato purée | 1 |
| heaping tablespoon tomato ketchup | 1 |
| heaping tablespoon tomato paste | 1 |
| heaping tablespoons oil-packed sun dried tomato | 1 |
| heaping tablespoons tomato paste | 3 |
| heaping tablespoons tomato purée | 1 |
| heaping teaspoon tomato paste | 1 |
| heinz tomato ketchup | 10 |
| heinz tomato paste | 1 |
| heinz® tomato juice | 2 |
| heirloom baby tomato sauce, recipe follows | 1 |
| heirloom baby tomatoes, for garnish | 1 |
| heirloom cherry tomato | 4 |
| heirloom cherry tomatoes, assorted sizes and colors | 1 |
| heirloom cherry tomatoes, halved | 2 |
| heirloom cherry tomatoes, halved or quartered depending on size | 1 |
| heirloom cherry tomatoes, quartered | 3 |
| heirloom or cherry tomato | 1 |
| heirloom or israeli tomato | 1 |
| heirloom or plum tomato, for garnish | 1 |
| heirloom tomato | 28 |
| heirloom tomato salad | 1 |
| heirloom tomato, cut into 1/2-inch slices | 1 |
| heirloom tomato, cut into 1/4-inch slices | 1 |
| heirloom tomato, small dice (recommended: brandywine) | 1 |
| heirloom tomatoes (8 to 10 ounces total), cored, cut into 1/2-inch cubes (about 2 cups) | 1 |
| heirloom tomatoes (about 2 1/2 pounds) | 1 |
| heirloom tomatoes (as many varieties as you can find) | 1 |
| heirloom tomatoes (assorted colors preferred), stemmed, seeded and cut into 1/4-inch dice | 1 |
| heirloom tomatoes (preferably assorted colors and shapes), cut into slices and wedges | 1 |
| heirloom tomatoes (preferably assorted colors), thinly sliced | 1 |
| heirloom tomatoes (preferably green or orange), seeded and cut into 1-inch cubes | 1 |
| heirloom tomatoes (various cuts) | 1 |
| heirloom tomatoes (yellow, green and red variety) diced small | 1 |
| heirloom tomatoes (you may substitute vine ripened tomatoes) | 2 |
| heirloom tomatoes about the size of roma tomato | 1 |
| heirloom tomatoes all the same color, seeded and cored | 1 |
| heirloom tomatoes cut into bite-size wedges | 1 |
| heirloom tomatoes, assorted colors and sizes | 1 |
| heirloom tomatoes, assorted sizes and colors | 1 |
| heirloom tomatoes, cored | 1 |
| heirloom tomatoes, cut in various shapes | 1 |
| heirloom tomatoes, cut into 1 1/2-inch pieces (about 2 cups) | 1 |
| heirloom tomatoes, cut into 1/2-inch dice | 1 |
| heirloom tomatoes, cut into 1/4-inch cubes | 1 |
| heirloom tomatoes, cut into 1/4-inch-thick slices | 1 |
| heirloom tomatoes, cut into large cubes | 1 |
| heirloom tomatoes, cut into pieces | 1 |
| heirloom tomatoes, cut into wedges | 2 |
| heirloom tomatoes, different colors and sizes | 1 |
| heirloom tomatoes, for serving | 1 |
| heirloom tomatoes, halved | 2 |
| heirloom tomatoes, halved and seeded | 1 |
| heirloom tomatoes, julienned, different types and colors if possible | 1 |
| heirloom tomatoes, mixed colors and sizes | 1 |
| heirloom tomatoes, quartered and seeded | 1 |
| heirloom tomatoes, seeded and chopped (about 4 medium tomatoes) | 1 |
| heirloom tomatoes, seeded and diced | 1 |
| heirloom tomatoes, thickly sliced into 5 slices each | 1 |
| heirloom tomatoes, thinly sliced | 2 |
| heirloom tomatoes, various colors, cut into wedges | 1 |
| herb and oil marinated sun-dried tomatoes, pureed in a food processor, plus oil for griddle, preferably with garlic, herbs and dried tomato | 1 |
| homemade or purchased tomato-herb sauce | 1 |
| homemade or store bought tomato sauce | 1 |
| homemade or store-bought roasted tomato half | 1 |
| homemade or store-bought tomato sauce | 1 |
| homemade or store-bought tomato sauce, for serving | 1 |
| homemade or store-bought tomato sauce, or ketchup | 1 |
| homemade plum tomato sauce | 1 |
| homemade sun-dried tomato buns | 1 |
| homemade tomato sauce or good quality store bought sauce | 1 |
| hot pepper jelly or: chili sauce, tomatillo or tomato salsa, taco sauce ? whichever you have on hand | 1 |
| huge fresh tomato, cut into chucks | 1 |
| hunt's® diced tomatoes with basil, garlic and oregano, undrained | 1 |
| hunt's® diced tomatoes, drained | 7 |
| hunt's® diced tomatoes, drained well | 1 |
| hunt's® diced tomatoes, undrained | 3 |
| hunt's® fire roasted diced tomatoes, drained | 1 |
| hunt's® petite diced tomatoes, undrained | 2 |
| hunt's® tomato ketchup | 1 |
| hunt's® tomato paste | 2 |
| hunt's® tomato sauce | 7 |
| hunt's® tomato sauce with basil, garlic and oregano | 1 |
| hunt's® tomato sauce-no salt added | 2 |
| hydrated sun-dried tomato | 1 |
| i pound green (unripe) tomatoes, cored and coarsely chopped | 1 |
| i tablespoon tomato paste | 1 |
| ice water or tomato juice for thinning soup | 1 |
| in a bowl, combine the tomatoes, onion, garlic, olive oil, lemon juice, basil, tarragon, salt, and pepper. add the croutons and toss well | 1 |
| ingredient info: chipotle chiles are dried, smoked jalapeños in a spicy tomato sauce called adobo; they're available at some supermarkets and at specialty foods stores and latin markets | 1 |
| ingredient info: chipotle chiles are often sold in a spicy tomato sauce called adobo. they're available at some supermarkets and at specialty foods stores and latin markets | 1 |
| ingredient info: chipotle chiles in adobo (a spicy tomato sauce) are available at some supermarkets and at specialty foods stores and latin markets. liquid smoke is a smoke-flavored liquid seasoning. look for it at supermarkets and specialty foods stores | 1 |
| ingredient info: look for tomatillos (green, tomato-like fruits with papery husks) at supermarkets and latin markets | 1 |
| ingredient info: look for tomatillos, the green, tomato-like fruit with a papery husk, and canned chipotles in adobo at better supermarkets and at latin markets | 1 |
| italian canned plum tomatoes, cut into strips | 1 |
| italian canned tomatoes and their juice | 2 |
| italian cherry tomato | 1 |
| italian double-concentrated tomato paste*** | 1 |
| italian hot or sweet or combination of both sausages in red sauce from make-ahead meal earlier in week (browned sausages simmered in tomato sauce with stock) | 1 |
| italian hot or sweet or combination of both sausages in red sauce from make-ahead meal earlier in week (browned sausages simmered in tomato sauce with stock), recipe follows | 1 |
| italian plum san marzano tomato | 2 |
| italian plum tomato | 4 |
| italian plum tomatoes, cut in half lengthwise, thinly sliced | 1 |
| italian plum tomatoes, cut into wedges | 1 |
| italian plum tomatoes, drained and crushed | 1 |
| italian plum tomatoes, with juices | 1 |
| italian roma tomato | 11 |
| italian roma tomato, cored, seeded and diced | 1 |
| italian roma tomatoes, cored | 1 |
| italian roma tomatoes, cored and chopped | 3 |
| italian roma tomatoes, cored and cut into quarters | 1 |
| italian roma tomatoes, cored and diced | 3 |
| italian roma tomatoes, cored and seeds | 1 |
| italian roma tomatoes, cored, seeded and chopped | 1 |
| italian roma tomatoes, cored, seeded and cut into 1/4-inch dice | 1 |
| italian roma tomatoes, cored, seeded and diced | 1 |
| italian roma tomatoes, cored, seeded julienned | 1 |
| italian roma tomatoes, cored, seeded, and chopped (or use canned) | 1 |
| italian roma tomatoes, cut crosswise 1/4-inch thick | 1 |
| italian roma tomatoes, cut in 4 slices | 1 |
| italian roma tomatoes, seeded and chopped | 1 |
| italian roma tomatoes, seeded and diced | 4 |
| italian roma tomatoes, seeded and diced, for serving (optional) | 1 |
| italian roma tomatoes, stemmed, quartered and seed scooped out | 1 |
| italian style stewed tomato | 1 |
| italian tomato | 2 |
| italian tomato paste | 2 |
| italian tomatoes, blanched and peeled | 1 |
| italian tomatoes, halved | 1 |
| italian-seasoned tomato paste | 1 |
| italian-style diced tomatoes, undrained | 1 |
| italian-style tomato paste | 1 |
| jar (14 oz.) tomato pasta sauce | 1 |
| jar bertolli® tomato & basil sauce | 7 |
| jar bertolli® tomato & basil sauce, heated | 1 |
| jar bertolli® vineyard premium collections fire roasted tomato with cabernet sauvignon sauce | 3 |
| jar chunky tomato sauce (preferably lucini brand sicilian eggplant and olive)* | 1 |
| jar chunky tomato sauce with onion and garlic | 1 |
| jar classico® tomato and basil sauce | 3 |
| jar dickinson's® tomato ketchup | 1 |
| jar garlic-and-tomato pasta sauce | 1 |
| jar hot mexican-style tomato sauce (picante tomato sauce) | 1 |
| jar julienne sliced sun-dried tomatoes in oil, drained | 1 |
| jar low-fat tomato pasta sauce | 1 |
| jar marinara or tomato-basil sauce, warmed | 1 |
| jar mediterranean sun-dried tomatoes packed in oil, drained and chopped | 1 |
| jar muir glenn tomato sauce | 1 |
| jar oil-packed sun-dried tomato | 2 |
| jar oil-packed sun-dried tomatoes, drained and sliced | 1 |
| jar oil-packed sun-dried tomatoes, drained well and roughly chopped | 1 |
| jar oil-packed sun-dried tomatoes, drained, cut into strips | 1 |
| jar or can organic tomato paste | 1 |
| jar patak's rich tomato & onion cooking sauce (dopiaza) | 1 |
| jar ragu® chunky tomato, garlic & onion sauce | 1 |
| jar simple tomato sauce, recipe follows or other purchased marinara sauce | 1 |
| jar spicy roasted red pepper tomato sauce | 1 |
| jar spicy tomato sauce (such as diavolo) | 1 |
| jar sugar free, fat free tomato salsa | 2 |
| jar sun-dried tomato | 1 |
| jar sun-dried tomatoes in oil | 2 |
| jar sun-dried tomatoes in oil, 2 tablespoons oil reserved and tomatoes chopped | 1 |
| jar sun-dried tomatoes packed in oil | 1 |
| jar sun-dried tomatoes packed in oil, drained and chopped | 2 |
| jar sun-dried tomatoes packed in oil, drained and chopped (reserve oil) | 1 |
| jar sun-dried tomatoes packed in olive oil | 1 |
| jar sun-dried tomatoes, drained and chopped | 1 |
| jar sun-dried tomatoes, julienned (1 cup) | 1 |
| jar sun-dried tomatoes, packed in oil | 2 |
| jar sun-dried tomatoes, packed in oil - drained, oil reserved | 1 |
| jar sun-dried tomatoes, thinly sliced | 1 |
| jar tomato and basil pasta sauce (such as classico®) | 1 |
| jar tomato and olive pasta sauce (such as papayiannides® tomato & olive & ouzo sauce) | 2 |
| jar tomato basil pasta sauce | 2 |
| jar tomato basil pasta sauce (such as barilla®) | 1 |
| jar tomato pasta sauce | 4 |
| jar tomato puree | 3 |
| jar tomato sauce | 5 |
| jar tomato-based pasta sauce | 1 |
| jar tomato-basil pasta sauce, heated | 1 |
| jarred all-natural tomato sauce | 1 |
| jarred marinara or tomato-basil sauce | 1 |
| jarred or homemade tomato salsa | 1 |
| jarred sun-dried tomato pesto | 1 |
| jarred sundried tomatoes packed in oil | 1 |
| jarred tomato basil sauce, such as gdl for target tomato basil | 1 |
| jarred tomato salsa | 1 |
| jarred tomato salsa, plus more for serving | 1 |
| jarred tomato sauce | 3 |
| jarred tomato-basil sauce, such as giada de laurentiis for target | 4 |
| jarred tomato-basil sauce, such as giada delaurentiis for target | 1 |
| jars (16 ounces) tomato sauce | 1 |
| jars bertolli® tomato & basil sauce | 2 |
| jars classico® tomato and basil sauce | 1 |
| jars marinara sauce (such as classico® tomato and basil) | 1 |
| jars roasted tomato salsa such as frontera brand | 1 |
| jars sun-dried tomatoes, drained | 1 |
| jars tomato and basil pasta sauce (such as bertolli®) | 1 |
| jars tomato basil pasta sauce | 1 |
| jars tomato, onion, and garlic spaghetti sauce (such as prego®) | 1 |
| jars tomato-basil pasta sauce | 1 |
| jersey tomato | 1 |
| jersey tomatoes, cut into eights | 1 |
| juicy chopped fresh tomato | 1 |
| juicy tomatoes, cut into wedges | 2 |
| julienne cut sun-dried tomatoes with herbs, drained, oil reserved | 1 |
| julienne of sun dried tomato | 1 |
| julienne oil packed sun-dried tomato | 1 |
| julienne sliced sun-dried tomato | 1 |
| julienne sun-dried tomato | 1 |
| julienne tomato | 1 |
| julienne tomato concasse (peeled and seeded) | 1 |
| julienned oil-packed sun-dried tomato | 1 |
| julienned oven-dried tomato | 1 |
| julienned sun-dried tomato | 3 |
| julienned sun-dried tomatoes with oil | 1 |
| ketchup or 2 tablespoons tomato paste | 1 |
| ketchup or 3 tablespoons tomato paste and a pinch of sugar | 1 |
| ketchup or tomato puree | 1 |
| ketchup or tomato sauce | 3 |
| kraft sun-dried tomato vinaigrette dressing | 1 |
| la salsa di 5 minuti tomato sauce, as much as you need | 1 |
| large (35-ounce) cans of high quality plum tomato | 2 |
| large (8 oz.) tomatoes, blanched, seeded, and julienned | 1 |
| large (about 4 pounds) tomatoes, stemmed and quartered | 1 |
| large 1/2-inch-thick tomato slices | 1 |
| large 1/3-inch-thick tomato slices | 1 |
| large beef steak tomato | 1 |
| large beef steak tomato, seeded and finely diced | 1 |
| large beef tomato | 1 |
| large beefsteak or other tomato | 1 |
| large beefsteak tomato | 9 |
| large beefsteak tomato, about 3/4 to 1 pound, seeds removed and cut into 1/2-inch dice | 1 |
| large beefsteak tomato, cut into 1/2-inch thick slices | 1 |
| large beefsteak tomato, cut into 6 slices | 1 |
| large beefsteak tomato, cut into 8 wedges | 1 |
| large beefsteak tomato, cut into wedges | 1 |
| large beefsteak tomato, seeded and cut into 1/2-inch dice | 1 |
| large beefsteak tomato, thinly sliced into 6 round slices | 1 |
| large beefsteak tomato, thinly sliced into 8 slices | 1 |
| large beefsteak tomatoes (about 12 ounces each) | 2 |
| large beefsteak tomatoes (each about 9 to 10 ounces) | 1 |
| large beefsteak tomatoes, cut into 1/2-inch thick slices | 2 |
| large beefsteak tomatoes, cut into 1/4-inch-thick rounds | 1 |
| large beefsteak tomatoes, halved crosswise | 1 |
| large beefsteak tomatoes, quartered | 1 |
| large beefsteak tomatoes, quartered and thinly sliced | 1 |
| large beefsteak tomatoes, thinly sliced | 1 |
| large beefsteak tomatoes, very ripe | 1 |
| large can (28 ounces) peeled whole tomatoes, preferably san marzano | 1 |
| large can (29 to 32-ounces) crushed tomato | 1 |
| large can baked beans (not the tomato kind) | 1 |
| large can crushed tomato | 1 |
| large can diced tomato | 1 |
| large can peeled tomatoes, quartered | 1 |
| large can plum tomatoes and juices | 1 |
| large can san marzano crushed tomatoes (28 ounces) | 1 |
| large can san marzano tomato | 2 |
| large can tomato sauce | 1 |
| large can tomato soup | 1 |
| large can v-8 spicy tomato juice | 1 |
| large can whole tomato | 1 |
| large canned tomato | 1 |
| large cans italian san marzano tomato | 1 |
| large cans tomato | 2 |
| large cans tomato juice | 1 |
| large cans tomato paste | 3 |
| large cans whole tomato | 2 |
| large cans whole tomatoes, preferably san marzano | 2 |
| large cherry tomato | 1 |
| large cherry tomatoes (3/4 lb total) | 1 |
| large cherry tomatoes, cut in half | 1 |
| large cherry tomatoes, halved | 2 |
| large cherry tomatoes, quartered | 2 |
| large chopped fresh tomato | 1 |
| large creole or vine-ripened tomatoes, 6 cored and roughly chopped, 2 cored | 1 |
| large finely chopped fresh tomato | 1 |
| large firm heirloom tomatoes (about 10 ounces each), cored, cut horizontally in half | 1 |
| large firm ripe tomato | 1 |
| large firm ripe tomatoes (a mix of colors but of similar size) | 1 |
| large firm ripe tomatoes, seeded and chopped or 2 (1-pound) cans tomatoes, drained and chopped | 1 |
| large firm tomato | 3 |
| large firm tomato, cut horizontally into 4 slices | 1 |
| large firm, ripe tomato | 1 |
| large fresh beefsteak tomato | 1 |
| large fresh chopped tomatoes or 16 ounces whole peeled canned tomato | 1 |
| large fresh plum tomato | 1 |
| large fresh tomato | 15 |
| large fresh tomatoes (about 2 pounds) | 1 |
| large fresh tomatoes, seeds removed and medium diced | 1 |
| large green heirloom tomato, cored | 1 |
| large green roma tomato | 1 |
| large green tomato | 14 |
| large green tomato, cored | 1 |
| large green tomato, quartered lengthwise and thinly sliced | 1 |
| large green tomatoes (or firm, unripe heirloom or beefsteak tomatoes) | 1 |
| large green tomatoes, cut into 1/4-inch slices | 1 |
| large green tomatoes, cut into 1/4-inch-thick slices | 1 |
| large green tomatoes, cut into large chunks | 1 |
| large green tomatoes, seeded, cored and diced | 1 |
| large green zebra or yellow tomato | 1 |
| large heirloom beefsteak tomato | 1 |
| large heirloom multi-colored tomatoes, about 3 pounds | 1 |
| large heirloom or organic tomato | 1 |
| large heirloom tomato | 12 |
| large heirloom tomato, cut into 4 slices | 1 |
| large heirloom tomato, cut into 4 thick slices | 1 |
| large heirloom tomato, cut into 6 slices | 1 |
| large heirloom tomato, thickly sliced | 1 |
| large heirloom tomatoes (about 2 1/2 pounds) or 4 to 5 large plum tomato | 1 |
| large heirloom tomatoes (about 2 1/2 pounds), cored | 1 |
| large heirloom tomatoes (about 2 pounds) | 1 |
| large heirloom tomatoes (preferably brandywine), cut into 1/4-inch slices | 1 |
| large heirloom tomatoes (yellow and red beefsteaks can be substituted) | 1 |
| large heirloom tomatoes, all varieties and colors, seeded and diced into 1/4-inch cubes (reserve seeds and juices) | 1 |
| large heirloom tomatoes, any color, thinly sliced | 1 |
| large heirloom tomatoes, cut into 1/4-inch slices | 1 |
| large heirloom tomatoes, cut into 4 slices each | 1 |
| large heirloom tomatoes, cut into thick slices | 1 |
| large heirloom tomatoes, each cut into 4 slices | 1 |
| large heirloom tomatoes, halved | 1 |
| large heirloom tomatoes, stemmed | 1 |
| large hothouse tomato | 1 |
| large jars tomato sauce | 1 |
| large jersey tomato (beefsteak) | 1 |
| large multi-colored heirloom tomatoes, washed and dried | 1 |
| large oil-packed sun-dried tomatoes, well drained | 1 |
| large or 2 average overripe tomato | 1 |
| large or 2 medium beefsteak or hothouse tomato | 1 |
| large or 2 medium heirloom or beefsteak tomato | 1 |
| large or 2 medium very ripe tomato | 1 |
| large or 2 medium-size gorgeous, luscious, ripe red tomatoes, thinly sliced | 1 |
| large or 2 small ripe tomato | 1 |
| large or 3 medium red tomatoes, seeded and diced | 1 |
| large or 3 medium ripe tomatoes, cored | 1 |
| large or 3 medium tomato | 1 |
| large or 3 medium yellow tomatoes, seeded and diced | 1 |
| large or 4 -to 5 medium-sized ripe tomatoes (about 1 pound) | 1 |
| large overly-ripe beefsteak tomato | 1 |
| large peeled tomatoes, recipe below | 1 |
| large plum (roma) tomato, halved lengthwise, seeded, and cut into 1/4-inch dice | 1 |
| large plum or 5 campari tomato | 1 |
| large plum tomato | 33 |
| large plum tomato (about 4 ounces) | 1 |
| large plum tomato, cored and quartered | 1 |
| large plum tomato, cut crosswise into 8 slices, discarding ends | 1 |
| large plum tomato, halved, seeded and roasted until soft | 1 |
| large plum tomato, seeded | 2 |
| large plum tomato, seeds squeezed out | 1 |
| large plum tomato, thinly sliced crosswise | 1 |
| large plum tomatoes (1 1/2 lb), halved lengthwise | 1 |
| large plum tomatoes (1 1/3 pounds), halved lengthwise | 1 |
| large plum tomatoes (1 pound), trimmed and halved lengthwise | 1 |
| large plum tomatoes (3/4 to 1 pound total) | 1 |
| large plum tomatoes (about 1 1/2 pounds), quartered lengthwise | 1 |
| large plum tomatoes (about 1 1/4 pounds) | 1 |
| large plum tomatoes (about 1 pound), cut lengthwise into 1/3-inch thick slices | 1 |
| large plum tomatoes (about 10 ounces), seeded | 1 |
| large plum tomatoes (about 10) | 1 |
| large plum tomatoes (about 12 ounces) | 1 |
| large plum tomatoes (about 12 ounces), halved lengthwise | 1 |
| large plum tomatoes (about 2 1/2 pounds), halved lengthwise | 1 |
| large plum tomatoes (about 2/3 pound), each pricked 4 times with a fork | 1 |
| large plum tomatoes (about 8 ounces), each cut into 4 wedges | 1 |
| large plum tomatoes (about 8 ounces), seeded | 1 |
| large plum tomatoes, cored | 1 |
| large plum tomatoes, cored and halved | 1 |
| large plum tomatoes, cored, quartered | 1 |
| large plum tomatoes, cored, quartered lengthwise | 1 |
| large plum tomatoes, cored, seeded and cut into 1-inch pieces | 1 |
| large plum tomatoes, cut into 1/2-inch cubes | 1 |
| large plum tomatoes, cut into thin wedges | 1 |
| large plum tomatoes, each cut into 1/2-inch-thick rounds | 1 |
| large plum tomatoes, each cut into 4 wedges | 1 |
| large plum tomatoes, each cut into 6 wedges | 1 |
| large plum tomatoes, halved | 1 |
| large plum tomatoes, halved crosswise | 1 |
| large plum tomatoes, halved lengthwise | 1 |
| large plum tomatoes, halved lengthwise and seeded | 1 |
| large plum tomatoes, quartered | 2 |
| large plum tomatoes, quartered lengthwise | 2 |
| large plum tomatoes, quartered, seeds and membranes discarded, tomatoes diced | 1 |
| large plum tomatoes, seeded | 8 |
| large plum tomatoes, seeded and chopped | 2 |
| large plum tomatoes, seeded and cut into 1/4-inch dice | 1 |
| large plum tomatoes, seeded and diced | 1 |
| large plum tomatoes, seeded and finely diced | 1 |
| large plum tomatoes, thinly sliced | 1 |
| large plum tomatoes, very thinly sliced | 1 |
| large red and yellow cherry tomatoes (1-inch size) | 1 |
| large red and/or yellow tomatoes, about 8 ounces each, thinly sliced | 1 |
| large red and/or yellow tomatoes, each cut crosswise in half | 1 |
| large red beefsteak tomato | 1 |
| large red heirloom tomato | 3 |
| large red heirloom tomatoes, cored | 1 |
| large red tomato | 5 |
| large red tomatoes (2 lb total), cored and each cut crosswise into 5 slices | 1 |
| large red tomatoes, cut into wedges (about 2 pounds) | 1 |
| large red tomatoes, quartered | 1 |
| large red tomatoes, thickly sliced | 1 |
| large restaurant-size cans crushed tomatoes, at least 64 ounces | 1 |
| large rip kula beefsteak tomato | 1 |
| large ripe beefsteak or heirloom tomatoes, cut into 1/2" slices | 1 |
| large ripe beefsteak tomato, cut into 4 slices | 1 |
| large ripe beefsteak tomato, cut into 6 slices | 1 |
| large ripe beefsteak tomato, seeded and chopped | 1 |
| large ripe beefsteak tomatoes, each cut in to 6 to 8 thin slices | 1 |
| large ripe beefsteak tomatoes, seeded | 1 |
| large ripe fresh tomato | 1 |
| large ripe heirloom or organic beefsteak tomato, cored and chopped | 1 |
| large ripe heirloom tomatoes (about 1 1/4 pounds), very thinly sliced crosswise | 1 |
| large ripe plum tomato | 1 |
| large ripe plum tomatoes, halved lengthwise and seeded | 1 |
| large ripe plum tomatoes, seeded and diced (1/4 inch) | 1 |
| large ripe plum tomatoes, very thinly sliced | 1 |
| large ripe red tomato | 1 |
| large ripe summer tomatoes, seeded and diced | 1 |
| large ripe tomato | 67 |
| large ripe tomato (1/2 pound) | 1 |
| large ripe tomato (1/2 pound) peeled and chopped | 1 |
| large ripe tomato (9 to 10 ounces) | 1 |
| large ripe tomato or 2 roma tomato | 1 |
| large ripe tomato, cored | 1 |
| large ripe tomato, cored, halved and chopped | 1 |
| large ripe tomato, cut into 1-inch cubes | 1 |
| large ripe tomato, cut into 4 slices | 1 |
| large ripe tomato, cut into 8 thin slices | 1 |
| large ripe tomato, halved and thinly sliced | 1 |
| large ripe tomato, seeded and diced | 3 |
| large ripe tomato, seeded and diced into 2/3-inch cubes | 1 |
| large ripe tomato, seeded and diced, or 1 (15-ounce) can diced tomatoes, drained well | 1 |
| large ripe tomato, seeds removed and diced | 1 |
| large ripe tomato, skinned and finely chopped or grated | 1 |
| large ripe tomato, thinly sliced | 2 |
| large ripe tomatoes (1 pound) | 2 |
| large ripe tomatoes (about 1 1/2 pounds) | 1 |
| large ripe tomatoes (about 1 pound) | 2 |
| large ripe tomatoes (about 2 1/2 pounds) | 1 |
| large ripe tomatoes (about 2 pounds) | 1 |
| large ripe tomatoes (each about 8 ounces) | 1 |
| large ripe tomatoes of your choosing, colorful or one color, cut in half | 1 |
| large ripe tomatoes or 1 pint grape tomatoes, halved | 1 |
| large ripe tomatoes, 3 inches in diameter | 1 |
| large ripe tomatoes, about 1 pound total, trimmed, seeded and diced (1/4-inch) | 2 |
| large ripe tomatoes, cored and cut into 1/4" slices | 1 |
| large ripe tomatoes, cored, seeded, and chopped (about 2 cups) | 1 |
| large ripe tomatoes, cut crosswise into 1/4-inch thick slices | 1 |
| large ripe tomatoes, cut in ?-inch dice | 1 |
| large ripe tomatoes, cut into 1-inch chunks, or 20 cherry tomatoes, halved | 1 |
| large ripe tomatoes, cut into 1-inch pieces | 1 |
| large ripe tomatoes, cut into 3/4inch cubes | 1 |
| large ripe tomatoes, cut into bite-size pieces | 1 |
| large ripe tomatoes, cut into strips | 1 |
| large ripe tomatoes, cut into wedges | 4 |
| large ripe tomatoes, de-cored | 1 |
| large ripe tomatoes, halved and seeded | 1 |
| large ripe tomatoes, large dice | 2 |
| large ripe tomatoes, medium dice | 2 |
| large ripe tomatoes, mixed colors, 1 " large dice | 2 |
| large ripe tomatoes, mixed colors, 1 inch large dice | 1 |
| large ripe tomatoes, preferably 1 red and 1 yellow | 1 |
| large ripe tomatoes, preferably green or orange heirlooms, seeded and cut into 1-inch cubes | 1 |
| large ripe tomatoes, quartered | 1 |
| large ripe tomatoes, red or yellow or a combination of both | 1 |
| large ripe tomatoes, roasted (see note) | 1 |
| large ripe tomatoes, seeded and chopped | 1 |
| large ripe tomatoes, seeded and cut into 1/2 inch dice | 1 |
| large ripe tomatoes, seeded and diced | 3 |
| large ripe tomatoes, seeds removed and diced | 1 |
| large ripe tomatoes, seeds removed and diced into 1/4-inch pieces | 1 |
| large ripe tomatoes, seeds removed and diced small | 1 |
| large ripe tomatoes, small diced | 1 |
| large ripe tomatoes, thickly sliced | 2 |
| large ripe tomatoes, thinly sliced | 1 |
| large ripe tomatoes, washed, pureed in a food processor until smooth | 1 |
| large ripe yellow or red tomato | 1 |
| large ripe yellow tomatoes, (1 pound), trimmed, seeded and diced (1/4-inch) | 2 |
| large ripe yet firm fresh tomato, very thinly sliced with a mandoline | 1 |
| large ripe yet firm tomatoes, cored and thickly sliced | 1 |
| large roma (plum) tomato | 3 |
| large roma (plum) tomato, seeded and diced | 1 |
| large roma (plum) tomatoes, halved | 1 |
| large roma (plum) tomatoes, halved and seeded | 1 |
| large roma (plum) tomatoes, seeded and diced | 1 |
| large roma or heirloom tomato | 1 |
| large roma tomato | 9 |
| large roma tomato, thinly sliced | 1 |
| large roma tomatoes, cut into 1/2-inch-thick slices | 1 |
| large roma tomatoes, quartered | 1 |
| large roma tomatoes, whole, not cored or cut in any way | 1 |
| large round tomato | 3 |
| large round tomatoes, medium dice | 1 |
| large round tomatoes, seeded and chopped | 1 |
| large seeded and diced tomato | 1 |
| large slice tomato | 1 |
| large slices fresh tomato | 1 |
| large slices oven roasted tomato, recipe follows | 1 |
| large slices ripe red tomato, quartered | 1 |
| large slices tomato | 1 |
| large slices tomatoes, halved | 1 |
| large smoked tomatoes (see cook's note) | 1 |
| large sun-dried tomato | 2 |
| large sun-dried tomatoes (not oil-packed; about 3 ounces), cut into 1/4-inch strips | 1 |
| large sundried tomato | 1 |
| large thin tomato slices | 1 |
| large tomato | 383 |
| large tomato (1/2 lb) | 1 |
| large tomato (1/2 lb), cored | 1 |
| large tomato (12 to 13 ounces), halved, seeded, cut into 3/4-inch cubes | 1 |
| large tomato (4 ounces), seeded and diced | 1 |
| large tomato (about 1/2 pound) | 1 |
| large tomato (about 1/4 pound) | 1 |
| large tomato (about 4 inches in diameter) and 2 medium tomatoes (about 2 1/2 inches in diameter) | 1 |
| large tomato (about 8 ounces), cored, seeded, and cut into small dice (about 1 1/2 cups) | 1 |
| large tomato (about 9 ounces) | 1 |
| large tomato or 2 plum tomato | 1 |
| large tomato peeled, seeded and diced (or one can dice tomato in juice) | 1 |
| large tomato slices | 10 |
| large tomato slices (optional) | 1 |
| large tomato slices, about 1/4-inch thick | 1 |
| large tomato, (4 ounces) seeded and diced | 1 |
| large tomato, (8 ounces), halved, seeded, and the flesh cut into 1/2-inch dice (1 1/4 cups) | 1 |
| large tomato, about 8 ounces, halved and grated on the large holes of a box grater | 1 |
| large tomato, cored and chopped | 1 |
| large tomato, cored and sliced | 1 |
| large tomato, cored, cut into small cubes | 1 |
| large tomato, cored, seeded and chopped | 1 |
| large tomato, cored, seeded, and coarsely chopped | 1 |
| large tomato, cored, seeded, and diced | 1 |
| large tomato, cubed | 3 |
| large tomato, cut into 1/2-inch cubes | 1 |
| large tomato, cut into 1/2-inch-thick slices | 2 |
| large tomato, cut into 1/3-inch thick slices | 1 |
| large tomato, cut into 1/4-inch slices | 1 |
| large tomato, cut into 4 slices | 1 |
| large tomato, cut into 6 slices | 1 |
| large tomato, cut into 8 half-moon slices | 1 |
| large tomato, cut into 8 slices | 1 |
| large tomato, cut into chunks | 2 |
| large tomato, cut into cubes | 1 |
| large tomato, cut into four 1/4-inch-thick slices | 2 |
| large tomato, cut into large chunks | 2 |
| large tomato, cut into small dice | 1 |
| large tomato, cut into thin wedges | 1 |
| large tomato, cut into wedges | 9 |
| large tomato, halved | 1 |
| large tomato, halved and seeded | 1 |
| large tomato, halved and sliced | 1 |
| large tomato, halved and thinly sliced | 1 |
| large tomato, halved crosswise, seeded and thinly sliced | 1 |
| large tomato, halved, seeded | 1 |
| large tomato, halved, seeded, and chopped | 1 |
| large tomato, medium dice | 1 |
| large tomato, or 2 plum tomatoes, cut into 1/4inch thick slices | 1 |
| large tomato, preferably heirloom | 1 |
| large tomato, pureed | 1 |
| large tomato, quartered | 5 |
| large tomato, quartered, seeded, thinly sliced | 2 |
| large tomato, roasted | 1 |
| large tomato, seeded | 10 |
| large tomato, seeded and chopped | 11 |
| large tomato, seeded and chopped or 1 can 15 ounces can diced tomatoes, drained | 1 |
| large tomato, seeded and diced | 7 |
| large tomato, seeded and finely chopped | 2 |
| large tomato, seeded and finely diced | 4 |
| large tomato, seeded, and cut into medium dice (about 1 1/4 cups) | 1 |
| large tomato, seeds and pulp removed and chopped finely | 1 |
| large tomato, seeds removed and medium diced | 1 |
| large tomato, skinned, seeded, and sliced crossways into 6 "stars" | 1 |
| large tomato, stemmed | 1 |
| large tomato, the best you can find | 1 |
| large tomato, thickly sliced (4 slices) | 1 |
| large tomato, thinly sliced | 10 |
| large tomato, thinly sliced crosswise | 1 |
| large tomato-flavored tortilla | 1 |
| large tomato-flavored tortillas (or flour tortillas, if not available) | 1 |
| large tomatoes (1 1/2 lb total) | 2 |
| large tomatoes (1 1/2 to 2 pounds total) | 1 |
| large tomatoes (1 pound total) | 1 |
| large tomatoes (13 oz / 380 g in total), cut into 2/3-inch / 1.5cm dice | 1 |
| large tomatoes (2 thinly sliced, 1 grated) | 1 |
| large tomatoes (3 lb) | 1 |
| large tomatoes (3 pounds) | 1 |
| large tomatoes (4 1/2 lb) | 1 |
| large tomatoes (about 1 1/2 pounds) | 1 |
| large tomatoes (about 1 3/4 pounds), cut into 1-inch chunks | 2 |
| large tomatoes (about 1 pound total) | 1 |
| large tomatoes (about 1 pound) | 1 |
| large tomatoes (about 1 pound), trimmed and each cut into 8 wedges | 1 |
| large tomatoes (about 3 inches in diameter) | 1 |
| large tomatoes (about 3 pounds) | 2 |
| large tomatoes (about 3 pounds), cored | 1 |
| large tomatoes (preferably heirloom; 2 lb total) | 1 |
| large tomatoes - peeled, cored, and chopped | 1 |
| large tomatoes - peeled, seeded and chopped | 5 |
| large tomatoes - peeled, seeded, and coarsely chopped | 1 |
| large tomatoes chopped | 1 |
| large tomatoes cut in wedges | 1 |
| large tomatoes cut into wedges | 1 |
| large tomatoes diced | 1 |
| large tomatoes diced medium | 1 |
| large tomatoes grated on box grater | 1 |
| large tomatoes or 4 small ones | 1 |
| large tomatoes with bottoms (opposite the dimple) cut off | 1 |
| large tomatoes, 1/4-inch slices and seasoned with salt and pepper | 1 |
| large tomatoes, about 1 1/2 pounds, cut into 1/2-inch-thick slices | 1 |
| large tomatoes, boiled 30 seconds | 1 |
| large tomatoes, brunoise or small dice | 2 |
| large tomatoes, cored | 8 |
| large tomatoes, cored and quartered | 2 |
| large tomatoes, cored and seeded | 1 |
| large tomatoes, cored, seeded and chopped | 1 |
| large tomatoes, cored, seeded and diced | 1 |
| large tomatoes, cores removed, bottoms scored | 1 |
| large tomatoes, cubed | 5 |
| large tomatoes, cut in 1/2 | 1 |
| large tomatoes, cut in cubes | 1 |
| large tomatoes, cut in half crosswise | 1 |
| large tomatoes, cut in wedges | 2 |
| large tomatoes, cut into 1/2-inch dice | 3 |
| large tomatoes, cut into 1/2-inch pieces (2 cups) | 1 |
| large tomatoes, cut into 1/2-inch slices | 2 |
| large tomatoes, cut into 1/2-inch-thick slices | 1 |
| large tomatoes, cut into 1/4 inch slices | 1 |
| large tomatoes, cut into 1/4-inch cubes | 1 |
| large tomatoes, cut into 1/4-inch-thick rounds | 1 |
| large tomatoes, cut into 8 wedges | 1 |
| large tomatoes, cut into chunks | 2 |
| large tomatoes, cut into quarters | 1 |
| large tomatoes, cut into thin wedges | 3 |
| large tomatoes, cut into wedges | 10 |
| large tomatoes, cut julienne | 1 |
| large tomatoes, each cut crosswise into 4 slices | 1 |
| large tomatoes, each cut horizontally into 4 round slices | 1 |
| large tomatoes, each cut into 4 (1/2-inch-thick) slices | 1 |
| large tomatoes, each cut into 8 wedges | 2 |
| large tomatoes, halved | 5 |
| large tomatoes, halved and sliced | 1 |
| large tomatoes, halved and thinly sliced | 1 |
| large tomatoes, halved crosswise | 1 |
| large tomatoes, halved, cored and seeded | 1 |
| large tomatoes, preferably heirloom | 1 |
| large tomatoes, pureed | 2 |
| large tomatoes, quartered | 6 |
| large tomatoes, quartered and grated | 1 |
| large tomatoes, quartered, pulp and seeds removed, rolled up in double layer of paper towels, gently squeezed, paper removed, and coarsely diced | 1 |
| large tomatoes, ripe (suggest one black russian, one green zebra, one lemon boy, and 1 red better boy; if available) | 1 |
| large tomatoes, roasted and quartered | 1 |
| large tomatoes, seeded | 9 |
| large tomatoes, seeded and chopped | 6 |
| large tomatoes, seeded and chopped (3 cups) | 1 |
| large tomatoes, seeded and coarsely chopped | 2 |
| large tomatoes, seeded and cut into 1-inch chunks | 1 |
| large tomatoes, seeded and cut into 1/4inch dice | 1 |
| large tomatoes, seeded and diced | 3 |
| large tomatoes, seeded and diced (about 2 cups) | 1 |
| large tomatoes, seeded and finely diced | 1 |
| large tomatoes, seeded and sliced | 1 |
| large tomatoes, seeds removed | 1 |
| large tomatoes, seeds removed and diced | 1 |
| large tomatoes, seeds removed and diced fine | 1 |
| large tomatoes, seeds removed and medium diced | 1 |
| large tomatoes, skinned, seeded and chopped | 1 |
| large tomatoes, skinned, seeded, and quartered | 1 |
| large tomatoes, stems removed | 1 |
| large tomatoes, such as beefsteak (about 1 pound) | 1 |
| large tomatoes, thickly sliced | 1 |
| large tomatoes, thinly sliced | 7 |
| large tomatoes, washed and sliced | 1 |
| large unripe (green) tomatoes, cored, cut into 1/4-inch dice | 1 |
| large unripe tomatoes, cut into 1/2-inch thick slices, ends removed | 1 |
| large vine ripe tomato | 1 |
| large vine ripe tomatoes or beefsteak tomato | 1 |
| large vine ripened tomato, seeded and chopped | 1 |
| large vine ripened tomatoes, about 1 pound | 1 |
| large vine ripened tomatoes, quartered | 1 |
| large vine-ripe tomato | 4 |
| large vine-ripened tomato | 10 |
| large vine-ripened tomato (about 1/2 pound), seeded and chopped | 1 |
| large vine-ripened tomato, cut into 1/4 inch slices | 1 |
| large vine-ripened tomato, thinly sliced | 2 |
| large vine-ripened tomato, whole | 1 |
| large vine-ripened tomatoes or 1 (12-ounce) can tomato | 1 |
| large vine-ripened tomatoes, cut into 1/4-inch-thick slices | 1 |
| large vine-ripened tomatoes, cut into large dice | 1 |
| large vine-ripened tomatoes, quartered | 1 |
| large vine-ripened tomatoes, skinned, seeded and diced | 1 |
| large whole tomato | 1 |
| large whole wheat tortillas (or white, corn or sun-dried tomato) | 1 |
| large yellow beefsteak tomato | 1 |
| large yellow heirloom tomato | 1 |
| large yellow heirloom tomato, cored | 1 |
| large yellow tomato | 3 |
| large yellow tomatoes (2 lb total), cored and each cut crosswise into 5 slices | 1 |
| large yellow tomatoes, halved, hollowed | 1 |
| large yellow tomatoes, tops removed, seeded and flesh removed | 1 |
| large, extra-ripe tomato | 1 |
| large, firm green tomatoes, cut crosswise into 1/2-inch slices | 1 |
| large, firm plum tomatoes, seeded and diced | 1 |
| large, firm, ripe tomato, thinly sliced | 1 |
| large, plump sun-dried tomatoes (about 2 cups) | 1 |
| large, red heirloom tomato | 1 |
| large, red-ripe tomato, cut into chunks | 1 |
| large, ripe plum tomatoes, cut in half lengthwise | 1 |
| large, ripe tomato | 5 |
| large, ripe tomato, cored and coarsely chopped | 1 |
| large, ripe tomatoes, cored and diced | 1 |
| large, ripe tomatoes, cut into 1-inch cubes | 1 |
| large, ripe tomatoes, medium dice | 1 |
| large, ripe tomatoes, seeded and cut into 1/2-inch cubes | 1 |
| large, ripe, firm tomatoes, weighing approximately 3/4 pound each | 1 |
| large, round tomato, cut into 1/4-inch dice | 1 |
| large, thin tomato slices | 1 |
| large, very ripe tomato | 1 |
| leek-tomato quinoa | 1 |
| leftover asparagus stems from asparagus and tomato tart, recipe follows | 1 |
| leftover cooked spaghetti (with tomato sauce clinging to it) | 1 |
| leftover potatoes and tomato | 2 |
| leftover potatoes and tomatoes, recipe follows | 1 |
| leftover spaghetti with olives and tomato sauce, recipe follows | 1 |
| leftover tomato sauce, recipe follows | 1 |
| leftover tomatoes from chicken souvlaki recipe | 1 |
| lengthwise-halved grape tomato | 1 |
| lettuce and sliced tomato, for topping | 1 |
| lettuce and sliced tomato, for topping sandwiches | 1 |
| lettuce and sliced tomatoes, for topping | 1 |
| lettuce and tomato as accompaniments | 1 |
| lettuce and tomato slices | 1 |
| lettuce and tomato slices, for topping | 2 |
| lettuce and tomato, for burger | 1 |
| lettuce and tomatoes, as a garnish | 2 |
| lettuce leaves and sliced tomatoes, for serving | 1 |
| lettuce leaves, red onion slices, tomato slices (optional) | 1 |
| lettuce tomato slices, and red onion slices | 1 |
| lettuce, tomato, avocado | 1 |
| lettuce, tomato, onion | 1 |
| lettuce, tomato, onion and pickle, for garnish | 1 |
| lettuce, tomato, onion, for serving | 1 |
| lettuce, tomato, onion, pickles, for dressing the burger | 1 |
| lettuce, tomato, onions, for garnish | 1 |
| lettuce, tomato, onions, ketchup, mustard, for serving or whatever else you like on a burger | 1 |
| lettuce, tomato, pickles for garnish | 1 |
| lettuce, tomato, red onion and tartar sauce, for serving | 1 |
| lettuce, tomatoes, onion | 1 |
| level tablespoon tomato puree | 1 |
| light tomato sauce | 1 |
| lightly cooked crushed tomatoes * | 1 |
| lightly sauteed fresh tomato sauce | 1 |
| liquid (wine, bouillon, tomatoes, vegetable broth, etc.) | 1 |
| liquid drained from 1 (10-oz [283-g]) can diced tomatoes with green chiles (i like rotel) | 1 |
| liquid from canned tomato | 2 |
| local tomato | 1 |
| lomi tomato relish, recipe follows | 1 |
| loosely packed tender sun-dried tomatoes (not packed in oil) | 1 |
| low-fat creamy tomato soup or canned crushed tomato | 1 |
| low-sodium canned chopped tomatoes with juice | 1 |
| low-sodium tomato | 1 |
| low-sodium tomato juice | 5 |
| low-sodium tomato paste | 2 |
| low-sodium tomato sauce | 3 |
| lpound cherry or grape tomatoes (3 cups) | 1 |
| make sausage stuffing with spicy sausage and semolina bread. toss in 1 cup sliced sun-dried tomatoes with the bread. sprinkle with 1/4 cup grated parmesan before baking | 1 |
| mango or tomato chutney, for serving | 1 |
| marinara or tomato sauce | 1 |
| marinara or tomato-basil sauce | 1 |
| marinara sauce or tomato puree | 2 |
| marinated sun dried tomatoes, julienned | 1 |
| marinated sun dried tomatoes, reserve 1/3 cup of oil from marinade | 1 |
| marinated sun-dried tomato | 1 |
| marinated sun-dried tomatoes, cut in strips | 1 |
| marinated sun-dried tomatoes, cut into large shreds | 1 |
| marinated sundried tomatoes (about 2 ounces) | 1 |
| marinated tomato | 1 |
| mayonnaise, mustard or tomato jam | 1 |
| meat and tomato sauce, recipe follows | 1 |
| meatballs and 1 cup sauce from turkey meatball and spicy tomato sauce recipe | 1 |
| meaty plum tomatoes (about 1 pound), halved lengthwise | 1 |
| mediterranean alligator with a tomato and caper sauce, recipe follows | 1 |
| mediterranean-style (with basil, kalamata olive, and sun-dried tomato) crumbled feta cheese | 1 |
| medium (12 ounces) heirloom or 4 plum tomatoes, cut into 1/8-inch thick slices | 1 |
| medium beefsteak tomato | 4 |
| medium beefsteak tomato, cut into 4 slices | 1 |
| medium beefsteak tomato, halved then very thinly sliced | 1 |
| medium beefsteak tomato, seeded and cut into 1/2-inch dice | 1 |
| medium beefsteak tomatoes, cut into 1-inch chunks | 1 |
| medium beefsteak tomatoes, cut into 8 slices | 1 |
| medium beefsteak tomatoes, halved crosswise | 1 |
| medium diced plum tomato | 1 |
| medium early girl tomato | 2 |
| medium firm ripe tomato | 1 |
| medium fresh tomato | 7 |
| medium fresh tomato, or 1/2 cup canned plum tomato | 1 |
| medium fresh tomatoes - cored, quartered, and sliced as thin as possible | 1 |
| medium fresh tomatoes, cut into 1 inch chunks | 1 |
| medium fresh tomatoes, quartered | 1 |
| medium golden tomatoes, cut and seeded to form cups | 1 |
| medium green heirloom tomatoes, cored and cut into 1-inch cubes | 1 |
| medium green tomato | 3 |
| medium green tomato cut into 4 (1/4-inch) slices | 1 |
| medium green tomatoes (about 1 1/2 pounds) | 2 |
| medium green tomatoes (such as green zebra) | 1 |
| medium green tomatoes, cut into wedges | 1 |
| medium green tomatoes, thinly sliced | 1 |
| medium heat taco sauce or 1 (14-oz) can stewed or fire roasted tomato | 1 |
| medium heirloom tomato | 4 |
| medium heirloom tomato or other ripe beefsteak tomato, thinly sliced | 1 |
| medium heirloom tomatoes (about 1 1/4 pounds) | 1 |
| medium heirloom tomatoes (different varieties, if possible) | 1 |
| medium heirloom tomatoes, cut into 1" wedges | 1 |
| medium heirloom tomatoes, cut into thin wedges | 1 |
| medium heirloom tomatoes, cut into wedges | 2 |
| medium heirloom tomatoes, each cut into 4 slices | 1 |
| medium italian roma tomatoes, skinned, seeded | 1 |
| medium non-acidic tomato | 1 |
| medium or 2 large yellow tomatoes, seeded and chopped | 1 |
| medium or 2 small tomatoes, quartered, seeded, and roughly diced | 1 |
| medium or 3 plum tomato | 1 |
| medium or 4 very large ripe tomatoes (about 4 pounds), cored | 1 |
| medium or 5 roma tomatoes, cored, seeded and diced | 1 |
| medium or large heirloom tomato | 1 |
| medium or large tomato, cut crosswise into 1/4-inch thick slices | 1 |
| medium organic plum tomato | 1 |
| medium overripe and cracked or bruised tomato | 1 |
| medium plum (roma) tomato, seeded and chopped | 1 |
| medium plum tomato | 14 |
| medium plum tomato, cored and diced (about 1/4 cup) | 1 |
| medium plum tomatoes (1/2 pound) | 1 |
| medium plum tomatoes (about 15 ounces) | 1 |
| medium plum tomatoes (about 2 1/4 pounds) | 1 |
| medium plum tomatoes, ends removed | 1 |
| medium plum tomatoes, halved lengthwise | 1 |
| medium plum tomatoes, halved lengthwise and seeded | 1 |
| medium plum tomatoes, halved lengthwise, gently seeded, and thinly sliced | 1 |
| medium plum tomatoes, halved lengthwise, seeded, and thinly sliced | 1 |
| medium plum tomatoes, quartered | 1 |
| medium plum tomatoes, roasted | 1 |
| medium plum tomatoes, seeded | 1 |
| medium plum tomatoes, seeded and chopped coarse | 1 |
| medium plum tomatoes, seeded and diced | 1 |
| medium plum tomatoes, seeded and quartered | 2 |
| medium plum tomatoes, thinly sliced crosswise | 1 |
| medium plum tomatoes, trimmed and cut into 1/4-inch dice (3/4 cup) | 1 |
| medium red and yellow tomatoes, stemmed and quartered | 1 |
| medium red heirloom tomatoes, cored and cut into 1-inch cubes | 1 |
| medium red tomatoes (about 1 pound), cut into 1/2-inch-thick wedges | 1 |
| medium red tomatoes, cut into wedges | 1 |
| medium red vine ripe tomatoes, cut into wedges | 1 |
| medium ripe fresh red tomato | 1 |
| medium ripe red tomato, seeded and coarsely chopped | 1 |
| medium ripe red tomatoes, quartered and seeded | 1 |
| medium ripe tomato | 23 |
| medium ripe tomato, blanched | 1 |
| medium ripe tomato, cored and cut into 4 thick slices | 1 |
| medium ripe tomato, cored, thinly sliced | 1 |
| medium ripe tomato, cut into thin wedges | 1 |
| medium ripe tomatoes (12 ounces) | 1 |
| medium ripe tomatoes (about 1 1/2 pounds) | 1 |
| medium ripe tomatoes, cored and cut into slim wedges (no need to peel) | 1 |
| medium ripe tomatoes, cored and diced | 1 |
| medium ripe tomatoes, cored and roughly chopped | 1 |
| medium ripe tomatoes, cored, seeded and finely diced | 1 |
| medium ripe tomatoes, cored, seeded, and chopped | 1 |
| medium ripe tomatoes, cored, seeded, and finely diced | 7 |
| medium ripe tomatoes, cored,seeded, and finely diced | 1 |
| medium ripe tomatoes, cut into 1/2-inch dice | 1 |
| medium ripe tomatoes, cut into 1/4-inch thick slices | 1 |
| medium ripe tomatoes, cut into chunks | 2 |
| medium ripe tomatoes, cut into medium sized cubes | 1 |
| medium ripe tomatoes, cut into wedges | 1 |
| medium ripe tomatoes, halved | 1 |
| medium ripe tomatoes, seeded and chopped | 1 |
| medium ripe tomatoes, seeded and cut into 1/2-inch dice | 2 |
| medium ripe tomatoes, seeds removed | 1 |
| medium ripe whole tomato | 1 |
| medium ripe yellow or red tomatoes (about 2 pounds) | 2 |
| medium ripe, tomatoes, cut into 1-inch pieces | 1 |
| medium roma (plum) tomato | 1 |
| medium roma tomato | 5 |
| medium roma tomato, seeded and diced | 1 |
| medium roma tomatoes (2 pounds) | 5 |
| medium roma tomatoes, cored, seeded and chopped (about 2/3 cup) | 1 |
| medium roma tomatoes, cored, seeded and diced | 1 |
| medium roma tomatoes, halved | 1 |
| medium roma tomatoes, halved crosswire | 1 |
| medium seeded and chopped fresh tomatoes or 2 cups store-bought fresh salsa | 1 |
| medium size ripe roma tomato | 2 |
| medium size tomato | 1 |
| medium size very ripe tomato | 1 |
| medium sized fresh, red, ripe tomato | 1 |
| medium sized red tomato | 1 |
| medium sized round tomato | 1 |
| medium sun-dried tomatoes (not packed in oil) | 1 |
| medium to large green tomatoes (about 3 pounds) | 1 |
| medium to large ripe heirloom tomato | 1 |
| medium to large tomatoes, halved | 1 |
| medium to small vine-ripened tomato | 3 |
| medium tomatillos (husks removed and rinsed) or 2 green tomato | 1 |
| medium tomato | 253 |
| medium tomato (about 5 ounces), seeded and diced | 1 |
| medium tomato (about 6 ounces), halved | 1 |
| medium tomato - peeled, seeded and chopped | 7 |
| medium tomato, cored | 2 |
| medium tomato, cored and chopped | 1 |
| medium tomato, cored and cut into quarters | 1 |
| medium tomato, cored and seeded, flesh roughly chopped | 1 |
| medium tomato, cored, cut in 1/2 inch dice | 1 |
| medium tomato, cored, seeded and diced | 2 |
| medium tomato, cored, seeded, and diced | 1 |
| medium tomato, cut in half and sliced | 1 |
| medium tomato, cut in small dice (3/4 cup) | 1 |
| medium tomato, cut into 1/4-inch dice | 1 |
| medium tomato, cut into 1/4-inch-thick slices | 1 |
| medium tomato, cut into wedges | 2 |
| medium tomato, halved | 2 |
| medium tomato, halved and sliced 1/4 inch thick | 1 |
| medium tomato, quartered | 1 |
| medium tomato, quartered and seeded | 1 |
| medium tomato, seeded | 2 |
| medium tomato, seeded and chopped | 1 |
| medium tomato, seeded and chopped (optional) | 1 |
| medium tomato, seeded and cut into 1/4 inch dice | 1 |
| medium tomato, seeded and cut into 1/4-inch dice | 1 |
| medium tomato, seeded and diced | 2 |
| medium tomato, seeded and finely chopped (about 3/4 cup) | 1 |
| medium tomato, seeded and finely diced | 1 |
| medium tomato, seeded and small-diced | 1 |
| medium tomato, seeded and squeezed to eliminate liquid | 1 |
| medium tomato, seeded, and small-diced | 3 |
| medium tomato, seeds removed | 1 |
| medium tomato, stemmed and halved | 1 |
| medium tomato, thickly sliced | 1 |
| medium tomato, thinly sliced | 7 |
| medium tomato, thinly sliced (optional) | 1 |
| medium tomatoes (1 lb total), cut into 1/2-inch-thick wedges | 1 |
| medium tomatoes (1 pound) | 1 |
| medium tomatoes (1 pound), halved and cored | 1 |
| medium tomatoes (1 sliced, 1 chopped) | 1 |
| medium tomatoes (1 whole, 1 thickly sliced) | 1 |
| medium tomatoes (1/2 pound) | 1 |
| medium tomatoes (1/8 lb total), cut into 1/2-inch-thick wedges | 1 |
| medium tomatoes (10 ounces total) | 1 |
| medium tomatoes (3/4 lb total), cut into 3/4-inch-thick slices | 1 |
| medium tomatoes (3/4 pound) | 1 |
| medium tomatoes (3/4 pound), seeded and cut into 1/2-inch pieces | 1 |
| medium tomatoes (about 1 1/2 pounds total) | 1 |
| medium tomatoes (about 1 1/4 lbs) | 1 |
| medium tomatoes (about 1 pound), broiled | 1 |
| medium tomatoes (about 1 pound), cut into thick wedges | 1 |
| medium tomatoes (about 1 pound), each cut into 6 wedges | 1 |
| medium tomatoes (about 10), halved, cored, seeded | 1 |
| medium tomatoes (about 2 pounds), seeded, cut into 1/2" pieces | 1 |
| medium tomatoes (about 3) | 1 |
| medium tomatoes (about 3/4 pound total), each cut into 8 wedges | 1 |
| medium tomatoes (about 6), cut crosswise into 1/2-inch-thick slices | 1 |
| medium tomatoes (smoked for 10 to 15 minutes on a home smoker) | 1 |
| medium tomatoes (such as cluster or vine-ripened; do not use heirloom; about 5) | 1 |
| medium tomatoes - peeled, seeded, and coarsely chopped | 1 |
| medium tomatoes cored, seeded and diced | 1 |
| medium tomatoes diced (2 cups) | 1 |
| medium tomatoes or large romas, cored, halved crosswise, seeded | 1 |
| medium tomatoes sliced | 1 |
| medium tomatoes with stems still attached | 1 |
| medium tomatoes, 1/4-inch dice | 1 |
| medium tomatoes, blanched | 2 |
| medium tomatoes, blanched, skinned, seeds removed, cut into quarters | 1 |
| medium tomatoes, cored | 3 |
| medium tomatoes, cored and cut into 1/4-inch dice | 1 |
| medium tomatoes, cored and finely chopped | 2 |
| medium tomatoes, cored and quartered | 1 |
| medium tomatoes, cored and sliced into 1/2-inch thick slices | 1 |
| medium tomatoes, cored, halved and thinly sliced | 1 |
| medium tomatoes, cored, seeded | 1 |
| medium tomatoes, cored, seeded and chopped | 1 |
| medium tomatoes, cored, seeded and diced | 4 |
| medium tomatoes, cored, seeded and julienned | 1 |
| medium tomatoes, cored, seeded plus 1 tomato | 1 |
| medium tomatoes, cored, seeded, and finely chopped | 2 |
| medium tomatoes, cored, seeded, cut into 1/4-inch cubes | 1 |
| medium tomatoes, cut crosswise into 1/4-inch-thick slices | 2 |
| medium tomatoes, cut in 1/2 | 1 |
| medium tomatoes, cut in quarters | 1 |
| medium tomatoes, cut into 1/2-inch slices | 1 |
| medium tomatoes, cut into 1/2-inch-thick wedges | 1 |
| medium tomatoes, cut into 1/2-inch-thick wedges, or 1 pint cherry tomatoes, halved | 1 |
| medium tomatoes, cut into 1/4 inch slices | 1 |
| medium tomatoes, cut into 1/4-inch dice | 1 |
| medium tomatoes, cut into 12 slices | 1 |
| medium tomatoes, cut into 4 slices each | 1 |
| medium tomatoes, cut into chunks | 3 |
| medium tomatoes, cut into eight 1/4-inch thick slices | 2 |
| medium tomatoes, cut into large dice | 1 |
| medium tomatoes, cut into medium dice | 1 |
| medium tomatoes, cut into quarters and seeded | 1 |
| medium tomatoes, cut into thin wedges | 3 |
| medium tomatoes, cut into wedges | 6 |
| medium tomatoes, halved | 9 |
| medium tomatoes, halved and cored | 1 |
| medium tomatoes, halved crosswise | 3 |
| medium tomatoes, halved horizontally | 1 |
| medium tomatoes, halved through cores | 1 |
| medium tomatoes, halved, seeded | 1 |
| medium tomatoes, halved, seeded, cut into 3/4-inch pieces | 1 |
| medium tomatoes, preferably heirloom varieties | 1 |
| medium tomatoes, preferably with stems intact | 2 |
| medium tomatoes, pureed | 1 |
| medium tomatoes, quartered | 6 |
| medium tomatoes, quartered and seeded (about 3 pounds total) | 1 |
| medium tomatoes, roasted | 1 |
| medium tomatoes, seeded | 3 |
| medium tomatoes, seeded and chopped | 8 |
| medium tomatoes, seeded and chopped into 1/2-inch pieces | 1 |
| medium tomatoes, seeded and coarsely chopped | 1 |
| medium tomatoes, seeded and cut into strips | 1 |
| medium tomatoes, seeded and diced | 10 |
| medium tomatoes, seeded and diced (about 2 cups) | 5 |
| medium tomatoes, seeded and finely chopped | 2 |
| medium tomatoes, seeded and pureed | 1 |
| medium tomatoes, seeded and roughly chopped | 1 |
| medium tomatoes, seeded, cut into 1/2-inch pieces | 1 |
| medium tomatoes, seeds removed, and chopped | 1 |
| medium tomatoes, such as plum or vine-ripened style | 1 |
| medium tomatoes, thinly sliced | 9 |
| medium vine ripe tomatoes, about 8 ounces | 1 |
| medium vine ripened red tomatoes, wedged | 1 |
| medium vine ripened tomato | 1 |
| medium vine ripened yellow tomatoes, wedged | 1 |
| medium vine-ripe or roma tomato | 1 |
| medium vine-ripe red tomato | 1 |
| medium vine-ripe tomato | 1 |
| medium vine-ripe tomatoes, seeded and chopped | 1 |
| medium vine-ripened or heirloom tomato | 1 |
| medium vine-ripened red tomatoes (about 1 1/2 pounds) | 1 |
| medium vine-ripened tomato | 11 |
| medium vine-ripened tomato (about 1/2 pound), cut into 1-inch chunks | 1 |
| medium vine-ripened tomato, seeded and puréed (about 1/2 cup) | 1 |
| medium vine-ripened tomato, thinly sliced | 1 |
| medium vine-ripened tomatoes (about 2 1/4 pounds) | 1 |
| medium vine-ripened tomatoes (about 5) | 1 |
| medium vine-ripened tomatoes, cored and cut into 12 wedges | 1 |
| medium vine-ripened tomatoes, cut into thin wedges | 1 |
| medium vine-ripened tomatoes, cut into wedges | 1 |
| medium vine-ripened tomatoes, halved and cut into 1/4-inch-thick slices | 1 |
| medium vine-ripened tomatoes, seeded and chopped | 1 |
| medium vine-ripened tomatoes, seeded and diced | 1 |
| medium vine-ripened tomatoes, thinly sliced | 1 |
| medium vine-ripened yellow tomatoes (about 1 1/2 pounds) | 1 |
| medium vined ripened tomatoes, seeded and chopped | 1 |
| medium vineripened tomatoes, thinly sliced | 1 |
| medium yellow beefsteak tomatoes (1 3/4 pounds) | 1 |
| medium yellow heirloom tomatoes, cored and cut into 2-inch cubes | 1 |
| medium yellow tomato | 1 |
| medium yellow tomato cut into 4 (1/2-inch) slices | 1 |
| medium yellow tomato, cut into 1/4-inch slices | 1 |
| medium yellow tomatoes (about 1 pound) | 1 |
| medium yellow tomatoes (about 2) or 1/2 pound plum tomatoes, cut into 1/2-inch wedges | 2 |
| medium yellow tomatoes (about 3/4 pound) | 1 |
| medium yellow tomatoes, cut into 1/2-inch thick wedges (about 1 pound) | 1 |
| medium yellow vine ripe tomatoes, cut into wedges | 1 |
| medium yellow vine-ripe tomatoes or yellow-green tone heirloom tomatoes or 1 cup yellow grape tomato | 1 |
| medium zucchini, cut into cubes the size of the tomato | 1 |
| medium, firm vine-ripened tomato | 1 |
| medium, ripe tomato | 2 |
| medium-dice tomato | 3 |
| medium-dice tomatoes (seeded before dicing) | 1 |
| medium-diced tomato | 1 |
| medium-large tomatoes, or 8 large (about 2 pounds) plum tomatoes, cut into 1-inch pieces | 1 |
| medium-large vine ripened tomato | 1 |
| medium-ripe green tomato | 1 |
| medium-ripe japanese beefsteak/heirloom tomatoes, thinly sliced in rounds and kept together | 1 |
| medium-ripe tomatoes, cored and cut into 3/4-inch pieces | 1 |
| medium-size deep-red ripe tomatoes (such as early girl), halved, seeded, cored | 1 |
| medium-size ripe tomato | 2 |
| medium-size ripe tomatoes, cut into 1/2-inch-thick wedges | 1 |
| medium-size ripe tomatoes, cut into wedges | 1 |
| medium-size tomato | 1 |
| medium-size tomato, cored and cut into 1-inch cubes | 1 |
| medium-size tomato, cut into wedges, for garnish | 1 |
| medium-size vine-ripened tomato | 1 |
| medium-size, ripe tomato | 1 |
| medium-sized beefsteak tomato | 1 |
| medium-sized ripe tomato | 3 |
| medium-sized ripe tomatoes, cut into 8 pieces | 1 |
| medium-sized roma tomatoes, thinly sliced lengthwise | 1 |
| medium-sized round vine ripened tomato | 1 |
| medium-sized tomato | 2 |
| medium-sized tomatoes, quartered | 1 |
| medium-sized unripe tomatoes, cut into wedges | 1 |
| medium-small ripe red or yellow tomato | 1 |
| melted butter or 1/2 cup tomato sauce or 1/2 cup homemade meat sauce | 1 |
| mexican green tomato or tomatillo | 1 |
| mexican hot-style tomato sauce | 1 |
| mexican hot-style tomato sauce (recommended: el pato brand) | 1 |
| mexican-flavored canned tomatoes, drained and chopped | 2 |
| mexican-style hot tomato sauce (such as el pato salsa de chile fresco®) | 1 |
| mexican-style tomato sauce | 1 |
| mexican-style tomato sauce, recipe follows | 1 |
| mild tomato salsa | 1 |
| milled or crushed canned italian plum tomato | 4 |
| minced and seeded tomato | 1 |
| minced drained bottled dried tomato | 1 |
| minced drained oil-packed sun-dried tomato | 1 |
| minced drained sun-dried tomatoes in oil | 1 |
| minced drained sundried tomatoes packed in oil | 1 |
| minced sun-dried tomato | 1 |
| minced tomato | 4 |
| mini plum tomatoes or large cherry tomato | 1 |
| mini pumpkins (each about the size of a large tomato) | 1 |
| miniature cherry tomatoes (such as katinka cherry or red currant tomatoes) | 1 |
| miniature red pear tomatoes, halved | 1 |
| miniature yellow grape tomatoes, halved | 1 |
| mix 1 tsp. of sundried tomato pesto and 1 tbsp. of chopped sun dried tomatoes into a ½ cup stick of softened butter | 1 |
| mixed cherry or grape tomatoes, halved | 1 |
| mixed cherry tomato | 1 |
| mixed cherry tomatoes (1 pound), halved | 1 |
| mixed chopped seasonal fresh vegetables, such as squash, broccoli, cauliflower, zucchini, red onion, tomato, and carrot | 1 |
| mixed colors and sizes heirloom tomato | 1 |
| mixed green tomatoes (not unripe), cut into 3/4-inch wedges | 1 |
| mixed heirloom tomato | 6 |
| mixed heirloom tomatoes (2 to 2 1/2 inches) | 1 |
| mixed heirloom tomatoes, cored, seeded and cut into 1/2-inch pieces | 1 |
| mixed heirloom tomatoes, cut in wedges | 1 |
| mixed heirloom tomatoes, cut into 1 1/4-inch chunks | 1 |
| mixed heirloom tomatoes, cut into chunks | 1 |
| mixed heirloom tomatoes, not overly ripe, medium dice | 1 |
| mixed heirloom tomatoes, whole or cut into wedges, depending on size microgreens (for serving) | 1 |
| mixed red and purple raw fruits and vegetables (such as tomatoes, plums, berries, radishes, beets, rainbow carrots, and watermelon), halved | 1 |
| mixed red and yellow grape tomatoes (about 12 ounces) | 1 |
| mixed red, yellow and green grape tomato | 1 |
| mixed shapes and sizes tomato | 1 |
| mixed small tomato | 1 |
| mixed small tomatoes, such as sun gold, cherry, or heirloom, halved | 1 |
| mixed specialty or vine-ripened tomato | 1 |
| mixed tomato salsa, recipe follows | 1 |
| mixed tomatoes (different colors) | 1 |
| mixed yellow and orange raw fruits and vegetables (such as corn, sun gold tomatoes, golden beets, apricots, clementines, and pineapple), halved | 1 |
| mixed-color cherry tomatoes, on the vine | 1 |
| more or less, fresh tomato pulp | 1 |
| muir glen® organic crushed tomatoes with basil | 1 |
| multicolored cherry tomatoes, halved | 1 |
| multicolored cherry tomatoes, halved (quartered if large) | 1 |
| naturesweet cherry tomatoes, halved | 2 |
| nice tomato | 1 |
| no salt added canned crushed tomato | 1 |
| no sugar added tomato paste | 1 |
| no sugar added tomato sauce | 2 |
| no-salt added tomato | 1 |
| no-salt added tomato paste | 2 |
| no-salt crushed tomatoes in puree | 1 |
| no-salt-added chopped tomato | 1 |
| no-salt-added crushed tomato | 1 |
| no-salt-added tomato paste | 2 |
| no-salt-added tomato sauce | 4 |
| no-sugar added tomato salsa | 1 |
| no-sugar-added tomato paste | 2 |
| no-sugar-added tomato sauce | 2 |
| of chopped tomato | 2 |
| of diced tomato | 3 |
| of diced tomatoes with chilis | 1 |
| of either green olive paste, pesto or sundried tomato puree | 1 |
| of fresh red tomato | 1 |
| of plum tomato | 2 |
| of ripe tomatoes, cut into 1/4 inch slices | 1 |
| of sugar (if roasting the tomato in the oven) | 1 |
| of tomato juice | 1 |
| of tomato paste | 1 |
| of tomato paste or sauce | 1 |
| of tomatoes (chopped 1/4 inch dice) | 1 |
| oil from jar of sun-dried tomato | 1 |
| oil from oil-packed sun-dried tomatoes or olive oil | 1 |
| oil from the jar of sun-dried tomato | 1 |
| oil from the sun-dried tomato | 2 |
| oil packed sun-dried tomato | 2 |
| oil packed sun-dried tomatoes, cut into thin strips | 1 |
| oil packed sun-dried tomatoes, drained and finely chopped | 1 |
| oil packed sun-dried tomatoes, drained and sliced | 1 |
| oil packed sundried tomatoes, cut into slivers | 1 |
| oil, from marinated sun-dried tomato | 1 |
| oil-cured sundried tomato | 1 |
| oil-marinated sun-dried tomato | 1 |
| oil-packed sliced sun-dried tomato | 1 |
| oil-packed sun dried tomatoes, thinly sliced | 1 |
| oil-packed sun-dried tomato | 14 |
| oil-packed sun-dried tomato halves, drained and chopped | 1 |
| oil-packed sun-dried tomato halves, patted dry | 1 |
| oil-packed sun-dried tomatoes (3 ounces) | 1 |
| oil-packed sun-dried tomatoes, cut into thin strips | 1 |
| oil-packed sun-dried tomatoes, drained | 7 |
| oil-packed sun-dried tomatoes, drained (4-6 pieces) | 1 |
| oil-packed sun-dried tomatoes, drained and chopped | 6 |
| oil-packed sun-dried tomatoes, drained and cut into strips | 4 |
| oil-packed sun-dried tomatoes, drained and diced | 3 |
| oil-packed sun-dried tomatoes, drained and finely chopped | 2 |
| oil-packed sun-dried tomatoes, drained and halved | 1 |
| oil-packed sun-dried tomatoes, drained and julienned, patted dry | 1 |
| oil-packed sun-dried tomatoes, drained and roughly chopped | 1 |
| oil-packed sun-dried tomatoes, drained and sliced | 2 |
| oil-packed sun-dried tomatoes, drained and sliced into thin strips | 1 |
| oil-packed sun-dried tomatoes, drained and torn into bite-size pieces (heaping 1/2 cup) | 1 |
| oil-packed sun-dried tomatoes, drained, patted dry | 1 |
| oil-packed sun-dried tomatoes, in their oil | 1 |
| oil-packed sun-dried tomatoes, julienned | 2 |
| oil-packed sun-dried tomatoes, julienned, oil reserved | 1 |
| oil-packed sun-dried tomatoes, plus 3 tablespoons of the oil | 1 |
| oil-packed sundried tomato half | 1 |
| oil-packed sundried tomato halves, drained, oil reserved | 1 |
| oil-poached cherry tomatoes on the vine, recipe follows | 1 |
| okra cooked with tomato | 1 |
| okra, onion and tomato stew, recipe follows | 1 |
| olive oil (1 tablespoon for the tomatoes and 1 tablespoon to toss with the couscous) | 1 |
| olive oil for brushing tomato | 1 |
| olive oil from jar of sun-dried tomato | 1 |
| olive oil tomato sauce to cover pizza | 1 |
| olive oil, plus additional for drizzling tomato | 1 |
| olive oil, plus extra for tomato | 1 |
| olive oil, tomatoes, basil | 2 |
| once 15-ounce can fire roasted tomatoes, stewed tomatoes or diced tomatoes with chiles | 1 |
| one #10 can san marzano tomatoes (about 6 pounds 6 ounces) | 1 |
| one (14.5-ounce) can diced tomato | 1 |
| one (28-ounce) can crushed tomatoes, or plum tomatoes in puree | 1 |
| one (28-ounce) can stewed tomato | 1 |
| one 10 3/4-ounce can condensed cream of tomato soup | 1 |
| one 10- or 15-ounce can diced tomatoes with green chiles | 1 |
| one 10-ounce can chopped tomatoes with green chiles, such as ro*tel | 1 |
| one 10-ounce can diced tomatoes and green chiles | 1 |
| one 10-ounce can diced tomatoes and green chiles, such as rotel | 2 |
| one 10-ounce can diced tomatoes and green chilies, such as rotel | 1 |
| one 10-ounce can diced tomatoes and onions with lime juice and cilantro | 2 |
| one 10-ounce can diced tomatoes with green chiles | 1 |
| one 10-ounce can diced tomatoes with green chiles, such as ro*tel | 2 |
| one 10-ounce can stewed tomatoes with chilies, such as rotel original | 1 |
| one 10-ounce can tomatoes and chiles, such as ro-tel, drained | 1 |
| one 10-ounce can tomatoes with chiles, such as rotel | 1 |
| one 10.5-ounce container grape tomato | 2 |
| one 102-ounce (#10 can) tomato fillets | 1 |
| one 12-ounce can diced tomato | 1 |
| one 12-ounce can diced tomatoes and green chiles | 1 |
| one 12-ounce can peeled whole tomato | 1 |
| one 12-ounce can tomato paste | 4 |
| one 12-ounce can tomato puree | 1 |
| one 12-ounce can tomato sauce | 1 |
| one 12-ounce jar sun-dried tomatoes in oil, drained well | 1 |
| one 14 1/2-ounce can crushed tomato | 1 |
| one 14 1/2-ounce can diced tomato | 3 |
| one 14 1/2-ounce can diced tomatoes in juice | 1 |
| one 14 1/2-ounce can diced tomatoes, drained | 2 |
| one 14 1/2-ounce can no-salt added diced tomato | 1 |
| one 14 1/2-ounce can petite diced tomato | 1 |
| one 14 1/2-ounce can petite-cut, no-salt diced tomato | 1 |
| one 14 1/2-ounce can whole peeled tomato | 1 |
| one 14 1/2-ounce can whole peeled tomatoes, with their juice | 2 |
| one 14-ounce can chopped tomato | 2 |
| one 14-ounce can chunky crushed tomato | 1 |
| one 14-ounce can chunky style crushed tomato | 1 |
| one 14-ounce can crushed or diced fire-roasted tomatoes or diced tomatoes with green chilies | 1 |
| one 14-ounce can crushed tomato | 7 |
| one 14-ounce can diced tomato | 11 |
| one 14-ounce can diced tomatoes or petite diced tomato | 1 |
| one 14-ounce can diced tomatoes with green chiles or 1 can diced tomatoes mixed with one 4-ounce can chopped green chiles | 1 |
| one 14-ounce can diced tomatoes with juices | 1 |
| one 14-ounce can diced tomatoes, in puree | 1 |
| one 14-ounce can fire-roasted diced tomato | 1 |
| one 14-ounce can fire-roasted tomatoes, with liquid | 1 |
| one 14-ounce can italian crushed tomato | 1 |
| one 14-ounce can italian tomatoes, drained | 1 |
| one 14-ounce can no-salt-added diced tomato | 2 |
| one 14-ounce can peeled plum tomato | 1 |
| one 14-ounce can peeled san marzano tomatoes, broken apart with your hands | 1 |
| one 14-ounce can petite diced tomato | 2 |
| one 14-ounce can san marzano tomato | 1 |
| one 14-ounce can san marzano tomatoes, crushed by hand and mixed with half of the sauce | 1 |
| one 14-ounce can san marzano tomatoes, with juice | 1 |
| one 14-ounce can seedless chopped tomatoes, well drained and rinsed | 1 |
| one 14-ounce can stewed tomato | 1 |
| one 14-ounce can stewed tomatoes, pureed | 1 |
| one 14-ounce can tomato puree | 1 |
| one 14-ounce can tomato puree or tomato sauce | 1 |
| one 14-ounce can tomato sauce | 8 |
| one 14-ounce can tomatoes with green chilies (recommended: ro-tel) | 1 |
| one 14-ounce can tomatoes, seeded and chopped, liquid drained | 1 |
| one 14-ounce can whole peeled plum tomatoes, crushed by hand | 1 |
| one 14-ounce can whole plum tomato | 1 |
| one 14-ounce can whole tomato | 2 |
| one 14-ounce can whole tomatoes, crushed through your fingers or coarsely chopped | 1 |
| one 14.5-ounce can crushed fire-roasted tomato | 1 |
| one 14.5-ounce can crushed tomato | 2 |
| one 14.5-ounce can crushed tomatoes in thick puree | 1 |
| one 14.5-ounce can diced fire-roasted tomato | 1 |
| one 14.5-ounce can diced tomato | 8 |
| one 14.5-ounce can diced tomatoes in their juices | 1 |
| one 14.5-ounce can diced tomatoes with basil, garlic and oregano | 1 |
| one 14.5-ounce can diced tomatoes with juice | 1 |
| one 14.5-ounce can diced tomatoes with liquid | 1 |
| one 14.5-ounce can diced tomatoes, drained | 1 |
| one 14.5-ounce can diced tomatoes, drained and juice reserved | 2 |
| one 14.5-ounce can diced tomatoes, drained well | 1 |
| one 14.5-ounce can diced tomatoes, undrained | 1 |
| one 14.5-ounce can diced tomatoes, with juice | 2 |
| one 14.5-ounce can fire-roasted diced tomato | 3 |
| one 14.5-ounce can fire-roasted diced tomatoes, such as glen muir | 1 |
| one 14.5-ounce can fire-roasted diced tomatoes, such as muir glen | 1 |
| one 14.5-ounce can fire-roasted tomato | 2 |
| one 14.5-ounce can no-salt-added diced tomatoes, drained | 1 |
| one 14.5-ounce can no-salt-added fire-roasted diced tomato | 1 |
| one 14.5-ounce can peeled plum tomato | 1 |
| one 14.5-ounce can petite diced tomato | 1 |
| one 14.5-ounce can stewed tomato | 2 |
| one 14.5-ounce can tomato sauce, such as pomi | 1 |
| one 14.5-ounce can whole fire-roasted tomatoes, crushed by hand | 1 |
| one 14.5-ounce can whole peeled (pelati) tomato | 1 |
| one 14.5-ounce can whole peeled plum tomatoes, drained and roughly chopped | 1 |
| one 14.5-ounce can whole peeled tomatoes with their juices | 1 |
| one 14.5-ounce can whole peeled tomatoes, crushed well | 1 |
| one 14.5-ounce can whole plum tomato | 1 |
| one 14.5-ounce can whole tomato | 1 |
| one 14.5-ouncecan crushed tomato | 1 |
| one 14.75-ounce can crushed tomato | 1 |
| one 15- oz. can tomato sauce, preferably no salt added | 1 |
| one 15-ounce can chopped tomato | 1 |
| one 15-ounce can crushed fire-roasted tomato | 1 |
| one 15-ounce can crushed tomato | 9 |
| one 15-ounce can crushed tomatoes (preferably low-sodium) | 1 |
| one 15-ounce can diced fire roasted or chunky-style crushed tomato | 1 |
| one 15-ounce can diced fire-roasted tomato | 3 |
| one 15-ounce can diced fire-roasted tomatoes or diced tomatoes with green chilies | 1 |
| one 15-ounce can diced tomato | 11 |
| one 15-ounce can diced tomatoes in juice | 2 |
| one 15-ounce can diced tomatoes in juice, drained | 1 |
| one 15-ounce can diced tomatoes or tomatoes with green chiles | 1 |
| one 15-ounce can diced tomatoes with basil and oregano | 2 |
| one 15-ounce can diced tomatoes with their juice | 1 |
| one 15-ounce can diced tomatoes, drained | 1 |
| one 15-ounce can fire roasted diced tomato | 1 |
| one 15-ounce can fire roasted tomato | 1 |
| one 15-ounce can fire roasted tomatoes (with their juices) | 1 |
| one 15-ounce can fire-roasted diced tomato | 1 |
| one 15-ounce can fire-roasted tomato | 1 |
| one 15-ounce can low-sodium tomato sauce | 1 |
| one 15-ounce can no-salt-added diced tomato | 1 |
| one 15-ounce can no-salt-added tomato sauce | 1 |
| one 15-ounce can of tomato | 1 |
| one 15-ounce can plum tomatoes, crushed by hand | 1 |
| one 15-ounce can plum tomatoes, drained | 1 |
| one 15-ounce can stewed tomato | 1 |
| one 15-ounce can tomato paste | 1 |
| one 15-ounce can tomato puree | 3 |
| one 15-ounce can tomato sauce | 16 |
| one 15-ounce can tomato sauce (plain, not marinara) | 1 |
| one 15-ounce can tomato sauce or tomato puree | 1 |
| one 15-ounce can whole peeled tomatoes in juice | 1 |
| one 15-ounce can whole peeled tomatoes, undrained | 1 |
| one 15-ounce can whole plum tomatoes, crushed by hand | 2 |
| one 15.5-ounce can whole peeled tomatoes, drained | 1 |
| one 16-ounce can crushed tomato | 7 |
| one 16-ounce can diced fire-roasted tomato | 1 |
| one 16-ounce can diced tomato | 1 |
| one 16-ounce can diced tomatoes with chiles or spicy peppers, drained | 1 |
| one 16-ounce can diced tomatoes, drained | 1 |
| one 16-ounce can san marzano diced tomato | 1 |
| one 16-ounce can san marzano tomato | 2 |
| one 16-ounce can san marzano tomato sauce | 1 |
| one 16-ounce can seasoned tomato sauce | 1 |
| one 16-ounce can tomato paste | 2 |
| one 16-ounce can tomato puree | 1 |
| one 16-ounce can tomato sauce | 2 |
| one 16-ounce can whole peeled tomatoes, crushed by hand, with the juices | 1 |
| one 16-ounce can whole roma tomato | 1 |
| one 16-ounce can whole tomato | 2 |
| one 16-ounce can whole tomatoes, drained and pureed | 1 |
| one 16-ounce jar medium-spicy tomato salsa | 3 |
| one 19-ounce can diced tomato | 1 |
| one 20-ounce can tomato juice | 1 |
| one 24-ounce can crushed tomato | 1 |
| one 24-ounce can diced tomatoes, with juice | 1 |
| one 24-ounce can peeled crushed/ground tomatoes (recommended: kitchen ready) | 1 |
| one 24-ounce can tomato sauce | 1 |
| one 24-ounce jar crushed tomato | 1 |
| one 24-ounce jar of your favorite tomato or marinara sauce | 1 |
| one 26-ounce can or box diced tomatoes, such as pomi | 1 |
| one 26-ounce jar arrabiata or tomato-basil sauce | 1 |
| one 26-ounce jar marinara or tomato-basil sauce | 1 |
| one 26-ounce jar tomato-basil sauce (3 1/4 cups) | 1 |
| one 26-ounce jar tomato-basil sauce, such as giada de laurentiis for target tomato-basil sauce | 1 |
| one 26.42-ounce container chopped tomatoes, such as pomi | 1 |
| one 26.45-ounce box strained tomatoes, such as pomi | 1 |
| one 28 to 32-ounce can italian san marzano tomatoes, crushed | 1 |
| one 28- to 32-ounce can d.o.p. san marzano tomato | 1 |
| one 28- to 32-ounce can fire roasted tomato | 1 |
| one 28- to 32-ounce can fire roasted tomatoes or diced tomato | 1 |
| one 28- to 32-ounce can good-quality whole peeled tomatoes, drained | 1 |
| one 28- to 32-ounce can plum tomato | 1 |
| one 28- to 32-ounce can san marzano plum tomato | 1 |
| one 28- to 32-ounce can san marzano tomato | 4 |
| one 28- to 32-ounce can stewed tomatoes or italian san marzano tomato | 1 |
| one 28-ounce can chopped san marzano tomato | 2 |
| one 28-ounce can chopped tomato | 5 |
| one 28-ounce can chopped tomatoes in juice | 1 |
| one 28-ounce can concentrated crushed tomato | 1 |
| one 28-ounce can crushed fire-roasted tomato | 2 |
| one 28-ounce can crushed fire-roasted tomatoes, with their juice | 1 |
| one 28-ounce can crushed or pureed tomato | 1 |
| one 28-ounce can crushed or puréed tomato | 1 |
| one 28-ounce can crushed plum tomatoes with juice | 1 |
| one 28-ounce can crushed san marzano tomato | 2 |
| one 28-ounce can crushed to tomato | 1 |
| one 28-ounce can crushed tomato | 35 |
| one 28-ounce can crushed tomatoes (preferably no-salt-added) | 1 |
| one 28-ounce can crushed tomatoes in tomato puree | 1 |
| one 28-ounce can crushed tomatoes, (recommended: san marzano) | 1 |
| one 28-ounce can crushed tomatoes, preferably san marzano | 1 |
| one 28-ounce can crushed tomatoes, with their liquid | 1 |
| one 28-ounce can diced fire-roasted tomato | 3 |
| one 28-ounce can diced tomato | 19 |
| one 28-ounce can diced tomatoes in juice | 1 |
| one 28-ounce can diced tomatoes with their juice | 1 |
| one 28-ounce can diced tomatoes with their liquid | 1 |
| one 28-ounce can diced tomatoes, drained | 2 |
| one 28-ounce can diced tomatoes, such as glen muir fire roasted | 1 |
| one 28-ounce can diced tomatoes, with juice | 1 |
| one 28-ounce can fire roasted diced tomato | 2 |
| one 28-ounce can fire roasted tomatoes, such as glen muir | 1 |
| one 28-ounce can fire-roasted dice tomato | 1 |
| one 28-ounce can fire-roasted diced tomato | 2 |
| one 28-ounce can fire-roasted diced tomatoes, such as muir glen | 1 |
| one 28-ounce can italian plum tomatoes in their juice (do not drain) | 1 |
| one 28-ounce can italian plum tomatoes, crushed or pureed | 1 |
| one 28-ounce can low-sodium whole tomato | 1 |
| one 28-ounce can no-salt whole tomatoes, crushed well by hand | 1 |
| one 28-ounce can no-salt-added crushed tomato | 2 |
| one 28-ounce can no-salt-added tomato puree | 1 |
| one 28-ounce can no-salt-added whole plum tomato | 1 |
| one 28-ounce can no-salt-added whole plum tomatoes (pureed) | 1 |
| one 28-ounce can no-salt-added whole plum tomatoes, crushed by hand | 1 |
| one 28-ounce can peeled whole tomato | 2 |
| one 28-ounce can peeled whole tomatoes, drained and chopped | 1 |
| one 28-ounce can plain tomato sauce | 1 |
| one 28-ounce can plum tomato | 3 |
| one 28-ounce can plum tomatoes and their juice, processed until smooth | 1 |
| one 28-ounce can plum tomatoes packed in puree, crushed | 1 |
| one 28-ounce can plum tomatoes, coarsely crushed | 1 |
| one 28-ounce can plum tomatoes, crushed by hand | 1 |
| one 28-ounce can plum tomatoes, drained of the can juices | 1 |
| one 28-ounce can plum tomatoes, preferably san marzano | 1 |
| one 28-ounce can plum tomatoes, with juices, pureed | 1 |
| one 28-ounce can plus one 14-ounce can diced fire roasted tomatoes, such as glen muir | 1 |
| one 28-ounce can pureed tomato | 1 |
| one 28-ounce can san marzano diced tomatoes with juices | 1 |
| one 28-ounce can san marzano plum tomatoes, crushed by hand | 1 |
| one 28-ounce can san marzano tomato | 1 |
| one 28-ounce can san marzano tomatoes, crushed | 1 |
| one 28-ounce can san marzano tomatoes, crushed by hand | 1 |
| one 28-ounce can san marzano tomatoes, pureed | 1 |
| one 28-ounce can san marzano whole peeled tomato | 1 |
| one 28-ounce can stewed tomato | 1 |
| one 28-ounce can tomato puree | 6 |
| one 28-ounce can tomato sauce | 3 |
| one 28-ounce can tomato sauce puree | 1 |
| one 28-ounce can whole fire-roasted tomato | 1 |
| one 28-ounce can whole fire-roasted tomatoes, with their juices | 2 |
| one 28-ounce can whole or diced tomato | 1 |
| one 28-ounce can whole or diced tomatoes (with their juice) | 1 |
| one 28-ounce can whole or diced tomatoes, with juice | 1 |
| one 28-ounce can whole peeled (pelati) tomatoes, blended | 2 |
| one 28-ounce can whole peeled plum tomatoes, crushed by hand | 1 |
| one 28-ounce can whole peeled tomato | 5 |
| one 28-ounce can whole peeled tomatoes in juice | 1 |
| one 28-ounce can whole peeled tomatoes in sauce | 1 |
| one 28-ounce can whole peeled tomatoes in tomato juice | 1 |
| one 28-ounce can whole peeled tomatoes with juice | 1 |
| one 28-ounce can whole peeled tomatoes, blended in a food processor | 1 |
| one 28-ounce can whole peeled tomatoes, crushed by hand | 4 |
| one 28-ounce can whole peeled tomatoes, crushed by hand, with juices | 2 |
| one 28-ounce can whole peeled tomatoes, drained and chopped | 1 |
| one 28-ounce can whole peeled tomatoes, hand crushed or coarsely chopped, juice reserved | 1 |
| one 28-ounce can whole peeled tomatoes, lightly crushed | 1 |
| one 28-ounce can whole peeled tomatoes, preferably san marzano, drained | 1 |
| one 28-ounce can whole peeled tomatoes, tomatoes crushed by hand | 1 |
| one 28-ounce can whole plum tomato | 2 |
| one 28-ounce can whole plum tomatoes, crushed by hand | 4 |
| one 28-ounce can whole plum tomatoes, drained | 1 |
| one 28-ounce can whole plum tomatoes, lightly crushed | 1 |
| one 28-ounce can whole san marzano tomato | 3 |
| one 28-ounce can whole san marzano tomatoes, crushed by hand, reserve the can | 1 |
| one 28-ounce can whole san marzano tomatoes, drained and roughly chopped | 1 |
| one 28-ounce can whole tomato | 3 |
| one 28-ounce can whole tomatoes (preferably san marzano), drained, juice reserved | 1 |
| one 28-ounce can whole tomatoes in juice, pureed in a blender | 2 |
| one 28-ounce can whole tomatoes packed in juice, drained, and chopped | 1 |
| one 28-ounce can whole tomatoes with juice | 2 |
| one 28-ounce can whole tomatoes, crushed (or 2 pounds fresh tomato | 1 |
| one 28-ounce can whole tomatoes, crushed well by hand | 1 |
| one 28-ounce can whole tomatoes, drained with seeds removed | 1 |
| one 28-ounce can whole tomatoes, drained, reserving the juice (recommended: san marzano) | 1 |
| one 28-ounce crushed tomatoes, plus one 10-ounce can | 1 |
| one 28-ounce jar crushed red tomatoes, canned at the peak of the season, or store-bought canned crushed tomato | 2 |
| one 28-ounce jar tomato-basil sauce, such as giada delaurentiis for target | 1 |
| one 28-oz. can whole peeled tomato | 1 |
| one 28-to-32 ounce can whole san marzano tomatoes (look for the dop label) | 1 |
| one 28-to-32-ounce can crushed italian tomato | 1 |
| one 28-to-32-ounce can diced tomatoes or whole san marzano tomato | 1 |
| one 28-to-32-ounce can whole peeled san marzano tomato | 1 |
| one 29-ounce can tomato puree | 1 |
| one 3-ounce package frieda's dried tomatoes, reconstituted according to package directions | 1 |
| one 3-pound can whole tomatoes, drained, puree reserved | 1 |
| one 32-ounce can chopped tomato | 1 |
| one 32-ounce can chunky style crushed tomato | 1 |
| one 32-ounce can crushed san marzano tomato | 1 |
| one 32-ounce can crushed seasoned tomato | 1 |
| one 32-ounce can crushed tomato | 2 |
| one 32-ounce can fire roasted crushed or diced tomato | 1 |
| one 32-ounce can fire roasted tomato | 1 |
| one 32-ounce can fire roasted tomatoes of any variety (whole | 1 |
| one 32-ounce can italian crushed tomato | 1 |
| one 32-ounce can pureed tomato | 1 |
| one 32-ounce can san marzano tomato | 4 |
| one 32-ounce can san marzano tomatoes, drained and processed in a food mill or food processor | 1 |
| one 32-ounce can stewed tomato | 2 |
| one 32-ounce can tomato puree | 1 |
| one 32-ounce can whole d.o.p. san marzano tomato | 1 |
| one 32-ounce can whole peeled tomato | 1 |
| one 32-ounce can whole san marzano tomato | 1 |
| one 35-ounce can italian plum tomatoes (preferably san marzano) with their liquid | 1 |
| one 35-ounce can whole peeled tomato | 1 |
| one 35-ounce can whole tomatoes, such as san marnano tomato's | 1 |
| one 4-ounce can tomato paste | 2 |
| one 46-ounce bottle or can tomato juice | 1 |
| one 46-ounce can crushed tomatoes, such as 7/11 ground tomato | 1 |
| one 5-ounce bottle pickapeppa sauce (this contains: mangos, raisins, tamarinds, salt and pepper, tomatoes) | 1 |
| one 6-ounce can tomato juice | 1 |
| one 6-ounce can tomato paste | 32 |
| one 6-ounce can tomato puree | 1 |
| one 6.5-ounce jar oil-packed sun-dried tomatoes, drained and coarsely chopped | 1 |
| one 7-ounce jar sun-dried tomatoes, drained and coarsely chopped | 1 |
| one 8-ounce can diced tomato | 1 |
| one 8-ounce can diced tomatoes, with juice | 1 |
| one 8-ounce can peeled italian tomatoes (or 1 pint vine-ripe cherry tomatoes) | 1 |
| one 8-ounce can tomato paste | 2 |
| one 8-ounce can tomato sauce | 12 |
| one 8-ounce can tomato sauce or 1 cup passata or tomato puree | 1 |
| one 8-ounce can tomato sauce or 8 ounces crushed tomato | 1 |
| one 8-ounce jar sun-dried tomatoes packed in oil, drained and chopped, oil reserved | 1 |
| one 8-ounce jar tomato sauce | 1 |
| one 96-ounce can (or, if you can find it, 1-kg) or four 28-ounce cans italian tomato | 1 |
| one and a half 24-ounce jars passata di pomodoro (tomato puree) | 1 |
| one and one-half 14.5-ounce cans whole tomato | 1 |
| onion powder, plus more for seasoning tomato | 1 |
| onion, tomato, and cucumber slices, for garnish | 1 |
| optional additions: 1/2 to 1 cup grated seeded cucumbers, or seeded diced tomatoes or 1/4 cup puree of roasted red pepper | 1 |
| optional ingredients: homemade tomato sauce, bell peppers, mushrooms, or your favorite cheese | 1 |
| optional tomato ingredients such as 1 1/2 cups or more of crushed tomatoes, tomato puree or 1/4 cup tomato paste | 1 |
| optional toppings: lettuce, onion, tomato, salsa, cheese, avocado | 1 |
| or 1 cup hunt's® tomato sauce | 1 |
| or 3 (15-ounce) cans tomato sauce | 1 |
| or 3 cans chopped plum tomatoes (32 to 48 ounces total) | 2 |
| or 3 medium tomatoes, cut into 1/3-inch-thick slices | 1 |
| or 3 ripe tomatoes, core end discarded | 1 |
| or 3 slices tomato | 1 |
| or 3 small tomatoes (about 2 1/4-inches diameter) | 1 |
| or 3 tablespoons sun dried tomato | 1 |
| or 4 cherry tomato | 1 |
| or 4 large firm green tomato | 1 |
| or 4 large tomatoes, halved | 1 |
| or 4 small to medium heirloom tomatoes, in assorted colors, cored and cut into 3/4-inch chunks | 1 |
| or 6 roma or plum tomatoes, seeded and diced | 1 |
| or 6 vine-ripened tomato | 1 |
| or 8 cherry tomato | 1 |
| or 9 fresh plum tomatoes, skinned, seeded and coarsely chopped to measure 1 1/2 (packed) cups | 1 |
| or jar ( 15 ounces, or 420 g) tomato sauce | 1 |
| or more drained and seeded canned italian plum tomatoes, if needed | 1 |
| orange and yellow vine-ripened tomatoes, cut into 1/3-inch cubes | 1 |
| orange baby tomatoes, halved | 2 |
| orange or yellow tomato | 1 |
| orange tomato | 1 |
| orange tomato sauce, recipe follows | 1 |
| orange tomato, cubed | 1 |
| organic canned diced tomato | 2 |
| organic canned tomatoes, hand-crushed (recommended: san marzano) | 1 |
| organic cherry tomato | 1 |
| organic diced tomatoes with basil and garlic, drained, muir glen® | 1 |
| organic grape tomatoes, halved | 1 |
| orzo with feta, tomatoes, and dill | 1 |
| oven dried cherry tomatoes, recipe follows | 1 |
| oven dried tomatoes, recipe follows | 3 |
| oven roasted plum tomato | 1 |
| oven roasted tomato | 3 |
| oven roasted tomatoes (plum tomatoes, cut in half and baked in 200 degree oven with olive oil, salt, and pepper for about 6 hours) | 1 |
| oven-dried tomato | 3 |
| oven-dried tomato chopped | 1 |
| oven-dried tomatoes , drained | 1 |
| oven-dried tomatoes, drained, recipe follows | 4 |
| oven-dried tomatoes, recipe follows | 2 |
| oven-dried tomatoes, recipe follows, cut into thin slices | 1 |
| oven-roasted tomato | 2 |
| overripe medium tomato | 1 |
| pack sun-dried tomato pesto sauce mix | 1 |
| package al fresco® all natural sun dried tomato with basil chicken sausage | 1 |
| package al fresco® sun dried tomato chicken sausage | 1 |
| package creamy tomato sauce mix (recommended: knorr) | 1 |
| package crumbled feta cheese with basil and sun-dried tomato | 2 |
| package crumbled tomato and basil feta cheese (such as athenos®) | 1 |
| package dole® extra veggie™ with grape tomato | 1 |
| package grape or cherry tomatoes, each halved | 1 |
| package pre-cooked sun-dried tomato and garlic polenta, drained and cut into 1/2-inch rounds | 1 |
| package sweet cocktail tomato | 1 |
| package sweet cocktail tomatoes, cut into quarters | 1 |
| package tomato basil feta cheese | 1 |
| package tomato basil feta cheese, crumbled | 2 |
| package tomato lentil couscous mix | 1 |
| packed soft dried tomatoes (not packed in oil; 1 1/4 oz) | 1 |
| packed sun-dried tomatoes, fully rehydrated | 1 |
| packet dry tomato soup mix | 1 |
| packet salsa tomato mix (such as mrs. wages®) | 1 |
| pancetta tomato sauce, recipe follows, for serving | 1 |
| parts tomato juice (i recommend using low-sodium) | 2 |
| passata (italian tomato puree in glass jars) or canned tomato puree | 1 |
| passata or pureed, strained tomato | 1 |
| passata or tomato puree | 2 |
| passata or tomato puree or tomato sauce | 1 |
| passata or tomato sauce | 10 |
| pasta sauce (such as classico fire-roasted tomato & garlic sauce), heated | 1 |
| pear or cherry tomato | 2 |
| pear or cherry tomatoes (preferably small) | 1 |
| pear tomato | 2 |
| peeled and chopped fresh tomato | 1 |
| peeled and chopped tomato | 2 |
| peeled and chopped tomatoes (fresh or canned) | 1 |
| peeled and crushed plum tomato | 1 |
| peeled and crushed tomato | 1 |
| peeled and diced heirloom tomato | 1 |
| peeled and diced roma tomato | 1 |
| peeled and diced tomato | 1 |
| peeled and diced tomatoes with juice | 1 |
| peeled and diced tomatoes, about 3 to 5 roma tomato | 1 |
| peeled and quartered tomato | 1 |
| peeled and seeded chopped tomato (if using fresh; will need 3/4 pound) | 1 |
| peeled and seeded tomato | 1 |
| peeled canned low-sodium tomato | 1 |
| peeled canned tomato | 2 |
| peeled chopped tomato | 2 |
| peeled fresh heirloom tomato | 1 |
| peeled italian plum tomato | 1 |
| peeled plum tomato | 3 |
| peeled plum tomatoes, crushed, from a can | 1 |
| peeled plum tomatoes, including the liquid | 1 |
| peeled plum tomatoes, thoroughly crushed | 1 |
| peeled san marzano tomato | 1 |
| peeled seeded and diced tomato | 1 |
| peeled tomato | 1 |
| peeled tomato chunks | 1 |
| peeled whole canned tomatoes (preferably san marzano) | 1 |
| peeled whole tomatoes (can use 16 ounces canned tomatoes) | 1 |
| peeled whole tomatoes in juice, cut into 1/2-inch dice | 1 |
| peeled, crushed, and seeded plum tomato | 1 |
| peeled, seed, and chopped fresh tomatoes or chopped canned italian tomatoes with their juice | 1 |
| peeled, seeded and chopped fresh or canned tomato | 1 |
| peeled, seeded and chopped plum tomato | 1 |
| peeled, seeded and chopped tomato | 4 |
| peeled, seeded and diced fresh tomato, canned or fresh | 1 |
| peeled, seeded and diced plum tomato | 1 |
| peeled, seeded and diced ripe tomato | 1 |
| peeled, seeded and finely diced roma tomato | 1 |
| peeled, seeded and julienned fresh tomato | 1 |
| peeled, seeded and medium-diced tomato | 1 |
| peeled, seeded ripe tomato | 1 |
| peeled, seeded, and chopped fresh tomato | 2 |
| peeled, seeded, and chopped tomato | 12 |
| peeled, seeded, and chopped tomato or 1 1/2 cups drained canned plum tomato | 2 |
| peeled, seeded, and chopped tomato or 28-ounce can tomatoes, drained and chopped | 1 |
| peeled, seeded, and chopped vine-ripened tomato | 1 |
| peeled, seeded, and chopped vine-ripened tomato or chopped canned plum tomato | 1 |
| peeled, seeded, and chopped vine-ripened tomatoes, about 1/2 pounds | 1 |
| peeled, seeded, and coarsely chopped fresh ripe tomatoes (4 to 5 pounds) or 4 cups canned whole plum tomatoes with their juice (two 28-ounce cans) | 1 |
| peeled, seeded, and coarsely chopped tomato | 1 |
| peeled, seeded, and cored tomatoes with juice | 1 |
| peeled, seeded, and diced red tomato | 1 |
| peeled, seeded, and diced roma tomato | 2 |
| peeled, seeded, and diced tomato | 6 |
| peeled, seeded, and finely diced tomato | 1 |
| peeled, seeded, and roughly chopped plum tomato | 1 |
| peeled, seeded, and small diced tomato | 1 |
| peeled, seeded, crushed tomato | 1 |
| peeled, whole tomatoes, undrained | 1 |
| pendula tomatoes or 2 1/2 cups fresh tomato sauce | 1 |
| perfectly ripe yellow (or red) medium-size beefsteak tomato | 1 |
| pesto, sun dried tomato or black olive paste to taste | 1 |
| petite diced tomato | 1 |
| petite diced tomatoes or stewed tomato | 1 |
| petite-cut diced tomatoes with sweet onions, drained and juice reserved | 1 |
| petite-diced tomatoes, hunt's | 1 |
| picante tomato sauce, recipe follows | 1 |
| pickled green tomato | 2 |
| pickled tomato salad, recipe follows | 1 |
| pickled tomato salsa, recipe follows, for serving | 1 |
| piece heirloom tomato | 1 |
| pieces campari tomato on the vine (about 2 times the size of cherry tomatoes) | 1 |
| pieces sliced tomato | 1 |
| pieces sun-dried tomato | 2 |
| pieces sun-dried tomato (packed in oil), thinly sliced (about 1 tablespoon) | 1 |
| pieces sun-dried tomato packed in oil, drained and finely chopped | 1 |
| pieces sun-dried tomato, soaked 15 minutes in 1/2 cup warm water, then chopped, reserve liquid | 1 |
| pieces sun-dried tomatoes (not oil-packed) | 1 |
| pieces thinly sliced tomato | 2 |
| pieces tomato confit, recipe follows | 1 |
| pimientos, tomato, red onion and/or lettuce, for topping | 1 |
| pineapple tomato salsa, recipe follows | 1 |
| pint (1 cup) cherry tomato | 1 |
| pint (1 cup) cherry tomatoes, halved | 1 |
| pint (10 ounces) grape tomato | 1 |
| pint (16 ounces) cherry tomatoes, halved | 1 |
| pint (2 cups) cherry tomatoes, halved | 2 |
| pint (2 cups) grape or cherry tomato | 1 |
| pint (2 cups) ripe cherry or grape tomatoes, quartered | 1 |
| pint assorted cherry tomatoes, cut in half | 1 |
| pint baby tomatoes, halved | 1 |
| pint baby tomatoes, washed and quartered | 1 |
| pint basket cherry tomatoes, halved | 1 |
| pint basket of small tomatoes: cherry, red or golden currant tomatoes, yellow pear | 1 |
| pint cherry (sweet 100's or heirloom) tomatoes, washed, dried and stemmed | 1 |
| pint cherry heirloom tomatoes, halved | 1 |
| pint cherry or campari tomatoes, halved | 1 |
| pint cherry or grape tomato | 5 |
| pint cherry or grape tomatoes (12 ounces) | 1 |
| pint cherry or grape tomatoes, cut in 1/2 | 1 |
| pint cherry or grape tomatoes, halved | 8 |
| pint cherry tomato | 77 |
| pint cherry tomato, quarters | 2 |
| pint cherry tomatoes (12 to 14 ounces) | 1 |
| pint cherry tomatoes (about 2 cups, or 12 ounces), halved | 1 |
| pint cherry tomatoes (about 30) | 2 |
| pint cherry tomatoes (preferably assorted colors), halved | 1 |
| pint cherry tomatoes cut in half | 1 |
| pint cherry tomatoes on the vine | 1 |
| pint cherry tomatoes, assorted colors | 1 |
| pint cherry tomatoes, cleaned | 1 |
| pint cherry tomatoes, cored | 1 |
| pint cherry tomatoes, cut in 1/2 | 1 |
| pint cherry tomatoes, cut in half | 3 |
| pint cherry tomatoes, cut in half or quarters | 1 |
| pint cherry tomatoes, cut in half or quarters if large | 1 |
| pint cherry tomatoes, cut into quarters | 2 |
| pint cherry tomatoes, halved | 79 |
| pint cherry tomatoes, halved (quartered if very large) | 1 |
| pint cherry tomatoes, halved and seeded | 2 |
| pint cherry tomatoes, halved crosswise | 1 |
| pint cherry tomatoes, halved or 1 (28-ounce) can whole | 1 |
| pint cherry tomatoes, halved or quartered if large | 1 |
| pint cherry tomatoes, halved, yellow if possible | 1 |
| pint cherry tomatoes, quarter | 1 |
| pint cherry tomatoes, quartered | 17 |
| pint cherry tomatoes, rinsed, stemmed, and halved | 1 |
| pint cherry tomatoes, some halved, some whole | 1 |
| pint cherry tomatoes, stemmed | 3 |
| pint cherry tomatoes, trimmed | 1 |
| pint cherry tomatoes, washed | 1 |
| pint cherry tomatoes, washed and tops removed | 1 |
| pint cherry tomatoes, washed, cut through the center in two | 1 |
| pint cherry tomatoes, whole | 1 |
| pint currant tomato | 1 |
| pint each red and yellow cherry tomato | 1 |
| pint fresh red cherry tomato | 1 |
| pint grape or cherry tomato | 5 |
| pint grape or cherry tomatoes (10 ounces), quartered | 1 |
| pint grape or cherry tomatoes (multi-color if available), halved | 1 |
| pint grape or cherry tomatoes, cut in 1/2 | 1 |
| pint grape or cherry tomatoes, halved | 9 |
| pint grape or cherry tomatoes, halved or quartered | 1 |
| pint grape or cherry tomatoes, heirloom multi colored, red or yellow, halved | 1 |
| pint grape or pear tomato | 1 |
| pint grape tomato | 38 |
| pint grape tomatoes (24 to 30) | 1 |
| pint grape tomatoes (about 2 1/2 cups) | 1 |
| pint grape tomatoes (about 20) | 2 |
| pint grape tomatoes or 4 roma tomatoes, halved | 1 |
| pint grape tomatoes or baby heirloom tomatoes, halved (about 1 cup) | 1 |
| pint grape tomatoes or baby heirlooms | 1 |
| pint grape tomatoes, cored | 1 |
| pint grape tomatoes, cut a few in 1/2 and leave a bunch whole | 1 |
| pint grape tomatoes, cut in half | 1 |
| pint grape tomatoes, cut into thirds | 1 |
| pint grape tomatoes, halved | 55 |
| pint grape tomatoes, halved (1 3/4 cups) | 1 |
| pint grape tomatoes, halved lengthwise | 1 |
| pint grape tomatoes, halved or cherry tomatoes, quartered | 1 |
| pint grape tomatoes, left whole, or cherry tomatoes, halved | 1 |
| pint grape tomatoes, or sweet 100 tomatoes or pear tomato | 1 |
| pint grape tomatoes, quartered | 9 |
| pint grape tomatoes, rinsed | 1 |
| pint grape tomatoes, thinly sliced | 1 |
| pint grape tomatoes, washed and dried | 1 |
| pint grape tomatoes, washed and sliced in 1/2 | 1 |
| pint halved grape tomato | 1 |
| pint heirloom cherry tomatoes, assorted sizes and colors | 1 |
| pint heirloom cherry tomatoes, halved | 1 |
| pint heirloom cherry tomatoes, halved lengthwise | 1 |
| pint heirloom cherry tomatoes, multi colored if available, halved | 1 |
| pint home-canned or one 15-ounce can tomato | 1 |
| pint large cherry tomatoes (about 30) | 1 |
| pint mixed cherry tomato | 1 |
| pint mixed red and yellow cherry or pear tomato | 1 |
| pint mixed red and yellow currant tomatoes or small cherry tomato | 1 |
| pint mixed tiny heirloom tomatoes, such as cherry, cherub, grape, or pear, of different colors and sizes | 1 |
| pint multi colored, red or yellow cherry tomato | 1 |
| pint multi colored, yellow or red heirloom cherry tomato | 1 |
| pint multi-color, yellow or red cherry heirloom tomatoes or 2 medium vine-ripe tomatoes, cut into bite-size pieces | 1 |
| pint multi-colored baby heirloom tomatoes, or grape tomatoes, halved | 1 |
| pint multi-colored baby or grape tomatoes or red grape tomato | 1 |
| pint multicolored cherry tomato | 1 |
| pint of cherry tomato | 1 |
| pint of grape tomatoes, halved | 1 |
| pint of pear tomato | 1 |
| pint organic cherry tomato | 1 |
| pint pear or cherry tomatoes, halved | 1 |
| pint pear tomatoes, halved | 1 |
| pint plain tomato sauce | 1 |
| pint red and yellow cherry tomatoes, washed and cut into half | 1 |
| pint red and/or yellow cherry tomatoes, stemmed and halved or quartered | 1 |
| pint red cherry tomato | 1 |
| pint red cherry tomatoes (as small as possible) | 1 |
| pint red cherry tomatoes, halved or quartered | 1 |
| pint red grape or cherry tomatoes, halved (preferably an heirloom variety such as tommy toe) | 1 |
| pint red grape or pear tomato | 1 |
| pint red grape tomato | 1 |
| pint red grape tomatoes or cherry tomatoes, cut in half | 1 |
| pint red grape tomatoes, halved | 1 |
| pint red grape tomatoes, halved lengthwise | 3 |
| pint red or yellow cherry tomato | 1 |
| pint red or yellow cherry tomatoes or a combination, quartered | 1 |
| pint red pear tomatoes, halved | 1 |
| pint ripe cherry tomatoes, halved | 1 |
| pint ripe cherry tomatoes, quartered | 1 |
| pint slow cooked tomato sauce (recommended: freshdirect) | 1 |
| pint small cherry or grape tomato | 1 |
| pint small cherry tomato | 1 |
| pint small cherry tomatoes, halved | 2 |
| pint small cherry tomatoes, stems removed, crushed between your thumb and forefinger | 1 |
| pint small heirloom tomatoes, halved | 1 |
| pint small vine-ripened red cherry tomatoes, larger tomatoes halved | 2 |
| pint small, ripe cherry tomatoes, tossed in a bowl with a little oil | 1 |
| pint sun gold tomato | 1 |
| pint sweet 100 tomato | 1 |
| pint sweet 100 tomatoes or cherry tomatoes, halved | 1 |
| pint sweet grape tomato | 1 |
| pint tear-drop tomatoes, cut in 1/2 | 1 |
| pint teardrop or cherry tomatoes, halved | 1 |
| pint teardrop tomato | 1 |
| pint teardrop tomatoes, halved | 1 |
| pint tiny, ripe cherry tomatoes (preferably sweet 100s), each quartered | 1 |
| pint tiny, ripe tomatoes (preferably sweet 100s), each quartered | 1 |
| pint tomato juice, low sodium | 1 |
| pint tomato ketchup | 1 |
| pint tomatoes, grape, quartered | 1 |
| pint vine cherry tomato | 1 |
| pint vine-ripened cherry tomato | 2 |
| pint vine-ripened cherry tomatoes, halved | 3 |
| pint vine-ripened cherry tomatoes, quartered | 1 |
| pint vine-ripened red cherry tomatoes, washed and dried | 1 |
| pint vine-ripened yellow cherry tomato | 2 |
| pint whole cherry tomato | 1 |
| pint whole grape tomato | 2 |
| pint yellow and red cherry tomatoes, quartered | 1 |
| pint yellow cherry or grape tomato | 1 |
| pint yellow cherry tomato | 2 |
| pint yellow cherry tomatoes (as small as possible) | 1 |
| pint yellow cherry tomatoes, halved | 1 |
| pint yellow grape or pear tomato | 1 |
| pint yellow grape tomato | 1 |
| pint yellow grape tomatoes, halved | 2 |
| pint yellow grape tomatoes, halved lengthwise | 3 |
| pint yellow or red grape tomato | 1 |
| pint yellow pear tomatoes or cherry tomatoes, cut in half | 1 |
| pint yellow pear tomatoes, halved | 2 |
| pint yellow tomatoes, halved or 2 vine ripe yellow tomatoes, seeded and chopped | 1 |
| pint/300 g cherry tomato | 1 |
| pintcherry tomatoes, quartered | 1 |
| pints (6 cups) cherry tomato | 1 |
| pints assorted baby tomatoes (pear tomatoes, cherry tomatoes) | 1 |
| pints assorted heirloom cherry tomato | 1 |
| pints cherry and/or grape tomatoes, halved | 1 |
| pints cherry or grape tomato | 1 |
| pints cherry or grape tomatoes, halved | 1 |
| pints cherry or grape tomatoes, halved or 7 to 8 small roma tomatoes, thinly sliced lengthwise | 1 |
| pints cherry tomato | 29 |
| pints cherry tomatoes (such as orange, red, and yellow teardrop varieties) | 1 |
| pints cherry tomatoes or grape tomato | 1 |
| pints cherry tomatoes or grape tomatoes, halved | 1 |
| pints cherry tomatoes or multi-colored baby heirloom tomatoes, halved or quartered | 1 |
| pints cherry tomatoes, halved | 11 |
| pints cherry tomatoes, halved (about 3 cups) | 1 |
| pints cherry tomatoes, halved if large | 1 |
| pints cherry tomatoes, halved or, if large, quartered | 1 |
| pints cherry tomatoes, large tomatoes halved and small tomatoes left whole | 1 |
| pints cherry tomatoes, mixed sizes and colors | 1 |
| pints cherry tomatoes, on the vine | 1 |
| pints cherry tomatoes, quartered | 3 |
| pints cherry tomatoes, quartered lengthwise | 1 |
| pints cherry tomatoes, rinsed and stems removed | 1 |
| pints cherry tomatoes, stemmed and halved | 1 |
| pints cherry tomatoes, tops cut off | 1 |
| pints cherry tomatoes,(yellow and red), stemmed | 1 |
| pints cherry tomatoes,halved | 1 |
| pints firm small mixed cherry and grape tomato | 1 |
| pints firm vine-ripened cherry tomato | 1 |
| pints grape or cherry tomato | 1 |
| pints grape or cherry tomatoes, halved | 1 |
| pints grape tomato | 10 |
| pints grape tomatoes (about 1 pound) | 1 |
| pints grape tomatoes or cherry tomato | 1 |
| pints grape tomatoes, halved | 5 |
| pints grape tomatoes, red or mixed colors | 1 |
| pints grape tomatoes, rinsed | 1 |
| pints mini japanese heirloom tomatoes, blanched and shocked, then peeled | 1 |
| pints red and yellow, grape and pear tomato | 1 |
| pints red cherry tomato | 2 |
| pints red or yellow pear tomatoes or cherry tomatoes or a combination, halved | 1 |
| pints ripe cherry tomato | 1 |
| pints ripe cherry tomatoes, halved | 1 |
| pints small cherry tomatoes or grape tomoatoes | 1 |
| pints small cherry tomatoes, halved | 1 |
| pints sun gold or other cherry tomato | 1 |
| pints sweet cherry tomato | 1 |
| pints sweet cherry tomatoes, blanched, shocked, and peeled | 1 |
| pints vine-ripened cherry tomato | 1 |
| pints vine-ripened red and yellow cherry tomatoes (about 2/3 pound) | 1 |
| pints vine-ripened small tomato | 1 |
| pints yellow cherry tomato | 2 |
| pints yellow cherry tomatoes, or red grape tomatoes, or both | 1 |
| piquillo peppers, drained, or 8 small plum tomatoes, hollowed out, or a combination of peppers and tomato | 1 |
| pizza sauce, or other tomato sauce | 1 |
| plain sun-dried tomato | 1 |
| plain tomato sauce | 3 |
| plain tomato sauce, purchased or homemade | 1 |
| plum (roma) tomato | 7 |
| plum (roma) tomato, seeded and diced | 1 |
| plum (roma) tomatoes (diced) | 1 |
| plum (roma) tomatoes (seeds removed and brunoise cut) | 1 |
| plum (roma) tomatoes, cut into thin wedges | 1 |
| plum (roma) tomatoes, halved | 2 |
| plum (roma) tomatoes, halved lengthwise | 1 |
| plum (roma) tomatoes, quartered | 1 |
| plum (roma) tomatoes, roasted | 1 |
| plum (roma) tomatoes, seeded | 1 |
| plum (roma) tomatoes, seeded and cubed | 1 |
| plum (roma) tomatoes, thinly sliced | 1 |
| plum or 2 large tomato | 1 |
| plum or 2 regular medium tomatoes, seeded | 1 |
| plum or beefsteak tomato | 1 |
| plum or heirloom tomato | 1 |
| plum or regular tomatoes, cut into 1/4-inch dice | 1 |
| plum or roma tomato | 1 |
| plum or roma tomatoes, halved | 1 |
| plum or vine tomatoes, seeded and diced | 1 |
| plum ripe tomato | 1 |
| plum roma tomatoes or small, vine ripe tomatoes, seeded and chopped | 1 |
| plum tomato | 386 |
| plum tomato (preferably roma) | 1 |
| plum tomato or 1 vine tomato, seeded and chopped or 3 tablespoons chopped sun-dried tomato -- your preference or, depending on what you have on hand | 1 |
| plum tomato or 1/2 of a large tomato | 1 |
| plum tomato slices | 2 |
| plum tomato, cored and quartered | 2 |
| plum tomato, cut into 1/2-inch pieces | 1 |
| plum tomato, cut into 1/4-inch slices | 1 |
| plum tomato, cut into quarters | 1 |
| plum tomato, halved | 1 |
| plum tomato, halved and seeded or 2 sun-dried tomatoes in oil, drained and patted dry | 1 |
| plum tomato, halved lengthwise | 2 |
| plum tomato, medium diced | 1 |
| plum tomato, quartered | 1 |
| plum tomato, roasted and peeled | 1 |
| plum tomato, seeded | 6 |
| plum tomato, seeded and chopped | 6 |
| plum tomato, seeded and chopped (about 1/3 cup) | 3 |
| plum tomato, seeded and chopped, for garnish | 1 |
| plum tomato, seeded and cut into 1/2-inch dice | 1 |
| plum tomato, seeded and diced | 4 |
| plum tomato, seeded and finely chopped | 5 |
| plum tomato, seeded and finely diced | 5 |
| plum tomato, seeded and minced | 1 |
| plum tomato, seeds removed | 1 |
| plum tomato, thinly sliced | 3 |
| plum tomato,seeded and chopped fine | 1 |
| plum tomatoes (1 1/4 lb) | 1 |
| plum tomatoes (1 lb), halved lengthwise | 1 |
| plum tomatoes (1 to 1 1/4 pounds), cored, halved, and diced | 1 |
| plum tomatoes (1/2 pound total), seeded and thinly sliced lengthwise | 1 |
| plum tomatoes (10 to 12), halved lengthwise | 1 |
| plum tomatoes (2 chopped and 2 thinly sliced crosswise) | 1 |
| plum tomatoes (2 or 3 medium) | 1 |
| plum tomatoes (2 pounds), halved lengthwise | 1 |
| plum tomatoes (3/4 pounds total) | 1 |
| plum tomatoes (4 to 6) | 1 |
| plum tomatoes (6 to 8 tomatoes) | 1 |
| plum tomatoes (8 large) | 1 |
| plum tomatoes (8 large), halved lengthwise | 1 |
| plum tomatoes (about 1 1/2 pounds) | 1 |
| plum tomatoes (about 1 1/4 pounds) | 3 |
| plum tomatoes (about 1 1/4 pounds), cut in half lengthwise | 1 |
| plum tomatoes (about 1 pound) | 1 |
| plum tomatoes (about 1 pound), halved lengthwise | 1 |
| plum tomatoes (about 1 pound), seeded and cut into 1-inch pieces | 1 |
| plum tomatoes (about 10 ounces), stemmed | 1 |
| plum tomatoes (about 10) | 1 |
| plum tomatoes (about 10), halved lengthwise | 1 |
| plum tomatoes (about 12 ounces total) | 1 |
| plum tomatoes (about 12 ounces) | 1 |
| plum tomatoes (about 12 ounces), cored and diced (2 1/2 cups) | 1 |
| plum tomatoes (about 18 ounces), seeded, cut into 1/4-inch pieces | 1 |
| plum tomatoes (about 2 pounds), halved and seeded | 1 |
| plum tomatoes (about 2/3 pounds), quartered lengthwise, then crosswise | 1 |
| plum tomatoes (about 3 medium) | 1 |
| plum tomatoes (about 3), seeded and chopped | 1 |
| plum tomatoes (about 4 large) | 1 |
| plum tomatoes (about 4) | 2 |
| plum tomatoes (about 4; see cooks' notes) | 1 |
| plum tomatoes (about 6 large) | 1 |
| plum tomatoes (about 6), cut into 1/4-inch-thick slices | 1 |
| plum tomatoes (about 6), halved, cored | 1 |
| plum tomatoes (or canned tomatoes, drained) | 1 |
| plum tomatoes (whole or crushed) | 1 |
| plum tomatoes canned | 1 |
| plum tomatoes chopped (seeds and all) | 1 |
| plum tomatoes cored, halved, seeded | 1 |
| plum tomatoes cut in 1/4-inch¿thick rounds | 1 |
| plum tomatoes cut into 1/2-inch wedges | 2 |
| plum tomatoes cut into 1/4-inch slices | 1 |
| plum tomatoes diced | 1 |
| plum tomatoes in heavy puree, drained | 1 |
| plum tomatoes in tomato puree | 1 |
| plum tomatoes or 1 (28- to 32-ounce) can whole tomatoes in juice, drained | 1 |
| plum tomatoes or 1 large tomato, cored and halved | 1 |
| plum tomatoes or 2 jersey tomato | 1 |
| plum tomatoes or 4 beefsteak tomatoes, halved | 1 |
| plum tomatoes or small vine-ripened tomato | 1 |
| plum tomatoes peeled, seeded and finely chopped | 1 |
| plum tomatoes roasted | 2 |
| plum tomatoes such as roma, halved lengthwise | 1 |
| plum tomatoes with their juices | 1 |
| plum tomatoes, 1/4-inch dice | 1 |
| plum tomatoes, about 1 3/4 pounds, tops cut off and quartered and sliced | 1 |
| plum tomatoes, and their juices | 1 |
| plum tomatoes, blackened on dry skillet and peeled | 1 |
| plum tomatoes, cored | 9 |
| plum tomatoes, cored and chopped | 3 |
| plum tomatoes, cored and coarsely chopped | 1 |
| plum tomatoes, cored and cut in half lengthwise | 1 |
| plum tomatoes, cored and cut into 1-inch pieces | 1 |
| plum tomatoes, cored and cut into 1-inch thick slices | 1 |
| plum tomatoes, cored and cut into large chunks | 1 |
| plum tomatoes, cored and cut into sixths | 1 |
| plum tomatoes, cored and cut lengthwise | 1 |
| plum tomatoes, cored and diced | 2 |
| plum tomatoes, cored and finely diced | 1 |
| plum tomatoes, cored and halved | 1 |
| plum tomatoes, cored and halved (canned are fine; drain and reserve liquid for another use) | 1 |
| plum tomatoes, cored and halved lengthwise | 2 |
| plum tomatoes, cored and quartered | 2 |
| plum tomatoes, cored and roughly chopped | 2 |
| plum tomatoes, cored and seeded | 2 |
| plum tomatoes, cored, cut lengthwise into thin wedges | 1 |
| plum tomatoes, cored, halved lengthwise | 2 |
| plum tomatoes, cored, halved lengthwise, seeded | 1 |
| plum tomatoes, cored, halved the short way | 1 |
| plum tomatoes, cored, halved, seeded | 1 |
| plum tomatoes, cored, quartered | 1 |
| plum tomatoes, cored, quartered, and puréed in a blender | 1 |
| plum tomatoes, cored, seeded and cut into large chunks | 1 |
| plum tomatoes, cored, seeded and diced | 1 |
| plum tomatoes, cored, seeded and finely diced | 1 |
| plum tomatoes, cored, seeded and roughly chopped | 1 |
| plum tomatoes, cored, seeded, and chopped | 1 |
| plum tomatoes, crushed | 2 |
| plum tomatoes, cut 1/2-inch dice (about 2 1/2 pounds) | 1 |
| plum tomatoes, cut in 1/2 and seeded | 1 |
| plum tomatoes, cut in 1/2, lengthwise | 1 |
| plum tomatoes, cut in 1/4-inch slices | 1 |
| plum tomatoes, cut in half | 1 |
| plum tomatoes, cut in half lengthwise | 2 |
| plum tomatoes, cut in half, seeds removed and grilled | 1 |
| plum tomatoes, cut in rounds | 1 |
| plum tomatoes, cut into 1 1/2-inch chunks | 1 |
| plum tomatoes, cut into 1 inch dice | 1 |
| plum tomatoes, cut into 1-inch cubes | 1 |
| plum tomatoes, cut into 1-inch pieces | 2 |
| plum tomatoes, cut into 1/2-inch dice | 3 |
| plum tomatoes, cut into 1/2-inch pieces | 2 |
| plum tomatoes, cut into 1/2-inch slices, seeds removed | 1 |
| plum tomatoes, cut into 1/4-inch dice (about 1 cup) | 1 |
| plum tomatoes, cut into 1/4-inch diced (about 1 cup) | 2 |
| plum tomatoes, cut into 1/4-inch slices | 1 |
| plum tomatoes, cut into 20 thin slices | 1 |
| plum tomatoes, cut into chunks | 1 |
| plum tomatoes, cut into quarters, seeds removed | 1 |
| plum tomatoes, cut into small dice | 1 |
| plum tomatoes, cut into strips | 1 |
| plum tomatoes, cut into thick slices | 3 |
| plum tomatoes, cut into thin wedges | 1 |
| plum tomatoes, cut into wedges | 2 |
| plum tomatoes, cut lengthwise in half | 1 |
| plum tomatoes, cut lengthwise into 1/4-inch-thick slices | 1 |
| plum tomatoes, drained and chopped | 1 |
| plum tomatoes, drained and crushed | 2 |
| plum tomatoes, drained and purees through a food mill | 1 |
| plum tomatoes, each cut into 6 wedges | 4 |
| plum tomatoes, each cut lengthwise into 4 slices | 2 |
| plum tomatoes, each cut lengthwise into 6 slices | 1 |
| plum tomatoes, ends removed | 1 |
| plum tomatoes, ends removed and cut into thin slices | 1 |
| plum tomatoes, grilled or roasted until blackened, halved, seeded and diced | 1 |
| plum tomatoes, grilled until charred on all sides, and coarsely chopped | 2 |
| plum tomatoes, grilled, seeds and skin removed and coarsely chopped | 1 |
| plum tomatoes, grilled, seeds removed and halved | 1 |
| plum tomatoes, half of juices reserved and chopped | 1 |
| plum tomatoes, halved | 23 |
| plum tomatoes, halved and grilled | 2 |
| plum tomatoes, halved and roasted in oven until soft | 1 |
| plum tomatoes, halved and seeded | 3 |
| plum tomatoes, halved and seeds removed | 2 |
| plum tomatoes, halved crosswise | 1 |
| plum tomatoes, halved crosswise, seeded, cut into thin rounds | 1 |
| plum tomatoes, halved lengthwise | 37 |
| plum tomatoes, halved lengthwise, cored, and coarsely chopped (24 cups) | 1 |
| plum tomatoes, halved lengthwise, cores and seeds removed | 1 |
| plum tomatoes, halved lengthwise, seeded, and cut into julienne strips | 1 |
| plum tomatoes, halved lengthwise, seeded, and halves cut into sixths | 1 |
| plum tomatoes, halved lengthwise, seeds (not cores) removed | 1 |
| plum tomatoes, halved lengthwise, seeds and pulp removed, shells cut into long thin strips | 1 |
| plum tomatoes, halved lengthwise, seeds removed | 1 |
| plum tomatoes, halved through the stem ends | 1 |
| plum tomatoes, halved, seeded | 4 |
| plum tomatoes, halved, seeded and finely chopped | 1 |
| plum tomatoes, halved, seeded and finely diced | 1 |
| plum tomatoes, halved, seeded and julienned | 2 |
| plum tomatoes, halved, seeded and sliced | 1 |
| plum tomatoes, halved, seeded, and cut into 1/2-inch pieces (1 1/4 cups) | 1 |
| plum tomatoes, halved, seeded, and cut into a medium dice | 1 |
| plum tomatoes, halved, seeded, and finely chopped | 1 |
| plum tomatoes, halved, seeded, cut into 1/2-inch cubes | 1 |
| plum tomatoes, medium diced | 1 |
| plum tomatoes, oven roasted and coarsely chopped (see cook's note) | 1 |
| plum tomatoes, pureed | 1 |
| plum tomatoes, pureed until smooth with their juices | 1 |
| plum tomatoes, quartered | 18 |
| plum tomatoes, quartered (about 1 1/2 pounds) | 1 |
| plum tomatoes, quartered and seeded | 1 |
| plum tomatoes, quartered lengthwise | 6 |
| plum tomatoes, quartered lengthwise and halved crosswise | 1 |
| plum tomatoes, quartered lengthwise and seeded | 1 |
| plum tomatoes, quartered lengthwise, then cut across into 1/8-inch wide slices | 1 |
| plum tomatoes, quartered, seeded and cut into 1/2-inch triangles | 1 |
| plum tomatoes, roasted | 1 |
| plum tomatoes, roasted in a 375 degree oven until blackened | 1 |
| plum tomatoes, seeded | 34 |
| plum tomatoes, seeded and chopped | 32 |
| plum tomatoes, seeded and chopped (about 1 cup) | 1 |
| plum tomatoes, seeded and chopped (about 3 tomatoes) | 1 |
| plum tomatoes, seeded and chopped fine | 1 |
| plum tomatoes, seeded and chopped into 1/2-inch pieces | 1 |
| plum tomatoes, seeded and chopped into small pieces | 1 |
| plum tomatoes, seeded and coarsely chopped | 2 |
| plum tomatoes, seeded and coarsely diced | 1 |
| plum tomatoes, seeded and cut into 1/2-inch dice | 3 |
| plum tomatoes, seeded and cut into 1/2-inch wide pieces | 1 |
| plum tomatoes, seeded and cut into 1/4 inch dice | 1 |
| plum tomatoes, seeded and cut into 1/4-inch dice | 2 |
| plum tomatoes, seeded and cut into 1/4-inch dice, plus tomato slices for garnish | 1 |
| plum tomatoes, seeded and cut into 1/4-inch dice, plus tomato slices for garnish (about 1 cup diced) | 1 |
| plum tomatoes, seeded and cut into 1/4inch dice | 1 |
| plum tomatoes, seeded and cut into fine dice | 2 |
| plum tomatoes, seeded and cut into small dice | 1 |
| plum tomatoes, seeded and diced | 24 |
| plum tomatoes, seeded and diced fine | 1 |
| plum tomatoes, seeded and finely chopped | 3 |
| plum tomatoes, seeded and finely diced | 8 |
| plum tomatoes, seeded and minced | 1 |
| plum tomatoes, seeded and quartered | 1 |
| plum tomatoes, seeded and roughly chopped | 1 |
| plum tomatoes, seeded and very thinly sliced lengthwise | 1 |
| plum tomatoes, seeded then thinly sliced | 1 |
| plum tomatoes, seeded then thinly sliced lengthwise | 1 |
| plum tomatoes, seeded, and cut into 1/4-inch dice | 1 |
| plum tomatoes, seeded, cut into 1-inch pieces (about 6 cups) | 1 |
| plum tomatoes, seeded, cut into 1/2-inch pieces | 1 |
| plum tomatoes, seeded, cut into matchstick-size strips (about 1 1/2 cups) | 1 |
| plum tomatoes, seeded, quartered | 1 |
| plum tomatoes, seeds and pulp removed and medium-diced | 1 |
| plum tomatoes, seeds removed and cut brunoise | 2 |
| plum tomatoes, skin charred and chopped | 1 |
| plum tomatoes, smoked and chopped | 1 |
| plum tomatoes, thinly sliced | 12 |
| plum tomatoes, thinly sliced crosswise | 2 |
| plum tomatoes, thinly sliced into rounds | 1 |
| plum tomatoes, thinly sliced lengthwise | 2 |
| plum tomatoes, trim top and bottom, cut into 1/4-inch slices | 1 |
| plum tomatoes, trimmed and halved crosswise | 2 |
| plum tomatoes, trimmed, quartered | 1 |
| plum tomatoes, very thinly sliced | 2 |
| plum-style tomato | 1 |
| plus 1 tablespoon tomato paste (one 6-ounce can or a little less) | 1 |
| plus 1 teaspoon tomato paste | 1 |
| plus 2 1/2 tablespoons tomato paste | 1 |
| plus 2 tablespoons tomato paste | 1 |
| plus 2 tablespoons tomato paste (from a 6-ounce can) | 1 |
| plus 2 teaspoons chopped sun-dried tomato | 1 |
| plus 3 tablespoons diced tomato | 1 |
| plus 6 whole tomato | 1 |
| pomodoro confit tomatoes, recipe follows | 1 |
| pomodoro tomato | 1 |
| pomì strained tomato | 1 |
| pouch progresso™ recipe starters™ fire roasted tomato cooking sauce | 1 |
| pre-diced fresh tomato | 1 |
| premium tomato juice (or make your own from garden-fresh tomatoes--about 1 pound for an 8-ounce cocktail) | 2 |
| prepared mexican-style tomato sauce | 1 |
| prepared pasta sauce, basil pesto or sun-dried tomato pesto | 1 |
| prepared pizza sauce (not tomato sauce) | 1 |
| prepared pizza tomato sauce or homemade, recipe follows | 1 |
| prepared sun-dried tomato mayonnaise | 1 |
| prepared sun-dried tomato pesto | 3 |
| prepared sun-dried tomato pesto (or just a couple of pureed sun-dried tomatoes) | 1 |
| prepared sun-dried tomato tapenade | 2 |
| prepared tomato or spaghetti sauce | 1 |
| prepared tomato salsa | 1 |
| prepared tomato sauce | 17 |
| prepared tomato sauce or 1 cup diced tomato | 1 |
| prepared tomato sauce, heated | 1 |
| prepared tomato soup | 1 |
| prepared tomato soup (from can or jar) | 1 |
| prepared tomato-basil-garlic soup | 1 |
| progresso™ recipe starters™ fire roasted tomato cooking sauce | 1 |
| pt assorted cherry tomato | 1 |
| pt. cherry tomato | 1 |
| pt. grape tomatoes, halved | 1 |
| pulp of 3 or 4 tomato | 1 |
| pumpernickel, pita, fresh and sour tomatoes and an assortment of olives, as an accompaniment | 1 |
| purchased fresh tomato salsa | 2 |
| purchased sun-dried tomato pesto or 1/2 cup chopped drained oil-packed sun-dried tomato | 1 |
| purchased tomato salsa | 1 |
| purchased tomato-based barbecue sauce | 1 |
| purchased tomato-basil sauce | 1 |
| pure maple syrup or sliced tomatoes for accompaniment | 1 |
| pureed canned plum tomato | 3 |
| pureed canned tomato | 2 |
| pureed fresh tomato | 2 |
| pureed fresh tomatoes or canned tomato puree | 1 |
| pureed plum tomato | 3 |
| pureed red ripe peeled tomatoes (canned crushed tomatoes work also) | 1 |
| pureed tomato | 4 |
| pureed tomato salsa, recipe follows | 1 |
| purple cherokee tomato | 1 |
| qt. crushed tomato | 1 |
| qts tomato puree | 1 |
| quart cherry tomato | 1 |
| quart cherry tomatoes (multi-color if available) | 1 |
| quart clam-tomato juice, such as clamato | 1 |
| quart fresh tomatoes, seeded, medium dice | 1 |
| quart grandma nancy's marinara sauce or tomato meat sauce, recipe follows | 1 |
| quart green tomato | 1 |
| quart ketchup (recommended: heinz tomato ketchup) | 1 |
| quart peeled plum tomatoes, crushed | 1 |
| quart simple tomato sauce, recipe follows, or store-bought marinara sauce, blended until smooth | 1 |
| quart small heirloom tomatoes or red cherry tomatoes, halved | 1 |
| quart smoked tomato | 1 |
| quart stewed tomato | 1 |
| quart tomato juice | 6 |
| quart tomato or tomato-vegetable juice such as v8, chilled | 1 |
| quart tomato paste | 2 |
| quart tomato puree | 3 |
| quart tomato sauce, recipe follows | 1 |
| quart whole peeled smoked tomato | 1 |
| quarter-inch-thick slices plum tomato | 1 |
| quartered campari or other small vine-ripened tomato | 1 |
| quartered cherry or grape tomato | 3 |
| quartered cherry or grape tomatoes (about 12) | 1 |
| quartered cherry tomato | 16 |
| quartered grape tomato | 4 |
| quartered grape tomatoes (optional) | 1 |
| quartered grape tomatoes or diced plum tomato | 1 |
| quartered medium tomato | 1 |
| quartered plum tomato | 1 |
| quartered ripe tomato | 1 |
| quartered vine-ripened grape or cherry tomato | 2 |
| quartered yellow cherry tomato | 1 |
| quarts (700 ml) tomato sauce (or blended canned peeled italian tomatoes) | 1 |
| quarts canned plum tomato | 1 |
| quarts canned tomatoes (or 1 6 oz. can tomato paste) | 1 |
| quarts canned tomatoes with juice or 14 large, ripe fresh tomato | 1 |
| quarts canned whole peeled tomato | 3 |
| quarts canned whole tomatoes (with the liquid) | 1 |
| quarts crushed tomato | 1 |
| quarts grape tomato | 1 |
| quarts green tomato | 1 |
| quarts ketchup (recommended: heinz tomato ketchup) | 2 |
| quarts low-sodium tomato juice | 1 |
| quarts peeled, seeded ripe tomato | 1 |
| quarts plum tomato | 1 |
| quarts ripe tomato | 1 |
| quarts san marzano plum tomato | 1 |
| quarts tomato juice | 1 |
| quarts tomato juice, chilled | 1 |
| quarts tomato puree | 3 |
| quarts tomato sauce | 1 |
| quick tomato sauce, recipe follows | 2 |
| raw green tomato | 1 |
| razor red tomatoes (see cook's note) | 1 |
| ready-to-eat sun-dried tomato | 1 |
| ready-to-serve creamy tomato soup | 3 |
| ready-to-use sun-dried tomatoes (not packed in oil) | 1 |
| recipe basic tomato sauce, recipe follows | 1 |
| recipe cherry tomato salad, recipe follows | 1 |
| recipe michele's favorite tomato sauce, recipe follows | 1 |
| recipe roasted tomato couscous (recipe follows) | 1 |
| recipe tomato sauce (above) | 1 |
| recipe tomato sauce (recipe follows) | 1 |
| recipe tomato sauce, recipe follows | 1 |
| reconstituted sun-dried tomato | 1 |
| red and yellow cherry tomato | 1 |
| red and yellow cherry tomatoes (equal parts) | 1 |
| red and yellow cherry tomatoes, halved | 2 |
| red and yellow cherry tomatoes, some halved | 2 |
| red and yellow grape or cherry tomatoes, halved | 2 |
| red and yellow grape tomatoes, halved | 3 |
| red and yellow heirloom tomato | 1 |
| red and yellow pear and sweet 100 cherry tomatoes, cut in half | 1 |
| red and yellow pear or cherry tomato | 1 |
| red and yellow pear tomato | 1 |
| red and yellow sweet 100 tomatoes or cherry tomatoes, halved | 2 |
| red and yellow teardrop or grape tomatoes, halved | 1 |
| red and yellow teardrop tomatoes or grape tomatoes, halved | 1 |
| red and/or yellow cherry tomatoes, halved | 1 |
| red and/or yellow grape tomatoes, halved | 1 |
| red and/or yellow tomatoes, cut into 1/2-inch dice (about 2 to 3 tomatoes) | 1 |
| red baby tomato | 2 |
| red bell pepper and tomato salad | 1 |
| red cherry or grape tomato | 1 |
| red cherry or grape tomatoes, halved | 1 |
| red cherry tomato | 4 |
| red cherry tomatoes, quartered | 2 |
| red chile-tomato sauce, recipe follows | 2 |
| red currant tomato | 1 |
| red gold® tomato paste | 1 |
| red grape or cherry tomato | 1 |
| red grape tomato | 2 |
| red grape tomatoes, halved | 6 |
| red heirloom or plum tomato | 1 |
| red heirloom tomato, 1/4-inch dice | 1 |
| red heirloom tomatoes, quartered | 1 |
| red or orange grape tomatoes, halved | 1 |
| red or yellow cherry tomato | 1 |
| red or yellow cherry tomatoes, stemmed, and cut in half if large | 1 |
| red or yellow grape tomato | 1 |
| red or yellow teardrop tomatoes, halved | 1 |
| red or yellow tomatoes (4 medium), cut crosswise nto 1/2-inch-thick slices | 1 |
| red pack diced tomato | 2 |
| red pack tomato puree | 2 |
| red pear or cherry tomato | 1 |
| red pear tomatoes, halved | 2 |
| red ripe tomato, thinly sliced | 1 |
| red ripe tomatoes (2 to 3) | 1 |
| red roma tomatoes, cut lengthwise | 1 |
| red roma tomatoes, washed and quartered | 1 |
| red roma tomatoes, washed, core removed, and a small "x" drawn on the bottom of each with a knife | 1 |
| red teardrop tomatoes, halved | 2 |
| red tomato | 12 |
| red tomato puree, canned | 1 |
| red tomato salsa | 1 |
| red tomato salsa (recipe follows) | 2 |
| red tomato salsa, recipe follows | 1 |
| red tomato salsa, see recipe | 1 |
| red tomato, cut in 1/2 | 1 |
| red tomato, cut into 1/4-inch slices | 1 |
| red tomato, medium dice | 1 |
| red tomato, seeded and diced | 1 |
| red tomato, skinned and seeded (italian plum, brandywine) | 1 |
| red tomatoes (4 to 5 oz each) | 1 |
| red tomatoes, halved | 1 |
| red tomatoes, top removed like a "hat", the pulp scooped out and reserved | 1 |
| red wine, enough to fill the tomato paste can | 1 |
| red, ripe sauce tomatoes, broken into pieces, or canned italian peeled tomatoes, drained | 1 |
| red, yellow, and green grape tomato | 1 |
| red-leaf lettuce and sliced tomato, for serving | 1 |
| redi-cut tomato | 1 |
| reduced-sodium tomato juice | 2 |
| reduced-sodium tomato paste | 1 |
| regular or spicy tomato juice | 1 |
| regular tomato paste | 1 |
| rehydrated sun-dried tomato | 1 |
| reserved chopped tomato from caprese salad stuffed tomatoes recipe | 1 |
| reserved orzo from caprese salad stuffed tomatoes recipe | 1 |
| reserved sun-dried tomato oil | 1 |
| reserved tomato sauce | 1 |
| reserved tomato sauce from crispy eggplant parmesan recipe | 1 |
| reserved tomato vinaigrette | 1 |
| reserved tomatoes from shrimp stuffed cucumber cups, recipe follows | 1 |
| rich winter tomato sauce | 1 |
| ripe (or even slightly overripe) red tomatoes, washed and chopped | 1 |
| ripe beef steak tomatoes, halves and seeded and finely diced | 1 |
| ripe beefsteak (or any large variety heirloom) tomatoes, washed, dried and stemmed | 1 |
| ripe beefsteak or heirloom tomatoes, cut into bite-size pieces | 1 |
| ripe beefsteak or large heirloom tomatoes, cut into thick slices | 1 |
| ripe beefsteak tomato | 11 |
| ripe beefsteak tomatoes or 4 ripe plum tomato | 2 |
| ripe beefsteak tomatoes, cheeks removed and julienned | 1 |
| ripe beefsteak tomatoes, cut into 1/2-inch dice | 1 |
| ripe beefsteak tomatoes, cut into 1/2-inch thick slices | 1 |
| ripe beefsteak tomatoes, seeded | 1 |
| ripe beefsteak tomatoes, seeded and diced | 1 |
| ripe but firm large tomato | 1 |
| ripe but firm plum tomato | 1 |
| ripe cherry tomatoes (about 4 cups) | 1 |
| ripe cherry tomatoes, cut in half | 1 |
| ripe cherry tomatoes, halved | 4 |
| ripe diced tomato | 1 |
| ripe fresh tomato | 4 |
| ripe green heirloom tomatoes, cored, cut into large chunks | 1 |
| ripe green tomatoes (such as green zebra), cubed | 1 |
| ripe halved tomato | 1 |
| ripe heirloom or beefsteak tomato | 1 |
| ripe heirloom or cherry tomatoes, 1/2-inch-diced | 1 |
| ripe heirloom or vine tomato | 1 |
| ripe heirloom tomato | 3 |
| ripe heirloom tomatoes (different varieties and colors) or beefsteak tomato | 1 |
| ripe heirloom tomatoes of different colors and shapes | 1 |
| ripe heirloom tomatoes, cored | 2 |
| ripe heirloom tomatoes, cored and chopped | 1 |
| ripe italian plum tomato | 1 |
| ripe italian plum tomatoes, cut into 8 pieces each | 1 |
| ripe italian roma tomatoes, cored | 4 |
| ripe large tomato | 1 |
| ripe large tomatoes or 9 ripe plum tomato | 1 |
| ripe large tomatoes, cored and quartered | 1 |
| ripe large tomatoes, cut into 1/3-inch-thick rounds | 1 |
| ripe medium red tomatoes (about 1-1/4 pounds total) | 1 |
| ripe medium size tomato, medium dice | 1 |
| ripe medium tomato | 9 |
| ripe medium tomato, halved | 1 |
| ripe medium tomatoes (1 red and 1 yellow), cored and roughly chopped (about 1 1/2 cups) | 1 |
| ripe medium tomatoes (about 1 pound) | 1 |
| ripe medium tomatoes (red and yellow if available), seeded and chopped | 1 |
| ripe medium tomatoes cubed | 1 |
| ripe medium tomatoes or 4 plum tomatoes, cored and diced | 1 |
| ripe medium tomatoes, about 1/2 pound each | 1 |
| ripe medium tomatoes, cored | 1 |
| ripe medium tomatoes, cored and diced | 2 |
| ripe medium tomatoes, cored, halved, cut into 1/4-inch-thick slices | 1 |
| ripe medium tomatoes, seeded and coarsely chopped | 1 |
| ripe medium-size tomatoes, seeded and small-diced | 1 |
| ripe medium-sized tomatoes, seeded and cut into 8 pieces each | 1 |
| ripe orange beefsteak tomato | 1 |
| ripe organic vine tomatoes or large plum tomato | 5 |
| ripe plum or small vine tomato | 1 |
| ripe plum tomato | 27 |
| ripe plum tomato (about 2 ounces), seeded, cored, and diced | 2 |
| ripe plum tomato, cored and diced | 4 |
| ripe plum tomato, cut into 1/4-inch strips | 1 |
| ripe plum tomato, seeded and cut into 1/8-inch dice | 1 |
| ripe plum tomatoes (preferably san marzano-style) | 1 |
| ripe plum tomatoes (see cooks' note, below) | 1 |
| ripe plum tomatoes halved crosswise | 1 |
| ripe plum tomatoes or 2 medium regular tomatoes, seeded and diced | 1 |
| ripe plum tomatoes or 4 beefsteak tomatoes, cored and scored | 1 |
| ripe plum tomatoes or 48 ripe cherry tomato | 1 |
| ripe plum tomatoes or two 28-ounce can diced tomatoes in juice, such as organic muir glen | 2 |
| ripe plum tomatoes* | 1 |
| ripe plum tomatoes, cored | 1 |
| ripe plum tomatoes, cored and cut in half lengthwise | 1 |
| ripe plum tomatoes, cored and halved lengthwise | 1 |
| ripe plum tomatoes, cored and quartered | 1 |
| ripe plum tomatoes, cored, halved | 1 |
| ripe plum tomatoes, cut in half | 1 |
| ripe plum tomatoes, cut in half lengthwise | 3 |
| ripe plum tomatoes, cut in quarters | 1 |
| ripe plum tomatoes, cut into 1/2-inch pieces | 1 |
| ripe plum tomatoes, cut into 1/4-inch thick rounds | 1 |
| ripe plum tomatoes, cut into 3/4-inch dice | 1 |
| ripe plum tomatoes, cut into eighths | 1 |
| ripe plum tomatoes, cut into julienne | 1 |
| ripe plum tomatoes, cut into medium dice | 1 |
| ripe plum tomatoes, cut into quarters, lengthwise | 1 |
| ripe plum tomatoes, cut into small cubes | 1 |
| ripe plum tomatoes, halved | 3 |
| ripe plum tomatoes, halved lengthwise | 4 |
| ripe plum tomatoes, halved lengthwise, seeds squeezed out, and finely diced | 1 |
| ripe plum tomatoes, roasted (see note) | 1 |
| ripe plum tomatoes, seeded | 1 |
| ripe plum tomatoes, seeded and chopped | 1 |
| ripe plum tomatoes, seeded and cut into 1/2-inch pieces | 1 |
| ripe plum tomatoes, seeded and cut into 1/4 inch dice | 1 |
| ripe plum tomatoes, seeded and cut into 1/4-inch dice | 2 |
| ripe plum tomatoes, seeded and diced | 5 |
| ripe plum tomatoes, seeded and finely diced | 1 |
| ripe plum tomatoes, seeded and sliced lengthwise into thin strips | 1 |
| ripe plum tomatoes, thinly sliced | 1 |
| ripe plum tomatoes, washed, cored and split lengthwise | 2 |
| ripe red beefsteak tomato | 1 |
| ripe red cherry or pear tomatoes, stemmed | 1 |
| ripe red cherry tomato | 1 |
| ripe red tomato | 2 |
| ripe red tomato, quartered | 1 |
| ripe red tomato, seeded and cut into 1/4-inch dice | 1 |
| ripe red tomato, seeded and cut into dice | 1 |
| ripe red tomatoes, cored and 1-inch diced | 1 |
| ripe roma or beefsteak tomatoes, quartered | 1 |
| ripe roma or heirloom tomatoes, cored and halved | 1 |
| ripe roma tomato | 10 |
| ripe roma tomatoes (about 12 tomatoes), cut into wedges | 1 |
| ripe roma tomatoes or 2 whole canned napoli tomatoes, fine diced | 1 |
| ripe roma tomatoes peeled and seeded | 1 |
| ripe roma tomatoes, halved lengthwise | 1 |
| ripe roma tomatoes, quartered | 2 |
| ripe summer tomato | 1 |
| ripe tolstoi tomatoes or other red juicy tomatoes (about 8 medium), cored, seeded | 1 |
| ripe tomato | 179 |
| ripe tomato (4 ounces) | 1 |
| ripe tomato on the vine, quartered | 1 |
| ripe tomato or 2 ripe plum tomatoes, seeded and cut into 1/4inch dice | 1 |
| ripe tomato, cored and diced | 1 |
| ripe tomato, cut into 4 slices | 1 |
| ripe tomato, cut into 8ths | 1 |
| ripe tomato, cut into eighths | 1 |
| ripe tomato, cut into small cubes | 1 |
| ripe tomato, cut into thin wedges | 1 |
| ripe tomato, halved | 1 |
| ripe tomato, quartered | 1 |
| ripe tomato, quartered and thinly sliced | 1 |
| ripe tomato, seeded | 1 |
| ripe tomato, seeded and chopped | 1 |
| ripe tomato, seeded and diced | 1 |
| ripe tomatoes (2 1/2 to 3-inches in diameter) | 1 |
| ripe tomatoes (2 or 3 tomatoes) | 1 |
| ripe tomatoes (about 1 pound), halved | 1 |
| ripe tomatoes (about 2 1/4 pounds total), cored and scored on the bottom | 1 |
| ripe tomatoes (about 3 medium) | 1 |
| ripe tomatoes (about 3) | 1 |
| ripe tomatoes (about 3), seeded and chopped | 1 |
| ripe tomatoes (about 5 large) | 1 |
| ripe tomatoes (about 5 medium) | 1 |
| ripe tomatoes (about 6) | 1 |
| ripe tomatoes (about 7 medium) | 1 |
| ripe tomatoes (about 9 globe or 24 plum), stemmed, halved, and seeded | 1 |
| ripe tomatoes (preferably heirloom) in assorted colors, cored, cut into 1 1/4-inch chunks (about 6 cups) | 1 |
| ripe tomatoes (yellow and red),1/2-inch dice | 1 |
| ripe tomatoes - peeled and seeded | 1 |
| ripe tomatoes - peeled, seeded, and chopped | 2 |
| ripe tomatoes chopped | 2 |
| ripe tomatoes cut into 1/2-inch slices | 1 |
| ripe tomatoes on the vine (about 1 1/3 pounds), stemmed, halved lengthwise | 1 |
| ripe tomatoes or 4 plum tomatoes, cored and roughly chopped | 2 |
| ripe tomatoes or one 14-ounce can crushed tomato | 1 |
| ripe tomatoes or peeled tomatoes (if in a hurry) | 1 |
| ripe tomatoes such as roma, early girl or heirloom, halved | 1 |
| ripe tomatoes, (beefsteak, yellow, and heirloom) | 1 |
| ripe tomatoes, 1/4-inch dice (2 large tomatoes) | 1 |
| ripe tomatoes, about 5 to 6 medium tomatoes, seeded | 1 |
| ripe tomatoes, assorted colors and sizes | 1 |
| ripe tomatoes, blanched | 1 |
| ripe tomatoes, cored | 1 |
| ripe tomatoes, cored and cut into 1-inch pieces or 2 (28-ounce) cans plum tomatoes, drained | 1 |
| ripe tomatoes, cored and cut into 3/4-inch pieces, chilled | 1 |
| ripe tomatoes, cored and cut into thick wedges | 1 |
| ripe tomatoes, cored and quartered | 3 |
| ripe tomatoes, cored and seeded and cut into 1/4-inch cubes | 1 |
| ripe tomatoes, cored and thinly sliced | 1 |
| ripe tomatoes, cored, seeded (reserve the seeds and tomato juice) and flesh roughly chopped | 1 |
| ripe tomatoes, cored, seeded and diced | 2 |
| ripe tomatoes, cubed | 1 |
| ripe tomatoes, cut crosswise into 1/2-inch-thick slices | 1 |
| ripe tomatoes, cut in eighths | 1 |
| ripe tomatoes, cut into 1-inch cubes | 1 |
| ripe tomatoes, cut into 1/2-inch pieces | 1 |
| ripe tomatoes, cut into 1/4-inch cubes | 1 |
| ripe tomatoes, cut into 1/4-inch dice | 1 |
| ripe tomatoes, cut into bite-size chunks* | 1 |
| ripe tomatoes, cut into chunks, for garnish | 1 |
| ripe tomatoes, cut into cubes | 1 |
| ripe tomatoes, cut into large chunks (into 8ths) (about 3 to 4 medium tomatoes) | 1 |
| ripe tomatoes, cut into large dice | 1 |
| ripe tomatoes, cut into wedges | 5 |
| ripe tomatoes, cut into wedges (6 small tomatoes) | 2 |
| ripe tomatoes, cut into wedges, or 1 pint grape tomatoes, halved | 1 |
| ripe tomatoes, halved, seeded,and finely chopped | 1 |
| ripe tomatoes, large-diced | 1 |
| ripe tomatoes, medium-diced | 2 |
| ripe tomatoes, or 3 cups canned peeled whole plum tomato | 1 |
| ripe tomatoes, or 3 cups canned whole peeled tomatoes with their juice | 1 |
| ripe tomatoes, preferably roma | 1 |
| ripe tomatoes, quartered | 6 |
| ripe tomatoes, rinsed and drained, stems removed | 1 |
| ripe tomatoes, seeded | 1 |
| ripe tomatoes, seeded and chopped | 4 |
| ripe tomatoes, seeded and chopped (about 2 cups) | 1 |
| ripe tomatoes, seeded and cut into 1/2-inch dice | 1 |
| ripe tomatoes, seeded and cut into fine dice | 1 |
| ripe tomatoes, seeded and diced | 8 |
| ripe tomatoes, seeded and finely diced | 1 |
| ripe tomatoes, seeded and roughly chopped | 2 |
| ripe tomatoes, seeded, cored, and 1/2-inch-diced | 1 |
| ripe tomatoes, seeds removed and diced | 2 |
| ripe tomatoes, seeds scooped out (leave pulp intact) and diced large | 1 |
| ripe tomatoes, skinned, seeded, and chopped | 1 |
| ripe tomatoes, small dice | 1 |
| ripe tomatoes, small diced | 1 |
| ripe tomatoes, smoked | 1 |
| ripe tomatoes, stems and cores removed | 1 |
| ripe tomatoes, the greatest variety of colors, sizes and shapes possible | 1 |
| ripe tomatoes, thinly sliced | 4 |
| ripe tomatoes, washed | 1 |
| ripe vine tomato | 1 |
| ripe vine-ripened tomato | 1 |
| ripe yellow beefsteak tomato | 1 |
| ripe yellow cherry or pear tomatoes, stemmed | 1 |
| ripe yellow cherry tomato | 1 |
| ripe yellow tomato | 3 |
| ripe yellow tomatoes, cored and diced | 1 |
| ripe, large tomato, roasted or boiled, cored and peeled or 3/4 15-ounce can tomatoes, drained | 1 |
| ripe, large tomatoes, seeded and roughly chopped | 1 |
| ripe, medium roma tomatoes, cored | 1 |
| ripe, medium-large tomato, cored and very finely chopped | 2 |
| ro*tel diced tomatoes & green chilies, drained | 1 |
| ro*tel diced tomatoes & green chilies, undrained | 7 |
| ro*tel® mexican diced tomatoes with lime juice & cilantro, drained | 2 |
| ro*tel® mexican diced tomatoes with lime juice & cilantro, drained, liquid reserved | 1 |
| ro*tel® mexican diced tomatoes with lime juice & cilantro, undrained | 1 |
| ro*tel® mild diced tomatoes & green chilies, drained | 1 |
| ro*tel® mild diced tomatoes & green chilies, undrained | 1 |
| ro*tel® original diced tomatoes & green chilies | 1 |
| ro*tel® original diced tomatoes & green chilies, drained | 6 |
| ro*tel® original diced tomatoes & green chilies, drained, liquid reserved | 3 |
| ro*tel® original diced tomatoes & green chilies, undrained | 9 |
| ro*tel® original tomato & green chili sauce | 1 |
| roasted cherry or grape tomatoes, as needed | 2 |
| roasted cherry tomato | 1 |
| roasted cherry tomato sauce, recipe follows | 1 |
| roasted chicken, goat cheese, and sun-dried tomato | 1 |
| roasted diced tomato | 1 |
| roasted garlic (from roasted tomato recipe), recipe follows | 1 |
| roasted garlic and herb tomato sauce | 1 |
| roasted garlic and sun-dried tomato dressing, recipe follows | 1 |
| roasted garlic tomato sauce | 1 |
| roasted grape tomato, orange, and basil relish | 1 |
| roasted jalapeño-tomato salsa | 1 |
| roasted or peeled tomatoes with their juice | 1 |
| roasted plum tomato | 3 |
| roasted plum tomato sauce, recipe follows | 1 |
| roasted plum tomatoes (5 plum tomatoes cut in half, drizzled with olive oil, put in a roasting pan and roasted at 325 degrees for about 45 minutes, then skinned and cored, and the flesh chopped) | 2 |
| roasted plum tomatoes, recipe follows | 1 |
| roasted red pepper and tomato sauce | 1 |
| roasted red tomatoes, recipe follows | 1 |
| roasted roma (plum) tomato | 2 |
| roasted roma tomato | 1 |
| roasted roma tomatoes, skinned and seeded | 1 |
| roasted tomato | 3 |
| roasted tomato (see note) | 1 |
| roasted tomato aioli, recipe follows | 1 |
| roasted tomato and onion dipping sauce, recipe follows | 1 |
| roasted tomato and pepper sauce, recipe follows | 1 |
| roasted tomato basil soup | 1 |
| roasted tomato half | 1 |
| roasted tomato halves, from pan seared chicken with roasted tomato sauce | 1 |
| roasted tomato halves, recipe follows | 1 |
| roasted tomato mayonnaise | 1 |
| roasted tomato remoulade sauce, recipe follows | 1 |
| roasted tomato salsa | 3 |
| roasted tomato sauce, recipe follows | 1 |
| roasted tomato-chile de arbol salsa | 1 |
| roasted tomato-chile de arbol salsa, recipe follows | 1 |
| roasted tomato-chile de arbol salsa: | 1 |
| roasted tomatoes, recipe follows | 3 |
| roasted tomatoes: | 1 |
| roma (plum) tomato | 145 |
| roma (plum) tomato, seeded and chopped | 3 |
| roma (plum) tomato, seeded and diced | 2 |
| roma (plum) tomato, thinly sliced | 6 |
| roma (plum) tomatoes - halved, seeded, and chopped | 1 |
| roma (plum) tomatoes - peeled, seeded and chopped | 2 |
| roma (plum) tomatoes, cut into bite-size pieces | 1 |
| roma (plum) tomatoes, cut into eighths | 1 |
| roma (plum) tomatoes, halved | 5 |
| roma (plum) tomatoes, halved and seeded | 1 |
| roma (plum) tomatoes, halved and sliced | 1 |
| roma (plum) tomatoes, halved lengthwise | 4 |
| roma (plum) tomatoes, halved, seeded, and chopped | 1 |
| roma (plum) tomatoes, or more to taste, cut into 1 1/2-inch cubes | 1 |
| roma (plum) tomatoes, quartered | 3 |
| roma (plum) tomatoes, quartered, or more to taste | 1 |
| roma (plum) tomatoes, seeded and chopped | 12 |
| roma (plum) tomatoes, seeded and chopped (optional) | 1 |
| roma (plum) tomatoes, seeded and cut into 1/4-inch dice | 1 |
| roma (plum) tomatoes, seeded and diced | 5 |
| roma (plum) tomatoes, seeded and diced, or more to taste | 2 |
| roma (plum) tomatoes, thinly sliced | 10 |
| roma or italian plum tomatoes, thinly sliced | 1 |
| roma or plum tomato, seeded and finely chopped, for garnish | 1 |
| roma or plum tomatoes, cubed | 2 |
| roma or plum tomatoes, halved and thinly sliced | 1 |
| roma or plum tomatoes, seeded and chopped | 1 |
| roma plum tomatoes, halved lengthwise and seeds removed | 1 |
| roma tomato | 249 |
| roma tomato, cut in half | 1 |
| roma tomato, cut in small dice | 2 |
| roma tomato, cut into thin slices | 1 |
| roma tomato, cut into wedges | 1 |
| roma tomato, fresh, small chop | 1 |
| roma tomato, halved lengthwise and thinly sliced | 1 |
| roma tomato, julienned | 1 |
| roma tomato, quartered | 3 |
| roma tomato, seeded and chopped | 1 |
| roma tomato, seeded and cut into 1/4-inch dice | 1 |
| roma tomato, seeded and cut into 1/4-inch dice, for garnish | 1 |
| roma tomato, seeded and diced | 4 |
| roma tomato, seeded, small dice | 1 |
| roma tomato, thinly sliced | 2 |
| roma tomatoes (about 1 pound) | 1 |
| roma tomatoes (about 1-pound), ends trimmed, cut into thin slices | 2 |
| roma tomatoes (about 2 1/4 pounds) | 1 |
| roma tomatoes (fresh or from a can of san marzano tomatoes) | 1 |
| roma tomatoes (slightly under ripe is fine) | 5 |
| roma tomatoes - peeled, seeded and chopped | 2 |
| roma tomatoes or sun-dried tomato | 1 |
| roma tomatoes sliced | 2 |
| roma tomatoes sliced lengthwise 1/4 inch thick | 1 |
| roma tomatoes, (roasted, skinned and chopped) | 1 |
| roma tomatoes, about 12 medium-sized tomato | 1 |
| roma tomatoes, blanch, de-skinned, seeded, and chopped | 1 |
| roma tomatoes, blanched and peeled | 1 |
| roma tomatoes, cored | 5 |
| roma tomatoes, cored and chopped | 1 |
| roma tomatoes, cored and cut in half lengthwise | 1 |
| roma tomatoes, cored and cut into 6 slices | 1 |
| roma tomatoes, cored and cut into chunks | 1 |
| roma tomatoes, cored and cut into thin strips | 1 |
| roma tomatoes, cored and quartered | 1 |
| roma tomatoes, cored and scored | 1 |
| roma tomatoes, cored and sliced lengthwise | 1 |
| roma tomatoes, cored, halved and diced | 1 |
| roma tomatoes, cored, seeded and julienned | 1 |
| roma tomatoes, cored, seeded and roughly chopped (about 2 1/2 pounds) | 2 |
| roma tomatoes, cut crosswise into 1/4-inch-thick slices | 1 |
| roma tomatoes, cut in 1/2 | 2 |
| roma tomatoes, cut in half | 1 |
| roma tomatoes, cut in half lengthwise | 1 |
| roma tomatoes, cut into 1/2-inch cubes | 1 |
| roma tomatoes, cut into 1/2-inch pieces | 1 |
| roma tomatoes, cut into 1/2-inch slices | 1 |
| roma tomatoes, cut into 1/4-inch slices | 1 |
| roma tomatoes, cut into eighths | 1 |
| roma tomatoes, cut into large dice | 1 |
| roma tomatoes, cut into quarters | 1 |
| roma tomatoes, cut into wedges | 1 |
| roma tomatoes, each cut into 4 pieces | 1 |
| roma tomatoes, each cut into 4 wedges | 1 |
| roma tomatoes, ends trimmed and cut into 12 slices | 1 |
| roma tomatoes, for garnish | 1 |
| roma tomatoes, halved | 6 |
| roma tomatoes, halved (about 1 pound)* | 2 |
| roma tomatoes, halved and seeded | 6 |
| roma tomatoes, halved and sliced | 1 |
| roma tomatoes, halved lengthwise | 5 |
| roma tomatoes, halved lengthwise, plus 1/4 cup seeded and diced ripe tomato | 1 |
| roma tomatoes, halved, seeded and oven dried (procedure follows) | 1 |
| roma tomatoes, halved, seeds and inner flesh removed | 1 |
| roma tomatoes, julienned | 1 |
| roma tomatoes, medium dice | 1 |
| roma tomatoes, pulp removed, cut into 1/2-inch cubes | 1 |
| roma tomatoes, quartered | 9 |
| roma tomatoes, quartered (10 to 12 tomatoes) | 2 |
| roma tomatoes, quartered lengthwise | 2 |
| roma tomatoes, rubbed with olive oil | 1 |
| roma tomatoes, scored, blanched, shocked in ice water and peeled | 1 |
| roma tomatoes, seeded | 2 |
| roma tomatoes, seeded and chopped | 20 |
| roma tomatoes, seeded and chopped (about 3 cups) | 1 |
| roma tomatoes, seeded and chopped 1/4-inch | 2 |
| roma tomatoes, seeded and chopped into 1-inch pieces | 1 |
| roma tomatoes, seeded and diced | 16 |
| roma tomatoes, seeded and finely diced | 1 |
| roma tomatoes, seeded and roughly chopped | 1 |
| roma tomatoes, seeded and small diced | 2 |
| roma tomatoes, seeds removed and diced | 2 |
| roma tomatoes, skinned, seeded, cut into 1/4-inch pieces | 1 |
| roma tomatoes, small diced | 1 |
| roma tomatoes, split and oven dried | 1 |
| roma tomatoes, squeezed and roughly diced | 1 |
| roma tomatoes, strained | 1 |
| roma tomatoes, thick sliced | 1 |
| roma tomatoes, thickly sliced | 2 |
| roma tomatoes, thinly sliced | 10 |
| roma tomatoes, thinly sliced plus 2 tomato | 1 |
| roma tomatoes, thinly sliced, or halved, seeded, and diced | 1 |
| roma tomatoes, tops trimmed and halved | 1 |
| romaine lettuce and sliced tomato, for topping | 1 |
| room temperature tomato juice | 1 |
| rosso bruno tomatoes, cored and diced | 1 |
| rotelle extra hot diced tomato | 1 |
| rough chopped red tomato | 1 |
| roughly chopped green tomato | 1 |
| roughly chopped marinated sun-dried tomato | 3 |
| roughly chopped oil packed sun-dried tomato | 1 |
| roughly chopped peeled tomato | 1 |
| roughly chopped raw vegetables (i like a combination of carrots, red onions, cucumbers, tomatoes, green or red bell peppers, and zucchini) | 1 |
| roughly chopped ripe tomato | 2 |
| roughly chopped sun-dried tomato | 1 |
| roughly chopped sun-dried tomatoes (not oil-packed) | 1 |
| roughly chopped tomato | 1 |
| round, ripe tomato | 2 |
| rounded tablespoon tomato paste | 2 |
| rounded tablespoon tomato paste* | 1 |
| rounded tablespoons tomato paste | 3 |
| saffron-tomato rice, recipe follows | 1 |
| salt (if using no-salt-added tomatoes), or to taste | 1 |
| salt and freshly ground black pepper, plus coarse sea salt and cracked black pepper, for tomato | 1 |
| salt-free tomato sauce | 1 |
| salted tomato slices, for topping | 1 |
| san marzano style tomato | 1 |
| san marzano tomato | 4 |
| san marzano tomato puree | 2 |
| san marzano tomato sauce | 1 |
| san marzano tomatoes, drained | 1 |
| san marzano tomatoes, hand crushed | 2 |
| sandwich wraps, sundried tomato flavor | 1 |
| sausage, tomato, and artichoke heart, recipe follows | 1 |
| sauteed green tomato | 1 |
| sauteed peas and tomatoes, recipe follows | 1 |
| sauteed zucchini and tomatoes, recipe follows | 1 |
| scant 1/2 cup (100 grams) handcrushed tomato | 1 |
| scant cup cherry tomatoes, halved | 1 |
| scant cup diced plum tomato | 1 |
| seasoned tomato juice, such as v8 | 1 |
| seasoned tomato sauce | 3 |
| seeded 1/2-inch diced tomato | 1 |
| seeded and chopped cherry tomato | 1 |
| seeded and chopped plum tomato | 1 |
| seeded and chopped roma tomato | 1 |
| seeded and chopped tomato | 4 |
| seeded and chopped tomato (about 1 large tomato) | 1 |
| seeded and chopped tomatoes (about 1/2 pound) | 1 |
| seeded and diced green tomato | 1 |
| seeded and diced heirloom tomato | 1 |
| seeded and diced plum tomatoes, including juices | 1 |
| seeded and diced ripe plum tomato | 1 |
| seeded and diced roma (plum) tomato | 1 |
| seeded and diced roma tomato | 2 |
| seeded and diced roma tomato, for garnish | 1 |
| seeded and diced tomato | 8 |
| seeded and diced tomatoes, including any juices | 1 |
| seeded and finely chopped firm ripe plum or vine-ripened tomato | 1 |
| seeded and finely chopped tomato | 4 |
| seeded and finely diced roma tomatoes (about 4) | 1 |
| seeded and sliced tomato | 1 |
| seeded and small diced tomato | 1 |
| seeded chopped ripe tomato | 1 |
| seeded chopped tomato | 3 |
| seeded chopped tomatoes (from 2 tomatoes) | 1 |
| seeded diced firm ripe tomato | 1 |
| seeded diced plum (roma) tomato | 1 |
| seeded diced tomato | 2 |
| seeded tomato | 1 |
| seeded, and coarsely chopped tomato | 1 |
| seedless tomatoes, quartered | 1 |
| serving suggestion: all-purpose tomato sauce, such as anne's marinara sauce | 1 |
| serving suggestion: creamy tomato soup, recipe follows | 1 |
| serving suggestion: green bean salad and a tomato - basil salad | 1 |
| serving suggestion: lettuce leaves and sliced tomato | 1 |
| serving suggestion: serve with roasted tomatoes and peasant bread | 1 |
| serving suggestion: tomato salad drizzled with olive oil | 1 |
| serving suggestion: warmed tomato-basil sauce | 1 |
| serving suggestions: chopped fresh cilantro, halved cherry tomatoes, avocado wedges, queso fresco, tortillas and grilled corn | 1 |
| serving suggestions: green leaf lettuce, halved cherry tomatoes, thinly sliced red onions, shredded carrots and sliced celery | 1 |
| serving suggestions: lettuce, tomato slices and red onion slices | 1 |
| serving suggestions: pitas, lettuce, tomato and sesame sauce | 1 |
| serving suggestions: rolls with ketchup, tomato, fried onions, feta cheese | 1 |
| serving suggestions: serve with tomato relish and zucchini (recipes follow). piling the relish and the chicken in a warm pita is a fun way to combine the flavors and textures of the 2 recipes | 1 |
| serving suggestions: shredded lettuce, pickles and tomato | 1 |
| serving suggestions: steamed haricot verts (french green beans) or asparagus along with wedges of ripe tomato, halved pitted black olives, snipped chives and chopped parsley | 1 |
| serving suggestions: toasted piece of baguette or fresh tomato-basil sauce | 1 |
| serving suggestions: whole wheat wraps, lettuce, tomato and avocado | 1 |
| several tomato | 2 |
| shot (1-ounce or 2 tablespoons) fresh tomato juice | 1 |
| shot (3 tablespoons) fresh tomato juice | 1 |
| shot tomato juice | 1 |
| shredded iceberg lettuce and sliced tomatoes, for serving | 1 |
| shredded lettuce and chopped tomatoes, avocado and/or radishes, for topping | 1 |
| shredded lettuce and diced tomatoes, for garnish | 1 |
| shredded lettuce and tomato slices | 1 |
| shredded lettuce, thinly sliced tomatoes and hot sauce, for serving | 1 |
| simple and quick tomato sauce, to serve, recipe follows | 1 |
| simple tomato sauce of choice | 1 |
| simple tomato sauce, for serving | 1 |
| simple tomato sauce, recipe follows | 2 |
| simple tomato sauce, recipe follows or jarred marinara sauce, warmed | 1 |
| simple tomato sauce, recipe follows, or purchased marinara sauce | 1 |
| simple tomato sauce, recipe follows, or store-bought marinara sauce | 2 |
| six 1/2-inch-thick tomato slices | 1 |
| skinned whole tomato | 1 |
| skinned, seeded and diced tomato | 1 |
| slice beefsteak tomato | 2 |
| slice fresh tomato | 1 |
| slice tomato | 9 |
| sliced avocado and tomato, for topping | 1 |
| sliced avocado, fresh tomato salsa, cilantro, and lime wedges (for serving) | 1 |
| sliced beefsteak or vine ripe tomato, for topping | 1 |
| sliced cherry tomato | 3 |
| sliced drained oil-packed sun-dried tomato | 3 |
| sliced grape tomato | 1 |
| sliced green tomato | 2 |
| sliced heirloom tomatoes (we like using a mix of colors) | 1 |
| sliced heirloom tomatoes, to serve | 1 |
| sliced large tomato | 1 |
| sliced oil-packed sun-dried tomato | 1 |
| sliced oil-packed sun-dried tomatoes, 2 tablespoons oil reserved | 1 |
| sliced oil-packed sun-dried tomatoes, plus more for garnish | 1 |
| sliced plum tomato | 2 |
| sliced plum tomatoes and baby arugula, for topping | 1 |
| sliced plum tomatoes, for garnish | 2 |
| sliced plum tomatoes, for topping | 1 |
| sliced plum tomatoes, fresh basil, olive oil, crema (or sour cream) | 1 |
| sliced red onion and sliced yellow and plum tomato | 1 |
| sliced red onion, tomato and avocado, for serving | 1 |
| sliced ripe beefsteak tomato | 1 |
| sliced ripe tomato | 1 |
| sliced ripe tomatoes, for garnish | 1 |
| sliced roma tomato | 4 |
| sliced roma tomatoes, for topping | 1 |
| sliced sun-dried tomato | 2 |
| sliced sun-dried tomatoes (not oil-packed) | 1 |
| sliced sun-dried tomatoes (packed in oil) | 1 |
| sliced sun-dried tomatoes, drained (packed in oil) | 1 |
| sliced tomato | 34 |
| sliced tomato (optional) | 1 |
| sliced tomato, cucumber, lettuce, red onion and some plain yogurt | 1 |
| sliced tomato, cucumber, lettuce, red onion, and some plain yogurt, for serving | 1 |
| sliced tomato, for garnish | 1 |
| sliced tomato, for serving | 2 |
| sliced tomatoes (optional) | 1 |
| sliced tomatoes and thinly sliced red onion | 1 |
| sliced tomatoes drizzled with cracked black pepper garnish, recipe follows | 2 |
| sliced tomatoes, arugula | 1 |
| sliced tomatoes, for serving | 5 |
| sliced tomatoes, for topping | 2 |
| sliced vine-ripe tomato | 1 |
| sliced, reconstituted sun-dried tomato | 1 |
| slices (1/4-inch-thick) tomato | 1 |
| slices beefsteak or heirloom tomato | 1 |
| slices beefsteak tomato | 17 |
| slices beefsteak tomato (optional) | 1 |
| slices beefsteak tomatoes, for serving | 1 |
| slices brioche or potato bread yellow and red tomato | 1 |
| slices chopped tomato | 1 |
| slices cocktail tomatoes (2 per sandwich) | 1 |
| slices firm tomato | 1 |
| slices fresh tomato | 1 |
| slices green tomato | 3 |
| slices green tomato, 3/4 to 1-inch thick (about 2 medium green tomatoes) | 1 |
| slices greentomatoes, 1/2-inch thick (about 3 green tomatoes) | 1 |
| slices heirloom tomato | 1 |
| slices heirloom tomato (from about 1 large) | 1 |
| slices heirloom tomato, for serving | 1 |
| slices juicy red tomato | 1 |
| slices large beefsteak tomato | 1 |
| slices large tomato, each 1/4-inch thick | 1 |
| slices large vine-ripe tomato | 1 |
| slices of monterey jack cheese, lettuce, tomato, onion, avocado, red onion, etc | 1 |
| slices of plum tomato | 1 |
| slices of tomato | 2 |
| slices of white bread, lettuce and tomato, for making sandwiches | 1 |
| slices plum (roma) tomatoes (about 6 medium) | 1 |
| slices plum tomato | 1 |
| slices red beefsteak tomato | 1 |
| slices red tomato | 4 |
| slices red-ripe plum tomato | 1 |
| slices ripe costoluto genovese tomatoes or other ripe red heirloom tomato | 1 |
| slices ripe large tomato, such as beefsteak | 1 |
| slices ripe red tomato | 1 |
| slices ripe tomato | 12 |
| slices ripe tomatoes (about 3 small) | 1 |
| slices ripe, red beefsteak tomato | 1 |
| slices roma (plum) tomato | 2 |
| slices roma tomato | 2 |
| slices tomato | 75 |
| slices tomato (1/2-inch thick) | 1 |
| slices tomato (about 2 tomatoes) | 1 |
| slices tomato (from 2 to 3 tomatoes) | 1 |
| slices tomato (optional) | 2 |
| slices tomato slices | 2 |
| slices tomato, 1/2-inch thick | 1 |
| slices tomato, 1/4-inch thick | 2 |
| slices tomato, about 2 medium tomato | 1 |
| slices tomato, cut thin (or 4 large slices, depending on how big your tomato is) | 1 |
| slices tomato, halved | 1 |
| slices tomato, or to taste | 1 |
| slices vine ripe tomato | 2 |
| slices vine-ripe beefsteak tomatoes, cut into half moons | 1 |
| slices vine-ripened tomato | 4 |
| slicing tomatoes, quartered (about 3 pounds) | 2 |
| slivered reconstitituted sundried tomato | 1 |
| slivered sun-dried tomato | 1 |
| slow roasted tomato sauce, recipe follows | 1 |
| slow roasted tomatoes, halved (recipe follows) | 1 |
| slow-braised tomato | 1 |
| small (1 1/2- to 2-inch) tomatoes (preferably campari), halved | 1 |
| small (2 1/2-inch-wide) tomato | 1 |
| small (2- to 2 1/2-inch) tomatoes (not plum tomatoes) | 1 |
| small (6-ounce) can tomato paste | 1 |
| small (8-ounce) can tomato sauce | 1 |
| small (about 1 1/4 pounds) roma tomato | 1 |
| small (about 2" diameter) tomato | 1 |
| small beefsteak tomatoes (about 2 pounds), halved crosswise | 1 |
| small can (12 ounces) peeled crushed tomatoes (or 1 pound fresh tomato | 1 |
| small can chopped tomato | 1 |
| small can diced tomato | 1 |
| small can tomato paste | 11 |
| small can tomato puree | 1 |
| small can tomato sauce | 1 |
| small cans (14 to 16 ounces each) whole tomatoes including juice | 1 |
| small cans (4-ounce) tomato sauce | 1 |
| small cans tomato paste | 1 |
| small cherry or grape tomato | 1 |
| small cherry or grape tomatoes, halved (about 5 ounces) | 1 |
| small cherry tomato | 3 |
| small cherry tomatoes (1 lb; preferably sungold), halved lengthwise | 1 |
| small cherry tomatoes (about 1 pint), halved | 1 |
| small cherry tomatoes (about 35) | 1 |
| small cherry tomatoes (such as sweet 100) | 1 |
| small cherry tomatoes (such as sweet 100s) or teardrop tomato | 1 |
| small cherry tomatoes on the vine (optional) | 1 |
| small cherry tomatoes or grape tomato | 1 |
| small cherry tomatoes, for garnish | 1 |
| small cherry tomatoes, halved | 4 |
| small cherry tomatoes, stemmed | 1 |
| small chopped tomato | 2 |
| small cocktail tomatoes (about 10 ounces), quartered | 1 |
| small colorful tomatoes (cherry/grape/heirloom) | 1 |
| small container cherry tomato | 2 |
| small dice tomato | 1 |
| small diced plum tomato | 1 |
| small diced roma tomato | 1 |
| small diced tomato | 1 |
| small diced vine-ripe red tomato | 1 |
| small firm cherry tomatoes (about 8 ounces), stemmed | 1 |
| small firm tomato, seeded and 1/4-inch diced, for garnish | 1 |
| small fresh tomato | 2 |
| small grape or cherry tomatoes, quartered | 1 |
| small green (unripe) tomato, seeded and finely chopped | 1 |
| small heirloom tomato | 1 |
| small heirloom tomatoes (about 8 ounces total), cored, cut into thin wedges | 1 |
| small heirloom tomatoes, cut into quarters | 1 |
| small heirloom tomatoes, halved or cut into wedges | 1 |
| small jar (6 to 8 ounces) sun-dried tomatoes in oil | 1 |
| small onion, chopped1can (10 3/4 ounce) condensed tomato soup | 1 |
| small or 1 large tomato (8 ounces) | 1 |
| small or 2 large juicy, vine-ripened tomato | 1 |
| small or 2 large ripe tomatoes, seeded and inner flesh removed, julienned | 1 |
| small pear tomatoes, halved lengthwise | 1 |
| small plum tomato | 8 |
| small plum tomato, cored and finely chopped | 1 |
| small plum tomato, halved lengthwise | 1 |
| small plum tomato, seeded and diced | 2 |
| small plum tomato, seeded and diced, for garnish | 1 |
| small plum tomato, seeded and finely chopped | 2 |
| small plum tomatoes, cut into 1/2-inch slices | 1 |
| small plum tomatoes, cut into 12 slices | 1 |
| small plum tomatoes, halved and seeded | 1 |
| small plum tomatoes, seeded | 2 |
| small plum tomatoes, seeded and chopped | 5 |
| small red and yellow cherry, pear, or grape tomatoes, halved | 1 |
| small red tomatoes, cut into wedges | 1 |
| small red, ripe tomato | 1 |
| small red, yellow, and orange cherry tomatoes, halved | 1 |
| small red-ripe tomato | 1 |
| small ripe tomato | 8 |
| small ripe tomato, quartered | 1 |
| small ripe tomatoes (about 1/2 pound) | 1 |
| small ripe tomatoes, halved | 1 |
| small ripe tomatoes, seeded and diced | 1 |
| small ripe tomatoes, skinned, seeded, and chopped (skin reserved for garnish) | 1 |
| small roma (plum) tomato | 2 |
| small roma tomato | 4 |
| small roma tomato, quartered | 1 |
| small round tomatoes (about 2 1/2 inches in diameter; 2 1/2 lb total) | 1 |
| small seeded and chopped tomato | 1 |
| small sun gold or cherry tomatoes, halved | 1 |
| small to medium sized vine ripened tomatoes, cut into 1/2-inch pieces | 1 |
| small to medium tomato, cored and finely chopped, or 1 cup cherry tomatoes, cut in half | 1 |
| small to medium vine ripe tomato | 1 |
| small tomato | 98 |
| small tomato, cut into 1/3-inch-thick slices | 1 |
| small tomato, cut into 1/4-inch dice | 1 |
| small tomato, cut into 4 slices | 2 |
| small tomato, cut into small dice | 1 |
| small tomato, cut into wedges | 2 |
| small tomato, halved | 2 |
| small tomato, halved and seeded | 1 |
| small tomato, halved, seeded and finely diced | 1 |
| small tomato, seeded | 3 |
| small tomato, seeded and chopped | 4 |
| small tomato, seeded and cut into 1/4-inch dice | 1 |
| small tomato, seeded and cut into tiny dice | 1 |
| small tomato, seeded and diced | 4 |
| small tomato, seeded and diced fine | 1 |
| small tomato, thinly sliced | 1 |
| small tomatoes (4 medium) | 1 |
| small tomatoes (about 1 1/2 pounds), cut crosswise into 1/4-inch-thick slices | 1 |
| small tomatoes (about 1 1/4 pounds) | 1 |
| small tomatoes (about 8), cut into wedges | 1 |
| small tomatoes - peeled, seeded and chopped | 1 |
| small tomatoes on the vine | 1 |
| small tomatoes such as campari or baby roma (about 2 inches wide) | 1 |
| small tomatoes, blanched and peeled | 1 |
| small tomatoes, cored and chopped | 1 |
| small tomatoes, cored, halved, thinly sliced | 1 |
| small tomatoes, cubed | 1 |
| small tomatoes, cut into 1/2-inch-thick wedges | 1 |
| small tomatoes, cut into 1/4-inch rounds | 1 |
| small tomatoes, cut into chunks | 1 |
| small tomatoes, cut into wedges | 4 |
| small tomatoes, cut into wedges (optional) | 1 |
| small tomatoes, cut into wedges, for garnish | 1 |
| small tomatoes, each cut into 8 wedges | 1 |
| small tomatoes, halved or whole | 1 |
| small tomatoes, like pear or cherry | 1 |
| small tomatoes, preferably heirloom, cut into 1/2" wedges | 1 |
| small tomatoes, preferably italian plum | 1 |
| small tomatoes, quartered | 2 |
| small tomatoes, quartered lengthwise, seeded, and cut into 1/4-inch-thick strips | 1 |
| small tomatoes, roasted (see note) | 1 |
| small tomatoes, seeded | 1 |
| small tomatoes, seeded and chopped | 4 |
| small tomatoes, seeded and sliced | 1 |
| small tomatoes, thinly sliced | 2 |
| small tomatoes, washed and cored and sliced | 1 |
| small vine ripe tomato | 1 |
| small vine ripe tomatoes with stem | 1 |
| small vine ripe tomatoes, seeded and diced | 2 |
| small vine ripened tomatoes, halved | 1 |
| small vine ripened tomatoes, seeded and cut into 1 inch chunks | 1 |
| small vine-ripe tomato | 2 |
| small vine-ripened tomato | 6 |
| small vine-ripened tomato, quartered | 1 |
| small vine-ripened tomatoes (about 1 pound) | 1 |
| small vine-ripened tomatoes, seeded and cut into 1/4-inch dice | 1 |
| small vine-ripened yellow tomatoes, cut into wedges | 1 |
| small yellow tomatoes, cored, seeded and chopped | 1 |
| small yellow tomatoes, seeded and chopped | 1 |
| small, ripe tomato, cut into 1/4-inch thick slices | 1 |
| small-diced roma tomato | 1 |
| small-diced tomato | 1 |
| smoked plum tomatoes, recipe follows | 1 |
| smoked sun-dried tomatoes or regular sun-dried tomatoes (not packed in oil), thinly sliced | 1 |
| smoked tomato beurre blanc, recipe follows | 1 |
| smoked tomato essence, recipe follows | 1 |
| smoked tomato ketchup, recipe follows | 1 |
| smoked tomato puree | 1 |
| smoked tomato puree, recipe follows | 1 |
| smoked tomato relish, recipe follows | 1 |
| smoked tomato vinaigrette, recipe follows | 2 |
| smooth tomato sauce, recipe follows | 1 |
| smothered okra and tomatoes, for service | 1 |
| soft dried tomatoes (not packed in oil), cut crosswise into 1/8-inch-thick slices | 1 |
| soft sun-dried tomato | 3 |
| soft sun-dried tomatoes (not packed in oil), cut into thin slivers | 1 |
| soup reserved from tomato soup recipe | 1 |
| sour cream and chopped fresh tomatoes for topping | 1 |
| sour cream and diced tomato, for topping | 1 |
| sour tomato | 1 |
| spaghetti sauce, or pesto, or green olive puree or chopped sun-dried tomatoes or chopped roasted | 1 |
| spanish style tomato sauce | 1 |
| special equipment: kitchen shears; 2 (10-inch) heavy skillets (one well-seasoned cast-iron or heavy nonstick); a 10-inch round of parchment paper; 5 to 6 lb of weights such as 3 (28-oz) cans of tomato | 1 |
| spicy smoked tomato mayonnaise, recipe follows | 1 |
| spicy tomato broth, warmed, recipe follows | 1 |
| spicy tomato juice | 2 |
| spicy tomato juice, such as spicy hot v-8 juice | 1 |
| spicy tomato relish, recipe follows | 1 |
| spicy tomato salsa with cilantro and chiles , or storebought tomato salsa | 1 |
| spicy tomato sauce | 2 |
| spicy tomato sauce (recipe follows) | 1 |
| spicy tomato sauce, recipe follows | 1 |
| spicy tomato-basil sauce | 1 |
| spicy tomato-cheese soup, recipe follows | 1 |
| spicy tomato-vegetable juice cocktail (e.g., v-8) | 2 |
| spicy tomato-vegetable juice cocktail (such as v8®) (optional) | 1 |
| spicy vegetable juice (such as spicy hot v-8) or spicy tomato juice | 1 |
| spicy vegetable juice or spicy tomato juice | 1 |
| spinach or sun-dried tomato flavored flour tortilla wraps | 1 |
| stems cherry tomatoes on the vine (3 to 4 pounds) | 1 |
| stewed italian tomatoes, s&w | 1 |
| stewed tomato | 19 |
| stewed tomatoes and whipped potatoes, for serving | 1 |
| stewed tomatoes or canned plum tomatoes, broken up | 1 |
| stewed tomatoes with chiles | 1 |
| stewed tomatoes, 28 ounces | 1 |
| stewed tomatoes, mexican flavor if possible | 1 |
| stewed tomatoes, recipe follows | 1 |
| store bought sun-dried tomato pesto | 1 |
| store bought tomato salsa, your favorite brand and flavor | 1 |
| store-bought gluten-free tomato sauce | 1 |
| store-bought or homemade tomato sauce | 1 |
| store-bought tomato sauce | 1 |
| strained plum roma tomato | 1 |
| strained tomato | 1 |
| strained tomato purée | 1 |
| strained tomatoes (such as pomì) | 1 |
| strawberry tomatoes, halved | 1 |
| stuffed tomato | 1 |
| sugar (to take the acidity off the tomatoes) | 2 |
| suggested servings: sliced tomato and cucumbers | 1 |
| summer tomato relish, recipe follows | 1 |
| sun dried tomato | 6 |
| sun dried tomato pesto | 2 |
| sun dried tomatoes (in oil) | 1 |
| sun dried tomatoes in oil, drained and coarsely chopped | 1 |
| sun dried tomatoes in oil, drained and sliced | 1 |
| sun dried tomatoes packed in oil | 1 |
| sun dried tomatoes, as many as you like | 1 |
| sun dried tomatoes, julienne | 1 |
| sun dried tomatoes, packed in olive oil | 1 |
| sun gold or cherry tomato | 2 |
| sun gold or cherry tomatoes, halved | 1 |
| sun gold tomatoes, halved | 1 |
| sun gold tomatoes, halved (substitute: any yellow cherry tomato) | 1 |
| sun-dried tomato | 103 |
| sun-dried tomato (in olive oil) | 1 |
| sun-dried tomato and basil vinaigrette, recipe follows | 1 |
| sun-dried tomato and oregano salad dressing | 1 |
| sun-dried tomato basil tortilla wraps | 1 |
| sun-dried tomato basil wraps | 1 |
| sun-dried tomato chutney, recipe follows | 1 |
| sun-dried tomato cream sauce, recipe follows | 1 |
| sun-dried tomato dressing | 1 |
| sun-dried tomato dressing, recipe follows | 1 |
| sun-dried tomato half | 5 |
| sun-dried tomato halves (about 3/4 cup) | 1 |
| sun-dried tomato halves (not packed in oil), soaked in hot water until tender, then drained and chopped | 1 |
| sun-dried tomato halves in oil, drained and chopped | 1 |
| sun-dried tomato halves in oil, drained and coarsely chopped | 1 |
| sun-dried tomato halves packed in oil, drained and coarsely chopped | 1 |
| sun-dried tomato halves packed in olive oil with herbs, cut into strips | 1 |
| sun-dried tomato halves packed in olive oil, drained, and coarsely chopped | 1 |
| sun-dried tomato halves, thinly sliced | 1 |
| sun-dried tomato oil | 1 |
| sun-dried tomato paste | 7 |
| sun-dried tomato pesto | 9 |
| sun-dried tomato phyllo cups (available at gourmet stores) | 1 |
| sun-dried tomato puree | 1 |
| sun-dried tomato salad dressing | 1 |
| sun-dried tomato slices for garnish | 1 |
| sun-dried tomato spread | 1 |
| sun-dried tomato spread or tapenade | 1 |
| sun-dried tomato tapenade | 1 |
| sun-dried tomato tapenade, recipe follows | 1 |
| sun-dried tomato vinaigrette | 1 |
| sun-dried tomato wraps or tortillas | 1 |
| sun-dried tomato, blanched | 1 |
| sun-dried tomatoes (about 1 ounce; not oil-packed), thinly sliced | 1 |
| sun-dried tomatoes (about 8 pieces, do not used oil-packed variety) | 1 |
| sun-dried tomatoes (do not use oil-packed) | 1 |
| sun-dried tomatoes (dry-packed) | 1 |
| sun-dried tomatoes (from a jar, or if dehydrated soaked in warm water) | 1 |
| sun-dried tomatoes (not in oil) | 1 |
| sun-dried tomatoes (not oil packed) | 1 |
| sun-dried tomatoes (not oil-packed) | 1 |
| sun-dried tomatoes (not packed in oil) | 5 |
| sun-dried tomatoes (not packed in oil), snipped into small pieces | 2 |
| sun-dried tomatoes (not packed in oil), soaked in hot water for 5 minutes and drained well | 2 |
| sun-dried tomatoes (not packed in oil, about 10) | 1 |
| sun-dried tomatoes (not packed in oil, about 30), soaked in hot water for 5 minutes and drained well, reserving 3 tablespoons of the soaking liquid | 1 |
| sun-dried tomatoes (not packed in oil; 1 1/2 ounces) | 1 |
| sun-dried tomatoes (not packed in oil; not rehydrated) | 1 |
| sun-dried tomatoes (oil-packed or re-hydrated in water if dry packed), cut into 1/4-inch pieces | 1 |
| sun-dried tomatoes (optional) | 1 |
| sun-dried tomatoes (packed in olive oil) | 1 |
| sun-dried tomatoes and potatoes, as an accompaniment, recipe follows | 1 |
| sun-dried tomatoes cut into strips | 1 |
| sun-dried tomatoes from a jar | 1 |
| sun-dried tomatoes in oil | 8 |
| sun-dried tomatoes in oil (drained) | 1 |
| sun-dried tomatoes in oil, cut into 1/2-inch dice | 1 |
| sun-dried tomatoes in oil, drained | 4 |
| sun-dried tomatoes in oil, drained and chopped | 4 |
| sun-dried tomatoes in oil, drained and chopped (8 tomatoes) | 1 |
| sun-dried tomatoes in oil, drained and finely chopped | 2 |
| sun-dried tomatoes in oil, drained and julienned | 1 |
| sun-dried tomatoes in oil, drained and small-diced | 1 |
| sun-dried tomatoes in oil, drained and thinly sliced | 1 |
| sun-dried tomatoes in oil, drained and thinly sliced (about 1/4 cup) | 1 |
| sun-dried tomatoes in oil, drained well | 1 |
| sun-dried tomatoes in oil, drained, 10 to 12 pieces | 1 |
| sun-dried tomatoes in oil, drained, oil reserved, julienned | 1 |
| sun-dried tomatoes in oil, drained, reserving 2 tablespoons of the oil | 1 |
| sun-dried tomatoes in oil, plus 1 tablespoon oil from jar | 1 |
| sun-dried tomatoes in olive oil | 1 |
| sun-dried tomatoes in olive oil, drained | 1 |
| sun-dried tomatoes in olive oil, drained and chopped | 1 |
| sun-dried tomatoes packed in oil | 8 |
| sun-dried tomatoes packed in oil or if de-hydrated soaked in | 1 |
| sun-dried tomatoes packed in oil, drained | 3 |
| sun-dried tomatoes packed in oil, drained and chopped | 6 |
| sun-dried tomatoes packed in oil, drained and cut into strips | 1 |
| sun-dried tomatoes packed in oil, drained and diced | 2 |
| sun-dried tomatoes packed in oil, drained and finely chopped | 1 |
| sun-dried tomatoes packed in oil, drained and sliced | 1 |
| sun-dried tomatoes packed in oil, drained and thinly sliced | 1 |
| sun-dried tomatoes packed in oil, drained and very thinly sliced | 1 |
| sun-dried tomatoes packed in oil, drained, reserving 2 tomatoes whole for garnish, and the remaining tomatoes minced | 1 |
| sun-dried tomatoes packed in oil, drained,rinsed and roughly chopped | 1 |
| sun-dried tomatoes packed in oil, well-drained | 1 |
| sun-dried tomatoes packed in oil; 1 tbsp. plus 2 tsp. of oil | 1 |
| sun-dried tomatoes packed in olive oil | 3 |
| sun-dried tomatoes packed in olive oil with garlic, drained and chopped | 1 |
| sun-dried tomatoes packed in olive oil, drained and cut into thin strips | 1 |
| sun-dried tomatoes, (not oil-packed) | 1 |
| sun-dried tomatoes, 5 or 6 pieces (not in oil, available in produce department, packaged in pouches) | 1 |
| sun-dried tomatoes, cut in thin strips | 1 |
| sun-dried tomatoes, cut into 1-inch pieces if large | 1 |
| sun-dried tomatoes, cut into 1/8-inch julienne matchsticks | 1 |
| sun-dried tomatoes, cut into pieces | 1 |
| sun-dried tomatoes, cut into strips | 2 |
| sun-dried tomatoes, cut into thin strips | 1 |
| sun-dried tomatoes, drained | 1 |
| sun-dried tomatoes, drained (about 3/4 cup) | 1 |
| sun-dried tomatoes, drained and chopped | 2 |
| sun-dried tomatoes, drained and finely chopped | 1 |
| sun-dried tomatoes, drained and minced | 1 |
| sun-dried tomatoes, drained and thinly sliced | 3 |
| sun-dried tomatoes, drained well and roughly chopped | 1 |
| sun-dried tomatoes, halved | 1 |
| sun-dried tomatoes, in oil | 1 |
| sun-dried tomatoes, in oil, drained | 1 |
| sun-dried tomatoes, julienned | 2 |
| sun-dried tomatoes, packed in oil | 3 |
| sun-dried tomatoes, packed in oil or if dehydrated soaked in water to rehydrate | 1 |
| sun-dried tomatoes, packed in oil, cut into 1/2-inch cubes | 1 |
| sun-dried tomatoes, packed in oil, drained | 1 |
| sun-dried tomatoes, packed in oil, drained and chopped | 1 |
| sun-dried tomatoes, packed in oil, drained and julienned | 1 |
| sun-dried tomatoes, packed in oil, drained and oil reserved | 1 |
| sun-dried tomatoes, packed in olive oil finely chopped | 1 |
| sun-dried tomatoes, packed without oil | 2 |
| sun-dried tomatoes, plus 1 tablespoon finely diced | 1 |
| sun-dried tomatoes, preferably not oil-packed | 2 |
| sun-dried tomatoes, quartered | 1 |
| sun-dried tomatoes, re-hydrated and chopped | 1 |
| sun-dried tomatoes, reconstituted either in olive oil or white wine | 1 |
| sun-dried tomatoes, reconstituted in boiling water for 10 minutes | 1 |
| sun-dried tomatoes, rehydrated | 1 |
| sun-dried tomatoes, rehydrated in warm poaching liquid for 1 hour | 1 |
| sun-dried tomatoes, rehydrated in water | 2 |
| sun-dried tomatoes, rehydrated or packed in oil | 1 |
| sun-dried tomatoes, soaked in 1 cup hot water for 30 minutes, then drained and julienned | 1 |
| sun-dried tomatoes, soaked in 1/2 cup boiling water | 1 |
| sun-dried tomatoes, soaked in hot water for 10 minutes and drained | 1 |
| sun-dried tomatoes, soaked in hot water, drained, and julienne | 1 |
| sun-dried tomatoes, soaked in warm water and halved | 1 |
| sun-dried tomatoes, soaked in water for 2 hours (1 cup soaking water reserved) | 1 |
| sun-dried tomatoes, thinly sliced | 2 |
| sun-dried tomatoes, thinly sliced, plus more for topping | 1 |
| sun-dried tomatoes, very finely diced | 1 |
| sun-dried tomatoes, with oil from jar | 1 |
| sunday ragu, recipe above, or other tomato sauce | 1 |
| sundried tomato | 5 |
| sundried tomato half | 1 |
| sundried tomato paste | 1 |
| sundried tomato pesto, or approximately 1/3 cup rehydrated sundried tomato | 1 |
| sundried tomato pieces, marinated in olive oil | 1 |
| sundried tomato-chardonnay sauce, recipe follows | 1 |
| sundried tomatoes (about 8 pieces do not use the oilpacked type) | 1 |
| sundried tomatoes and spinach salad | 1 |
| sundried tomatoes in oil, plus 1 tablespoon flavored oil from the jar | 1 |
| sundried tomatoes not in oil (about 14) | 1 |
| sundried tomatoes packed in oil, drained and diced | 1 |
| sundried tomatoes, blanched | 1 |
| sundried tomatoes, in oil | 1 |
| sundried tomatoes, packed in oil | 1 |
| sundried tomatoes, packed in olive oil | 1 |
| sundried tomatoes, pureed | 1 |
| sundried tomatoes, soaked 1/2 hour in warm water | 1 |
| sundried tomatoes, soaked for 15 minutes in hot water | 1 |
| sundried tomatoes, thinly chopped | 1 |
| sundried tomatoes, washed in warm water, cut 1/2 by 1/4inch pieces | 1 |
| sweet 100 cherry tomatoes, cut in half | 1 |
| sweet 100 tomato | 1 |
| sweet 100 tomatoes, cut ½, 1 cup | 1 |
| sweet 100 tomatoes, halved | 2 |
| sweet 100's tomatoes, halved | 1 |
| sweet and sour tomato jam, recipe follows | 1 |
| sweet and tangy roasted tomato | 1 |
| sweet cherry tomatoes, halved | 1 |
| sweet grape tomato | 1 |
| sweet kris tomato | 1 |
| sweet ripe tomato | 1 |
| sweet tomato chutney, for serving, recipe follows | 1 |
| sweet tomato petals, recipe follows | 1 |
| sweet tomatoes, halved, or more to taste | 1 |
| szechuan tomato dressing, recipe follows | 1 |
| tablespoons tomato paste | 1 |
| taco salad (chopped lettuce and diced tomatoes, tossed in oil and red wine vinegar) | 1 |
| tangy tomato relish, recipe follows | 1 |
| tarator sauce ; chopped tomatoes; chopped onion; pita bread | 1 |
| tbs. peeled and minced tomato | 1 |
| tbs. tomato puree | 1 |
| tear drop, or grape tomatoes, halved | 1 |
| teardrop or grape tomatoes, halved | 1 |
| teardrop tomatoes, cut in half | 1 |
| teardrop tomatoes, halved lenghtwise | 1 |
| teardrop tomatoes, stemmed | 1 |
| teardrop, or grape tomatoes, halved | 1 |
| tender sun-dried tomatoes (available in pouches or tubs in produce section) | 1 |
| tender sun-dried tomatoes, thinly sliced, available in small pouches in produce department | 1 |
| thick large tomato slices | 1 |
| thick slices beefsteak tomato | 5 |
| thick slices heirloom tomato | 2 |
| thick slices ripe slicing tomato | 1 |
| thick slices ripe tomato (from 2 tomatoes), sauteed until lightly browned | 1 |
| thick slices tomato | 8 |
| thick tomato pasta sauce | 1 |
| thick tomato slices | 1 |
| thick, ripe beefsteak tomato slices | 1 |
| thick-fleshed tomatoes, such as roma | 1 |
| thin plum tomato slices (from 2 to 3 tomatoes) | 2 |
| thin round slices of small tomato | 1 |
| thin slice tomato | 2 |
| thin slices beefsteak tomato | 1 |
| thin slices of ripe tomato | 1 |
| thin slices of tomato | 3 |
| thin slices plum tomato | 1 |
| thin slices red tomato (optional) | 1 |
| thin slices ripe beefsteak tomato | 1 |
| thin slices ripe tomato | 2 |
| thin slices tomato | 9 |
| thin slices tomato and diced tomatoes, for garnish | 1 |
| thin slices tomato, halved to create half moons | 1 |
| thin slices vine-ripened tomato, about 1 large | 1 |
| thin tomato slice | 1 |
| thin tomato slices | 2 |
| thin-sliced tomato | 1 |
| thin-sliced tomato skin, julienned | 1 |
| thinly sliced drained oil-packed sun-dried tomato | 7 |
| thinly sliced grape or cherry tomato | 1 |
| thinly sliced heirloom tomato | 1 |
| thinly sliced oil-packed sun-dried tomato | 1 |
| thinly sliced plum tomatoes, for serving | 1 |
| thinly sliced ripe tomato, for garnish | 1 |
| thinly sliced rounds beefsteak tomato | 2 |
| thinly sliced sun-dried tomato | 1 |
| thinly sliced sun-dried tomatoes, reconstituted | 1 |
| thinly sliced tomatillos or small green tomatoes (about 8 medium) | 1 |
| thinly sliced tomato, for garnish | 1 |
| thinly sliced, halved (half moon shaped), green tomatoes, with any large seeds removed | 1 |
| thinly-sliced cherry tomatoes (4 to 6) | 1 |
| thinly-sliced sun-dried tomato | 2 |
| three 14 1/2-ounce cans diced tomatoes with liquid | 1 |
| three 14-ounce cans crushed tomato | 1 |
| three 14-ounce cans peeled cherry tomato | 1 |
| three 14.5-ounce cans crushed tomato | 1 |
| three 14.5-ounce cans diced (or whole) tomato | 1 |
| three 14.5-ounce cans whole tomatoes with juice | 1 |
| three 15-ounce cans crushed tomato | 6 |
| three 15-ounce cans whole peeled tomatoes (san marzano are best), crushed by hand | 1 |
| three 15-ounce cans whole peeled tomatoes, crushed by hand | 1 |
| three 26.5-ounce boxes strained tomatoes, such as pomi | 1 |
| three 28-ounce cans crushed tomato | 1 |
| three 28-ounce cans italian plum tomatoes, crushed with hands | 1 |
| three 28-ounce cans plum tomato | 1 |
| three 28-ounce cans tomato | 1 |
| three 28-ounce cans whole peeled tomatoes, including liquid | 1 |
| three 28-ounce cans whole san marzano plum tomato | 1 |
| three 28-ounce cans whole tomato | 2 |
| three 7-ounce cans mexican tomato sauce (i use el patobrand) or enchilada sauce | 1 |
| three 8 ounces cans tomato sauce | 1 |
| tin (can) chopped tomato | 2 |
| tinned tomato | 1 |
| tins chopped tomato | 1 |
| tins peeled cherry tomato | 1 |
| tiny cherry-type tomato | 1 |
| to 1 1/2 cups cherry tomatoes, quartered | 1 |
| to 1 1/2 cups tomato juice or vegetable-tomato juice | 1 |
| to 1 1/2 cups tomato sauce | 2 |
| to 1 cup chopped tomato | 1 |
| to 1 cup sundried tomato | 1 |
| to 1 cup tomato juice, if needed | 1 |
| to 1 cup tomato paste | 1 |
| to 1/2 cup chopped tomato | 1 |
| to 1/2 cup sun-dried tomato | 1 |
| to 1/2 cup tomato paste | 1 |
| to 10 cherry tomato | 1 |
| to 10 cherry tomatoes, hand crushed | 1 |
| to 10 heirloom tomato | 1 |
| to 10 plum tomatoes, washed | 2 |
| to 10 small cherry tomatoes, mixed colors | 1 |
| to 10 small cherry tomatoes, quartered | 1 |
| to 12 cherry tomato | 1 |
| to 12 fresh plum tomatoes (approximately 2 to 2 1/2 pounds) | 1 |
| to 12 grape tomatoes, halved | 1 |
| to 12 medium firm tomato | 1 |
| to 12 plum shaped tomatoes, halved and seeded | 2 |
| to 12 slices beefsteak tomato | 1 |
| to 13 ounces cherry tomatoes and/or pear tomato | 1 |
| to 14 large roma or plum tomato | 1 |
| to 14 small vine-ripened tomatoes, quartered | 1 |
| to 15 cherry tomatoes, cut in half | 1 |
| to 15 plum tomato | 1 |
| to 15 slices tomato | 1 |
| to 15 super-ripe plum tomato | 1 |
| to 16 ounces tomato sauce | 1 |
| to 16-ounce can tomato | 1 |
| to 16oz can chopped plum tomatoes (with juice) | 2 |
| to 2 1/2 pounds large red tomato | 1 |
| to 2 cups (33 to 50 cl) homemade tomato sauce, at room temperature | 1 |
| to 2 cups bestquality tomato sauce or marinara sauce (if storebought, embellish with freshly minced garlic and chopped fresh basil leaves) | 1 |
| to 2 cups good olive oil (enough to just cover tomatoes in pan) | 1 |
| to 2 heirloom tomato | 1 |
| to 2 large green tomatoes, ends removed, cut into 4 slices, each 1/2 inch thick | 1 |
| to 2 large tomato | 1 |
| to 2 medium size tomatoes, seeded and small dice | 1 |
| to 2 medium tomato | 1 |
| to 2 pounds cherry tomato | 1 |
| to 2 ripe juicy tomato | 1 |
| to 2 small roma tomatoes, very thinly sliced into rounds | 1 |
| to 2 tablespoons tomato paste or ketchup | 1 |
| to 2 teaspoons purchased sun-dried tomato paste or italian tomato paste | 1 |
| to 20 cherry tomatoes, quartered | 1 |
| to 24 roasted tomatoes, recipe follows | 1 |
| to 28 ounces canned tomato | 1 |
| to 28 roma or beefsteak tomato slices | 1 |
| to 3 1/2 pounds firm but ripe medium tomato | 1 |
| to 3 cans chopped plum tomatoes (32 to 48 ounces total) | 1 |
| to 3 cans chopped tomato | 1 |
| to 3 cups prepared vegetables, such as braised leeks, broccoli, sauteed onions, mushrooms, spinach, peppers, tomato | 1 |
| to 3 cups tomato sauce | 2 |
| to 3 fresh tomato | 3 |
| to 3 heirloom tomato | 3 |
| to 3 heirloom tomatoes, thinly sliced | 1 |
| to 3 large green tomato | 1 |
| to 3 medium tomatoes, cut into 8 (1/2-inch) slices | 1 |
| to 3 plum tomato | 3 |
| to 3 plum tomatoes, cored and cut into small wedges | 3 |
| to 3 pounds assorted heirloom tomato | 1 |
| to 3 red heirloom tomato | 1 |
| to 3 ripe beefsteak tomato | 1 |
| to 3 ripe tomatoes, thinly sliced | 1 |
| to 3 roma tomato | 2 |
| to 3 slices beefsteak tomato | 1 |
| to 3 slices organic tomato | 1 |
| to 3 small cans tomato paste | 2 |
| to 3 small tomato | 2 |
| to 3 tablespoons tomato paste | 3 |
| to 3 tomato | 4 |
| to 3 tomatoes (preferably heirloom), thickly sliced | 1 |
| to 3 tomatoes, depending on type or size | 1 |
| to 3 tomatoes, thinly sliced | 1 |
| to 3/4 cup caramelized onion-tomato jam | 1 |
| to 3/4 cup fresh tomato sauce (or a very good canned one) | 1 |
| to 3/4 cup milled or crushed canned italian plum tomato | 1 |
| to 3/4 cup of jarred tomato-basil sauce, such as giada de laurentiis for target, plus extra for serving | 1 |
| to 30 red or yellow cherry tomatoes, tossed in 1 teaspoon olive oil | 1 |
| to 30 roma tomato | 1 |
| to 32-ounce can whole tomatoes with juice | 1 |
| to 4 cups diced tomato | 1 |
| to 4 green tomato | 1 |
| to 4 handfuls fresh veggies such as sliced tomatoes, arugula/rocket, sorrel, shaved zucchini/courgette, kale, swiss chard, corn, or mushrooms | 1 |
| to 4 heirloom tomato | 1 |
| to 4 heirloom tomatoes, cut into wedges (use different sizes and colors) | 1 |
| to 4 large ripe tomato | 1 |
| to 4 large tomatoes, halved crosswise and cored | 1 |
| to 4 medium ripe tomatoes, quartered | 1 |
| to 4 medium tomato | 2 |
| to 4 medium tomatoes, thinly sliced | 1 |
| to 4 plum tomatoes or 1 (14-ounce) can diced tomatoes or stewed tomato | 1 |
| to 4 ripe plum tomatoes (about 1 pound), cored and cut into chunks | 1 |
| to 4 ripe plum tomatoes, cored and cut into chunks | 1 |
| to 4 ripe red tomatoes quartered through the stem or 12 to 16 ripe full-flavored cherry tomatoes halved through the stem | 1 |
| to 4 ripe tomatoes, thinly sliced | 1 |
| to 4 roma tomato | 1 |
| to 4 sun-dried tomatoes (not packed in oil), plumped 10 minutes in hot water and drained | 1 |
| to 4 thick slices vine-ripened tomato | 1 |
| to 4 tomatoes (about 1 1/2 pounds), cored and roughly chopped | 1 |
| to 4 tomatoes, quartered | 1 |
| to 46 lbs roma-style tomato | 1 |
| to 5 (1/4-inch-thick) slices plum (roma) tomato (about 1 large tomato) | 1 |
| to 5 heirloom tomato | 1 |
| to 5 large, firm, ripe red summer tomatoes, preferably heirloom | 1 |
| to 5 medium tomatoes or 10 to 15 plum tomato | 1 |
| to 5 plum tomatoes, seeded and finely chopped (1 1/2 cups), or 1 1/2 cups chopped drained | 1 |
| to 5 ripe red tomatoes, blended and strained | 1 |
| to 5 sun-dried tomato | 1 |
| to 5 sun-dried tomatoes, packed in oil, cut into small dice (about 1/4 cup) | 1 |
| to 5 very ripe, extra-large or beefsteak tomatoes, cut into 1/2-inch thick slices | 1 |
| to 6 assorted heirloom tomato | 1 |
| to 6 assorted heirloom tomatoes, cut into wedges and various other shapes | 2 |
| to 6 fresh roma tomato | 1 |
| to 6 large beefsteak tomatoes (about 3 pounds total) | 1 |
| to 6 medium plum tomato | 1 |
| to 6 medium-sized early girl tomato | 1 |
| to 6 medium-sized, different colored heirloom tomato | 1 |
| to 6 plum tomato | 3 |
| to 6 ripe medium tomatoes, preferably assorted colors, cut into 1/4-inch slices | 1 |
| to 6 ripe plum tomatoes peeled, seeded and diced | 1 |
| to 6 ripe plum tomatoes, cored, seeded and diced | 1 |
| to 6 roma tomato | 3 |
| to 6 sun-dried tomatoes, oil packed or soaked in water if dehydrated or 2 tablespoons tomato paste | 2 |
| to 6 tablespoons prepared tomato sauce, ketchup or barbecue sauce | 1 |
| to 6 thick slices ripe tomato | 1 |
| to 6 tomatoes, halved | 1 |
| to 7 cherry tomato | 1 |
| to 7 large green tomato | 1 |
| to 7 sun-dried tomato | 1 |
| to 8 cherry tomato | 1 |
| to 8 halves cherry tomato | 1 |
| to 8 medium tomato | 1 |
| to 8 medium very ripe heirloom tomatoes or juicy beefsteak tomatoes, cut into wedges | 1 |
| to 8 plum tomatoes, cored | 1 |
| to 8 ripe plum tomatoes, halved lengthwise, seeded | 1 |
| to 8 ripe tomato | 1 |
| to 8 slices oven-dried tomato | 1 |
| to 8 small tomato | 1 |
| to 8 soft sun-dried tomato | 1 |
| to 8 thin slices tomato | 1 |
| to 8 tomato | 1 |
| to 8 tomatoes, blanched | 1 |
| tomatillo, green chili salsa or chipotle-tomato salsa, your choice | 1 |
| tomato | 1,205 |
| tomato & basil pizza burgers or burgers zesty tomato basil burger | 1 |
| tomato - peeled, seeded and chopped | 1 |
| tomato - peeled, seeded and diced | 1 |
| tomato - peeled, seeded and finely chopped | 1 |
| tomato - peeled, seeded, and chopped | 1 |
| tomato - peeled, seeded, and chopped (optional) | 1 |
| tomato - peeled, seeded, and diced | 1 |
| tomato -- grilled | 1 |
| tomato and artichoke sauce, recipe follows | 1 |
| tomato and avocado salsa, recipe follows | 1 |
| tomato and basil pasta sauce | 1 |
| tomato and basil sauce, store bought or home made, as accompaniment | 2 |
| tomato and clam juice cocktail | 7 |
| tomato and clam juice cocktail (such as clamato®) | 1 |
| tomato and clam juice cocktail (such as clamato®), or as needed | 1 |
| tomato and corn salsaepi:recipelink</epi:recipelink> | 1 |
| tomato and mint salad | 1 |
| tomato and onion salad, as an accompaniment | 1 |
| tomato and onion salad, recipe under this show number: tm1a04 | 1 |
| tomato and pepper coulis: | 1 |
| tomato and pineapple salsa fresca, recipe follows | 1 |
| tomato and red onion chutney | 1 |
| tomato and roasted red pepper aioli, recipe follows | 1 |
| tomato and seasonal greens salad, as an accompaniment, recipe follows | 1 |
| tomato based barbeque sauce | 2 |
| tomato based vegetable juice (recommended: v-8) | 1 |
| tomato basil feta cheese | 1 |
| tomato basil feta cheese, crumbled | 2 |
| tomato basil pasta sauce | 1 |
| tomato bouillon | 2 |
| tomato bredie, recipe follows | 1 |
| tomato broth, whole peeled can tomatoes pureed in blender | 1 |
| tomato cans of water | 2 |
| tomato catsup | 4 |
| tomato chermoula sauce | 1 |
| tomato chile jam, recipe follows | 1 |
| tomato chunks or chunky tomato sauce | 2 |
| tomato chutney | 3 |
| tomato chutney (recipe follows) | 1 |
| tomato chutney sauce, recipe follows | 1 |
| tomato chutney, for serving | 1 |
| tomato chutney, recipe follows | 4 |
| tomato clam juice | 1 |
| tomato compote, recipe follows | 1 |
| tomato con casse (tomatoes peeled, seeded and chopped) | 1 |
| tomato concasse | 19 |
| tomato concasse (peeled, seeded, and cut into julienned strips) | 1 |
| tomato concasse (seeds and skin removed | 1 |
| tomato concasse (skinned, seeded, and diced tomatoes) | 1 |
| tomato concasse* (see cook's note) | 1 |
| tomato concassee | 1 |
| tomato concentrate/puree | 1 |
| tomato confit, recipe follows | 1 |
| tomato coulis (recipe follows) | 2 |
| tomato couscous | 1 |
| tomato diced | 1 |
| tomato escabeche, recipe follows | 1 |
| tomato fillets (canned is fine) | 1 |
| tomato fondue or stewed tomato | 1 |
| tomato garlic basil sauce, recipe follows | 1 |
| tomato ginger vinaigrette | 2 |
| tomato horseradish sauce with lime juice, recipe follows | 1 |
| tomato jam | 4 |
| tomato jam, recipe follows | 4 |
| tomato juice | 197 |
| tomato juice (1/3 cup) | 1 |
| tomato juice (12 fluid ounces) | 1 |
| tomato juice (18 ounces) | 1 |
| tomato juice (3 cups) | 1 |
| tomato juice (optional) | 1 |
| tomato juice (or vegetable broth) | 1 |
| tomato juice (preferably campbell's) | 1 |
| tomato juice (preferably organic) | 1 |
| tomato juice (recommended: clamato juice) | 1 |
| tomato juice (recommended: sacramento) | 1 |
| tomato juice (recommended: v8) | 2 |
| tomato juice (such as mott's®) | 1 |
| tomato juice or 1 8-ounce can tomato sauce whisked with water to make 1 cup | 1 |
| tomato juice or beef broth | 1 |
| tomato juice or fish stock | 1 |
| tomato juice or tomato vegetable juice blend | 1 |
| tomato juice or tomato-vegetable juice cocktail | 1 |
| tomato juice or v-8 juice | 1 |
| tomato juice or water | 1 |
| tomato juice, chilled | 1 |
| tomato juice, fresh or bottled | 1 |
| tomato juice, homemade or store bought | 1 |
| tomato juice, made from blended san marzano tomato | 1 |
| tomato juice, or 3 cups peeled, seeded, and pureed tomato | 1 |
| tomato juice, plus more if needed | 1 |
| tomato juice, preferably sacramento | 1 |
| tomato ketchup | 31 |
| tomato ketchup and hot mustard or kikkoman sweet & sour sauce | 1 |
| tomato ketchup or barbecue sauce, to serve | 1 |
| tomato mango cucumber relish, recipe follows | 1 |
| tomato matzo balls | 1 |
| tomato mors or tomato puree | 1 |
| tomato olive vinaigrette, recipe follows | 1 |
| tomato onion chutney | 1 |
| tomato or alfredo sauce | 1 |
| tomato or spaghetti sauce, homemade or comercially prepared | 1 |
| tomato or vegetable juice | 1 |
| tomato or vegetable juice (such as v8) | 1 |
| tomato papaya salsa | 1 |
| tomato passata | 1 |
| tomato passata (whole tomatoes passed through a food mill) | 1 |
| tomato passata or puree | 2 |
| tomato passata or puréed whole peeled tomato | 1 |
| tomato pasta sauce | 7 |
| tomato paste | 1,764 |
| tomato paste (1/2 of 1 small can, reserving rest for the sauce) | 1 |
| tomato paste (10 ounces) | 4 |
| tomato paste (5 ounces) | 1 |
| tomato paste (about 1 tube) | 1 |
| tomato paste (about 1/2 small can) | 1 |
| tomato paste (about 7 1/2 ounces) | 1 |
| tomato paste (about half a 6-ounce can) | 1 |
| tomato paste (from a 6-ounce can) | 1 |
| tomato paste (from reserved 1/2 can) | 1 |
| tomato paste (not double concentrate) | 1 |
| tomato paste (optional) | 6 |
| tomato paste (optional; ellen doesn't use it, i do more often than not) | 1 |
| tomato paste (preferably from a tube) | 1 |
| tomato paste (preferably turkish) | 1 |
| tomato paste (recommend getting tube) | 1 |
| tomato paste 1 28-ounce can whole peeled tomatoes, drained | 1 |
| tomato paste 2 tablespoons finely snipped chives | 1 |
| tomato paste cans water | 2 |
| tomato paste concentrate (from tube) | 1 |
| tomato paste dissolved in 1 cup warm water | 1 |
| tomato paste dissolved in 2 cups water | 1 |
| tomato paste if needed | 1 |
| tomato paste or 1 tablespoon peeled, seeded, and finely chopped tomato | 1 |
| tomato paste or 2 tbsp ketchup | 1 |
| tomato paste or conserve | 1 |
| tomato paste or sun dried tomato paste | 1 |
| tomato paste or sun-dried tomato paste | 1 |
| tomato paste or tomato ketchup | 1 |
| tomato paste, (1 can) | 1 |
| tomato paste, look for this in a tube (it's easy to store that way) | 1 |
| tomato paste, mixed with 5 ounces broth of choice | 1 |
| tomato paste, or more as needed | 1 |
| tomato paste, or more to taste | 2 |
| tomato paste, or to taste | 2 |
| tomato peeled, seeded, and chopped | 1 |
| tomato pizza sauce (recipe precedes) | 1 |
| tomato powder | 2 |
| tomato powder (optional) | 1 |
| tomato powder (terra spices) | 1 |
| tomato pulp | 1 |
| tomato puree | 142 |
| tomato puree (from a 28-ounce can) | 1 |
| tomato puree (from fresh or canned peeled tomato) | 1 |
| tomato puree (preferably san marzano) | 1 |
| tomato puree or crushed tomato | 1 |
| tomato puree or ketchup | 1 |
| tomato puree or marinara sauce | 1 |
| tomato puree or passata | 1 |
| tomato puree or paste | 1 |
| tomato puree or tomato sauce | 1 |
| tomato puree, as needed for thickness | 2 |
| tomato puree, dissolved in 4 tablespoons water | 2 |
| tomato puree, or to taste | 1 |
| tomato puree, or to taste (optional) | 1 |
| tomato puree, recipe follows | 1 |
| tomato puree, such as mutti | 1 |
| tomato puree, such as pomi | 1 |
| tomato puree-400 grams | 1 |
| tomato purée | 8 |
| tomato purée from fresh or canned tomato | 1 |
| tomato purée, dried herbs, fennel seeds, bay leaf | 1 |
| tomato purée/tomato paste | 1 |
| tomato quarters | 1 |
| tomato quarters confit (remove the pips and interior) | 1 |
| tomato ranchero sauce, recipe follows | 1 |
| tomato relish | 1 |
| tomato relish, recipe follows | 3 |
| tomato relish, recipe to follow | 1 |
| tomato relish: | 1 |
| tomato salad with herbs, recipe follows | 1 |
| tomato salsa | 11 |
| tomato salsa (26 ounces) | 1 |
| tomato salsa (for garnish) | 1 |
| tomato salsa (see recipe below) | 1 |
| tomato salsa and chunky guacamole, as accompaniments | 1 |
| tomato salsa cruda, recipe follows | 2 |
| tomato salsa for serving | 1 |
| tomato salsa, for garnish | 1 |
| tomato salsa, for serving | 1 |
| tomato salsa, recipe follows | 4 |
| tomato salsa, your favorite or dos toros tomato salsa, recipe follows | 1 |
| tomato salsa: | 1 |
| tomato sauce | 365 |
| tomato sauce (about one 15-ounce can) | 1 |
| tomato sauce (gravy) | 1 |
| tomato sauce (optional) | 1 |
| tomato sauce (recipe above) | 1 |
| tomato sauce (recipe follows) | 1 |
| tomato sauce (recommended: el pato brand) | 1 |
| tomato sauce (recommended: hunt's) | 1 |
| tomato sauce (recommended: san marzano) | 1 |
| tomato sauce (see 'salsa di 5 minuti', recipe follows) | 1 |
| tomato sauce (such as classico® tomato and basil sauce) | 1 |
| tomato sauce (such as prego® heart smart) | 1 |
| tomato sauce (your own or store bought) | 2 |
| tomato sauce and cheese | 1 |
| tomato sauce and spices: | 1 |
| tomato sauce base | 1 |
| tomato sauce from a jar | 1 |
| tomato sauce made in a similar slow cooked fashion but meatless and with the addition of basil leaf | 1 |
| tomato sauce or ketchup | 1 |
| tomato sauce or la salsa di 5 minuti, recipe follows | 3 |
| tomato sauce or one 14-ounce can plus one 8-ounce can | 1 |
| tomato sauce or passata | 1 |
| tomato sauce or puree, or more if desired | 1 |
| tomato sauce or tomato puree | 1 |
| tomato sauce or tomato puree or passata | 1 |
| tomato sauce with chipotle | 1 |
| tomato sauce with italian seasonings | 1 |
| tomato sauce, 1 (8-ounce) can | 1 |
| tomato sauce, 8 ounces | 1 |
| tomato sauce, commercial or homemade | 1 |
| tomato sauce, for braising | 1 |
| tomato sauce, for serving | 2 |
| tomato sauce, for serving, recipe follows | 1 |
| tomato sauce, fresh or jarred | 1 |
| tomato sauce, from asian sloppy joes | 1 |
| tomato sauce, heated, recipe follows | 1 |
| tomato sauce, homemade or store bought | 1 |
| tomato sauce, homemade or store-bought | 1 |
| tomato sauce, jar or homemade | 1 |
| tomato sauce, jarred or homemade, recipe follows | 1 |
| tomato sauce, left over from spaghetti and meatballs or storebought | 1 |
| tomato sauce, marinara or pizza sauce, for dipping or five minute spicy marinara, recipe follows | 1 |
| tomato sauce, or more if needed | 1 |
| tomato sauce, or more to taste | 2 |
| tomato sauce, or other crushed tomato product | 1 |
| tomato sauce, or passata | 1 |
| tomato sauce, or to taste | 2 |
| tomato sauce, plus 1 cup warmed for dipping | 1 |
| tomato sauce, plus more for serving | 1 |
| tomato sauce, preferably homemade | 2 |
| tomato sauce, prepared | 1 |
| tomato sauce, recipe follows | 25 |
| tomato sauce, recipe follows, or your favorite jarred | 1 |
| tomato sauce, store bought | 1 |
| tomato sauce, store-bought | 1 |
| tomato sauce, such as san marzano | 1 |
| tomato sauce, thinned out with water | 1 |
| tomato sauce, tomato puree or passata | 1 |
| tomato sauce,( 8- ounce) can | 1 |
| tomato sauce: | 8 |
| tomato scraps (optional) | 2 |
| tomato skin made into 4 rose flowers, for garnish | 1 |
| tomato slice | 2 |
| tomato sliced | 1 |
| tomato slices | 38 |
| tomato slices (optional) | 2 |
| tomato slices, 1/4 inch thick | 1 |
| tomato slices, cut 1/4-inch thick | 1 |
| tomato slices, for garnish | 2 |
| tomato slices, for serving | 8 |
| tomato slices, for topping | 3 |
| tomato slices, lettuce leaf | 1 |
| tomato slices, or cherry tomato slices, for mini-burgers, for serving | 1 |
| tomato slices, or to taste | 1 |
| tomato slices, thick cut | 1 |
| tomato soup | 5 |
| tomato soup (optional) | 1 |
| tomato soup, as an accompaniment | 1 |
| tomato starfruit sauce, recipe follows | 1 |
| tomato vegetable juice | 1 |
| tomato vinegar | 1 |
| tomato vodka, recipe follows | 1 |
| tomato water | 2 |
| tomato water (recipe follows) | 1 |
| tomato water, recipe follows | 2 |
| tomato wedges | 5 |
| tomato wedges (optional) | 1 |
| tomato wedges, as needed | 1 |
| tomato wedges, for garnish | 1 |
| tomato wedges, quartered hard-cooked eggs, capers | 1 |
| tomato, as a garnish | 1 |
| tomato, concasse | 1 |
| tomato, concasse (with the skin on) | 1 |
| tomato, concasse* (see cook's note) | 1 |
| tomato, cored and chopped | 1 |
| tomato, cored and cut in quarters | 1 |
| tomato, cored and cut into wedges | 1 |
| tomato, cored and diced medium | 1 |
| tomato, cored and seeded, cut in strips | 1 |
| tomato, cored and thinly sliced | 1 |
| tomato, cored, cut into 6 to 8 wedges | 2 |
| tomato, cored, cut into thin wedges | 1 |
| tomato, cored, seeded | 1 |
| tomato, cored, seeded and cut into strips | 1 |
| tomato, cored, seeded and diced | 1 |
| tomato, cored, thinly sliced, and lightly salted | 1 |
| tomato, cubed | 8 |
| tomato, cubed and drained | 1 |
| tomato, cut in 1/2 | 1 |
| tomato, cut in half | 1 |
| tomato, cut in sections | 1 |
| tomato, cut into 1/2-inch dice | 1 |
| tomato, cut into 12 thin slices | 1 |
| tomato, cut into 8 slices | 3 |
| tomato, cut into bite-size pieces | 1 |
| tomato, cut into eighths | 1 |
| tomato, cut into large dice | 1 |
| tomato, cut into quarters | 1 |
| tomato, cut into small cubes | 1 |
| tomato, cut into thin wedges | 1 |
| tomato, cut into wedges | 7 |
| tomato, halved | 2 |
| tomato, halved and diced | 1 |
| tomato, halved and seeded | 1 |
| tomato, halved and sliced | 1 |
| tomato, halved and thinly sliced | 2 |
| tomato, halved crosswise | 1 |
| tomato, halved, seeded | 1 |
| tomato, julienne | 1 |
| tomato, julienned | 1 |
| tomato, marinara or pizza sauce for dipping or five minute spicy marinara, recipe follows | 1 |
| tomato, medium diced | 1 |
| tomato, medium ripe | 1 |
| tomato, overripe | 1 |
| tomato, quartered | 11 |
| tomato, quartered, plus 1 tomato sliced thinly, for garnish | 1 |
| tomato, roasted | 1 |
| tomato, roasted and coarsely chopped | 1 |
| tomato, seeded | 5 |
| tomato, seeded and chopped | 17 |
| tomato, seeded and chopped coarse | 1 |
| tomato, seeded and chopped fine | 1 |
| tomato, seeded and chopped fine (about 3/4 cup) | 1 |
| tomato, seeded and coarsely chopped | 1 |
| tomato, seeded and cut into 1/4-inch dice | 1 |
| tomato, seeded and cut into small dice | 1 |
| tomato, seeded and diced | 30 |
| tomato, seeded and diced (about 1/2 cup) | 1 |
| tomato, seeded and minced | 1 |
| tomato, seeded and small diced | 1 |
| tomato, seeded, cut into strips | 1 |
| tomato, seeds removed | 1 |
| tomato, skin removed and flesh chopped | 1 |
| tomato, skinned and seeded | 1 |
| tomato, small dice | 1 |
| tomato, small diced | 1 |
| tomato, thickly sliced | 3 |
| tomato, thinly sliced | 23 |
| tomato, thinly sliced to make 8 slices | 1 |
| tomato, thinly sliced, for serving | 1 |
| tomato, to garnish | 1 |
| tomato, very thinly sliced | 1 |
| tomato, washed and chopped | 3 |
| tomato, well ripened | 1 |
| tomato-based chile sauce (such as heinz®) | 1 |
| tomato-based chili sauce | 7 |
| tomato-based chili sauce (such as heinz®) | 1 |
| tomato-based pasta sauce | 3 |
| tomato-based vegetable juice | 1 |
| tomato-basil feta cheese, finely crumbled (1 cup) | 1 |
| tomato-basil or marinara sauce | 1 |
| tomato-basil sauce, for dipping, recipe follows | 1 |
| tomato-basil sauce, such as giada de laurentiis for target | 1 |
| tomato-basil sauce, such as giada de laurentiis for target sauce | 1 |
| tomato-basil sauce, such as giada de laurentiis for target tomato-basil sauce | 1 |
| tomato-caper bruschetta, for serving, recipe follows | 1 |
| tomato-chicken bouillon granules (such as knorr®) | 1 |
| tomato-chipotle salsa | 1 |
| tomato-clam juice (or 3 cups tomato juice mixed with 1/4 cup clam juice) | 1 |
| tomato-clam juice (recommended: clamato*) see cook's note | 1 |
| tomato-cumin relish, recipe follows | 1 |
| tomato-flavored bouillon | 1 |
| tomato-marjoram sauce | 1 |
| tomato-olive relish | 1 |
| tomato-red chile sauce, recipe follows | 1 |
| tomato-red pepper sauce, recipe follows | 1 |
| tomato-sausage sauce | 1 |
| tomato-seafood sauce: | 1 |
| tomato-serrano salsa | 1 |
| tomato-vegetable drink | 1 |
| tomato-vegetable juice | 2 |
| tomato-vegetable juice cocktail | 15 |
| tomato-vegetable juice cocktail (such as v8®) | 3 |
| tomato-vegetable juice, such as v8 | 2 |
| tomato/clam broth | 1 |
| tomato/garlic oil | 1 |
| tomatoes (1 chopped, 1 sliced) | 1 |
| tomatoes (1 medium-large round or 4 to 5 plum) thinly sliced | 1 |
| tomatoes (1/2 medium-large round or 2 to 3 plum) | 1 |
| tomatoes (1/2 pound total), seeded and chopped fine | 1 |
| tomatoes (2 large) | 1 |
| tomatoes (2 to 3 medium), quartered | 1 |
| tomatoes (3 medium) | 2 |
| tomatoes (3 medium), cut into 1/2-inch pieces | 1 |
| tomatoes (3 pounds), halved crosswise, seeded, and cut into 1-inch pieces | 1 |
| tomatoes (3 to 4 medium), cut into wedges | 1 |
| tomatoes (4 large) | 1 |
| tomatoes (4 medium) | 3 |
| tomatoes (4 medium), halved | 1 |
| tomatoes (4 pounds quartered, 1/2 pound chopped) | 1 |
| tomatoes (9 medium) | 1 |
| tomatoes (about 1 1/4 pounds), seeded and chopped fine | 1 |
| tomatoes (about 1 pound), boiled 30 seconds | 1 |
| tomatoes (about 1/2 pound), quartered | 1 |
| tomatoes (about 15 medium) | 1 |
| tomatoes (about 2 medium), cut into 1/4-inch cubes | 1 |
| tomatoes (about 2 medium), seeded and finely diced (1 1/2 cups) | 1 |
| tomatoes (about 2 pounds) | 1 |
| tomatoes (about 2 pounds), each cut into 1/3-inch-thick slices | 1 |
| tomatoes (about 3 pounds) | 1 |
| tomatoes (about 3/4 pound), cut into 1/2-inch dice | 1 |
| tomatoes (about 5), cut into 1/4-inch-thick slices | 2 |
| tomatoes (about 6 medium) | 1 |
| tomatoes (about 6) | 1 |
| tomatoes (about 7 cups) | 1 |
| tomatoes (any type) | 1 |
| tomatoes (heirloom if possible), cored and roughly cut | 1 |
| tomatoes (medium to large) seeded and diced | 1 |
| tomatoes (or to taste) | 1 |
| tomatoes (preferably a combination of red and yellow heirloom and/or cherry tomatoes) | 1 |
| tomatoes (recommended: san marzano) | 1 |
| tomatoes (the best quality you can find) | 1 |
| tomatoes - blanched | 3 |
| tomatoes - cored | 1 |
| tomatoes - cut in half | 1 |
| tomatoes - peeled, seeded and chopped | 5 |
| tomatoes - peeled, seeded and diced | 1 |
| tomatoes - peeled, seeded, and chopped | 4 |
| tomatoes - peeled, seeded, and coarsely chopped | 2 |
| tomatoes and onions, recipe follows | 1 |
| tomatoes chopped | 1 |
| tomatoes concasse or cut into strips | 1 |
| tomatoes cubed | 1 |
| tomatoes cut up with their juice, either ripe, firm, fresh plum tomatoes or canned imported san marzano italian tomato | 1 |
| tomatoes diced | 4 |
| tomatoes from (28-ounce) can whole tomatoes (recommended: san marzano) | 1 |
| tomatoes halved, seeded, grilled, and then chopped | 1 |
| tomatoes in chile-fennel oil | 1 |
| tomatoes of different variety | 1 |
| tomatoes on the vine, cored and chopped | 1 |
| tomatoes on the vine, cut in 1/2 | 1 |
| tomatoes or 1 qt. can | 1 |
| tomatoes or 4 canned tomato | 1 |
| tomatoes peeled and chopped | 1 |
| tomatoes peeled, seeded and chopped | 1 |
| tomatoes peeled, seeded and cut into 2-inch dice, or cherry tomatoes cut in half | 1 |
| tomatoes rough small chop | 1 |
| tomatoes seeded, smoked or baked | 1 |
| tomatoes with green chilies | 1 |
| tomatoes with juice | 1 |
| tomatoes, 1 peeled, seeded, and cut into 1/4-inch dice, the other just cut in half | 1 |
| tomatoes, 2-3 inches in diameter | 1 |
| tomatoes, about 1 cup | 1 |
| tomatoes, asado, technique follows | 1 |
| tomatoes, blanched | 1 |
| tomatoes, blanched and chopped | 1 |
| tomatoes, blanched and peeled or 4 cups (1 liter) canned tomato | 1 |
| tomatoes, blended or crushed | 1 |
| tomatoes, blended to a pulp in a food processor | 1 |
| tomatoes, blended to a puree in a food processor | 1 |
| tomatoes, concasse (finely chopped) | 1 |
| tomatoes, concassed (peeled, seeded, and cut into strips) | 1 |
| tomatoes, concassed and julienned | 1 |
| tomatoes, core removed | 2 |
| tomatoes, cored | 9 |
| tomatoes, cored and chopped | 2 |
| tomatoes, cored and coarsely chopped | 3 |
| tomatoes, cored and cut into 1-inch chunks | 1 |
| tomatoes, cored and cut into 1-inch-wide wedges | 1 |
| tomatoes, cored and cut into chunks | 2 |
| tomatoes, cored and cut into wedges | 1 |
| tomatoes, cored and diced | 2 |
| tomatoes, cored and finely chopped (juice reserved) | 1 |
| tomatoes, cored and halved | 1 |
| tomatoes, cored and sliced | 1 |
| tomatoes, cored, cubed | 1 |
| tomatoes, cored, cut into 3/4-inch dice, juices reserved | 1 |
| tomatoes, cored, cut into wedges | 1 |
| tomatoes, cored, quartered | 2 |
| tomatoes, cored, seeded | 3 |
| tomatoes, cored, seeded and chopped (about 1 1/4 cups) | 1 |
| tomatoes, cored, seeded and diced | 2 |
| tomatoes, cored, seeded, and chopped | 1 |
| tomatoes, cored, seeded, and cut into 1/2-inch dice | 2 |
| tomatoes, crushed | 1 |
| tomatoes, cubed | 13 |
| tomatoes, cut crosswise into 1/4-inch-thick slices | 1 |
| tomatoes, cut in 1/4-inch pieces, seed part removed and cut in small dice | 1 |
| tomatoes, cut in half | 2 |
| tomatoes, cut in half crosswise | 1 |
| tomatoes, cut in halves or fourths | 1 |
| tomatoes, cut in quarters | 1 |
| tomatoes, cut in small dice | 1 |
| tomatoes, cut into 1-inch chunks | 1 |
| tomatoes, cut into 1-inch dice | 1 |
| tomatoes, cut into 1-inch pieces | 3 |
| tomatoes, cut into 1/2-inch cubes | 1 |
| tomatoes, cut into 1/2-inch dice | 1 |
| tomatoes, cut into 1/2-inch pieces | 2 |
| tomatoes, cut into 1/2-inch-thick wedges | 1 |
| tomatoes, cut into 1/3-inch pieces | 1 |
| tomatoes, cut into 1/4 inch slices | 1 |
| tomatoes, cut into 1/4" slices | 1 |
| tomatoes, cut into 1/4-inch dice | 3 |
| tomatoes, cut into 1/4-inch dice (3 cups) | 1 |
| tomatoes, cut into 1/4-inch slices | 1 |
| tomatoes, cut into 1/8 dice | 1 |
| tomatoes, cut into 16 slices | 1 |
| tomatoes, cut into 2" pieces | 1 |
| tomatoes, cut into 3/4-inch-thick wedges, seeded | 1 |
| tomatoes, cut into 8 pieces each | 1 |
| tomatoes, cut into 8 slices | 2 |
| tomatoes, cut into 8 wedges | 2 |
| tomatoes, cut into 8 wedges each | 1 |
| tomatoes, cut into bite-size pieces | 3 |
| tomatoes, cut into bite-sized pieces | 3 |
| tomatoes, cut into chunks | 2 |
| tomatoes, cut into cubes | 2 |
| tomatoes, cut into large chunks | 1 |
| tomatoes, cut into quarters, or 2 cups roughly chopped canned tomato | 1 |
| tomatoes, cut into small cubes | 1 |
| tomatoes, cut into small dice | 2 |
| tomatoes, cut into small wedges | 1 |
| tomatoes, cut into wedges | 16 |
| tomatoes, cut into wedges (optional) | 1 |
| tomatoes, cut small dice | 1 |
| tomatoes, deseeded and diced | 1 |
| tomatoes, drained | 1 |
| tomatoes, each cut into 8 wedges | 3 |
| tomatoes, ends trimmed | 1 |
| tomatoes, for dipping | 1 |
| tomatoes, for serving | 1 |
| tomatoes, halved | 12 |
| tomatoes, halved and broiled, for garnish (optional) | 1 |
| tomatoes, halved and cored | 1 |
| tomatoes, halved and seeds squeezed out | 1 |
| tomatoes, halved and sliced | 1 |
| tomatoes, halved crosswise | 2 |
| tomatoes, halved horizontally, seeded, and cut into thin wedges | 1 |
| tomatoes, halved if large | 1 |
| tomatoes, halved lengthwise | 2 |
| tomatoes, halved, seeded | 1 |
| tomatoes, halved, seeded and finely diced | 1 |
| tomatoes, halved, seeded, and finely diced | 1 |
| tomatoes, halved, seeded, cut into 1/2-inch cubes | 1 |
| tomatoes, halved, seeded, very thinly sliced | 1 |
| tomatoes, heirloom preferred | 1 |
| tomatoes, including juice | 2 |
| tomatoes, insides removed and finely diced | 1 |
| tomatoes, juiced | 1 |
| tomatoes, julienne | 1 |
| tomatoes, julienned using a mandolin | 1 |
| tomatoes, large, well ripened | 1 |
| tomatoes, medium diced | 1 |
| tomatoes, medium diced for, garnish | 1 |
| tomatoes, preferably a mix of large heirloom tomatoes, cored and cut into wedges | 1 |
| tomatoes, pureed | 4 |
| tomatoes, pureed with their liquid | 1 |
| tomatoes, quartered | 34 |
| tomatoes, red and yellow | 1 |
| tomatoes, roasted | 1 |
| tomatoes, roasted (see note) | 1 |
| tomatoes, rough chopped | 1 |
| tomatoes, seeded | 12 |
| tomatoes, seeded and chopped | 42 |
| tomatoes, seeded and chopped (about 1 cup) | 1 |
| tomatoes, seeded and chopped (about 2 cups) | 1 |
| tomatoes, seeded and chopped into 1/2-inch pieces | 1 |
| tomatoes, seeded and coarsely chopped | 4 |
| tomatoes, seeded and cut into 1/2 inch dice | 1 |
| tomatoes, seeded and cut into 1/2inch dice | 2 |
| tomatoes, seeded and cut into chunks | 1 |
| tomatoes, seeded and cut into strips | 1 |
| tomatoes, seeded and diced | 29 |
| tomatoes, seeded and finely chopped | 5 |
| tomatoes, seeded and finely diced | 5 |
| tomatoes, seeded and quartered | 1 |
| tomatoes, seeded and sliced | 2 |
| tomatoes, seeded, and chopped | 1 |
| tomatoes, seeds removed and diced small | 1 |
| tomatoes, seeds removed and finely diced | 2 |
| tomatoes, seeds removed, cut into 1/4 dice | 1 |
| tomatoes, skin removed and chopped, juice reserved | 1 |
| tomatoes, skinned and chopped | 1 |
| tomatoes, skinned and chopped, or more to taste | 1 |
| tomatoes, skinned and diced | 1 |
| tomatoes, skinned, deseeded and coursely chopped | 1 |
| tomatoes, skinned, quartered and deseeded | 1 |
| tomatoes, skinned, seeded | 1 |
| tomatoes, skinned, seeded, and cubed | 1 |
| tomatoes, small dice | 4 |
| tomatoes, small diced | 1 |
| tomatoes, smoked and pureed | 1 |
| tomatoes, stemmed and cut into medium dice | 2 |
| tomatoes, stemmed and roughly chopped | 1 |
| tomatoes, thinly sliced | 24 |
| tomatoes, very thinly sliced | 1 |
| tomatoes, whole | 1 |
| tomatoes--12 to 18 months | 1 |
| tomatoes-sliced | 1 |
| tomatoes. peeled, seeded, and diced | 1 |
| toppings: lettuce, tomato, red onion, and sliced avocado | 1 |
| toppings: lettuce, tomato, red onion, thinly sliced fresh mozzarella and torn fresh basil leaf | 1 |
| toppings: rosemary, fresh tomato and basil, tomato sauce and cheese | 1 |
| traditional italian tomato sauce, recipe follows | 1 |
| traditional italian tomato sauce, recipe follows, warmed | 1 |
| tub sun-dried tomato pesto | 1 |
| tube of good tomato paste | 1 |
| tube sun-dried tomato paste | 1 |
| tube, 24 ounces, prepared polenta, plain or sun-dried tomato flavor, cut into 1/2-inch slices | 1 |
| twelve 1/4-inch-thick slices tomato | 1 |
| twelve 1/4-inch-thick tomato slices | 1 |
| two (14.5-ounce) cans petite-cut diced tomato | 1 |
| two 1 pound 12-ounce tins or 3 pounds fresh egg-shaped tomatoes, skinned, seeded and roughly chopped | 1 |
| two 10-ounce cans diced tomatoes and green chiles, such as rotel | 1 |
| two 10-ounce cans diced tomatoes with chiles, drained | 1 |
| two 10-ounce cans tomatoes with chilies, such as rotel original | 2 |
| two 10.75-ounce cans condensed tomato soup | 1 |
| two 12-ounce cans tomato paste | 2 |
| two 14 1/2-ounce cans diced tomato | 1 |
| two 14 1/2-ounce cans diced tomatoes, no salt added (you'll only use 1 1/2 cans; save the rest for another use) | 1 |
| two 14 1/2-ounce cans petite cut diced tomato | 1 |
| two 14- to 16-ounce cans whole tomatoes, drained and chopped coarse | 1 |
| two 14-ounce cans diced tomato | 1 |
| two 14-ounce cans diced tomatoes or stewed tomato | 1 |
| two 14-ounce cans diced tomatoes, with their juices | 1 |
| two 14-ounce cans fire-roasted diced tomatoes, drained and juice reserved | 1 |
| two 14-ounce cans italian plum tomato | 1 |
| two 14-ounce cans no-salt-added diced tomato | 1 |
| two 14-ounce cans tomato sauce | 1 |
| two 14-ounce cans whole tomato | 1 |
| two 14-oz/410-g cans peeled whole tomatoes, seeded and puréed with all the juices | 1 |
| two 14.5-ounce cans diced fire-roasted tomato | 1 |
| two 14.5-ounce cans diced tomato | 1 |
| two 14.5-ounce cans diced tomatoes with chiles, drained | 1 |
| two 14.5-ounce cans petite-cut diced tomato | 1 |
| two 14.5-ounce cans tomato sauce | 1 |
| two 14.5-ounce cans tomato sauce or marinara sauce | 1 |
| two 14.5-ounce cans whole tomato | 1 |
| two 15-ounce cans crushed tomato | 2 |
| two 15-ounce cans diced fire-roasted tomato | 1 |
| two 15-ounce cans diced tomato | 3 |
| two 15-ounce cans diced tomatoes in puree or juice | 1 |
| two 15-ounce cans fire-roasted tomato | 1 |
| two 15-ounce cans tomato sauce | 3 |
| two 15-ounce cans tomato sauce or marinara sauce | 1 |
| two 15-ounce cans whole peeled tomato | 1 |
| two 16-ounce cans crushed tomato | 1 |
| two 19-ounce cans diced tomato | 1 |
| two 20-ounce cans roma tomato | 1 |
| two 24.5-ounce bottles tomato puree, such as mutti | 1 |
| two 26-ounce boxes pomi chopped tomatoes or two 28-ounce cans whole plum tomato | 1 |
| two 26.5-ounce boxes strained tomatoes, such as pomi | 1 |
| two 28- to 32-ounce cans whole tomato | 1 |
| two 28- to 32-ounce cans whole tomatoes, drained, reserving juice, and chopped | 1 |
| two 28-ounce cans chopped tomato | 2 |
| two 28-ounce cans chunky ground tomatoes, such as pastene chunky kitchen ready | 2 |
| two 28-ounce cans crushed tomato | 10 |
| two 28-ounce cans diced tomatoes with peppers, such as rotel | 1 |
| two 28-ounce cans italian plum tomatoes, passed through a food mill or pureed | 1 |
| two 28-ounce cans italian tomato | 1 |
| two 28-ounce cans italian tomatoes, drained well and chopped | 1 |
| two 28-ounce cans low-sodium diced tomato | 1 |
| two 28-ounce cans peeled san marzano tomatoes, juices passed through a food mill | 1 |
| two 28-ounce cans peeled tomato | 1 |
| two 28-ounce cans peeled tomatoes in their juice | 1 |
| two 28-ounce cans plum tomatoes and their juices, pureed in a blender | 2 |
| two 28-ounce cans plum tomatoes in their juices | 1 |
| two 28-ounce cans plum tomatoes including the juice | 1 |
| two 28-ounce cans plum tomatoes, crushed by hand | 3 |
| two 28-ounce cans pomodori pelati tomatoes (whole peeled tomatoes), blended smooth | 2 |
| two 28-ounce cans san marzano tomato | 2 |
| two 28-ounce cans san marzano tomatoes, with their juice | 2 |
| two 28-ounce cans tomato puree | 1 |
| two 28-ounce cans tomato sauce | 2 |
| two 28-ounce cans whole fire-roasted tomatoes, crushed by hand | 1 |
| two 28-ounce cans whole fire-roasted tomatoes, with their juice | 1 |
| two 28-ounce cans whole peeled plum tomato | 1 |
| two 28-ounce cans whole peeled tomato | 1 |
| two 28-ounce cans whole peeled tomatoes, crushed by hand | 1 |
| two 28-ounce cans whole peeled tomatoes, preferably san marzano | 1 |
| two 28-ounce cans whole peeled tomatoes, with their juices | 1 |
| two 28-ounce cans whole plum tomato | 1 |
| two 28-ounce cans whole san marzano tomatoes, crushed with your hands | 1 |
| two 28-ounce cans whole tomato | 2 |
| two 28-ounce cans whole tomatoes, crushed by hand | 1 |
| two 28-ounce cans whole tomatoes, drained | 1 |
| two 28-ounce cans whole tomatoes, drained of their juices | 1 |
| two 28-ounce cans whole tomatoes, drained of their liquid | 1 |
| two 28-ounce cans whole tomatoes, drained, tomatoes chopped | 1 |
| two 28-ounce cans whole tomatoes, undrained and coarsely chopped | 1 |
| two 28-ounce containers crushed tomato | 1 |
| two 28-to-32 ounce can whole tomatoes including juice | 1 |
| two 28-to-32-ounce cans tomatoes, drained and chopped | 1 |
| two 29-ounce cans tomato puree | 2 |
| two 32-ounce cans crushed tomato | 4 |
| two 32-ounce cans san marzano tomato | 1 |
| two 32-ounce cans tomatoes, such as san marzano, drained and put through a food mill or food processor | 1 |
| two 35-ounce cans plum tomatoes in juice | 1 |
| two 400-gram (14-ounce) cans chopped tomato | 1 |
| two 6-ounce cans tomato paste | 3 |
| two 8-ounce cans tomato sauce | 7 |
| two more ways to go: add chopped fresh basil leaves and/or small cubes of mozzarella cheese. or use yellow and green tomatoes with the red ones to add summer color | 1 |
| two tomato | 1 |
| undrained canned tomatoes (28ounce can) | 1 |
| undrained chopped fresh or canned tomato | 1 |
| undrained chopped fresh or canned tomatoes (28ounce can) | 1 |
| unripe green tomato | 1 |
| v-8 tomato juice or the equivalent | 1 |
| v8 or tomato juice | 2 |
| vegetable juice or tomato sauce | 1 |
| vegetable oil for brushing the tomato | 1 |
| vegetable or tomato juice | 2 |
| vegetable or tomato juice (recommended: v8) | 1 |
| vegetable stock or tomato juice | 1 |
| vegetable-juice cocktail such as v-8, or tomato juice | 1 |
| very cold tomato juice | 1 |
| very red tomatoes, ripe and firm | 1 |
| very ripe beefsteak tomatoes, cored and diced | 1 |
| very ripe diced red tomato | 1 |
| very ripe diced yellow tomato | 1 |
| very ripe fresh tomatoes, passed through a food mill | 1 |
| very ripe heirloom tomato | 1 |
| very ripe large beefsteak tomatoes, halved, seeded and coarsely chopped | 1 |
| very ripe large tomatoes, cubed | 1 |
| very ripe medium tomato | 1 |
| very ripe medium-sized tomatoes (about 8 ounces each) | 1 |
| very ripe multicolored tomato | 1 |
| very ripe tomato | 6 |
| very ripe tomato cut in half | 1 |
| very ripe tomatoes (about 3 medium) | 1 |
| very ripe tomatoes, about 6 ounces each | 1 |
| very ripe tomatoes, cores removed | 1 |
| very ripe tomatoes, quartered, seeded, and chopped | 1 |
| very ripe, fresh tomato | 1 |
| very small cherry tomatoes, halved | 2 |
| very small cherry tomatoes, halved (optional)* | 2 |
| very small grape or pear tomatoes (1/4 pound), halved | 1 |
| very thin slices tomato | 1 |
| vine cherry tomatoes for garnish | 1 |
| vine ripe or small round red tomato | 1 |
| vine ripe orange or yellow tomato, seeded and finely chopped | 1 |
| vine ripe plum tomato, seeded and finely chopped | 1 |
| vine ripe red tomato, seeded and chopped | 1 |
| vine ripe tomato | 15 |
| vine ripe tomato slices | 1 |
| vine ripe tomato, seeded and chopped | 3 |
| vine ripe tomato, thinly sliced | 1 |
| vine ripe tomatoes cut into wedges | 1 |
| vine ripe tomatoes in 3/4-inch slices, seasoned with salt and pepper | 1 |
| vine ripe tomatoes or roma tomatoes, seeded and chopped | 1 |
| vine ripe tomatoes, cut into 8 wedges, each wedge cut in 1/2 | 1 |
| vine ripe tomatoes, cut into chunks | 1 |
| vine ripe tomatoes, cut small dice | 1 |
| vine ripe tomatoes, halved | 2 |
| vine ripe tomatoes, halved and thinly sliced | 1 |
| vine ripe tomatoes, red or yellow, tops trimmed and seeded | 1 |
| vine ripe tomatoes, red, yellow, or mixed | 1 |
| vine ripe tomatoes, seeded | 1 |
| vine ripe tomatoes, seeded and chopped | 4 |
| vine ripe tomatoes, seeded and diced | 3 |
| vine ripe tomatoes, thinly sliced | 3 |
| vine ripened island cherry tomato | 1 |
| vine ripened plum or round tomatoes, halved, seeds squeezed out, and diced | 1 |
| vine ripened red tomato | 2 |
| vine ripened red tomatoes, cut into 3/4-inch wedges | 2 |
| vine ripened tomato | 10 |
| vine ripened tomato slices | 1 |
| vine ripened tomato, boiled 30 seconds | 3 |
| vine ripened tomatoes, about 2 medium, 3/4-inch dice | 1 |
| vine ripened tomatoes, cut in half and seeded | 1 |
| vine ripened tomatoes, seeded and cut into 1/4inch dice | 1 |
| vine ripened tomatoes, seeded and diced | 2 |
| vine ripened tomatoes, seeds removed and cut brunoise (julienne then cut crosswise into 1/16th-inch cubes) | 2 |
| vine ripened tomatoes, washed and cut into small dice | 1 |
| vine ripened yellow tomatoes, cut into 3/4-inch wedges | 2 |
| vine stems of cherry tomato | 1 |
| vine tomato | 6 |
| vine tomatoes (about 3) | 1 |
| vine tomatoes, halved and thinly sliced | 1 |
| vine tomatoes, halved lengthwise, seeded and thinly sliced | 1 |
| vine-ripe medium tomatoes, quartered | 1 |
| vine-ripe medium tomatoes, seeded and coarsely chopped | 1 |
| vine-ripe or roma tomatoes, cut into 1/3-inch dice | 1 |
| vine-ripe tomato | 19 |
| vine-ripe tomato, seeded and chopped | 2 |
| vine-ripe tomato, seeded and coarsely chopped | 1 |
| vine-ripe tomato, seeded, and chopped | 1 |
| vine-ripe tomato, thickly sliced into 4 pieces | 1 |
| vine-ripe tomato, thinly sliced | 2 |
| vine-ripe tomatoes, 1/4-inch thick slices | 1 |
| vine-ripe tomatoes, halved | 1 |
| vine-ripe tomatoes, halved or quartered depending on their size, seeds removed | 1 |
| vine-ripe tomatoes, seeded and chopped | 2 |
| vine-ripe tomatoes, seeded and diced | 1 |
| vine-ripened cherry or grape tomatoes, halved | 3 |
| vine-ripened cherry tomato | 4 |
| vine-ripened cherry tomatoes, grape tomatoes, and golden pear tomato | 1 |
| vine-ripened cherry tomatoes, halved | 6 |
| vine-ripened cherry tomatoes, halved if large | 1 |
| vine-ripened cherry tomatoes, quartered | 2 |
| vine-ripened large tomatoes (about 5) | 1 |
| vine-ripened large yellow tomatoes or yellow bell peppers (or a mix of both) | 1 |
| vine-ripened or canned tomato | 1 |
| vine-ripened or plum tomatoes, cut into 1/3-inch dice (4 cups) | 1 |
| vine-ripened plum (roma) tomatoes, cored and cut into thin wedges | 1 |
| vine-ripened plum tomato | 3 |
| vine-ripened plum tomatoes, quartered | 1 |
| vine-ripened plum tomatoes, seeded and chopped (about 4) | 1 |
| vine-ripened red and/or orange tomatoes (about 5 medium) | 2 |
| vine-ripened red cherry tomatoes, halved | 3 |
| vine-ripened red tomato | 1 |
| vine-ripened red tomatoes (about 10 medium) | 2 |
| vine-ripened red tomatoes (about 10) | 1 |
| vine-ripened red tomatoes, cut into 3/4-inch wedges | 3 |
| vine-ripened small cherry tomatoes, halved | 1 |
| vine-ripened tomato | 42 |
| vine-ripened tomato, cored and cut into 16 wedges | 1 |
| vine-ripened tomato, cut into 4 slices | 1 |
| vine-ripened tomatoes (1 pound), each sliced into 8 wedges | 1 |
| vine-ripened tomatoes (8 small to medium) | 1 |
| vine-ripened tomatoes (about 1 pound), seeded and chopped fine | 1 |
| vine-ripened tomatoes (about 2 pounds) | 1 |
| vine-ripened tomatoes (about 2 tomatoes) | 2 |
| vine-ripened tomatoes (about 3 tomatoes) | 1 |
| vine-ripened tomatoes (about 3) | 1 |
| vine-ripened tomatoes (about 3/4 pound total), cut into 1/2-inch cubes | 1 |
| vine-ripened tomatoes (about 3/4-pound), cored and cut into 1/2-inch chunks | 1 |
| vine-ripened tomatoes (about 4 large) | 1 |
| vine-ripened tomatoes (about 4 medium) | 1 |
| vine-ripened tomatoes (about 5 medium), seeded and chopped coarse | 1 |
| vine-ripened tomatoes (about 8 medium) | 1 |
| vine-ripened tomatoes (about 8 ounces each for a total of 4 pounds) | 1 |
| vine-ripened tomatoes or roma tomato | 1 |
| vine-ripened tomatoes, about 1 pound total | 1 |
| vine-ripened tomatoes, blanched | 1 |
| vine-ripened tomatoes, cored | 1 |
| vine-ripened tomatoes, cored and diced | 1 |
| vine-ripened tomatoes, cored and quartered | 1 |
| vine-ripened tomatoes, cut into 1/2 inch pieces | 1 |
| vine-ripened tomatoes, cut into 1/2-inch thick slices | 1 |
| vine-ripened tomatoes, cut into 1/4-inch cubes | 1 |
| vine-ripened tomatoes, cut into 3/4-inch wedges | 1 |
| vine-ripened tomatoes, cut into 8 slices | 1 |
| vine-ripened tomatoes, cut into eighths | 1 |
| vine-ripened tomatoes, each cut into 6 slices | 1 |
| vine-ripened tomatoes, preferably a mixture of red, yellow, orange and variegated | 1 |
| vine-ripened tomatoes, preferably heirloom varieties | 1 |
| vine-ripened tomatoes, quartered and seeded | 1 |
| vine-ripened tomatoes, seeded and chopped | 2 |
| vine-ripened tomatoes, seeded and chopped (about 1 1/3 cups) | 1 |
| vine-ripened tomatoes, seeded and chopped fine | 5 |
| vine-ripened tomatoes, seeded and chopped fine (about 2 cups) | 1 |
| vine-ripened tomatoes, seeded and diced | 1 |
| vine-ripened tomatoes, seeded and finely chopped | 1 |
| vine-ripened tomatoes, seeded and finely diced | 2 |
| vine-ripened tomatoes, separated from vine | 1 |
| vine-ripened tomatoes, stems left on | 1 |
| vine-ripened tomatoes, thinly sliced | 2 |
| vine-ripened tomatoes, very thinly sliced | 1 |
| vine-ripened yellow cherry tomato | 1 |
| vine-ripened yellow cherry tomatoes, halved | 3 |
| vine-ripened yellow tomato | 1 |
| vine-ripened yellow tomatoes, cut into 3/4-inch wedges | 3 |
| vineripe tomatoes or other ripe varietals cut into quarters | 1 |
| vineripened tomato | 1 |
| vineripened tomatoes, seeded and cut into 1/2-inch dice | 1 |
| walnuts1/3 cup sundried tomato | 1 |
| warm red tomato salsa, recipe follows | 1 |
| warm simple tomato sauce, recipe follows, or store-bought chunky marinara sauce, drained of excess liquid | 1 |
| warm tomato juice | 1 |
| warm tomato-basil marinara sauce | 1 |
| water (3/4 cup if using canned tomatoes) | 1 |
| water (stock saved from boiling chiles and tomatoes) | 1 |
| water-pack tomatoes (do not drain) | 1 |
| weelicious tomato sauce | 1 |
| well ripened tomato | 1 |
| well-drained canned whole tomatoes (from a 14- to 16-oz can with juice) | 1 |
| white button mushrooms, wiped clean 2 tablespoons tomato paste | 1 |
| white cherry tomatoes, quartered | 1 |
| whole canned plum tomato | 1 |
| whole canned plum tomatoes (from 14 1/2-ounce can), drained | 1 |
| whole canned tomato | 4 |
| whole canned tomatoes (about 4 ounces) | 1 |
| whole canned tomatoes, crushed with hands | 1 |
| whole canned tomatoes, drained | 1 |
| whole canned tomatoes, drained and chopped | 1 |
| whole cherry tomato | 1 |
| whole chopped tomato | 1 |
| whole or sliced grape or cherry tomato | 1 |
| whole peeled canned tomato | 4 |
| whole peeled italian tomato | 1 |
| whole peeled plum tomato | 1 |
| whole peeled tomato | 8 |
| whole peeled tomatoes with liquid | 1 |
| whole peeled tomatoes, crushed | 1 |
| whole peeled tomatoes, drained | 1 |
| whole peeled tomatoes, drained and chopped | 1 |
| whole peeled tomatoes, in juice | 2 |
| whole peeled tomatoes, plus juices from one 15-ounce can or half of one 28-ounce can | 1 |
| whole peeled tomatoes, with liquid | 1 |
| whole peeled whole tomatoes, crushed, juices reserved | 1 |
| whole peeled, canned tomatoes in their juice | 1 |
| whole plum (roma) tomato | 1 |
| whole plum tomato | 1 |
| whole plum tomatoes (fresh or canned), crushed | 1 |
| whole plum tomatoes with their juice, crushed by hand | 1 |
| whole red cherry tomato | 2 |
| whole ripe tomato | 1 |
| whole ripe tomatoes, cut into 6 wedges each, then each wedge cut in half | 1 |
| whole roma tomato | 6 |
| whole san marzano tomato | 2 |
| whole san marzano tomatoes, drained | 1 |
| whole san marzano tomatoes, plus the liquid from the can | 2 |
| whole small cherry tomato | 1 |
| whole tomato | 16 |
| whole tomatoes from 28-ounce can, drained | 1 |
| whole tomatoes from a 15-ounce can | 2 |
| whole tomatoes in puree | 2 |
| whole tomatoes, canned | 1 |
| whole tomatoes, crushed (28 ounces) | 1 |
| whole tomatoes, drained and chopped | 1 |
| whole tomatoes, drained and hand-crushed | 1 |
| whole tomatoes, each tomato cut into quarters, juice reserved | 1 |
| whole tomatoes, plus juice | 1 |
| whole tomatoes, pureed with liquid | 1 |
| whole tomatoes, pureed with their juices | 1 |
| whole tomatoes, undrained and roughly chopped | 1 |
| whole-wheat sourdough rolls, split and toasted lettuce and tomato, for topping | 1 |
| worcestershire tomato ketchup, recipe follows | 1 |
| x 400 g (14 oz) cans italian tomatoes, pureed and sieved (about 2 cups) | 1 |
| yellow and red baby tomato | 1 |
| yellow and red cherry tomatoes, halved | 1 |
| yellow and red grape tomato | 1 |
| yellow and red grape tomatoes, halved | 1 |
| yellow and/or red grape tomatoes, halved | 1 |
| yellow baby plum tomatoes or cherry tomato | 1 |
| yellow beefsteak tomatoes, washed, core removed, a small "x" cut on the bottom of each | 1 |
| yellow cherry or grape tomatoes, halved | 2 |
| yellow cherry tomato | 3 |
| yellow cherry tomatoes, cut in half | 1 |
| yellow cherry tomatoes, cut into sixths | 1 |
| yellow cherry tomatoes, half of them sliced in half | 1 |
| yellow cherry tomatoes, halved | 1 |
| yellow cherry tomatoes, halved (1 cup) | 1 |
| yellow cherry tomatoes, quartered | 2 |
| yellow cherry tomatoes, whole | 1 |
| yellow currant tomato | 1 |
| yellow grape or cherry tomato | 1 |
| yellow grape or compari tomatoes, cored and halved | 1 |
| yellow grape tomato | 2 |
| yellow grape tomatoes, halved | 1 |
| yellow or orange tomatoes, seeded and diced | 1 |
| yellow or red cherry tomatoes, halved or quartered (depending upon how large they are) | 1 |
| yellow or red cherry tomatoes, quartered | 1 |
| yellow or red large round tomato | 1 |
| yellow or red tomatoes (preferably vine-ripened), seeded, cut into 1/2-inch pieces | 1 |
| yellow or red tomatoes, seeded and chopped | 1 |
| yellow or red vine ripe tomato | 1 |
| yellow or sun gold tomatoes, quartered, halved if small | 1 |
| yellow pear and red tear drop tomato | 1 |
| yellow pear and sweet 100 cherry tomatoes, cut in half | 1 |
| yellow pear or cherry tomato | 1 |
| yellow pear or cherry tomatoes (about 2 2/3 cups) | 2 |
| yellow pear or cherry tomatoes (about 2 2/3 cups) (red tomatoes may also be used) | 1 |
| yellow pear or cherry tomatoes, halved | 1 |
| yellow pear tomato | 3 |
| yellow pear tomatoes, halved | 5 |
| yellow pear tomatoes, halved or quartered depending on size | 1 |
| yellow pear tomatoes, stems removed | 1 |
| yellow plum tomato, thinly sliced | 1 |
| yellow roma tomato | 1 |
| yellow roma tomatoes, washed and quartered | 1 |
| yellow teardrop or grape tomatoes, halved | 1 |
| yellow teardrop tomatoes, halved | 2 |
| yellow tomato | 17 |
| yellow tomato (1 large) | 1 |
| yellow tomato salsa: any flavor or variety of store bought salsa that you may have in your pantry is a fine substitute here as well | 1 |
| yellow tomato, medium dice | 1 |
| yellow tomato, seeded and diced | 2 |
| yellow tomato, seeded and minced | 1 |
| yellow tomato-tarragon relish, recipe follows | 1 |
| yellow tomatoes (4 to 5 oz each) | 1 |
| yellow tomatoes (about 6) | 1 |
| yellow tomatoes, cored | 1 |
| yellow tomatoes, cut into 1/4-inch-thick slices | 1 |
| yellow tomatoes, cut into chunks | 1 |
| yellow tomatoes, halved | 3 |
| yellow tomatoes, halved, seeded and diced | 1 |
| yellow tomatoes, halved, seeded, grilled and chopped | 1 |
| yellow tomatoes, quartered (may use 4 cherry tomatoes, cut in half) | 1 |
| yellow tomatoes, quartered (use red if yellow not available) | 1 |
| yellow tomatoes, quartered, seeds removed | 1 |
| yellow tomatoes, seeded and | 1 |
| yellow tomatoes, seeded and chopped | 1 |
| yellow tomatoes, seeded and cut into 1/2-inch dice | 2 |
| yellow tomatoes, seeded and finely diced | 1 |
| yellow vine ripe tomatoes, seeded and diced | 2 |
| yellow vine-ripe tomato | 1 |
| yogurt-tomato sauce, recipe follows | 1 |
| your favorite condiments, such as ketchup, mustard, mayonnaise, lettuce, tomato slices, onion slices, and pickles | 1 |
| your favorite jarred tomato sauce | 1 |
| your favorite marinara sauce or 1 1/2 cups crushed and strained san marzano tomato | 1 |
| your favorite spicy salsa or mexican tomato sauce | 1 |
| ½ pound cherry or grape tomato | 1 |

### garlic

| Canonical value | Recipes |
|---|---:|
| "toe" of garlic | 1 |
| * season the pork loin with salt, pepper, and if desired, a mojo (a mixture of sour orange juice, garlic, and spices) | 1 |
| *asafetida, a spice made from the resin of the giant fennel (ferula), has a strong, disagreeable smell from sulfur compounds, so a little goes a long way. its flavor after cooking is like the mildest, mellowest garlic you've ever tasted. asafetida is sold in lump and ground form and is available at indian and middle eastern markets or kalustyans.com. if unavailable, garlic powder makes a good substitute | 1 |
| *green garlic is young garlic before it begins to form cloves. it resembles a baby leek, with a long green top and white bulb, and has a milder flavor than mature garlic. if you can't find green garlic, mild elephant garlic makes a good substitute. use 4 large clove | 1 |
| *spanish chorizo is a smoked pork sausage flavored with garlic and spices, and milder than mexican chorizo. available at spanish markets and specialty foods stores | 1 |
| *spanish chorizo, a fresh, garlic-flavored pork link sausage that is milder than mexican chorizo, is available at spanish markets. linguiça, a similar portuguese sausage, is available at spanish and latin american markets | 1 |
| *thin japanese wheat noodles and chili paste with garlic are available at asian markets, specialty foods stores, and in the asian section of some supermarkets | 1 |
| - 6 garlic clove | 1 |
| -1/2 tablespoons garlic | 1 |
| -1/2 teaspoons (5 grams) minced garlic | 1 |
| -1/2 teaspoons extra-virgin olive oil or garlic oil | 1 |
| -1/2 tsp. minced garlic | 1 |
| -10 cups simmering lightly salted vegetable broth (made with 1 onion, 1 garlic clove, 1 carrot, 1 celery stalk, and a few parsley stems, cooked for 15 minutes) or simmering water | 2 |
| -12 slices garlic sausage or chorizo | 1 |
| -15 cloves garlic | 1 |
| -2 garlic clove | 1 |
| -20 large cloves garlic, thinly sliced | 1 |
| -3 cloves garlic | 1 |
| -3 cloves of garlic | 1 |
| -3 garlic clove | 1 |
| -3 tablespoons garlic powder | 1 |
| -4 garlic cloves (to taste), split, germ removed, and coarsely chopped | 1 |
| -4 garlic cloves, thinly sliced or minced | 1 |
| -4 heaped tsp crushed garlic | 1 |
| -4 large cloves garlic | 2 |
| -5 cloves garlic | 1 |
| -5 garlic clove | 1 |
| -6 cloves garlic | 1 |
| -7 cloves garlic | 1 |
| -8 peeled garlic clove | 1 |
| -cheese garlic bread | 1 |
| -cup fresh garlic | 1 |
| -inch piece fresh garlic | 1 |
| -inch piece of garlic | 1 |
| -inch-thick slices peeled garlic (from about 4 cloves) | 1 |
| -ounce chopped garlic | 3 |
| -ounce diced garlic | 1 |
| -ounce extra-virgin olive oil, infused with garlic | 1 |
| -ounce garlic | 6 |
| -ounce garlic clove | 1 |
| -ounce garlic oil | 1 |
| -ounce garlic powder | 2 |
| -ounce garlic puree | 1 |
| -ounce garlic puree (see recipe below | 1 |
| -ounce garlic salt | 1 |
| -ounce granulated garlic | 1 |
| -ounce minced garlic | 3 |
| -ounce peeled garlic | 1 |
| -ounce roasted garlic | 2 |
| -ounce toasted garlic and red wine vinaigrette | 1 |
| -tsp. garlic powder | 1 |
| / 4 to 1/2 cup garlic | 1 |
| /100 g garlic chives | 1 |
| /120 g quick garlic croutons | 1 |
| /60ml garlic-stuffed olives, halved | 1 |
| 1-pound piece garlic sausage | 1 |
| 1/2 cup garlic and herb cheese (recommended: boursin) | 1 |
| 12-ounce jar roasted red bell peppers in olive oil with garlic, drained | 1 |
| 14 1/2-ounce can diced tomatoes with roasted garlic | 1 |
| 14 1/2-ounce can diced tomatoes with roasted garlic in juice | 1 |
| 14 1/2-ounce cans diced tomatoes in juice with garlic, oregano, and basil | 1 |
| 14 1/2-ounce cans diced tomatoes with garlic, basil, and oregano in juice | 1 |
| 14 1/2-ounce cans diced tomatoes with green pepper and garlic or italian-recipe tomato | 1 |
| 14 1/2-ounce cans diced tomatoes with roasted garlic | 1 |
| 5-ounce package garlic-and-herb cheese spread (such as boursin) | 1 |
| 5-ounce package garlic-and-herb cheese spread (such as boursin), at room temperature | 1 |
| 5.2-ounce package boursin cheese with herbs and garlic | 1 |
| 5.3-ounce package basil and roasted garlic goat cheese or 6 ounces soft fresh goat cheese (such as montrachet) | 1 |
| a 6-ounce head of garlic, outer husk removed and 1/4 inch trimmed from the stem end | 1 |
| a dash or two of garlic powder | 1 |
| about 1 1/2 large heads garlic, separated into cloves (about 30) | 1 |
| about 3 ounces, boursin or other garlic and herb soft cheese | 1 |
| about 36 fat unpeeled garlic cloves (1 2/3 to 2 cups) or an equivalent amount of smaller cloves, plus 1 teaspoon minced garlic | 1 |
| about 5 teaspoons fermented black beans, or to taste, (or 1 heaping tablespoon prepared black bean garlic sauce - see head note) | 1 |
| about 6 cloves garlic | 1 |
| accompaniment: garlic bread made from remainder of italian loaf | 1 |
| accompaniment: garlic flavored melba toasts or assorted crudités | 1 |
| accompaniment: olive oil and garlic whipped potato | 1 |
| accompaniment: prepared garlic bread | 1 |
| accompaniment: sautéed greens with garlic | 1 |
| accompaniment: yogurt garlic sauce | 1 |
| accompaniment:broiled eggplant with garlic sauce | 1 |
| accompaniments if desired: stir-fried spinach with ginger and garlic and gruyere potato gratin | 1 |
| accompaniments: butter lettuce or other soft-leaf lettuce; thinly sliced garlic; packaged kimchi*; steamed white rice | 1 |
| accompaniments: chicken kebabs and cilantro garlic yogurt sauce | 1 |
| add half a garlic clove, if desired | 1 |
| additional garlic (optional) | 1 |
| adobo seasoning (equal parts garlic powder, onion powder, ground cumin, and salt)* | 1 |
| aioli (garlic mayonnaise) | 1 |
| almonds, garlic and hazelnuts, crushed together with a mortar and pestle | 1 |
| amore garlic paste, or 6 garlic clove | 1 |
| any or all of the following, cut into large chunks if necessary: 1/2 peeled onion, 1 small peeled carrot, 1 celery rib, a garlic clove, a bay leaf, a small tomato, a thyme sprig or two, parsley stems | 1 |
| aromatics and seasonings (recommended: garlic, fresh herbs, citrus zest, spices, etc.) | 1 |
| asafetida or minced garlic | 1 |
| asian chile paste with garlic | 1 |
| asian chile paste with garlic* | 1 |
| asian chile-bean paste with garlic (preferably lan chi) | 1 |
| asian chili garlic paste | 1 |
| asian chili garlic paste, such as sambal oelek | 1 |
| asian chili garlic sauce | 3 |
| asian chili garlic sauce, or to taste | 1 |
| asian chili paste with garlic | 1 |
| asian chili-garlic paste | 1 |
| asian chili-garlic sauce | 1 |
| asian chili-garlic sauce, such as sambal olek | 1 |
| asian fried garlic (optional) | 1 |
| asian garlic chile sauce or sriracha sauce | 1 |
| asian garlic chili paste | 2 |
| asian-style hot chili sauce (can be chili-garlic sauce) | 1 |
| asian-style sriracha chile-garlic sauce | 1 |
| assorted condiments, such as mango chutney, honey mustard, garlic mayonnaise, thinly sliced onion, thinly sliced cucumbers, and hot pepper sauce | 1 |
| bag (24-ounce) frozen garlic-seasoned potatoes, ore-ida steam n' mash | 1 |
| bag garlic and butter croutons | 1 |
| bag gourmet chips, preferred brand terra chips in yukon gold onion and garlic flavor | 1 |
| bag pre-cooked rosemary and garlic diced red potatoes (recommended: reser's) | 1 |
| bag reduced fat potato chips (recommended: cape cod brand or terra brand garlic and onion flavor yukon chips) | 1 |
| baguette sliced, rubbed with garlic and toasted | 2 |
| basil and garlic tomato pasta sauce (from 16 ounce jar) | 1 |
| bear's garlic | 1 |
| bear's garlic pesto, for serving, recipe follows | 1 |
| bear's garlic, for serving | 1 |
| bertolli® olive oil & garlic sauce | 1 |
| bertolli® vidalia onion with roasted garlic sauce | 1 |
| big garlic clove | 1 |
| birds eye® recipe ready chopped onions & garlic | 1 |
| bite-sized garlic-flavored bagel chips | 1 |
| black bean garlic paste | 1 |
| black bean garlic sauce | 7 |
| black bean garlic sauce (recommended: lee kum kee) | 1 |
| black bean garlic sauce* | 3 |
| black bean sauce with garlic | 2 |
| black garlic | 2 |
| black garlic paste | 1 |
| black pumpernickel roll with garlic (south philly hoagie style roll) | 1 |
| blanched garlic | 3 |
| blanched garlic clove | 1 |
| bottle chili-garlic sauce | 1 |
| bottle garlic and herb marinade | 1 |
| bottled chili-garlic sauce | 1 |
| bottled minced garlic | 10 |
| bottled minced garlic or 6 fresh clove | 1 |
| bottled minced garlic or 8 cloves minced | 1 |
| bottled roasted garlic | 1 |
| bouquet garni (1 clove garlic, bay leaf, shallot, 1/2 teaspoon peppercorns in cheesecloth tied with butcher's twine with extra string to tie to handle of pot) | 1 |
| bouquet garni (3 sprigs parsley, 3 bay leaves, 1/2 bunch thyme, 4 cloves garlic, 3 clove | 1 |
| bouquet garni including basil leaves, 2 whole garlic clove | 1 |
| bouquet garni including parsley, 1 teaspoon thyme, 2 cloves garlic, 12 peppercorns and a bay leaf | 1 |
| bouquet garni including: the stems and roots of a bunch of cilantro, bay leaf, smashed peeled garlic clove, 2 red chili | 1 |
| bouquet garni wrapped in cheesecloth with 4 unpeeled garlic clove | 1 |
| bouquet garni wrapped in cheesecloth: parsley sprigs, bay leaf and sprigs of fresh thyme (or dried), 10 whole black peppercorns and 8 cloves peeled garlic | 1 |
| bouquet garni, tied up in cheesecloth, whole head peeled garlic cloves, 2 teaspoons of dried fennel and a bay leaf | 1 |
| bouquet garni, wrapped in cheesecloth bay leaf, parsley, 2 cloves garlic and thyme | 1 |
| bouquet garni: 1 peeled clove garlic, 4 sprigs parsley, 1 bay leaf and 1 teaspoon dried rosemary or thyme, tied in cheesecloth | 1 |
| box garlic & parmesan or your favorite variety of mrs. t's® pierogies | 1 |
| box garlic herb shake and bake (recommended: kraft) | 1 |
| box risotto (try lundberg garlic primavera) | 1 |
| broiled tomato sauce with roasted garlic | 1 |
| brown chicken stock, made with extra oregano and garlic | 1 |
| brunoise garlic | 1 |
| bulb black garlic (about 5 or 6 cloves), cloves separated and peeled | 1 |
| bulb fresh garlic, separated into cloves and peeled | 1 |
| bulb garlic | 17 |
| bulb garlic cloves, separated and peeled | 1 |
| bulb garlic, cloves peeled and minced | 1 |
| bulb garlic, cloves separated | 2 |
| bulb garlic, cloves separated and peeled | 2 |
| bulb garlic, cut in half equatorially | 1 |
| bulb garlic, cut in half horizontally | 1 |
| bulb garlic, ends cut to expose the clove | 1 |
| bulb garlic, halved | 1 |
| bulb garlic, roasted | 2 |
| bulb garlic, separated and peeled | 1 |
| bulb garlic, unpeeled | 1 |
| bulb garlic, unpeeled and cut horizontally | 1 |
| bulb of garlic, cloves intact | 1 |
| bulb roasted garlic | 1 |
| bulb roasted garlic cloves, pulp removed | 1 |
| bulbs fresh garlic (skin off but broken, deep-fried until golden brown) | 1 |
| bulbs garlic | 5 |
| bulbs garlic, cloves separated and peeled | 3 |
| bulbs garlic, plus 2 clove | 1 |
| bulbs hardneck garlic (about 24 cloves), cloves separated and skin left on | 1 |
| bulbs of garlic | 2 |
| bulbs of garlic, unpeeled with the tops sliced off | 1 |
| bulbs of split roasted garlic | 1 |
| bulbs roasted garlic | 1 |
| bulbs roasted garlic (see note) | 1 |
| bulbs roasted garlic, cloves squeezed from skins and pasted | 1 |
| bulbs roasted garlic, split | 1 |
| bulbs spring garlic, shaved fine | 1 |
| bulbs, yes bulbs not cloves of garlic! (an extra bulb for the mashers) | 1 |
| cabot tomato basil cheddar, cabot garlic & herb cheddar and cabot sharp, or cabot horseradish cheddar, cabot smoky bacon cheddar and cabot seriously sharp, or cabot pepper jack, cabot habanero cheddar and cabot mozzarella shredded | 1 |
| caesar style or garlic flavor large croutons, crushed or processed into crumbs | 1 |
| cajun spices (2 teaspoons paprika, 2 teaspoons cayenne, 2 teaspoons garlic powder) | 1 |
| campbell's® condensed cream of mushroom with roasted garlic soup | 1 |
| can aylmer® accents® garlic and olive oil petite cut tomato | 1 |
| can condensed cream of mushroom soup with roasted garlic | 4 |
| can creamy potato with roasted garlic soup | 1 |
| can crushed tomatoes with garlic | 1 |
| can diced tomatoes with basil and garlic | 1 |
| can diced tomatoes with basil, garlic and oregano | 2 |
| can diced tomatoes with basil, garlic, and oregano | 2 |
| can diced tomatoes with basil, garlic, and oregano - drained | 1 |
| can diced tomatoes with basil, garlic, and oregano, drained | 1 |
| can diced tomatoes with garlic | 3 |
| can diced tomatoes with garlic and herbs | 1 |
| can diced tomatoes with garlic and olive oil | 1 |
| can diced tomatoes with garlic and onion | 6 |
| can diced tomatoes with garlic and onion, drained | 1 |
| can diced tomatoes with garlic, onion, and peppers, drained | 1 |
| can diced tomatoes with roasted garlic | 1 |
| can fire-roasted diced tomatoes with garlic | 1 |
| can hunt’s® diced tomatoes with basil, garlic and oregano, undrained | 1 |
| can italian-style diced tomatoes (such as hunt's® diced tomatoes with basil, garlic and oregano) | 1 |
| can no-salt-added diced tomatoes with basil, garlic, and oregano | 1 |
| can petite-cut diced tomatoes with garlic and olive oil | 1 |
| can red gold® petite diced tomatoes with garlic & olive oil, well drained | 1 |
| can roasted garlic flavored spaghetti sauce | 1 |
| can roasted garlic tomato paste | 1 |
| can stewed tomatoes (with garlic and herbs) | 1 |
| can swanson® seasoned chicken broth with roasted garlic | 2 |
| can tomato paste with roasted garlic | 1 |
| can tomato sauce with garlic and onion | 1 |
| canned roasted-garlic chicken broth or low-salt chicken broth | 1 |
| cans canned tomatoes, flavored with garlic | 1 |
| cans condensed cream of mushroom soup with roasted garlic | 2 |
| cans contadina® diced tomatoes with roasted garlic, undrained | 1 |
| cans diced tomatoes with basil, garlic and oregano | 1 |
| cans diced tomatoes with garlic and basil, drained | 1 |
| cans diced tomatoes with seasonings (green pepper and onion or garlic and oregano, or any flavor you want) | 1 |
| cans fire-roasted tomatoes with garlic (such as hunt's®), drained | 1 |
| cans pasta sauce with roasted garlic (recommended: hunt's) | 1 |
| cans petite-cut tomatoes with onions and roasted garlic, undrained | 1 |
| cans red gold® diced tomatoes with basil, garlic & oregano | 1 |
| cans red gold® petite diced tomatoes with garlic & olive oil | 1 |
| caramelized garlic: | 1 |
| carton campbell's® creamy herb & garlic with chicken stock soup | 1 |
| cheese garlic dressing (dry ingredients only) (recommended: good seasons) | 1 |
| chicken and garlic filling: | 1 |
| chicken sausages, any flavors or brand, such as sun-dried tomato or garlic | 2 |
| chicken stock [for a vegetarian soup, use garlic broth ] | 1 |
| chicken stock [or garlic broth for a meatless soup] | 1 |
| chicken stock or garlic broth, recipe follows | 1 |
| chile garlic sauce | 3 |
| chile paste (sambal oelek) or chinese garlic chile paste | 1 |
| chile-garlic flavored butter | 1 |
| chile-garlic paste | 1 |
| chile-garlic sauce | 8 |
| chile-garlic sauce (such as sambal oelek) | 1 |
| chile-garlic sauce (such as sambal), or to taste | 1 |
| chile-garlic sauce (such as sriracha) | 5 |
| chile-garlic sauce (such as sriracha) (optional) | 1 |
| chile-garlic sauce (such as sriracha), or to taste | 1 |
| chile-garlic sauce (such as sriracha®) | 20 |
| chile-garlic sauce (such as sriracha®) (optional) | 1 |
| chile-garlic sauce (such as sriracha®), or more to taste | 2 |
| chile-garlic sauce (such as sriracha®), or more to taste (optional) | 1 |
| chile-garlic sauce (such as sriracha®), or to taste | 4 |
| chile-garlic sauce, or to taste | 1 |
| chili garlic oil, recipe follows | 2 |
| chili garlic paste | 3 |
| chili garlic paste (recommended: sambal) | 1 |
| chili garlic paste recommended: sambal) | 1 |
| chili garlic sauce | 25 |
| chili garlic sauce (such as lee kum kee) | 1 |
| chili garlic sauce (such as lee kum kee®) | 1 |
| chili garlic sauce* | 1 |
| chili garlic sauce, for serving | 1 |
| chili garlic sauce, passed through a sieve | 1 |
| chili paste (blended hot chili peppers, garlic, oil and salt) | 1 |
| chili paste with garlic | 4 |
| chili paste with garlic* | 6 |
| chili-garlic paste | 1 |
| chili-garlic sauce | 22 |
| chili-garlic sauce (sambal oelek) | 1 |
| chili-garlic sauce or chili sauce | 2 |
| chili-garlic sauce* | 15 |
| chili-garlic sauce** | 1 |
| chili-garlic sauce, plus more for serving | 1 |
| chili-garlic sauce, such as sambal | 1 |
| chili-garlic sauce, such as sambal oelek | 1 |
| chinese black bean and garlic sauce | 2 |
| chinese black bean garlic sauce | 1 |
| chinese chile garlic paste (preferably lan chi) or sriracha (southeast asian chile sauce) plus additional for serving | 1 |
| chinese chile garlic paste (preferably lan chi), or to taste | 1 |
| chinese chile paste with garlic or sambal olek | 1 |
| chinese chili garlic paste | 1 |
| chinese chili paste with garlic | 2 |
| chive or wild garlic flowers | 1 |
| chopped cloves garlic | 1 |
| chopped fresh garlic | 56 |
| chopped fresh garlic (1 garlic clove) | 1 |
| chopped fresh garlic (about 3 cloves) | 1 |
| chopped fresh garlic clove | 1 |
| chopped fresh garlic, chives, or leeks | 1 |
| chopped garlic | 971 |
| chopped garlic (1 clove) | 1 |
| chopped garlic (2 cloves) | 5 |
| chopped garlic (2 to 3 cloves) | 1 |
| chopped garlic (3 cloves) | 4 |
| chopped garlic (4 to 5 cloves) | 2 |
| chopped garlic (6 cloves) | 3 |
| chopped garlic (9 cloves) | 7 |
| chopped garlic (about 1 head) | 1 |
| chopped garlic (about 2 large cloves) | 1 |
| chopped garlic (about 4 large cloves) | 1 |
| chopped garlic (about 7 to 8 cloves) | 1 |
| chopped garlic (about 8 cloves) | 1 |
| chopped garlic (about 8 large cloves) | 1 |
| chopped garlic (optional) | 1 |
| chopped garlic (partial clove with center removed) | 1 |
| chopped garlic and herb-marinated sun-dried tomato | 1 |
| chopped garlic and shallots | 1 |
| chopped garlic chives | 6 |
| chopped garlic chives (regular chives can be substituted) | 2 |
| chopped garlic chives or chives | 1 |
| chopped garlic chives, may substitute regular chives | 1 |
| chopped garlic clove | 16 |
| chopped garlic clove until smooth | 1 |
| chopped garlic cloves (3 cloves) | 1 |
| chopped garlic dill pickles | 1 |
| chopped garlic in water (from 4.5-oz jar) or 1 clove garlic | 1 |
| chopped garlic scapes | 2 |
| chopped garlic, (may reduce to be kid friendly) | 1 |
| chopped garlic, blanched | 1 |
| chopped garlic, mashed to a paste with 1/2 teaspoon salt | 1 |
| chopped garlic, or more to taste | 3 |
| chopped garlic, or to taste | 1 |
| chopped garlic, plus 3 cloves whole garlic | 1 |
| chopped garlic-stuffed green olives | 1 |
| chopped green garlic | 1 |
| chopped green garlic or 1 regular garlic clove, blanched | 1 |
| chopped green garlic or scallion | 1 |
| chopped green garlic, light parts | 1 |
| chopped green garlic, white and light green parts only | 1 |
| chopped leeks (white and pale green parts only) 1 garlic clove | 1 |
| chopped mixed fresh herbs such as chives and garlic chives (with blossoms if desired) and thyme, parsley, mint and summer savory leaf | 1 |
| chopped mixed fresh herbs such as chives and garlic chives (with blossoms if desired)and thyme, parsley, mint, and summer savory leaf | 1 |
| chopped or crushed garlic | 1 |
| chopped or minced garlic | 1 |
| chopped poached garlic | 1 |
| chopped roasted garlic | 7 |
| chopped spring garlic | 1 |
| chopped spring garlic (substitute green onions in off season) | 1 |
| chopped, fresh garlic | 1 |
| citrus-garlic roasted chicken breast and 2 thighs, or your favorite roasted or rotisserie chicken pieces (about 3 cups meat) | 1 |
| citrus-garlic roasted chicken breast or large roasted or rotisserie chicken breast | 1 |
| clove garlic | 2 |
| clove of garlic | 1 |
| cloves garlic | 15 |
| cloves garlic, crushed | 3 |
| cloves garlic, mashed | 1 |
| cloves garlic, reserved from garlic oil | 1 |
| cloves garlic, smashed | 1 |
| cloves garlic, whole | 7 |
| coarse garlic salt | 1 |
| coarsely chopped fresh garlic | 3 |
| coarsely chopped garlic | 12 |
| coarsely chopped garlic (2 cloves) | 1 |
| coarsely chopped garlic (6 cloves) | 1 |
| coarsely chopped garlic, plus 1 garlic clove, quartered | 1 |
| coarsely chopped garlic, plus 2 garlic cloves, quartered | 1 |
| coarsely chopped very fresh garlic, at room temperature | 1 |
| coarsely crushed garlic croutons | 1 |
| commercial garlic, smashed | 1 |
| commercially prepared chili garlic sauce (recommended: lee kum kee), or more or less to taste | 1 |
| container (4 ounces) garlic & herb spreadable cheese | 1 |
| container garlic and herb flavored soft cheese (recommended: boursin) | 1 |
| container garlic-and-herb spreadable cheese (such as boursin®) | 1 |
| container garlic-herb flavored cheese spread | 1 |
| container herb and garlic flavored cream cheese | 2 |
| cooked breakfast potatoes seasoned with red chili powder or flakes, paprika, and garlic | 1 |
| cooked white beans (see cannellini beans with garlic and sage ), drained | 1 |
| cooked white beans (see cannellini beans with garlic and sage ), drained, chilled | 1 |
| cooked white beans with 1/2 cup reserved cooking liquid (see cannellini beans with garlic and sage ) | 1 |
| cooking spray (extra-virgin olive oil with garlic) | 1 |
| country bread or sour dough, toasted or grilled and rubbed with garlic clove | 1 |
| crab boil (or mix together 1 teaspoon garlic powder, 1 teaspoon chili powder, 1 teaspoon cayenne) | 1 |
| cracked cloves garlic, plus 2 finely chopped clove | 1 |
| cracked fresh garlic | 1 |
| cracked garlic | 7 |
| cracker meal (seasoned with salt, pepper, and garlic powder) | 3 |
| creamy garlic and herb cheese (such as boursin) | 1 |
| creamy garlic dressing, recipe follows | 1 |
| creole garlic marinade (recommended: cajun injector garlic creole butter) | 1 |
| creole-style butter injectable marinade (such as tony chachere's roasted garlic & herb marinade®) | 1 |
| crispy garlic chips | 1 |
| croutons fried in garlic-flavored olive oil | 1 |
| crumbed garlic-and-herb feta cheese (about 1/2 cup) | 1 |
| crumbled garlic and herb feta cheese | 1 |
| crumbled garlic-and-herb feta cheese (about 2 ounces) | 1 |
| crushed clove garlic | 1 |
| crushed cloves garlic | 2 |
| crushed fresh garlic | 3 |
| crushed garlic | 255 |
| crushed garlic (optional) | 1 |
| crushed garlic (recommended: christopher ranch) | 7 |
| crushed garlic (recommended: christopher) | 1 |
| crushed garlic clove | 7 |
| crushed garlic croutons | 1 |
| crushed garlic flavored pretzels | 2 |
| crushed garlic, (recommended: christopher ranch) | 1 |
| crushed garlic, as needed | 1 |
| crushed garlic, in the skin | 1 |
| crushed garlic-and-butter flavor croutons | 1 |
| crushed garlic-flavored bagel chips | 1 |
| crushed garlic-herb croutons | 1 |
| crushed or chopped garlic | 1 |
| crushed or finely chopped garlic | 1 |
| crushed tomatoes with garlic | 1 |
| crushed tomatoes with oregano, basil, garlic | 1 |
| crusty bread or garlic bread, for passing at the table | 1 |
| crème fraîche, extra virgin olive oil, and leek or green garlic tops for garnish | 1 |
| cubes frozen crushed garlic, such as dorot, or 2 cloves garlic | 1 |
| cups chicken stock or beef stock or, in england, imported beef or meat stock [or garlic broth for a vegetarian soup] | 1 |
| cupsherb-garlic marinade | 1 |
| cut clove of peeled garlic | 2 |
| dash chile-garlic sauce (such as sriracha®) (optional) | 1 |
| dash chile-garlic sauce (such as sriracha®), or to taste | 1 |
| dash chili garlic sauce (such as sriracha®), or to taste | 1 |
| dash garlic powder | 28 |
| dash garlic powder, or to taste | 1 |
| dash garlic salt | 7 |
| dash garlic-flavored hot sauce (recommended: garlic-flavored tabasco) | 1 |
| dash habanero garlic hot pepper sauce | 1 |
| dash of garlic powder | 1 |
| dashes chile-garlic sauce (such as sriracha®), or to taste | 2 |
| dashes chile-garlic sauce, or to taste | 1 |
| dashes garlic powder | 6 |
| dehydrated garlic | 1 |
| dehydrated minced garlic | 1 |
| diced cooked smithfield® garlic & herb seasoned loin filet or sirloin roast | 1 |
| diced fresh garlic | 4 |
| diced garlic | 20 |
| diced garlic (9 cloves) | 1 |
| diced portuguese chourico (garlic-paprika sausage) | 1 |
| diced tomatoes with garlic and onion | 1 |
| dietz & watson ny state garlic cheddar | 1 |
| dijon mustard and minced garlic to taste | 1 |
| double-blanched garlic, recipe follows | 2 |
| dressing made with olive oil, balsamic vinegar, garlic | 1 |
| dried garlic | 2 |
| dried garlic and herb rub | 1 |
| dried garlic and herb rub with cajun spices | 1 |
| dried garlic flakes | 7 |
| dried garlic powder | 1 |
| dried granulated garlic | 2 |
| dried italian seasoning with garlic | 1 |
| dried minced garlic | 25 |
| dried minced garlic (optional) | 2 |
| dried onions or garlic, for seasoning | 1 |
| dried roasted garlic | 1 |
| drop garlic-infused oil (or any oil really) | 1 |
| drop minced garlic | 1 |
| drops liquid garlic | 1 |
| dry minced garlic | 1 |
| each garlic and onion powder | 1 |
| each garlic powder and onion powder | 1 |
| each garlic, bulbs | 1 |
| each granulated garlic, onion powder, ground ginger | 2 |
| each ground ginger and minced garlic | 1 |
| each minced fresh garlic and ginger | 1 |
| each minced garlic and fresh ginger | 3 |
| each minced garlic and ginger | 1 |
| each of grated ginger and garlic | 1 |
| each young leeks and green garlic, about 10 plants total, or 2 large leeks, white part only, and 1–2 cloves garlic | 1 |
| elephant ear garlic | 1 |
| elephant garlic | 6 |
| envelope (0.9 ounce) garlic-mushroom recipe soup mix | 1 |
| envelope herb and garlic soup mix (such as lipton®) | 1 |
| extra virgin olive oil or garlic oil | 1 |
| extra-virgin olive oil, plus 1 teaspoon for roasting garlic | 1 |
| extra-virgin olive oil, plus about 1 tablespoon for roasting garlic | 1 |
| extra-virgin olive oil, plus extra for roasting garlic | 1 |
| fat clove garlic | 1 |
| fat cloves garlic | 2 |
| fat cloves garlic, crushed to a paste | 1 |
| fat-free roasted garlic salad dressing | 1 |
| favorite spices (garlic, ginger, onion powder, etc.) | 1 |
| finely chop the garlic and pulverize in a pestle and mortar. gradually add olive oil and paprika until it becomes thick and creamy like mayonnaise | 1 |
| finely chopped cloves garlic | 2 |
| finely chopped flowering chives, flat chinese chives (garlic chives), or scallion | 1 |
| finely chopped fresh garlic | 11 |
| finely chopped garlic | 310 |
| finely chopped garlic (1 clove) | 1 |
| finely chopped garlic (1 large head) | 1 |
| finely chopped garlic (2 cloves) | 3 |
| finely chopped garlic (2 large cloves) | 1 |
| finely chopped garlic (3 cloves) | 2 |
| finely chopped garlic (3 to 4 cloves) | 1 |
| finely chopped garlic (5 cloves) | 1 |
| finely chopped garlic (about 2 cloves) | 1 |
| finely chopped garlic (about 2 teaspoons) | 1 |
| finely chopped garlic (about 3 large cloves) | 1 |
| finely chopped garlic (about 4 cloves) | 2 |
| finely chopped garlic (from 4 cloves) | 1 |
| finely chopped garlic chives | 2 |
| finely chopped garlic chives (regular chives can be substituted) | 1 |
| finely chopped garlic clove | 7 |
| finely chopped garlic cloves, separated into 2 parts | 1 |
| finely chopped garlic or half-sour pickles | 1 |
| finely chopped garlic plus 2 cloves, halved | 1 |
| finely chopped or crushed fresh garlic | 3 |
| finely chopped or grated garlic | 1 |
| finely chopped shallots and 1 clove garlic cooked until tender in 2 tablespoons butter | 1 |
| finely chopped very fresh garlic | 1 |
| finely chopped yellow or green garlic chives (6 oz) | 1 |
| finely crushed garlic | 1 |
| finely crushed garlic, or to taste | 1 |
| finely diced fresh garlic | 2 |
| finely diced garlic | 6 |
| finely diced garlic clove, plus 1 smashed | 1 |
| finely grated (with a microplane) garlic (8 cloves) | 1 |
| finely grated (with a rasp) garlic | 4 |
| finely grated clove garlic | 1 |
| finely grated garlic | 15 |
| finely grated garlic clove | 5 |
| finely grated or minced garlic | 1 |
| finely grated peeled garlic (use a rasp grater) | 1 |
| finely mashed roasted garlic | 1 |
| finely minced fresh garlic | 5 |
| finely minced fresh garlic (for spice rub) | 1 |
| finely minced garlic | 85 |
| finely minced garlic (2 large cloves) | 1 |
| finely minced garlic (about 2 heads) | 1 |
| finely minced garlic (from 1 small clove) | 1 |
| finely minced garlic clove | 1 |
| finely minced garlic, about 3 clove | 1 |
| finely sliced garlic | 2 |
| finely slivered garlic | 3 |
| finely-chopped garlic | 3 |
| finely-minced garlic | 1 |
| flaked garlic | 1 |
| flavorings such as jam, honey, dulce de leche, molasses, fresh or dried fruit, garlic, herbs, etc (optional) | 1 |
| for dipping: soy sauce, hoisin sauce, chili garlic sauce, and hot chinese-style mustard | 1 |
| for the garlic chile dip: | 1 |
| fourteen 1/4-inch-thick french bread slices (about 2 ounces of 1 baguette), toasted and rubbed with 1/2 garlic clove | 1 |
| frank's garlic pesto spread | 1 |
| freeze-dried garlic | 1 |
| fresh bear's garlic | 1 |
| fresh chopped garlic | 7 |
| fresh chopped garlic or crushed garlic from jar | 1 |
| fresh cloves garlic | 2 |
| fresh cracked black pepper, plus extra for roasted garlic | 1 |
| fresh crushed garlic | 5 |
| fresh garlic | 68 |
| fresh garlic chives | 2 |
| fresh garlic clove | 8 |
| fresh garlic cloves roughly chopped (for roasting) | 1 |
| fresh garlic cloves, pressed | 1 |
| fresh garlic coarsely chopped | 1 |
| fresh garlic sausage, cut into 8 slices | 1 |
| fresh garlic scapes | 1 |
| fresh garlic, crushed | 3 |
| fresh garlic, cut in 1/2 | 1 |
| fresh garlic, cut in half lengthwise | 1 |
| fresh garlic, smashed | 1 |
| fresh garlic, smashed open | 1 |
| fresh garlic-pork sausage (not sweet or very spicy) such as saucisson à l'ail au vin rouge,saucisse de canard à l'armagnac, or a mixture of the two | 1 |
| fresh ginger (squeeze through garlic press- reserve all liquid and solids for the mixture) | 1 |
| fresh ground garlic | 1 |
| fresh italian sausage, removed from casings and sauteed in extravirgin olive oil with minced onion and garlic | 1 |
| fresh lamb sausages, spicy italian sausages, or garlic sausages | 1 |
| fresh minced garlic | 16 |
| fresh morel mushrooms, sauteed in 1 teaspoon of olive oil and butter with 1 teaspoon chopped shallots and 1/2 teaspoon chopped garlic | 1 |
| fresh roasted garlic | 1 |
| freshly chopped garlic | 17 |
| freshly crushed garlic | 1 |
| freshly grated garlic | 1 |
| freshly grated nutmeg 1 bulb garlic* | 1 |
| freshly ground black pepper and 1/4 cup garlic powder | 1 |
| freshly minced garlic | 10 |
| freshly minced garlic (not jarred) | 1 |
| freshly minced garlic clove | 1 |
| freshly minced garlic, or more to taste | 1 |
| fried garlic | 1 |
| fried garlic and baby spinach saute, recipe follows | 1 |
| fried garlic chile oil | 1 |
| fried garlic chip | 1 |
| fried garlic chips | 6 |
| fried garlic chips, for garnish | 1 |
| fried sliced garlic | 1 |
| frieda's elephant garlic | 2 |
| from 1 head garlic | 1 |
| from 1 head of garlic, separated and peeled | 1 |
| from 6 heads of garlic | 1 |
| frozen mrs. t's potato and roasted garlic pierogis | 1 |
| frozen vegetable blend (no garlic or onions) | 1 |
| fully cooked smoked garlic sausage (such as kielbasa or linguiça), thinly sliced into rounds | 1 |
| garlic | 13,475 |
| garlic (1 grated, 2 sliced) | 1 |
| garlic (1 minced) | 1 |
| garlic (1 smashed and 1 minced) | 1 |
| garlic (2 chopped, 2 grated) | 1 |
| garlic (2 chopped, 2 smashed) | 1 |
| garlic (2 finely chopped, 1 grated) | 1 |
| garlic (2 minced, 2 smashed and peeled) | 1 |
| garlic (2 minced, 4 unpeeled) | 1 |
| garlic (2 smashed, 4 finely chopped) | 1 |
| garlic (2 smashed; 2 minced) | 1 |
| garlic (2 whole, 2 thinly sliced) | 2 |
| garlic (3 smashed, 3 sliced) | 1 |
| garlic (3 teaspoons) | 1 |
| garlic (3 to 4 heads), lightly smashed | 1 |
| garlic (4 minced, 1 whole) | 1 |
| garlic (4 minced; 1 whole) | 1 |
| garlic (4 smashed and finely chopped; 2 just smashed) | 1 |
| garlic (4 smashed, 1 minced) | 1 |
| garlic (6 smashed; 4 minced) | 1 |
| garlic (about 1 head) | 4 |
| garlic (about 2 heads) | 1 |
| garlic (finely minced in a wooden mortar and pestle) | 1 |
| garlic (optional) | 4 |
| garlic (or more to taste), crushed | 1 |
| garlic (peeled) | 2 |
| garlic (separated but not peeled or crushed) | 1 |
| garlic (skin on) | 1 |
| garlic (thinly sliced) | 1 |
| garlic (unpeeled) | 1 |
| garlic (unpeeled), smashed | 1 |
| garlic - minced | 1 |
| garlic - minced, or amount to taste | 1 |
| garlic - peeled and sliced | 2 |
| garlic 1 clove | 1 |
| garlic about 1 tablespoon minced | 1 |
| garlic aioli (recipe follows) | 1 |
| garlic aioli dipping sauce, recipe follows | 1 |
| garlic aioli sauce, recipe follows | 1 |
| garlic aioli, for serving, recipe follows | 1 |
| garlic aioli, recipe follows | 4 |
| garlic aioli: | 2 |
| garlic and chili oil, recipe follows | 1 |
| garlic and dried vegetable seasoning | 1 |
| garlic and herb cheese (recommended: boursin), 2 (5-ounce) containers | 1 |
| garlic and herb cheese (such as boursin or alouette) or, cream cheese, cut or crumbled into small pieces | 1 |
| garlic and herb cheese spread (such as boursin®) | 1 |
| garlic and herb croutons | 1 |
| garlic and herb dressing mix | 2 |
| garlic and herb flavored prepared bread crumbs | 2 |
| garlic and herb goat cheese, such as montrachet | 1 |
| garlic and herb or black peppercorn flavored soft cheese (recommended: boursin or alouette brand) | 1 |
| garlic and herb pork tenderloin | 1 |
| garlic and herb sauce mix (recommended: knorr) | 1 |
| garlic and herb seasoned dry bread crumbs | 3 |
| garlic and herb seasoning | 6 |
| garlic and herb seasoning (such as mccormick®) | 1 |
| garlic and herb seasoning (such as spike®) | 1 |
| garlic and herb seasoning blend | 5 |
| garlic and herb seasoning blend (such as mrs. dash®) | 7 |
| garlic and herb seasoning blend (such as mrs. dash®), or to taste | 3 |
| garlic and herb seasoning, or more to taste | 3 |
| garlic and herb soft cheese (recommended: boursin) | 1 |
| garlic and herb vinaigrette, recipe follows | 1 |
| garlic and herbs cheese spread, 6.5 ounces | 1 |
| garlic and hot pepper marinade | 1 |
| garlic and onion seasoning | 1 |
| garlic and parsley vinaigrette, recipe follows | 1 |
| garlic and peppercorn marinade seasoning (recommended: mccormick) | 1 |
| garlic and red chile paste, or more to taste | 1 |
| garlic and rosemary focaccia, recipe follows | 1 |
| garlic and saffron mayonnaise (rouille) , for serving | 1 |
| garlic basil spread | 1 |
| garlic basil spread (see footnote for recipe link) | 6 |
| garlic blend, gourmet garden® | 1 |
| garlic bread crumbs, recipe follows | 1 |
| garlic bread or italian butter bread, for serving | 2 |
| garlic bread pudding, recipe follows | 1 |
| garlic bread, for serving | 1 |
| garlic bread, recipe follows | 4 |
| garlic bread: | 1 |
| garlic broth | 1 |
| garlic broth, recipe follows | 1 |
| garlic bruschetta, recipe follows | 2 |
| garlic bulb | 6 |
| garlic bulb, cloves removed and peeled | 1 |
| garlic bulb, crushed | 1 |
| garlic bulb, cut in half | 2 |
| garlic bulb, halved | 4 |
| garlic bulb, halved horizontally | 1 |
| garlic bulb, quartered | 3 |
| garlic bulb, roasted | 1 |
| garlic bulbs | 2 |
| garlic butter | 8 |
| garlic butter (homemade or store-bought) | 1 |
| garlic butter crostini, for serving, recipe follows | 1 |
| garlic butter english muffins, recipe follows | 1 |
| garlic butter plus extra for bread, recipe follows | 1 |
| garlic butter sauce, recipe follows | 1 |
| garlic butter sauce: | 1 |
| garlic butter, recipe follows | 2 |
| garlic chicken stock, recipe follows | 1 |
| garlic chile paste | 2 |
| garlic chile paste, or to taste | 1 |
| garlic chili paste | 1 |
| garlic chili sauce | 5 |
| garlic chili sauce (recommended: sriracha) | 1 |
| garlic chili tomato butter, recipe follows | 1 |
| garlic chips | 1 |
| garlic chips, recipe follows | 2 |
| garlic chive butter | 1 |
| garlic chive or garlic flavored goat cheese, (recommend: surfing goat dairy rolling green) | 1 |
| garlic chives | 7 |
| garlic chives or scallion | 1 |
| garlic chives with blossoms | 1 |
| garlic chives, 2 cut into 1" pieces | 1 |
| garlic chives, cut into 1/2-inch pieces | 1 |
| garlic chives, cut into 2-inch lengths | 1 |
| garlic chives, white and tender green parts only | 2 |
| garlic chopped | 5 |
| garlic chopped fine | 2 |
| garlic chopped finely | 1 |
| garlic chopped in olive oil | 1 |
| garlic clove | 4,855 |
| garlic clove (optional), pressed | 1 |
| garlic clove 1 | 1 |
| garlic clove chopped | 1 |
| garlic clove if desired | 1 |
| garlic clove minced | 3 |
| garlic clove peeled | 3 |
| garlic clove put through a press | 2 |
| garlic clove, bruised | 1 |
| garlic clove, cracked away from its skin | 1 |
| garlic clove, creamed | 1 |
| garlic clove, crushed | 47 |
| garlic clove, crushed and peeled | 1 |
| garlic clove, crushed and skin removed | 1 |
| garlic clove, crushed into a paste | 1 |
| garlic clove, crushed through a press | 2 |
| garlic clove, crushed with a garlic press or minced | 2 |
| garlic clove, cut in 1/2 | 4 |
| garlic clove, cut in half | 2 |
| garlic clove, cut in half lengthwise | 1 |
| garlic clove, cut into thin slivers | 1 |
| garlic clove, cut into thin strips | 1 |
| garlic clove, flattened | 1 |
| garlic clove, forced through a garlic press | 5 |
| garlic clove, halved | 27 |
| garlic clove, halved (finely minced if whisking dressing by hand) | 1 |
| garlic clove, halved crosswise | 11 |
| garlic clove, halved lengthwise | 3 |
| garlic clove, halved lengthwise, germ removed if green, and garlic finely chopped | 1 |
| garlic clove, lightly crushed | 2 |
| garlic clove, lightly crushed with the side of a knife blade and quartered | 4 |
| garlic clove, lightly crushed with the side of a knife blade, and minced | 1 |
| garlic clove, lightly crushed with the side of a knife blade, and quartered | 1 |
| garlic clove, lightly crushed with the side of a knife blade, then minced | 1 |
| garlic clove, mashed | 2 |
| garlic clove, mashed and diced | 1 |
| garlic clove, mashed with a mortar and pestle | 1 |
| garlic clove, pounded with a pinch of salt | 1 |
| garlic clove, pressed | 47 |
| garlic clove, pressed in a garlic press or minced and mashed to a paste | 1 |
| garlic clove, pressed or finely chopped | 1 |
| garlic clove, pressed or minced | 3 |
| garlic clove, pureed with knife | 1 |
| garlic clove, quartered | 4 |
| garlic clove, roasted | 1 |
| garlic clove, smashed | 53 |
| garlic clove, smashed and finely chopped | 4 |
| garlic clove, smashed and finely minced | 1 |
| garlic clove, smashed and peeled | 2 |
| garlic clove, smashed and very finely chopped | 1 |
| garlic clove, smashed then minced | 2 |
| garlic clove, thinly sliced | 28 |
| garlic clove, unpeeled | 3 |
| garlic clove, very finely chopped | 3 |
| garlic cloves (2 whole, 3 chopped) | 1 |
| garlic cloves (20–25), smashed | 1 |
| garlic cloves (3 thinly sliced and 1 minced) | 1 |
| garlic cloves (about 1 1/2 heads) | 1 |
| garlic cloves (about 1 head), lightly smashed and peeled | 1 |
| garlic cloves (about 2 heads) | 1 |
| garlic cloves (about 3/4 cup) | 1 |
| garlic cloves (about 6), unpeeled | 2 |
| garlic cloves (chopped) | 2 |
| garlic cloves (from 2 heads) | 1 |
| garlic cloves (halved if large) | 1 |
| garlic cloves (unpeeled but crushed) | 1 |
| garlic cloves (unpeeled) | 2 |
| garlic cloves and/or an onion | 1 |
| garlic cloves chopped | 3 |
| garlic cloves coarsely chopped | 1 |
| garlic cloves crushed | 4 |
| garlic cloves finely chopped | 1 |
| garlic cloves finely grated using a microplane | 1 |
| garlic cloves forced through a garlic press | 1 |
| garlic cloves if desired | 1 |
| garlic cloves minced | 5 |
| garlic cloves more or less to taste | 1 |
| garlic cloves put through a press | 1 |
| garlic cloves thinly sliced | 2 |
| garlic cloves, 1 chopped and mashed to a paste with 1/2 teaspoon salt and 1 minced | 1 |
| garlic cloves, 1 clove minced | 1 |
| garlic cloves, 1 crushed and 1 chopped and mashed to a paste with 1/2 teaspoon salt | 1 |
| garlic cloves, 1 finely grated, 1 thinly sliced | 1 |
| garlic cloves, 1 finely grated, 6 left whole | 1 |
| garlic cloves, 1 halved and 1 minced | 1 |
| garlic cloves, 1 halved, 2 thinly sliced | 1 |
| garlic cloves, 1 left whole and 2 minced | 1 |
| garlic cloves, 2 crushed and 3 minced | 1 |
| garlic cloves, 2 finely chopped, 8 whole | 1 |
| garlic cloves, 2 minced and 2 coarsely chopped | 1 |
| garlic cloves, 2 minced, 2 thinly sliced | 1 |
| garlic cloves, 2 peeled, 2 peeled and crushed | 1 |
| garlic cloves, 2 whole, 4 finely chopped, 2 thinly sliced | 1 |
| garlic cloves, 3 crushed and 2 chopped | 1 |
| garlic cloves, 3 finely grated, 1 halved | 1 |
| garlic cloves, 3 peeled and 1 minced | 1 |
| garlic cloves, 3 thinly sliced and 1 halved crosswise | 1 |
| garlic cloves, 3 thinly sliced, 1 finely grated | 1 |
| garlic cloves, 4 halved, 4 finely chopped | 1 |
| garlic cloves, 4 smashed and 2 chopped | 1 |
| garlic cloves, 4 whole, 2 chopped | 1 |
| garlic cloves, 5 chopped and 2 left whole | 1 |
| garlic cloves, 5 finely chopped, 1 whole | 1 |
| garlic cloves, 5 smashed, 6 sliced | 1 |
| garlic cloves, 6 smashed, 6 finely chopped | 1 |
| garlic cloves, 7 cloves chopped, 1 clove finely grated | 1 |
| garlic cloves, as large as possible | 1 |
| garlic cloves, blanched and chopped finely (about 1 tablespoon) | 1 |
| garlic cloves, bruised but not peeled | 2 |
| garlic cloves, cooked in boiling water for 15 minutes, drained | 1 |
| garlic cloves, cooked slowly in olive oil until soft | 1 |
| garlic cloves, cracked | 1 |
| garlic cloves, crushed | 176 |
| garlic cloves, crushed (about 1/2 cup) | 1 |
| garlic cloves, crushed and chopped | 1 |
| garlic cloves, crushed and finely chopped | 3 |
| garlic cloves, crushed and finely chopped (2 teaspoons) | 1 |
| garlic cloves, crushed and finely minced | 1 |
| garlic cloves, crushed and left in skins | 1 |
| garlic cloves, crushed and minced | 4 |
| garlic cloves, crushed and peeled | 5 |
| garlic cloves, crushed and roughly chopped | 1 |
| garlic cloves, crushed in a garlic press | 2 |
| garlic cloves, crushed in a mortar or a garlic press | 1 |
| garlic cloves, crushed lightly | 1 |
| garlic cloves, crushed lightly and left whole | 1 |
| garlic cloves, crushed or minced | 2 |
| garlic cloves, crushed through a press | 1 |
| garlic cloves, crushed to a paste or finely chopped | 1 |
| garlic cloves, crushed under a knife and peeled | 2 |
| garlic cloves, crushed with 1 teaspoon salt | 1 |
| garlic cloves, crushed with a garlic press | 1 |
| garlic cloves, crushed with a garlic press or minced | 1 |
| garlic cloves, crushed with side of a large knife | 1 |
| garlic cloves, crushed with side of chef's knife | 1 |
| garlic cloves, crushed with side of knife | 1 |
| garlic cloves, crushed with the flat blade of a knife | 2 |
| garlic cloves, crushed with the side of a knife | 2 |
| garlic cloves, crushed with the side of a knife blade and minced | 1 |
| garlic cloves, crushed- use remaining pulp | 1 |
| garlic cloves, cut in 1/2 | 1 |
| garlic cloves, cut in half | 2 |
| garlic cloves, cut in julienne strips | 1 |
| garlic cloves, cut in quarters | 2 |
| garlic cloves, cut into slivers | 3 |
| garlic cloves, cut into strips | 1 |
| garlic cloves, cut into thin slivers | 1 |
| garlic cloves, cut lengthwise into slivers | 1 |
| garlic cloves, dried rosemary | 1 |
| garlic cloves, ends cut off | 1 |
| garlic cloves, finely mashed | 2 |
| garlic cloves, finely smashed | 1 |
| garlic cloves, flattened | 2 |
| garlic cloves, for rubbing beef | 1 |
| garlic cloves, forced through a garlic press | 6 |
| garlic cloves, forced through a garlic press or minced | 1 |
| garlic cloves, forced through a press | 2 |
| garlic cloves, forced through a press or finely chopped | 1 |
| garlic cloves, gently smashed | 1 |
| garlic cloves, halved | 34 |
| garlic cloves, halved and smashed | 1 |
| garlic cloves, halved and thinly sliced | 1 |
| garlic cloves, halved crosswise | 3 |
| garlic cloves, halved lengthwise | 1 |
| garlic cloves, halved plus 1 tablespoon minced garlic | 1 |
| garlic cloves, in their skin, crushed with the side of a knife blade | 1 |
| garlic cloves, left unpeeled | 6 |
| garlic cloves, left whole, plus 4 garlic clove | 1 |
| garlic cloves, lightly crushed | 14 |
| garlic cloves, lightly crushed and quartered | 1 |
| garlic cloves, lightly crushed with the side of a knife blade | 1 |
| garlic cloves, lightly crushed with the side of a knife blade and minced | 6 |
| garlic cloves, lightly crushed with the side of a knife blade and quartered | 5 |
| garlic cloves, lightly crushed with the side of a knife blade to release oils, then finely minced | 1 |
| garlic cloves, lightly crushed with the side of a knife blade, and quartered | 1 |
| garlic cloves, lightly smashed | 5 |
| garlic cloves, mashed | 8 |
| garlic cloves, mashed into a paste | 2 |
| garlic cloves, mashed into a paste with 1/8 teaspoon salt | 1 |
| garlic cloves, mashed or chopped | 2 |
| garlic cloves, mashed to a paste with 1 teaspoon salt | 1 |
| garlic cloves, mashed to a paste with 1/2 teaspoon salt | 1 |
| garlic cloves, mashed to a paste with 1/8 teaspoon salt | 2 |
| garlic cloves, mashed to a paste with a pinch of salt and extra-virgin olive oil | 1 |
| garlic cloves, minced1 head of garlic, cut horizontally through the middle | 1 |
| garlic cloves, minces | 1 |
| garlic cloves, mined and mashed to a paste with 1/2 teaspoon salt | 1 |
| garlic cloves, or garlic bulbs, cut in 1/2 equatorially | 1 |
| garlic cloves, or more to taste | 1 |
| garlic cloves, or to taste | 5 |
| garlic cloves, plus 1 crushed clove, plus 1 crushed clove | 1 |
| garlic cloves, plus 1 head garlic, roasted | 1 |
| garlic cloves, plus 10 crushed clove | 1 |
| garlic cloves, plus 2 garlic clove | 1 |
| garlic cloves, plus 5 garlic clove | 1 |
| garlic cloves, pounded with the side of a knife blade to release oils, then finely minced | 1 |
| garlic cloves, pressed | 85 |
| garlic cloves, pressed or finely chopped | 1 |
| garlic cloves, pressed or grated | 1 |
| garlic cloves, pureed | 2 |
| garlic cloves, put through a garlic press | 1 |
| garlic cloves, put through a press or minced | 1 |
| garlic cloves, quartered | 3 |
| garlic cloves, roasted | 11 |
| garlic cloves, roasted and peeled | 1 |
| garlic cloves, roughly chop | 1 |
| garlic cloves, shaved | 1 |
| garlic cloves, skin-on | 1 |
| garlic cloves, slice paper-thin | 1 |
| garlic cloves, slivered | 11 |
| garlic cloves, smashed | 156 |
| garlic cloves, smashed and chopped | 4 |
| garlic cloves, smashed and finely chopped | 10 |
| garlic cloves, smashed and finely chopped, plus 2 whole clove | 1 |
| garlic cloves, smashed and peeled | 14 |
| garlic cloves, smashed to a paste | 1 |
| garlic cloves, smashed with back of knife and peeled | 1 |
| garlic cloves, smashed with flat side of a knife | 1 |
| garlic cloves, smashed with the back of a knife | 1 |
| garlic cloves, smashed with the flat side of a knife | 1 |
| garlic cloves, smashed with the flat side of knife | 1 |
| garlic cloves, smashed with the side of a knife | 1 |
| garlic cloves, smashed with the side of a knife and peeled | 1 |
| garlic cloves, smashed, plus 2 heads garlic, halved | 1 |
| garlic cloves, smashed, plus 2 whole clove | 1 |
| garlic cloves, split | 1 |
| garlic cloves, thinly sliced | 198 |
| garlic cloves, thinly sliced crosswise | 3 |
| garlic cloves, thinly sliced lengthwise | 3 |
| garlic cloves, thinly sliced lengthwise (1/4 cup) | 1 |
| garlic cloves, thinly slices | 1 |
| garlic cloves, to rub on bread, plus 1 tablespoon garlic | 1 |
| garlic cloves, unpeeled | 41 |
| garlic cloves, unpeeled and crushed | 1 |
| garlic cloves, unpeeled and cut in half | 1 |
| garlic cloves, unpeeled, halved | 1 |
| garlic cloves, unpeeled, lightly crushed | 1 |
| garlic cloves, very finely chopped | 5 |
| garlic cloves, very finely chopped or pressed through a garlic press | 1 |
| garlic cloves, very finely minced | 2 |
| garlic cloves, very thinly sliced | 11 |
| garlic cloves, whole | 7 |
| garlic cloves, whole clove left unpeeled | 1 |
| garlic cloves: 1 halved and 2 minced | 1 |
| garlic cloves: 2 | 1 |
| garlic cloves: 8 | 1 |
| garlic cloves; 1 minced, 1 halved | 1 |
| garlic cloves; 1 minced, 2 thinly sliced | 1 |
| garlic cloves; 1 pressed, 1 minced | 1 |
| garlic cloves; 1 smashed, 2 chopped | 1 |
| garlic cloves; 2 chopped, 1 crushed | 1 |
| garlic cloves; 2 pressed, 3 minced | 1 |
| garlic cloves; 2 thinly sliced, 2 pressed | 1 |
| garlic cloves; 3 peeled, 1 minced | 1 |
| garlic cloves; 4 quartered, 3 whole | 1 |
| garlic cloves; 5 sliced, 3 chopped | 1 |
| garlic cloves; 6 peeled, 10 unpeeled | 1 |
| garlic coarsely chopped | 3 |
| garlic confit | 1 |
| garlic confit (see above) | 1 |
| garlic confit oil or vegetable oil, plus more for drizzling | 1 |
| garlic confit oil, or any flavored oil or vegetable oil | 1 |
| garlic confit, for garnish, recipe follows | 1 |
| garlic confit, recipe follows | 2 |
| garlic coves | 1 |
| garlic crostini, recipe follows | 1 |
| garlic croutons | 4 |
| garlic croutons, for serving | 1 |
| garlic croutons, recipe follows | 2 |
| garlic crushed | 7 |
| garlic dill pickle | 1 |
| garlic finely chopped | 4 |
| garlic finely chopped (optional) | 1 |
| garlic finely grated | 1 |
| garlic finely minced | 2 |
| garlic fingerling potatoes, recipe follows | 1 |
| garlic flakes | 4 |
| garlic flavored cream cheese spread | 1 |
| garlic flavored croutons | 1 |
| garlic flavored olive oil | 6 |
| garlic flavored olive oil, plus more as needed | 1 |
| garlic flavored processed cheese, cubed | 1 |
| garlic fried noodles, recipe follows | 1 |
| garlic fried yukon gold potatoes, recipe follows | 1 |
| garlic gloves | 3 |
| garlic gloves, crushed | 1 |
| garlic granules | 10 |
| garlic granules or freshly minced | 1 |
| garlic head | 6 |
| garlic head, halved | 4 |
| garlic head, halved and stuck with 2 clove | 1 |
| garlic head, halved crosswise | 2 |
| garlic head, halved horizontally | 1 |
| garlic head, halved lengthwise | 1 |
| garlic head, roasted and still warm | 1 |
| garlic head, roasted and still warm, recipe follows | 1 |
| garlic head, separated into cloves and peeled (about 14 cloves) | 1 |
| garlic head, split | 1 |
| garlic head, unpeeled | 2 |
| garlic head, unpeeled, halved and broken into clove | 1 |
| garlic heads | 4 |
| garlic heads, halved | 1 |
| garlic heads, in their skins, cut in half horizontally | 1 |
| garlic heads, outer skins discarded and heads intact | 1 |
| garlic herb butter | 1 |
| garlic herb butter, recipe follows | 1 |
| garlic herb cheese | 1 |
| garlic herb oil, for serving | 1 |
| garlic herb sauce mix (recommended: knorr) | 1 |
| garlic herb seasoned bread crumbs | 1 |
| garlic herb seasoning blend | 1 |
| garlic hot sauce (recommended: tabasco) | 1 |
| garlic hummus | 1 |
| garlic in jackets (skins) | 1 |
| garlic infused olive oil | 6 |
| garlic infused olive oil, plus more for toasting bread | 1 |
| garlic juice | 3 |
| garlic lemon potatoes, recipe follows | 1 |
| garlic lime broth, plus another 3 tablespoons | 1 |
| garlic mashed potato | 2 |
| garlic mashed potatoes with chives | 1 |
| garlic mashed potatoes, recipe follows | 4 |
| garlic mashed potatoes, serving suggestion, recipe follows | 1 |
| garlic mashed sweet potatoes, recipe follows | 1 |
| garlic mashed with 1 teaspoon salt | 1 |
| garlic mayo, recipe above | 1 |
| garlic mayo, recipe follows | 2 |
| garlic mayonnaise as an accompaniment, recipe follows | 1 |
| garlic mayonnaise for serving | 1 |
| garlic mayonnaise: | 1 |
| garlic minced | 21 |
| garlic minced or pressed | 1 |
| garlic minced to a fine paste | 1 |
| garlic mojo, recipe follows | 1 |
| garlic mushroom marinara sauce | 1 |
| garlic mustard seeds | 1 |
| garlic oil | 15 |
| garlic oil (1 or 2 cloves chopped and heated in 1/2 cup extra-virgin olive oil) | 2 |
| garlic oil (optional) | 1 |
| garlic oil (or vegetable oil) | 1 |
| garlic oil (see toasted garlic-beef stock) or olive oil, plus more for drizzling | 1 |
| garlic oil , for drizzling | 1 |
| garlic oil, or olive oil mixed with 1 minced garlic clove | 1 |
| garlic oil, reserved from garlic chips | 1 |
| garlic oil: | 1 |
| garlic olive oil | 3 |
| garlic olive or vegetable oil | 1 |
| garlic or 1 whole head | 1 |
| garlic or 1/2 teaspoon granulated garlic | 1 |
| garlic or to taste | 1 |
| garlic parmesan snack factory® pretzel crisps® | 1 |
| garlic paste | 40 |
| garlic paste (1 large clove with pinch kosher salt, mashed into paste) | 1 |
| garlic paste (fresh garlic chopped to a paste with a little salt) | 1 |
| garlic paste, (2 cloves garlic smashed with the flat side of a knife and a sprinkle of salt, to make paste) | 1 |
| garlic paste, (use half of the salt and 5 cloves garlic smashed with the flat side of a knife, to make paste) | 1 |
| garlic paste, made by blending 1 garlic clove with 1 tablespoon water | 1 |
| garlic paste, or 1 clove fresh garlic | 1 |
| garlic paste, or to taste | 1 |
| garlic paste, recipe follows | 1 |
| garlic peeled | 1 |
| garlic peeled and sliced paper thin | 1 |
| garlic peeled, but left whole | 1 |
| garlic pepper | 17 |
| garlic pepper blend | 2 |
| garlic pepper seasoning | 13 |
| garlic pepper seasoning, or to taste | 1 |
| garlic pepper to taste | 1 |
| garlic pepper, or to taste | 2 |
| garlic pita chips | 1 |
| garlic potato pancake, recipe follows | 1 |
| garlic powder | 3,242 |
| garlic powder (make sure it's powder not garlic salt) | 1 |
| garlic powder (optional) | 18 |
| garlic powder (such as mccormick® california style) | 1 |
| garlic powder or 1 clove garlic | 1 |
| garlic powder or 2 cloves garlic | 1 |
| garlic powder or garlic salt | 1 |
| garlic powder or granulated garlic | 2 |
| garlic powder or minced fresh garlic | 1 |
| garlic powder to taste | 87 |
| garlic powder to taste (optional) | 2 |
| garlic powder* | 2 |
| garlic powder, 2/3 palmful | 1 |
| garlic powder, for seasoning | 2 |
| garlic powder, for sprinkling | 1 |
| garlic powder, or 1 clove garlic | 1 |
| garlic powder, or 1 medium-size clove garlic | 1 |
| garlic powder, or 1 small clove garlic | 1 |
| garlic powder, or 2 cloves garlic | 1 |
| garlic powder, or 2 teaspoons fresh minced garlic | 1 |
| garlic powder, or more to taste | 12 |
| garlic powder, or more to taste (optional) | 2 |
| garlic powder, or to taste | 116 |
| garlic powder, or to taste (optional) | 7 |
| garlic powder, plus 1/2 tablespoon and 1 1/4 teaspoons | 1 |
| garlic powder, plus more for seasoning tomato | 1 |
| garlic powder, plus more for sprinkling | 1 |
| garlic powder, preferably roasted | 1 |
| garlic powder, to coat each steak | 1 |
| garlic power | 1 |
| garlic puree | 14 |
| garlic puree (about 2 cloves) | 1 |
| garlic put through garlic press | 1 |
| garlic red bliss mash, recipe follows, for serving | 1 |
| garlic roasted tomato spread (see footnote for recipe link) | 1 |
| garlic rosemary jelly | 1 |
| garlic rub | 1 |
| garlic saffron mayonnaise (see above) | 1 |
| garlic salt | 624 |
| garlic salt (optional) | 6 |
| garlic salt (recommended: lawry's brand) | 1 |
| garlic salt (recommended: lawry's) | 3 |
| garlic salt and black pepper | 1 |
| garlic salt and pepper to taste (optional) | 1 |
| garlic salt or minced garlic | 1 |
| garlic salt to taste | 44 |
| garlic salt to taste (optional) | 2 |
| garlic salt with parsley (such as lawry's®) | 1 |
| garlic salt, as needed | 2 |
| garlic salt, for seasoning | 1 |
| garlic salt, for seasoning spinach | 1 |
| garlic salt, for sprinkling | 2 |
| garlic salt, or more to taste | 6 |
| garlic salt, or to taste | 58 |
| garlic salt, or to taste (optional) | 2 |
| garlic sambal | 1 |
| garlic sauce, recipe follows | 1 |
| garlic sausage | 4 |
| garlic sausage (preferably saucisson a l'ail) | 1 |
| garlic sausage, cut into 2-inch lengths | 1 |
| garlic sausage, pricked | 1 |
| garlic scape | 1 |
| garlic scapes | 12 |
| garlic scapes (stalks), trimmed (optional) | 1 |
| garlic scapes, cut into 2-inch pieces | 1 |
| garlic sea salt (such as morton's®) | 1 |
| garlic seasoned croutons | 1 |
| garlic seasoning, such as t-boys garlic seasoning | 1 |
| garlic sliced | 2 |
| garlic sliced then mashed in salt to puree consistency | 1 |
| garlic sliced thin | 1 |
| garlic slivered, plus 1 clove garlic roughly chopped | 1 |
| garlic smashed | 2 |
| garlic spread (2 sticks of butter mixed with 1 tablespoon minced garlic) | 1 |
| garlic spread (recommended: lawry's) | 1 |
| garlic spread seasoning (such as johnny's® great caesar! garlic spread & seasoning) | 1 |
| garlic sprouts (optional) | 1 |
| garlic stuffed green olives | 1 |
| garlic stuffed olives | 1 |
| garlic tahini sauce, recipe follows | 1 |
| garlic thinly sliced | 1 |
| garlic toast, as an accompaniment | 1 |
| garlic toast, for serving, recipe follows | 1 |
| garlic toast, recipe follows | 1 |
| garlic toasts with red pepper aioli, recipe follows | 1 |
| garlic topping, recipe follows | 1 |
| garlic vinegar | 2 |
| garlic whipped boniato, recipe follows | 1 |
| garlic wine sauce, recipe follows | 1 |
| garlic wine vinegar | 1 |
| garlic, (about 2 heads) peeled | 2 |
| garlic, 1 finely grated, 2 smashed | 1 |
| garlic, 1 halved, 2 minced | 1 |
| garlic, 1 minced and 1 whole | 1 |
| garlic, 1 minced or grated, 1 cut in half for rubbing bread | 1 |
| garlic, 1 minced, 3 chopped | 1 |
| garlic, 1 sliced and 1 minced | 2 |
| garlic, 1 smashed and the other finely chopped | 1 |
| garlic, 1 thinly sliced and 1 finely grated | 1 |
| garlic, 1 whole and 2 finely chopped | 1 |
| garlic, 1/16-inch slices | 2 |
| garlic, 2 chopped and 1 crushed | 1 |
| garlic, 2 chopped or grated, 1 peeled | 1 |
| garlic, 2 chopped, 1 cracked away from skin | 1 |
| garlic, 2 chopped, 1 crushed | 1 |
| garlic, 2 chopped, 1 left whole | 1 |
| garlic, 2 chopped, 1 whole cracked from skin | 1 |
| garlic, 2 clove | 1 |
| garlic, 2 cloves finely chopped, 2 thinly sliced | 1 |
| garlic, 2 cloves minced and 1 clove smashed | 1 |
| garlic, 2 crushed and 3 finely chopped (1 tablespoon) | 1 |
| garlic, 2 crushed, 1 thinly sliced | 1 |
| garlic, 2 crushed, and 1 for rubbing | 1 |
| garlic, 2 finely chopped, 4 thinly sliced | 1 |
| garlic, 2 peeled and smashed, 1 minced | 1 |
| garlic, 2 smashed and 2 left whole without paper | 1 |
| garlic, 2 smashed and 4 minced | 1 |
| garlic, 2 smashed, 1 reserved whole | 1 |
| garlic, 2 thinly sliced and 1 whole | 1 |
| garlic, 2 thinly sliced, 1 halved | 1 |
| garlic, 2 whole and 2 smashed and finely chopped | 1 |
| garlic, 3 cloves sliced thin and 2 cloves minced | 1 |
| garlic, 3 minced and 2 sliced | 1 |
| garlic, 3 minced or grated, 3 crushed | 1 |
| garlic, 3 pressed and 3 chopped | 1 |
| garlic, 3 smashed and 1 finely grated | 1 |
| garlic, 3 smashed and 1 whole | 1 |
| garlic, 3 thinly sliced, 1 cracked from skin | 1 |
| garlic, 3 thinly sliced, 1 peeled | 1 |
| garlic, 4 peeled and smashed, 2 finely chopped | 1 |
| garlic, 4 peeled and smashed, 4 grated or minced | 1 |
| garlic, 4 smashed the other 2 thinly sliced | 1 |
| garlic, 4 smashed, 2 finely chopped | 1 |
| garlic, 4 whole and 3 smashed and finely chopped | 1 |
| garlic, 5 minced, 5 unpeeled, lightly crushed | 1 |
| garlic, 7 minced and 2 whole | 1 |
| garlic, bashed | 2 |
| garlic, blanched and shocked | 1 |
| garlic, bruised | 4 |
| garlic, bruised with the side of a knife | 1 |
| garlic, brunoise | 2 |
| garlic, chive or red pepper butter | 1 |
| garlic, cooked in boiling water for 5 minutes | 1 |
| garlic, cracked | 7 |
| garlic, cracked and chopped | 1 |
| garlic, cracked away from peel | 1 |
| garlic, cracked away from skin | 13 |
| garlic, cracked away from skin and crushed | 3 |
| garlic, cracked away from skin and finely chopped | 1 |
| garlic, cracked away from skin with a whack against the flat of your knife | 1 |
| garlic, cracked away from skin with a whack between flat of knife and heel of hand | 1 |
| garlic, cracked away from skins | 4 |
| garlic, cracked away from the skin | 2 |
| garlic, cracked from skin | 14 |
| garlic, cracked from skin and halved | 1 |
| garlic, cracked from skin and sliced | 1 |
| garlic, cracked from skins | 1 |
| garlic, cracked, for garnish | 1 |
| garlic, creamed to a paste with kosher salt | 1 |
| garlic, crush slightly but unpeeled | 1 |
| garlic, crushed | 809 |
| garlic, crushed (optional) | 1 |
| garlic, crushed (or more to taste) | 3 |
| garlic, crushed 1 large carrot | 1 |
| garlic, crushed and chopped | 10 |
| garlic, crushed and cracked away from the peels | 1 |
| garlic, crushed and divided | 1 |
| garlic, crushed and finely chopped | 15 |
| garlic, crushed and minced | 8 |
| garlic, crushed and pasted with salt | 1 |
| garlic, crushed and peeled | 9 |
| garlic, crushed and roughly chopped, plus 2 cloves garlic | 1 |
| garlic, crushed and split away from skins | 1 |
| garlic, crushed away from skin | 2 |
| garlic, crushed away from skins | 1 |
| garlic, crushed away from the skins | 1 |
| garlic, crushed but kept whole | 1 |
| garlic, crushed in garlic press | 1 |
| garlic, crushed into a paste | 1 |
| garlic, crushed lightly with the side of a knife blade and minced | 1 |
| garlic, crushed or chopped | 1 |
| garlic, crushed or finely chopped | 1 |
| garlic, crushed or minced | 1 |
| garlic, crushed or to taste | 6 |
| garlic, crushed salt | 1 |
| garlic, crushed to a paste | 4 |
| garlic, crushed under the flat of your knife with the heal if your hand | 1 |
| garlic, crushed with a chef's knife | 1 |
| garlic, crushed with a little salt | 1 |
| garlic, crushed with garlic press | 1 |
| garlic, crushed with peel on | 1 |
| garlic, crushed with press | 1 |
| garlic, crushed with skin on | 1 |
| garlic, crushed with skins still on | 1 |
| garlic, crushed with the back of a knife | 1 |
| garlic, crushed with the flat of a knife blade | 2 |
| garlic, crushed with the flat side of a knife | 1 |
| garlic, crushed with the side of a cleaver or minced | 1 |
| garlic, crushed with the side of a knife blade and minced | 1 |
| garlic, crushed, 2 cloves garlic | 1 |
| garlic, crushed, or more to taste | 7 |
| garlic, crushed, or to taste | 7 |
| garlic, crushed, plus 1 clove, split in 1/2 | 1 |
| garlic, crushed, plus 2 clove | 1 |
| garlic, crushed, plus 2 cloves for browning bread | 1 |
| garlic, crushed, plus 2 tablespoons, thinly sliced | 1 |
| garlic, crushed, plus 3 teaspoons minced garlic | 1 |
| garlic, cut in 1/2 | 5 |
| garlic, cut in half | 9 |
| garlic, cut in half lengthwise | 2 |
| garlic, cut in half lengthwise, plus 2 cloves, thinly sliced | 1 |
| garlic, cut in quarters | 2 |
| garlic, cut into 3 chunks each | 1 |
| garlic, cut into 3 pieces | 2 |
| garlic, cut into 3 pieces each | 1 |
| garlic, cut into chunks | 3 |
| garlic, cut into matchsticks, plus 1 more for pressing | 1 |
| garlic, cut into razor thin slices | 2 |
| garlic, cut into sixths | 1 |
| garlic, cut into slivers | 1 |
| garlic, cut into slivers and divided | 1 |
| garlic, cut into small chunks | 1 |
| garlic, cut into thick slivers | 1 |
| garlic, cut into thin slices | 2 |
| garlic, cut into thin slivers | 1 |
| garlic, cut into thirds | 1 |
| garlic, cut into very thin slices | 1 |
| garlic, cut into wafer thin slices | 1 |
| garlic, each cut into slivers | 1 |
| garlic, each sliced lengthwise into 4 pieces | 1 |
| garlic, finely pressed | 1 |
| garlic, finely shaved lengthwise | 1 |
| garlic, finely smashed | 2 |
| garlic, finely-minced | 1 |
| garlic, finelyminced | 1 |
| garlic, for rubbing | 1 |
| garlic, fresh | 1 |
| garlic, fresh minced | 1 |
| garlic, gently bruised | 1 |
| garlic, gently cracked from skin and very thinly sliced | 1 |
| garlic, gently crushed | 1 |
| garlic, gently crushed with the blade of a knife and quartered | 2 |
| garlic, gently crushed with the side of a knife and minced | 1 |
| garlic, gently smashed | 1 |
| garlic, gently smashed and paper removed | 1 |
| garlic, germ removed | 1 |
| garlic, germ removed and clove crushed with back of knife | 1 |
| garlic, granulated | 5 |
| garlic, ground | 1 |
| garlic, half grated or minced, the other half sliced | 1 |
| garlic, halved | 71 |
| garlic, halved and cut into slivers | 1 |
| garlic, halved and smashed | 2 |
| garlic, halved lengthwise | 4 |
| garlic, halved lengthwise, or more to taste | 1 |
| garlic, halved, for rubbing | 1 |
| garlic, halved, germs removed | 1 |
| garlic, halved, or more to taste | 2 |
| garlic, herbs and spices | 1 |
| garlic, in paper | 1 |
| garlic, in the husk | 1 |
| garlic, in the skin | 2 |
| garlic, intact and unpeeled | 1 |
| garlic, just crushed | 1 |
| garlic, knife pureed | 1 |
| garlic, left in their skins | 1 |
| garlic, left unpeeled | 2 |
| garlic, left whole | 3 |
| garlic, lightly crushed | 16 |
| garlic, lightly crushed with the side of a knife blade | 2 |
| garlic, lightly crushed with the side of a knife blade and minced | 10 |
| garlic, lightly crushed with the side of a knife blade and quartered | 3 |
| garlic, lightly crushed with the side of a knife blade, and minced | 5 |
| garlic, lightly crushed with the side of a knife blade, and quartered | 1 |
| garlic, lightly crushed with the side of a knife blade, then minced | 4 |
| garlic, lightly smashed | 11 |
| garlic, lightly smashed and halved | 1 |
| garlic, made into a paste | 4 |
| garlic, made into a paste with salt | 1 |
| garlic, mashed | 15 |
| garlic, mashed (see tip, below) | 1 |
| garlic, mashed and 1 clove | 1 |
| garlic, mashed and coarsely chopped (1 1/2 tsp) | 1 |
| garlic, mashed and diced | 1 |
| garlic, mashed and minced | 5 |
| garlic, mashed and then minced | 1 |
| garlic, mashed into a paste | 4 |
| garlic, mashed into a paste with 1 teaspoon salt | 1 |
| garlic, mashed into a paste with a little salt | 1 |
| garlic, mashed into a paste with some salt | 1 |
| garlic, mashed into paste with some salt | 1 |
| garlic, mashed to a paste | 5 |
| garlic, mashed to a paste with 1/2 teaspoon salt | 1 |
| garlic, mashed to a paste with a little salt | 1 |
| garlic, mashed to a paste with some salt | 1 |
| garlic, mashed to paste with mortar and pestle | 1 |
| garlic, mashed with a fork | 2 |
| garlic, mined | 1 |
| garlic, not too large | 1 |
| garlic, or more to taste | 22 |
| garlic, or more to taste, crushed | 1 |
| garlic, or to taste | 9 |
| garlic, papery outer layer still attached | 1 |
| garlic, pasted | 1 |
| garlic, pasted or grated | 1 |
| garlic, pierced with a toothpick | 1 |
| garlic, plus 1 tablespoon | 1 |
| garlic, plus 2 cloves garlic | 1 |
| garlic, plus 2 teaspoons minced | 1 |
| garlic, plus 3 cloves garlic | 1 |
| garlic, plus 4 cloves garlic minced | 1 |
| garlic, poached in hot water for 2 minutes and minced | 1 |
| garlic, popped from skin | 2 |
| garlic, popped from skin, 1 clove minced | 1 |
| garlic, popped from skins | 1 |
| garlic, potato, asparagus, or sorrel puree | 2 |
| garlic, pounded (1 tablespoon) | 1 |
| garlic, pounded into a paste with 1/2 teaspoon salt | 1 |
| garlic, pressed | 135 |
| garlic, pressed (optional) | 1 |
| garlic, pressed and divided | 2 |
| garlic, pressed or finely minced | 1 |
| garlic, pressed or grated | 1 |
| garlic, pressed or minced | 6 |
| garlic, pressed or smashed | 1 |
| garlic, pressed through garlic press or finely minced | 1 |
| garlic, pressed, or more to taste | 1 |
| garlic, pressed, plus 2 whole clove | 1 |
| garlic, pricked with a fork | 1 |
| garlic, pureed | 8 |
| garlic, pureed (very finely minced) | 1 |
| garlic, pureed or finely chopped | 1 |
| garlic, pureed with salt | 2 |
| garlic, pushed through a press | 3 |
| garlic, put through a garlic press | 1 |
| garlic, put through a garlic press or finely minced | 1 |
| garlic, quartered | 18 |
| garlic, roasted | 11 |
| garlic, roasted and minced | 1 |
| garlic, roasted and peeled | 1 |
| garlic, rough chop | 1 |
| garlic, rough chopped | 3 |
| garlic, roughly | 1 |
| garlic, roughly crushed | 1 |
| garlic, salt, white peppercorns | 1 |
| garlic, shaved | 1 |
| garlic, shaved thin | 1 |
| garlic, shaved very thin | 1 |
| garlic, skin intact | 2 |
| garlic, skin on | 2 |
| garlic, skin on and crushed | 1 |
| garlic, skin-on, smashed | 1 |
| garlic, skins on | 1 |
| garlic, skins removed, and roughly chopped | 1 |
| garlic, slightly bruised | 1 |
| garlic, slightly crushed and peeled | 1 |
| garlic, slightly crushed with the side of a knife blade, and minced | 1 |
| garlic, slivered | 16 |
| garlic, slivered, or to taste | 1 |
| garlic, smashed | 638 |
| garlic, smashed (unpeeled) | 2 |
| garlic, smashed and chopped | 25 |
| garlic, smashed and chopped 1/4 cup olive oil | 1 |
| garlic, smashed and chopped into a paste | 1 |
| garlic, smashed and chopped small | 1 |
| garlic, smashed and chopped to a paste | 4 |
| garlic, smashed and coarsely chopped | 3 |
| garlic, smashed and divided | 1 |
| garlic, smashed and finely chopped | 82 |
| garlic, smashed and finely chopped to a paste | 1 |
| garlic, smashed and finely diced | 2 |
| garlic, smashed and minced | 11 |
| garlic, smashed and pasted with salt | 1 |
| garlic, smashed and peeled | 27 |
| garlic, smashed and peeled (omit if using garlic broth) | 1 |
| garlic, smashed and quartered | 5 |
| garlic, smashed and roughly chopped | 9 |
| garlic, smashed and thinly sliced | 2 |
| garlic, smashed and turned into a paste | 1 |
| garlic, smashed away from skin and finely chopped | 1 |
| garlic, smashed away from skins | 1 |
| garlic, smashed beneath the flat of your knife with the heel of your hand, discard skins | 1 |
| garlic, smashed but left whole | 1 |
| garlic, smashed flat | 1 |
| garlic, smashed into a paste | 2 |
| garlic, smashed into a paste with the back of a chef's knife | 1 |
| garlic, smashed into a paste with the flat of a knife | 1 |
| garlic, smashed or finely minced | 1 |
| garlic, smashed to a paste | 17 |
| garlic, smashed to a paste or finely grated | 1 |
| garlic, smashed to a paste with a pinch of salt | 1 |
| garlic, smashed to a paste with coarse salt | 2 |
| garlic, smashed to a paste with salt | 1 |
| garlic, smashed with a pinch of salt and a little olive oil | 1 |
| garlic, smashed with heel your hand | 1 |
| garlic, smashed with salt until paste | 1 |
| garlic, smashed with some kosher salt to make a paste | 2 |
| garlic, smashed with the side of a knife | 1 |
| garlic, smashed with the side of your chef's knife | 1 |
| garlic, smashed, plus 1 clove for the bread | 1 |
| garlic, smashed, plus 2 clove | 1 |
| garlic, smashed, plus 4 clove | 1 |
| garlic, split | 3 |
| garlic, split in 1/2 and sliced paper thin | 1 |
| garlic, sweated | 1 |
| garlic, thickly sliced | 1 |
| garlic, thinly sliced | 412 |
| garlic, thinly sliced (optional) | 1 |
| garlic, thinly sliced crosswise | 1 |
| garlic, thinly sliced in rounds | 1 |
| garlic, thinly sliced or chopped | 2 |
| garlic, thinly sliced or finely chopped | 2 |
| garlic, thinly sliced or minced | 1 |
| garlic, thinly sliced to equal 3 tablespoons | 1 |
| garlic, thinly sliced, 1/16-inch | 1 |
| garlic, thinly sliced, plus 2 more, thinly sliced | 1 |
| garlic, thinly sliced, shallow fried on medium heat until light brown and crispy | 1 |
| garlic, toasted in dry skillet | 1 |
| garlic, trimmed but unpeeled | 1 |
| garlic, unpeeled | 60 |
| garlic, unpeeled and halved | 2 |
| garlic, unpeeled and smashed | 1 |
| garlic, unpeeled, cut in 1/2 | 1 |
| garlic, unpeeled, plus 4 clove | 1 |
| garlic, unpeeled, smashed | 3 |
| garlic, very finely chopped | 15 |
| garlic, very finely chopped or pressed through a garlic press | 1 |
| garlic, very finely minced | 2 |
| garlic, very thinly sliced | 8 |
| garlic, very thinly sliced, or more to taste | 1 |
| garlic, well minced | 1 |
| garlic, whacked with the side of a knife and peeled | 1 |
| garlic, whole | 12 |
| garlic, whole clove | 1 |
| garlic, with loose paper removed but unpeeled | 1 |
| garlic, worked into a paste | 1 |
| garlic, zested | 4 |
| garlic,smashed and chopped to a paste | 1 |
| garlic- peeled and cut in half | 1 |
| garlic-and herb-flavored soft cheese such as boursin | 1 |
| garlic-and-herb cheese spread (such as alouette) | 1 |
| garlic-and-herb cheese spread (such as boursin) | 1 |
| garlic-and-herb goat cheese | 1 |
| garlic-and-herb goat cheese (recommended: montrachet) | 2 |
| garlic-and-herb or plain goat cheese (recommended: montrachet) at room temperature | 1 |
| garlic-and-herb soft goat cheese (recommended: montrachet} | 1 |
| garlic-and-herb spreadable cheese (such as alouette®) | 1 |
| garlic-and-herbs spreadable cheese | 2 |
| garlic-cheese bread, for serving | 2 |
| garlic-chili paste | 1 |
| garlic-chipotle love, recipe follows | 1 |
| garlic-flavor bite-size bagel chips or regular-size bagel chips, broken into 1-inch pieces | 1 |
| garlic-flavor olive oil or olive oil | 2 |
| garlic-flavored croutons | 7 |
| garlic-flavored french dressing | 1 |
| garlic-flavored fried croutons | 1 |
| garlic-flavored hot pepper sauce (recommended: garlic-flavored tabasco) | 1 |
| garlic-flavored oil | 1 |
| garlic-flavored olive oil | 9 |
| garlic-flavored olive oil or regular olive oil | 1 |
| garlic-flavored olive oil, for brushing on both sides of bread slices | 1 |
| garlic-flavored olive oil, plus more as needed | 1 |
| garlic-ginger paste, recipe follows | 1 |
| garlic-herb cheese, such as boursin | 1 |
| garlic-herb naan or 1 pound store-bought pizza dough | 2 |
| garlic-herb wraps (recommended: mission), or any large tortilla | 1 |
| garlic-infused extra-virgin olive oil, plus more for garnish | 1 |
| garlic-infused olive oil | 7 |
| garlic-infused vegetable oil | 1 |
| garlic-infused virgin olive oil | 1 |
| garlic-lemon croutons | 1 |
| garlic-lime aioli, recipe follows | 1 |
| garlic-mint tapenade, recipe follows | 1 |
| garlic-mustard glaze, recipe follows | 1 |
| garlic-mustard habanero hot sauce* (see cook's note) | 1 |
| garlic-parmesan crostini, recipe follows | 1 |
| garlic-pepper seasoning | 2 |
| garlic-ranch salad dressing mix | 1 |
| garlic-rubbed crostini | 1 |
| garlic-scented croutons, recipe follows | 1 |
| garlic-seasoned rice wine vinegar | 1 |
| garlic-soy dipping sauce, recipe follows | 1 |
| garlic-stuffed olives | 1 |
| garlic; 1 chopped, 1 smashed | 2 |
| garlic; 1 minced, 2 sliced | 1 |
| garlic; 1 minced, 2 smashed | 1 |
| garlic; 1 smashed, 1 minced | 1 |
| garlic; 2 crushed, 2 minced | 1 |
| garlic; 2 minced, 8 smashed | 1 |
| garlic; 3 crushed, 2 chopped | 1 |
| garlic; 5 pressed, 2 finely chopped, 3 cracked | 1 |
| garnish: fresh anaheim chiles, small heads of garlic, and tomatillos | 1 |
| generous pinch garlic powder | 1 |
| ginger and garlic paste | 2 |
| ginger and garlic stir-fry oil or peanut oil | 1 |
| ginger garlic paste | 15 |
| ginger-garlic paste | 12 |
| ginger-garlic paste, recipe follows | 4 |
| ginger-garlic paste, recipe follows (or 1 tablespoon grated fresh ginger and 3 cloves garlic put through a garlic press or finely minced) | 2 |
| ginger-garlic paste, recipe follows (or 6 cloves garlic and 2-inch thumb ginger minced) | 1 |
| ginger-garlic paste, recipe follows, or 1 clove garlic and 1/2-inch piece ginger | 1 |
| ginger-garlic paste, recipe follows, or 2 teaspoons grated ginger | 1 |
| ginger-garlic-chile glaze, recipe follows | 1 |
| glove garlic | 2 |
| gloves garlic | 5 |
| gloves garlic minced | 1 |
| gloves garlic, crushed | 1 |
| gloves garlic, smashed | 1 |
| golden or green garlic chives | 1 |
| good size garlic clove | 1 |
| goya minced garlic | 8 |
| goya minced garlic or 2 cloves fresh garlic | 1 |
| goya minced garlic, or 2 cloves garlic | 1 |
| goya® minced garlic | 5 |
| goya® minced garlic or 6 cloves garlic | 1 |
| grand marnier seasoning, 5 cloves garlic; 2 small onion | 1 |
| granulated garlic | 388 |
| granulated garlic and salt | 1 |
| granulated garlic for seasoning, plus 1/2 cup | 1 |
| granulated garlic or garlic powder | 4 |
| granulated garlic or minced garlic | 1 |
| granulated garlic powder | 22 |
| granulated garlic, (not garlic powder) | 1 |
| granulated garlic, 1/3 palmful | 1 |
| granulated garlic, a palmful | 1 |
| granulated garlic, a scant palmful | 1 |
| granulated garlic, for seasoning | 3 |
| granulated garlic, half a palmful | 2 |
| granulated garlic, or 3 cloves fresh garlic, crushed | 2 |
| granulated garlic, or garlic powder | 1 |
| granulated garlic, or more to taste | 1 |
| granulated garlic, or to taste | 2 |
| granulated garlic, plus 1 tablespoon | 1 |
| granulated garlic, plus 1 teaspoon | 1 |
| granulated garlic, plus more for garnish | 1 |
| granulated or powdered garlic | 3 |
| grapeseed oil (1 tablespoon to saute the leeks, 1 tablespoon to saute the onion and garlic for the sauce, and 1 tablespoon to sear the scallops) | 1 |
| grated fresh garlic | 7 |
| grated garlic | 17 |
| grated garlic clove | 2 |
| grated garlic scape | 1 |
| grated or finely chopped garlic | 1 |
| grated small garlic clove | 1 |
| green garlic (about 1 pound) | 1 |
| green garlic (garlic scapes), cut into pieces | 1 |
| green garlic bulbs | 1 |
| green garlic bulbs, tops sliced off | 1 |
| green garlic bulbs, white and pale-green parts only, or 2 garlic cloves, thinly sliced | 2 |
| green garlic butter, recipe follows | 1 |
| green garlic chives (also called chinese chives; flat parts only), cut into 1 1/2-inch pieces (4 cups) | 1 |
| green garlic, 1/4 cup (3/4 oz/20 g) thinly sliced, or 4 cloves garlic | 1 |
| green garlic-stuffed olives (available in the deli section) | 1 |
| green oil (a blend of olive oil, garlic and parsley) | 1 |
| green onions or garlic scapes, thinly sliced | 1 |
| gremolata (equal parts minced garlic, parsley, and lemon zest) | 1 |
| grilled garlic bread, recipe follows | 1 |
| grilled or broiled italian or tuscan bread rubbed with garlic | 1 |
| grind the seafood seasoning, paprika, salt, celery seeds, chili powder, garlic powder, onion powder and pepper. mix together | 1 |
| ground garlic | 5 |
| habanero-toasted garlic vinaigrette, recipe follows | 1 |
| halved garlic clove | 3 |
| halved head of garlic | 2 |
| hand of garlic, halved | 1 |
| handful garlic, about 12 clove | 1 |
| harisa (tunisian hot chili paste of guajillo chili peppers, garlic, oil, caraway, and coriander) | 1 |
| head (8 to 10 cloves) garlic | 1 |
| head (about 12 medium cloves) garlic | 1 |
| head elephant garlic | 1 |
| head fresh garlic | 1 |
| head fresh garlic (squeeze it: it should be solid and very firm) | 1 |
| head garlic | 155 |
| head garlic (3 inches wide) | 1 |
| head garlic (6 cloves whole, remaining cloves smashed) | 1 |
| head garlic (about 10 to 12 cloves), lightly smashed | 1 |
| head garlic (about 20 cloves) | 1 |
| head garlic (halved crosswise) | 1 |
| head garlic (horizontally split) | 1 |
| head garlic broken into cloves and peeled | 1 |
| head garlic clove | 4 |
| head garlic cloves, separated and peeled | 1 |
| head garlic cloves, smashed | 1 |
| head garlic plus 6 clove | 1 |
| head garlic roasted | 3 |
| head garlic, 1/2 inch trimmed off top | 1 |
| head garlic, 1/4 inch sliced off the top, exposing clove | 1 |
| head garlic, about 6 cloves, smashed | 1 |
| head garlic, broken into clove | 4 |
| head garlic, broken into cloves and peeled | 1 |
| head garlic, broken into peeled clove | 1 |
| head garlic, broken into unpeeled clove | 2 |
| head garlic, broken up into cloves (with skin) | 1 |
| head garlic, cleaned | 1 |
| head garlic, cloves crushed | 2 |
| head garlic, cloves peeled | 6 |
| head garlic, cloves peeled and halved lengthwise | 1 |
| head garlic, cloves peeled and lightly smashed | 1 |
| head garlic, cloves peeled and separated | 1 |
| head garlic, cloves peeled and sliced | 2 |
| head garlic, cloves peeled and thinly sliced lengthwise | 1 |
| head garlic, cloves removed | 2 |
| head garlic, cloves removed and peeled | 2 |
| head garlic, cloves roughly chopped | 1 |
| head garlic, cloves separated | 9 |
| head garlic, cloves separated and crushed | 2 |
| head garlic, cloves separated and left unpeeled | 2 |
| head garlic, cloves separated and minced | 1 |
| head garlic, cloves separated and peeled | 9 |
| head garlic, cloves separated and skins removed | 1 |
| head garlic, cloves separated and smashed | 2 |
| head garlic, cloves separated but not peeled | 3 |
| head garlic, cloves separated, and peeled (about 16) | 2 |
| head garlic, cloves separated, crushed but unpeeled | 1 |
| head garlic, cloves separated, skin left on | 1 |
| head garlic, cloves smashed | 1 |
| head garlic, cloves smashed and peeled | 2 |
| head garlic, cracked | 1 |
| head garlic, crushed | 2 |
| head garlic, cut horizontally | 1 |
| head garlic, cut horizontally through the middle | 1 |
| head garlic, cut in 1/2 | 4 |
| head garlic, cut in 1/2 crosswise | 1 |
| head garlic, cut in 1/2 equatorially | 1 |
| head garlic, cut in 1/2 horizontally | 2 |
| head garlic, cut in 1/2, skins on | 1 |
| head garlic, cut in half | 6 |
| head garlic, cut in half (do not peel) | 2 |
| head garlic, cut in half crosswise | 2 |
| head garlic, cut in half crosswise, cloves separated | 1 |
| head garlic, cut in half horizontally | 6 |
| head garlic, cut in half lengthwise | 1 |
| head garlic, cut through the equator | 1 |
| head garlic, cut through the middle | 1 |
| head garlic, end cut off, brushed with olive oil and wrapped in aluminum foil | 1 |
| head garlic, end trimmed | 1 |
| head garlic, halved | 32 |
| head garlic, halved across the equator | 1 |
| head garlic, halved crosswise | 26 |
| head garlic, halved crosswise, plus 3 garlic clove | 1 |
| head garlic, halved crosswise, plus 4 clove | 1 |
| head garlic, halved crosswise; plus 2 clove | 1 |
| head garlic, halved horizontally | 13 |
| head garlic, halved horizontally, not peeled | 1 |
| head garlic, halved lengthwise | 3 |
| head garlic, halved through its equator | 1 |
| head garlic, halved through the equator | 1 |
| head garlic, halved, plus 5 cloves garlic | 1 |
| head garlic, halved, plus 6 cloves sliced | 1 |
| head garlic, left unpeeled and halved crosswise | 1 |
| head garlic, left unpeeled and halved horizontally | 1 |
| head garlic, left whole | 1 |
| head garlic, left whole with skin | 1 |
| head garlic, not peeled | 1 |
| head garlic, outer layer skin removed, cut in half horizontally, bulb still intact | 1 |
| head garlic, outer papery skin removed and halved crosswise | 1 |
| head garlic, peel intact, wrapped in foil | 1 |
| head garlic, plus 1 smashed garlic clove | 1 |
| head garlic, pressed | 1 |
| head garlic, roasted | 5 |
| head garlic, roasted* | 1 |
| head garlic, roasted, cloves separated | 1 |
| head garlic, roasted, cloves squeezed in a bowl | 2 |
| head garlic, separated into clove | 3 |
| head garlic, separated into cloves (unpeeled) | 1 |
| head garlic, separated into cloves and crushed | 1 |
| head garlic, separated into cloves and peeled | 4 |
| head garlic, separated into cloves, unpeeled | 1 |
| head garlic, separated into cloves, with skin left on | 1 |
| head garlic, separated into whole cloves, papery skin removed (about 20 cloves) | 1 |
| head garlic, smashed | 5 |
| head garlic, smashed, husk still attached | 2 |
| head garlic, split | 7 |
| head garlic, split horizontally | 2 |
| head garlic, split in 1/2 crosswise | 1 |
| head garlic, split through the equator | 2 |
| head garlic, top 1/4-inch sliced off | 1 |
| head garlic, top sliced off | 2 |
| head garlic, top third sliced off and discarded | 1 |
| head garlic, unpeeled | 1 |
| head garlic, unpeeled and cut in 1/2 crosswise | 3 |
| head garlic, unpeeled and cut in half crosswise | 2 |
| head garlic, unpeeled and cut into quarters | 1 |
| head garlic, unpeeled cloves separated and lightly crushed | 1 |
| head garlic, unpeeled, cut in 1/2 crosswise | 1 |
| head garlic, unpeeled, cut in half crosswise | 2 |
| head garlic, unpeeled, halved horizontally to expose the clove | 1 |
| head garlic, whole | 1 |
| head garlic, whole and unpeeled | 1 |
| head garlic, with skins, cut in half horizontally | 1 |
| head garlic, wrapped in foil | 1 |
| head garlic-smashed into a paste | 1 |
| head new garlic or 3 large regular garlic clove | 1 |
| head new garlic or 3 large regular garlic cloves, thinly sliced | 1 |
| head of elephant garlic, broken into clove | 1 |
| head of elephant garlic, cloves separated | 1 |
| head of fresh garlic, trimmed and chopped roughly, or 5 cloves dried garlic, papery skins removed | 1 |
| head of garlic | 17 |
| head of garlic (2 inches in diameter), cloves separated and left unpeeled | 1 |
| head of garlic (about 12 cloves) | 1 |
| head of garlic (about 15 cloves) | 1 |
| head of garlic (not separated into cloves) | 1 |
| head of garlic clove | 1 |
| head of garlic minced | 1 |
| head of garlic, 3 cloves sliced, remaining head halved crosswise | 1 |
| head of garlic, broken into clove | 2 |
| head of garlic, cloves crushed | 1 |
| head of garlic, cloves peeled | 1 |
| head of garlic, cloves peeled and thinly sliced | 1 |
| head of garlic, cloves peeled, crushed | 2 |
| head of garlic, cloves separated | 4 |
| head of garlic, cloves separated and left unpeeled | 1 |
| head of garlic, cloves separated and peeled | 3 |
| head of garlic, cloves separated, smashed | 1 |
| head of garlic, cloves separated, thinly sliced | 1 |
| head of garlic, cloves thinly sliced | 1 |
| head of garlic, crushed (with peel) | 1 |
| head of garlic, cut crosswise in half | 1 |
| head of garlic, cut in half crosswise | 2 |
| head of garlic, for sachet | 1 |
| head of garlic, halved | 6 |
| head of garlic, halved crosswise | 16 |
| head of garlic, halved crosswise; plus 2 garlic cloves, crushed | 1 |
| head of garlic, halved horizontally | 3 |
| head of garlic, most of outer skin removed, cut in half crosswise | 1 |
| head of garlic, outer skin removed, cut crosswise in half | 1 |
| head of garlic, separated into cloves and peeled | 1 |
| head of garlic, separated into cloves but not peeled | 1 |
| head of garlic, separated into cloves, unpeeled | 1 |
| head of garlic, unpeeled, halved crosswise | 1 |
| head of wild spring garlic (or 1 large garlic clove) | 1 |
| head peeled garlic clove | 1 |
| head pickled garlic | 1 |
| head plus 8 cloves garlic | 1 |
| head roasted garlic | 12 |
| head roasted garlic, cloves removed | 1 |
| head roasted garlic, cloves removed and mashed to a paste | 1 |
| head roasted garlic, cloves removed and peeled | 2 |
| head roasted garlic, cloves separated and peeled | 1 |
| head roasted garlic, mashed into a paste | 1 |
| head roasted garlic, pureed | 1 |
| head roasted garlic, recipe follows, cloves squeezed from the skins | 1 |
| head roasted garlic, removed from skins, recipe follows | 1 |
| head roasted garlic, squeezed from the skins | 1 |
| head spring garlic | 1 |
| head spring garlic or hard neck garlic, cloves peeled and thinly sliced | 1 |
| heads black garlic, cloves peeled and chopped | 1 |
| heads elephant garlic or regular garlic, seperated into cloves (unpeeled) | 1 |
| heads garlic | 65 |
| heads garlic (2 halved crosswise; 2 crushed and cloves separated) | 1 |
| heads garlic (3 inches wide) | 1 |
| heads garlic (unpeeled), top 1/2 inch trimmed | 1 |
| heads garlic broken into individual cloves, unpeeled | 1 |
| heads garlic clove | 1 |
| heads garlic cut in half | 1 |
| heads garlic, broken into cloves and peeled | 1 |
| heads garlic, cloves (about 30), separated but unpeeled | 1 |
| heads garlic, cloves peeled | 2 |
| heads garlic, cloves peeled (3/4 cup cloves) | 1 |
| heads garlic, cloves peeled and coarsely chopped (about 1/2 cup total) | 1 |
| heads garlic, cloves peeled and halved lengthwise | 2 |
| heads garlic, cloves peeled and halved lengthwise and any green sprouts from center discarded | 1 |
| heads garlic, cloves peeled and left whole | 1 |
| heads garlic, cloves peeled and trimmed | 1 |
| heads garlic, cloves separated | 3 |
| heads garlic, cloves separated and crushed | 1 |
| heads garlic, cloves separated and peeled | 4 |
| heads garlic, cloves separated and smashed | 1 |
| heads garlic, cloves separated but not peeled | 1 |
| heads garlic, cloves separated, smashed and peeled | 1 |
| heads garlic, cut in 1/2 crosswise | 2 |
| heads garlic, cut in 1/2 horizontally | 1 |
| heads garlic, cut in half | 1 |
| heads garlic, cut through the equator | 1 |
| heads garlic, ends trimmed to expose clove | 1 |
| heads garlic, halved | 6 |
| heads garlic, halved crosswise | 1 |
| heads garlic, halved crosswise (do not peel) | 1 |
| heads garlic, halved crosswise, outer paper removed | 1 |
| heads garlic, halved horizontally | 4 |
| heads garlic, halved horizontally, plus 5 garlic clove | 1 |
| heads garlic, halved lengthwise | 1 |
| heads garlic, halved with skins left on | 1 |
| heads garlic, not peeled or separated, cut in 1/2 through the clove | 1 |
| heads garlic, roasted | 1 |
| heads garlic, roasted and mashed into a paste | 1 |
| heads garlic, roasted, skinned and broken into clove | 1 |
| heads garlic, roasted; paper skin removed and cored | 1 |
| heads garlic, root removed, cloves separated | 1 |
| heads garlic, roots removed, not peeled | 1 |
| heads garlic, separated into cloves (unpeeled) | 1 |
| heads garlic, separated into cloves, unpeeled (do not use elephant garlic) | 1 |
| heads garlic, separated into unpeeled clove | 1 |
| heads garlic, separated into unpeeled cloves (about 25 cloves) | 1 |
| heads garlic, split in half | 1 |
| heads garlic, split in half horizontally | 1 |
| heads garlic, top 1-inch cut off | 1 |
| heads garlic, top 1/3 trimmed to expose clove | 1 |
| heads garlic, top 1/4-inch sliced off | 1 |
| heads garlic, top cut off to reveal clove | 1 |
| heads garlic, top third sliced off and discarded | 1 |
| heads garlic, tops sliced off | 1 |
| heads garlic, tops trimmed off to expose all of the clove | 3 |
| heads garlic, tops, removed | 1 |
| heads garlic, tough outer skins removed and halved lengthwise | 1 |
| heads garlic, unpeeled | 5 |
| heads garlic, unpeeled and halved crosswise, plus 6 cloves garlic | 1 |
| heads garlic, unpeeled and halved horizontally | 1 |
| heads garlic, unpeeled, but separated | 1 |
| heads garlic, unpeeled, halved horizontally | 1 |
| heads garlic, whole | 1 |
| heads green garlic,* toughest green part removed and coarsely chopped | 1 |
| heads of elephant garlic, cloves unpeeled, separated | 1 |
| heads of garlic | 4 |
| heads of garlic (not separated into cloves) | 1 |
| heads of garlic, broken apart but not peeled | 1 |
| heads of garlic, cloved | 1 |
| heads of garlic, cloves chopped | 1 |
| heads of garlic, cloves peeled | 3 |
| heads of garlic, cloves separated | 2 |
| heads of garlic, cloves separated and peeled | 1 |
| heads of garlic, cloves separated, papery skin removed (but cloves left unpeeled) | 1 |
| heads of garlic, cloves separated, root ends trimmed, unpeeled | 1 |
| heads of garlic, cloves separated, unpeeled | 1 |
| heads of garlic, halved crosswise | 5 |
| heads of garlic, halved horizontally | 1 |
| heads of garlic, separated into clove | 1 |
| heads of garlic, the outer skin removed, leaving the cloves attached at the root end | 1 |
| heads of garlic, top 1/4 inch of each cut off and discarded | 1 |
| heads of garlic, top 3/4 inch cut off to expose clove | 1 |
| heads of garlic, top 3/4 inch of each cut off and discarded | 1 |
| heads of garlic, unpeeled, cut in half horizontally to expose clove | 1 |
| heads peeled garlic | 1 |
| heads roasted garlic | 5 |
| heads roasted garlic, cloves removed | 2 |
| heads roasted garlic, cloves squeezed out (oven roasted: tops cut off, drizzled with olive oil, seasoned, wrapped in foil, roasted at 350 degrees f for 45 minutes, until soft and colored) | 1 |
| heads roasted garlic, recipe follows | 2 |
| heads roasted garlic, removed from cloves and creamed into a paste | 1 |
| heads roasted garlic, smashed | 1 |
| heads, plus 4 cloves garlic | 1 |
| heaping 1/4 cup very thinly sliced garlic | 1 |
| heaping 1/4 teaspoon garlic powder | 1 |
| heaping cup minced fresh garlic | 1 |
| heaping tablespoon chopped garlic | 3 |
| heaping tablespoon finely minced garlic | 1 |
| heaping tablespoon garlic and herb seasoning blend | 1 |
| heaping tablespoon garlic powder | 2 |
| heaping tablespoon ginger garlic paste, recipe follows | 1 |
| heaping tablespoon ginger garlic paste, recipe follows, or 6 cloves garlic | 1 |
| heaping tablespoon ginger/garlic paste, recipe follows | 1 |
| heaping tablespoon minced garlic | 1 |
| heaping tablespoon store-bought fried garlic pieces | 1 |
| heaping tablespoons fresh minced garlic | 1 |
| heat the oil in a medium saute pan over medium high heat. add the onions and cook until soft, about 4 minutes. add the garlic and cook for 30 seconds. stir in the piquillo peppers, season with salt and pepper, and cook 5 minutes | 1 |
| herb and garlic cream cheese | 1 |
| herb and garlic flavored cream cheese spread | 1 |
| herb and garlic marinade dressing | 1 |
| herb and garlic soft spreadable cheese | 1 |
| herb and garlic spreadable cheese or goat cheese | 1 |
| herb and garlic-flavored cream cheese | 1 |
| herb and oil marinated sun-dried tomatoes, pureed in a food processor, plus oil for griddle, preferably with garlic, herbs and dried tomato | 1 |
| herb oil (a blend of a few fresh sprigs thyme, rosemary, and parsley with 2 cloves of minced garlic, chile pepper and 1/2 cup olive oil) | 1 |
| herb-and-garlic cheese (such as boursin) | 1 |
| herb-garlic cheese, slightly softened | 1 |
| herb-garlic marinade, plus 1/4 cup, plus 1/4 cup, recipe follows | 1 |
| herb-garlic marinade, plus 3/4 cup, plus 1/4 cup recipe follows | 1 |
| honey garlic barbecue sauce | 1 |
| honey garlic chicken kabobs | 1 |
| honey garlic sauce | 1 |
| hoover alexander's smoked garlic vinaigrette, recipe follows, or low-fat italian dressing | 1 |
| hot chile garlic sauce (sambal) | 1 |
| hot chili garlic sauce | 1 |
| hot chili-garlic sauce, such as sriracha, plus more to taste | 1 |
| hot garlic vinaigrette, recipe follows | 1 |
| hot sauce, chile-garlic sauce | 1 |
| hot sauce, or oriental chili paste with garlic | 1 |
| hunt's® diced tomatoes with basil, garlic and oregano, undrained | 1 |
| hunt's® tomato sauce with basil, garlic and oregano | 1 |
| if not using ginger garlic paste, 6 cloves garlic | 1 |
| in a bowl, combine the tomatoes, onion, garlic, olive oil, lemon juice, basil, tarragon, salt, and pepper. add the croutons and toss well | 1 |
| ingredient info: elephant garlic, available at better supermarkets and at melissas.com, looks like garlic that's been supersized | 1 |
| ingredient info: harissa powder is a spice blend sold at middle eastern markets and at wholespice.com. if unavailable, combine 2 teaspoons ground coriander; 1 1/2 teaspoons ground ancho chiles; 1 teaspoon each garlic powder, paprika, and cumin; 1/2 teaspoon salt; and 1/4 teaspoon cayenne pepper | 1 |
| ingredient info: harissa powder is a spice blend sold at middle eastern markets, specialty foods stores, and online at wholespice.com. if unavailable, combine 2 teaspoons ground coriander; 1 1/2 teaspoons ancho chile powder; 1 teaspoon each garlic powder, paprika, and cumin; 1/2 teaspoon salt; and 1/4 teaspoon cayenne pepper | 1 |
| ingredient info: smoked paprika is available at some supermarkets, at specialty foods stores, and from latienda.com. smoked spanish chorizo is a pork-link sausage flavored with garlic and spices. it's available at specialty foods stores and spanish markets and from latienda.com. look for manchego cheese at supermarkets and specialty foods stores | 1 |
| ingredient info: spanish chorizo is a pork-link sausage flavored with garlic and spices but milder than mexican chorizo; it's available at specialty foods stores and spanish markets and from latienda.com. petit basque cheese is available at some supermarkets and at cheese stores | 1 |
| irvine spices garlic pepper | 3 |
| irvine spices roasted garlic pepper | 2 |
| irvine spices roasted garlic pepper seasoning | 6 |
| irvine spices roasted garlic pepper seasoning, as needed for rub | 1 |
| jar barilla garlic alfredo sauce | 1 |
| jar barilla® garlic alfredo sauce | 2 |
| jar barilla® roasted garlic sauce | 1 |
| jar bertolli® olive oil & garlic sauce | 1 |
| jar bottled minced garlic | 1 |
| jar butter and garlic injection sauce | 1 |
| jar chili-garlic sauce | 1 |
| jar chunky tomato sauce with onion and garlic | 1 |
| jar garlic and onion spaghetti sauce (such as ragu® robusto® sauteed onion & garlic pasta sauce) | 1 |
| jar garlic-and-tomato pasta sauce | 1 |
| jar minced garlic | 2 |
| jar onion and garlic spaghetti sauce | 1 |
| jar peeled whole garlic clove | 1 |
| jar pre-peeled garlic clove | 1 |
| jar ragu® chunky tomato, garlic & onion sauce | 1 |
| jar spaghetti sauce with garlic | 1 |
| jarred minced garlic | 8 |
| jarred minced garlic or fresh | 1 |
| jarred roasted garlic | 1 |
| jars bottled minced garlic | 1 |
| jars mushroom and garlic spaghetti sauce | 1 |
| jars tomato, onion, and garlic spaghetti sauce (such as prego®) | 1 |
| keebler ® town house ® flatbread crisps - roasted garlic crackers | 1 |
| keebler® town house® flatbread crisps - roasted garlic crackers | 2 |
| kernels fresh garlic, smashed | 2 |
| key lime garlic mayonnaise, recipe follows | 1 |
| kikkoman roasted garlic teriyaki marinade & sauce | 1 |
| kosher salt, plus a generous pinch for the garlic | 1 |
| kosher salt, plus extra for garlic and mushrooms | 1 |
| kosher salt, plus extra for roasted garlic | 1 |
| kraft deli deluxe process 3 cheese garlic & herb cheese slice | 3 |
| large bulb garlic | 2 |
| large bulb garlic, separated into unpeeled clove | 1 |
| large bulbs garlic | 1 |
| large cheese and garlic croutons | 1 |
| large clove garlic | 203 |
| large clove garlic - peeled | 1 |
| large clove garlic crushed | 1 |
| large clove garlic, cracked | 3 |
| large clove garlic, cracked away from skin | 2 |
| large clove garlic, crushed | 15 |
| large clove garlic, halved | 3 |
| large clove garlic, lightly crushed with the side of a knife blade and minced | 1 |
| large clove garlic, lightly crushed with the side of a knife blade and quartered | 3 |
| large clove garlic, mashed | 1 |
| large clove garlic, pasted or grated | 1 |
| large clove garlic, pressed | 4 |
| large clove garlic, quartered | 1 |
| large clove garlic, reserved from above, cracked away from skin | 1 |
| large clove garlic, smashed | 9 |
| large clove garlic, smashed and finely chopped | 1 |
| large clove garlic, smashed away from skin | 1 |
| large clove garlic, split in half | 1 |
| large clove garlic, thinly sliced | 4 |
| large clove garlic, very finely chopped or pressed through a garlic press | 1 |
| large clove minced garlic | 1 |
| large clove of garlic | 2 |
| large clove of garlic (chopped) | 1 |
| large clove of garlic, puréed and then mashed with 1/4 teaspoon salt | 1 |
| large clove of garlic, thinly sliced | 1 |
| large cloves chopped garlic | 1 |
| large cloves cloves garlic | 1 |
| large cloves cracked garlic, 2 cloves chopped garlic | 1 |
| large cloves fresh garlic | 3 |
| large cloves garlic | 383 |
| large cloves garlic clove, crushed | 1 |
| large cloves garlic or 4 small | 1 |
| large cloves garlic, 1 grated, 1 halved | 1 |
| large cloves garlic, 2 minced or pasted, 2 sliced | 1 |
| large cloves garlic, 8 whole and 3 chopped | 1 |
| large cloves garlic, blended to a paste with 1 tablespoon water | 1 |
| large cloves garlic, cracked | 1 |
| large cloves garlic, cracked away from skin | 6 |
| large cloves garlic, cracked away from skins and finely chopped | 3 |
| large cloves garlic, cracked from skin | 1 |
| large cloves garlic, cracked from skin and split | 1 |
| large cloves garlic, cracked from skins | 1 |
| large cloves garlic, crushed | 30 |
| large cloves garlic, crushed or minced | 1 |
| large cloves garlic, crushed plus 2 tablespoons chopped | 1 |
| large cloves garlic, cut in half | 1 |
| large cloves garlic, cut into slivers | 1 |
| large cloves garlic, either thinly sliced or finely chopped | 1 |
| large cloves garlic, flattened | 1 |
| large cloves garlic, germs removed | 1 |
| large cloves garlic, halved | 3 |
| large cloves garlic, lightly crushed | 1 |
| large cloves garlic, lightly crushed with the side of a knife blade and minced | 3 |
| large cloves garlic, lightly crushed with the side of a knife blade and quartered | 1 |
| large cloves garlic, lightly crushed with the side of a knife blade, then minced | 1 |
| large cloves garlic, lightly smashed | 1 |
| large cloves garlic, pasted | 1 |
| large cloves garlic, pasted or grated | 1 |
| large cloves garlic, pressed | 5 |
| large cloves garlic, quartered | 1 |
| large cloves garlic, quartered lengthwise | 1 |
| large cloves garlic, slivered | 1 |
| large cloves garlic, smashed | 11 |
| large cloves garlic, smashed and chopped | 3 |
| large cloves garlic, smashed and peeled | 3 |
| large cloves garlic, smashed and skinned | 1 |
| large cloves garlic, thinly sliced | 15 |
| large cloves garlic, thinly sliced or chopped | 1 |
| large cloves garlic, thinly sliced or grated | 1 |
| large cloves garlic, un-peeled | 1 |
| large cloves garlic, unpeeled | 4 |
| large cloves garlic, unpeeled, lightly crushed | 1 |
| large cloves garlic, very finely chopped | 1 |
| large cloves garlic, very thinly sliced | 3 |
| large cloves garlic. minced | 1 |
| large cloves hardneck or purple garlic, unpeeled | 1 |
| large cloves of garlic | 16 |
| large cloves of garlic unpeeled | 1 |
| large cloves of garlic, crushed | 1 |
| large cloves of garlic, cut | 1 |
| large cloves of garlic, thinly sliced | 1 |
| large cloves rough chopped garlic | 1 |
| large elephant ear garlic clove | 1 |
| large garlic | 2 |
| large garlic bulbs | 1 |
| large garlic clove | 1,131 |
| large garlic clove sliced | 1 |
| large garlic clove, blanched and minced | 1 |
| large garlic clove, crushed | 4 |
| large garlic clove, crushed and finely chopped | 1 |
| large garlic clove, crushed with a press | 1 |
| large garlic clove, cut in half | 1 |
| large garlic clove, flattened | 1 |
| large garlic clove, forced through a garlic press | 1 |
| large garlic clove, halved | 2 |
| large garlic clove, halved crosswise | 2 |
| large garlic clove, halved lengthwise | 4 |
| large garlic clove, lightly crushed with the side of a knife blade and minced | 1 |
| large garlic clove, mashed | 1 |
| large garlic clove, mashed to a paste | 2 |
| large garlic clove, mashed with the flat side of a knife | 1 |
| large garlic clove, or to taste | 1 |
| large garlic clove, pressed | 16 |
| large garlic clove, quartered | 1 |
| large garlic clove, roasted and peeled | 1 |
| large garlic clove, smashed | 10 |
| large garlic clove, smashed and skin removed | 1 |
| large garlic clove, smashed with flat side of a knife | 1 |
| large garlic clove, thinly sliced | 2 |
| large garlic clove, unpeeled | 1 |
| large garlic clove, very finely chopped | 1 |
| large garlic cloves (2 cloves finely chopped and 3 cloves chopped) | 1 |
| large garlic cloves (2 minced, 1 halved) | 1 |
| large garlic cloves (unpeeled) | 2 |
| large garlic cloves or 2 small | 1 |
| large garlic cloves or 4 small | 1 |
| large garlic cloves sliced thin | 1 |
| large garlic cloves, 1 minced and 1 halved | 1 |
| large garlic cloves, 2 cloves minced, 3 cloves smashed | 1 |
| large garlic cloves, 2 slivered, 2 flattened | 1 |
| large garlic cloves, 4 cloves peeled and left whole and 2 cloves coarsely chopped | 1 |
| large garlic cloves, 4 grated, 1 whole | 1 |
| large garlic cloves, coarsely crushed | 1 |
| large garlic cloves, crushed | 21 |
| large garlic cloves, crushed and chopped | 1 |
| large garlic cloves, crushed and minced to a paste | 1 |
| large garlic cloves, crushed and peeled | 1 |
| large garlic cloves, crushed or minced | 1 |
| large garlic cloves, cut into slivers | 1 |
| large garlic cloves, cut into thin slivers | 3 |
| large garlic cloves, cut lengthwise into 20 thin slices | 1 |
| large garlic cloves, each cut lengthwise into 4 slices | 1 |
| large garlic cloves, flattened | 2 |
| large garlic cloves, forced through a garlic press | 3 |
| large garlic cloves, ground to a fine paste with mortar and pestle | 1 |
| large garlic cloves, halved | 14 |
| large garlic cloves, halved lengthwise | 2 |
| large garlic cloves, left unpeeled | 1 |
| large garlic cloves, left unpeeled and forced through a garlic press | 1 |
| large garlic cloves, lightly crushed and peeled | 1 |
| large garlic cloves, lightly crushed with the side of a chef's knife, then peeled | 1 |
| large garlic cloves, or more to taste | 1 |
| large garlic cloves, pressed | 42 |
| large garlic cloves, pressed with a garlic press or finely chopped | 1 |
| large garlic cloves, put through a press or minced | 1 |
| large garlic cloves, quartered | 1 |
| large garlic cloves, quartered lengthwise | 1 |
| large garlic cloves, smashed | 12 |
| large garlic cloves, smashed and chopped | 4 |
| large garlic cloves, smashed and peeled | 2 |
| large garlic cloves, smashed flat | 1 |
| large garlic cloves, smashed with flat side of a large knife | 2 |
| large garlic cloves, thickly sliced | 7 |
| large garlic cloves, thinly sliced | 29 |
| large garlic cloves, thinly sliced (about 1/2 cup) | 1 |
| large garlic cloves, thinly sliced and fried | 2 |
| large garlic cloves, thinly sliced lengthwise | 6 |
| large garlic cloves, thinly sliced or minced | 1 |
| large garlic cloves, thinly slivered | 1 |
| large garlic cloves, unpeeled | 20 |
| large garlic cloves, very finely chopped | 1 |
| large garlic cloves, very thinly sliced | 2 |
| large garlic cloves, whole | 2 |
| large garlic cloves; 1 whole, 1 finely chopped | 1 |
| large garlic cloves; 3 chopped, 1 sliced | 1 |
| large garlic gloves | 1 |
| large garlic scapes | 1 |
| large half sour or garlic pickles | 1 |
| large head garlic | 18 |
| large head garlic (about 2 to 3 ounces) | 1 |
| large head garlic, cloves peeled and minced | 1 |
| large head garlic, cloves separated and peeled | 1 |
| large head garlic, cut in 1/2 horizontally through clove | 1 |
| large head garlic, left unpeeled, plus 4 large clove | 1 |
| large head garlic, separated into clove | 1 |
| large head garlic, separated into cloves (about 12) | 1 |
| large head garlic, separated into cloves and peeled | 1 |
| large head garlic, top sliced off | 1 |
| large head of fresh garlic, cut crosswise through center | 1 |
| large head of garlic | 1 |
| large head of garlic, cloves separated and peeled (about 21) | 1 |
| large head of garlic, halved crosswise | 1 |
| large head of garlic, outer skin peeled leaving the head intact | 1 |
| large head of garlic, separated into clove | 1 |
| large head of garlic, separated into individual clove | 1 |
| large head of garlic, top 1/2 inch cut off | 1 |
| large head of garlic, unpeeled, top 1/2 inch cut off to expose clove | 1 |
| large heads garlic | 7 |
| large heads garlic or 4 small, cut in half | 1 |
| large heads garlic, left whole, plus 3 garlic cloves, smashed | 1 |
| large heads garlic, unpeeled | 1 |
| large heads of garlic | 6 |
| large heads of garlic, 1/4 inch of root end cut off and discarded to expose clove | 1 |
| large heads of garlic, cut horizontally in half | 1 |
| large heads of garlic, halved crosswise | 1 |
| large heads of garlic, top 1/2 inch cut off | 1 |
| large heads of garlic, top 1/3 trimmed to expose clove | 1 |
| large heads of garlic, unpeeled, top 1/3 inch cut off to expose garlic | 1 |
| large minced garlic clove | 1 |
| large onion, squeezed through a garlic press | 1 |
| large or 2 small cloves garlic | 1 |
| large or 2 small heads garlic, separated into cloves and peeled | 1 |
| large or 3 medium cloves garlic | 1 |
| large or 3 small cloves garlic | 2 |
| large or 3 to 4 small cloves garlic | 1 |
| large peeled and very thinly sliced garlic clove | 1 |
| large unpeeled garlic clove | 5 |
| large whole clove garlic | 1 |
| large whole heads garlic | 1 |
| large-size garlic clove | 1 |
| lawry's® garlic powder with parsley | 1 |
| lawry's® herb & garlic marinade with lemon juice | 2 |
| lawry's® steak & chop marinade with garlic & cracked black pepper | 1 |
| lea & perrins® roasted garlic worcestershire sauce * | 1 |
| lee kum kee chili garlic sauce | 1 |
| leek and garlic fondue, recipe follows | 1 |
| leftover risotto from roasted garlic and mushroom risotto recipe | 2 |
| lemon garlic mayonnaise , for serving | 1 |
| lemon pepper garlic vinaigrette | 1 |
| lemon-pepper seasoning with garlic and onion | 1 |
| light garlic-and-herbs spreadable cheese | 2 |
| light roasted garlic and balsamic salad dressing | 1 |
| light roasted garlic balsamic salad dressing, plus 2 tablespoons divided | 1 |
| lime, garlic, and oregano mojo | 1 |
| lime-garlic salsa (recommended: pace) | 1 |
| lindsay® garlic stuffed spanish olives | 1 |
| little bit of minced garlic | 1 |
| loaf foccacia or garlic bread | 2 |
| loaf garlic bread | 1 |
| loaf garlic bread, homemade or store bought | 1 |
| loaf store-bought garlic bread, baked per package directions | 1 |
| mango garlic sauce, recipe follows | 1 |
| mango garlic seafood seasoning | 1 |
| marinated rib-eye slices, leftover from rib-eye marinated in garlic, anaheim chiles and | 1 |
| mashed and minced garlic | 1 |
| mashed and pureed garlic | 1 |
| mashed garlic | 6 |
| mashed garlic (about 8 large garlic cloves) | 1 |
| mashed garlic cloves, smashed | 1 |
| mashed garlic paste | 1 |
| mashed potatoes (i boiled 2 small red potatoes, then mashed it with 1/4 cup milk and 1/4 teaspoon garlic powder) | 1 |
| mayonnaise mixed with 1/2 teaspoon garlic powder | 1 |
| mccormick® garlic powder | 7 |
| mccormick® garlic salt | 2 |
| medium bulb garlic, end cut off, 1 clove reserved | 1 |
| medium clove garlic | 11 |
| medium clove garlic, smashed | 1 |
| medium clove minced garlic | 1 |
| medium cloves garlic | 52 |
| medium cloves garlic cloves garlic | 1 |
| medium cloves garlic, 1 minced and 1 thinly sliced | 1 |
| medium cloves garlic, cracked | 1 |
| medium cloves garlic, crushed | 5 |
| medium cloves garlic, ground into a paste with kosher salt or grated | 1 |
| medium cloves garlic, pressed into a paste | 1 |
| medium cloves garlic, smashed | 1 |
| medium cloves garlic, thinly sliced | 4 |
| medium cloves garlic, thinly sliced (about 2 tablespoons) | 1 |
| medium cloves garlic, unpeeled | 2 |
| medium cloves garlic, very finely chopped | 1 |
| medium cloves garlic,smashed | 1 |
| medium cloves of garlic | 1 |
| medium garlic clove | 79 |
| medium garlic clove, halved | 1 |
| medium garlic clove, halved lengthwise | 1 |
| medium garlic clove, or to taste | 1 |
| medium garlic clove, pressed or finely grated | 1 |
| medium garlic cloves (about 3 heads) | 1 |
| medium garlic cloves garlic, smashed | 1 |
| medium garlic cloves minced | 2 |
| medium garlic cloves, crushed | 3 |
| medium garlic cloves, crushed in a press | 1 |
| medium garlic cloves, each cut in 1/2 lengthwise | 1 |
| medium garlic cloves, halved | 1 |
| medium garlic cloves, pressed | 4 |
| medium garlic cloves, skin on | 1 |
| medium garlic cloves, smashed | 10 |
| medium garlic cloves, smashed and peeled | 4 |
| medium garlic cloves, split | 2 |
| medium garlic cloves, thinly sliced | 13 |
| medium garlic cloves, thinly sliced (about 1 tablespoon) | 1 |
| medium garlic cloves, unpeeled | 1 |
| medium head garlic | 15 |
| medium head garlic - peeled and sliced | 1 |
| medium head garlic, cloves peeled, half the cloves minced, half sliced | 1 |
| medium head garlic, unpeeled | 1 |
| medium head of garlic | 2 |
| medium head of garlic, cloves peeled and thinly sliced | 1 |
| medium heads garlic | 10 |
| medium heads garlic, left whole | 1 |
| medium heads garlic, separated into cloves, unpeeled | 1 |
| medium heads of garlic, separated into clove | 1 |
| medium heads unpeeled garlic | 1 |
| medium jars spaghetti sauce with roasted garlic | 1 |
| medium roasted garlic clove | 1 |
| medium spring garlic bulbs, 1-2 garlic scapes, or 2 regular garlic cloves, thinly sliced | 1 |
| medium whole cloves garlic, halved | 1 |
| medium-size clove garlic | 1 |
| medium-size cloves garlic | 3 |
| medium-size garlic cloves, crushed | 1 |
| medium-sized bulbs garlic | 1 |
| minced (3 large cloves) garlic | 1 |
| minced and mashed garlic | 1 |
| minced clove garlic | 4 |
| minced clove of garlic | 3 |
| minced fresh garlic | 99 |
| minced fresh garlic (3 cloves) | 1 |
| minced fresh garlic chives or regular chives | 1 |
| minced fresh garlic, plus 1 tablespoon | 1 |
| minced fresh green garlic or 1 garlic clove | 1 |
| minced garlic | 3,059 |
| minced garlic (1 clove) | 1 |
| minced garlic (1 small clove) | 1 |
| minced garlic (2 cloves) | 19 |
| minced garlic (2 large cloves) | 2 |
| minced garlic (2 medium cloves) | 1 |
| minced garlic (3 cloves) | 30 |
| minced garlic (3 large cloves) | 1 |
| minced garlic (3 to 4 large cloves) | 1 |
| minced garlic (4 cloves) | 16 |
| minced garlic (4 or 5 large cloves) | 1 |
| minced garlic (4 to 5 cloves) | 2 |
| minced garlic (4 to 6 cloves) | 1 |
| minced garlic (5 to 6 cloves) | 1 |
| minced garlic (6 cloves) | 7 |
| minced garlic (6 to 8 cloves) | 1 |
| minced garlic (8 large cloves) | 1 |
| minced garlic (8 to 12 cloves) | 1 |
| minced garlic (9 cloves) | 2 |
| minced garlic (about 1 large clove) | 3 |
| minced garlic (about 1/2 clove) | 2 |
| minced garlic (about 1/2 small clove) | 1 |
| minced garlic (about 2 cloves) | 3 |
| minced garlic (about 2 large cloves) | 1 |
| minced garlic (about 2 teaspoons) | 1 |
| minced garlic (about 3 cloves) | 3 |
| minced garlic (about 3 cloves), mashed to a paste with side of a large heavy knife | 1 |
| minced garlic (about 3 to 4 cloves) | 2 |
| minced garlic (about 6 cloves) | 1 |
| minced garlic (about 6 large cloves) | 1 |
| minced garlic (about 6 to 9 garlic cloves) | 4 |
| minced garlic (about 9 large cloves) | 1 |
| minced garlic (about three cloves) | 1 |
| minced garlic (from 1 to 2 cloves) | 1 |
| minced garlic (from 1 to 2 heads) | 1 |
| minced garlic (from about 4 medium cloves) | 1 |
| minced garlic (from about 5 large cloves) | 1 |
| minced garlic (optional) | 5 |
| minced garlic (or to taste) | 1 |
| minced garlic chives | 1 |
| minced garlic clove | 18 |
| minced garlic fresh herbs | 1 |
| minced garlic from a jar | 1 |
| minced garlic in olive oil | 1 |
| minced garlic in water (from a jar) | 1 |
| minced garlic mashed with 1/4 teaspoon salt | 1 |
| minced garlic or 3 cloves fresh garlic | 1 |
| minced garlic or garlic paste | 1 |
| minced garlic or garlic powder | 1 |
| minced garlic or garlic puree | 1 |
| minced garlic or pickled garlic | 1 |
| minced garlic plus 1 head of garlic, cloves separated | 1 |
| minced garlic plus 1 whole clove | 1 |
| minced garlic plus 2 clove | 1 |
| minced garlic, (1 or 2 cloves) | 1 |
| minced garlic, about 2 clove | 1 |
| minced garlic, lightly sauteed in olive oil | 1 |
| minced garlic, mashed to a paste with 1/2 teaspoon salt | 1 |
| minced garlic, mashed to a paste with 1/4 teaspoon salt | 1 |
| minced garlic, mashed to paste | 1 |
| minced garlic, or 1 clove grated | 2 |
| minced garlic, or 2 to 3 teaspoons granulated garlic | 2 |
| minced garlic, or more to taste | 9 |
| minced garlic, or to taste | 33 |
| minced garlic, or to taste (optional) | 1 |
| minced garlic, plus 1 teaspoon | 1 |
| minced garlic, plus 1/4 cup | 1 |
| minced garlic, plus 2 cloves chopped | 1 |
| minced garlic, plus 2 teaspoons | 2 |
| minced garlic, raw | 1 |
| minced or crushed garlic | 2 |
| minced organic garlic | 1 |
| minced peeled garlic | 1 |
| minced roasted garlic | 4 |
| minced roasted garlic, recipe follows | 1 |
| minced roasted garlic, see cook's note | 1 |
| minced shallots or garlic | 1 |
| minced smoked garlic | 1 |
| minced, fresh garlic chives | 1 |
| mined garlic, or to taste | 1 |
| mixed good olives, preferably manzanillas, kalamatas or green garlic | 1 |
| mixed olives, pitted and mixed with 2 chopped cloves garlic, oregano, and parsley | 1 |
| mixed sausages (such as sweet italian, kielbasa, and smoked garlic) | 1 |
| mixed scallion, garlic and onion | 1 |
| mixed vegetables (such as scallions, garlic scapes, romano beans, halved small eggplants, halved baby or new potatoes) | 1 |
| montrachet goat cheese, with garlic and herbs | 1 |
| mrs. dash® garlic & herb seasoning blend | 4 |
| mrs. dash® garlic and herb seasoning blend | 2 |
| muffuletta bun spread with garlic butter | 2 |
| mussels, steamed in wine with 3 sprigs parsley, 3 sprigs thyme, and 1 clove crushed garlic | 1 |
| nigella seeds are available at indian markets or online. tahini sauce stir garlic, tahini, lemon juice, oil, and 1/4 cup water in a small bowl; season with salt | 1 |
| nigella seeds, poppy seeds, cumin seeds, sesame seeds, or chopped garlic (optional) | 1 |
| of 24-ounce purchased basil-garlic-seasoned polenta roll | 1 |
| of 3 heads of garlic | 1 |
| of 5.2-ounce package boursin or other french garlic-and-herb cheese, cut into 6 wedges | 1 |
| of chopped garlic | 3 |
| of combined basil, olive oil, pine nuts, parmesan cheese and garlic blended very well (i.e., pesto) | 1 |
| of cream of aji (6 to 9 ajies in the blender with salt, 1 clove of garlic, ground black pepper, and 1/2 cup oil) | 1 |
| of finely chopped garlic | 3 |
| of fresh garlic | 1 |
| of garlic | 84 |
| of garlic (1 smashed and 1 minced) and 1 bay leaf | 1 |
| of garlic (unpeeled) | 1 |
| of garlic chopped | 2 |
| of garlic finely minced | 1 |
| of garlic in fine dice | 1 |
| of garlic mashed fine | 1 |
| of garlic peeled | 1 |
| of garlic powder | 2 |
| of garlic salt | 1 |
| of garlic sliced thin | 1 |
| of garlic smashed and chopped | 1 |
| of garlic, crushed | 4 |
| of garlic, crushed with skin on | 1 |
| of garlic, crushed with the flat end of a knife | 1 |
| of garlic, cut into slivers | 1 |
| of garlic, halved | 1 |
| of garlic, left whole | 1 |
| of garlic, lightly bruised and peeled | 1 |
| of garlic, mashed | 1 |
| of garlic, mined | 1 |
| of garlic, pealed | 1 |
| of garlic, thinly sliced | 7 |
| of garlic, thinly slivered | 1 |
| of garlic, unpeeled and lightly bruised | 1 |
| of garlic, very finely mashed into a paste with 1/4 teaspoon coarse salt | 1 |
| of minced garlic | 2 |
| of peeled garlic | 2 |
| of roasted garlic | 2 |
| of very finely chopped fresh garlic | 1 |
| oil-packed minced garlic | 2 |
| olive oil (garlic-infused oil will yield more flavor) plus 1 tablespoon | 1 |
| olive oil (preferably infused with garlic) | 1 |
| olive oil 3 heads garlic | 1 |
| olive oil mixed with 4 cloves crushed garlic | 1 |
| olive oil or garlic-flavored olive oil | 1 |
| olive oil which has been mixed with 1 crushed garlic clove | 1 |
| olive oil, enough to sauté garlic and onion | 1 |
| olive oil, for roasting garlic | 1 |
| olive oil-packed minced garlic | 1 |
| one 14.5-ounce can diced tomatoes with basil, garlic and oregano | 1 |
| one 26-ounce can garlic and herbs spaghetti sauce | 1 |
| one 9-ounce package cheese and roasted garlic tortellini | 1 |
| onion and garlic mix | 5 |
| onion and garlic yukon gold potato chips, (preferred brand: terra chips) | 1 |
| onion and garlic-flavored croutons | 1 |
| onion powder teaspoon garlic powder | 1 |
| onion sprouts or garlic chive sprouts (2 cups) | 1 |
| onion-and garlic-seasoned croutons | 1 |
| onions, shallots and garlic | 1 |
| or 1 head, garlic, cloves separated but not peeled | 1 |
| or 1 large head garlic | 1 |
| or 2 cloves garlic | 1 |
| or 2 garlic clove | 2 |
| or 2 heads garlic | 1 |
| or 3 cloves garlic | 7 |
| or 3 cloves garlic, crushed | 2 |
| or 3 cloves garlic, smashed | 1 |
| or 3 cloves garlic, very finely chopped | 1 |
| or 3 fresh garlic clove | 1 |
| or 3 large cloves garlic | 1 |
| or 3 large cloves garlic, crushed | 1 |
| or 3 large cloves garlic, smashed | 1 |
| or 3 large garlic clove | 1 |
| or 3 large garlic cloves, or to taste | 1 |
| or 3 large garlic cloves, put through a garlic press (about 1 teaspoon garlic puree) | 1 |
| or 3 leaves fresh sage, very thinly sliced or mashed together with the garlic using a mortar and pestle | 1 |
| or 3 medium garlic clove | 1 |
| or 3 slices eggplant, marinated in extra-virgin olive oil, garlic, and spices, and grilled | 1 |
| or 3 slices french bread or garlic bread, toasted and cut into croutons | 1 |
| or 4 cloves garlic | 7 |
| or 4 cloves garlic (to taste) | 1 |
| or 4 cloves garlic, cracked from skin | 1 |
| or 4 cloves garlic, slivered | 1 |
| or 4 garlic clove | 1 |
| or 4 whole heads garlic, left unpeeled and halved horizontally | 1 |
| or 5 cloves fresh garlic | 1 |
| or 5 cloves garlic | 2 |
| or 5 garlic cloves, crushed | 1 |
| or 5 garlic cloves, cut into small dice | 1 |
| or 5 large garlic clove | 2 |
| or 5 rounds of french bread rubbed with 1/2 clove garlic (optional) | 1 |
| or 6 cloves garlic | 1 |
| or 6 cloves garlic, crushed | 1 |
| or 6 cloves garlic, smashed | 1 |
| or 6 garlic clove | 1 |
| or 7 large garlic clove | 1 |
| or more chili-garlic sauce | 1 |
| or more cloves garlic, mashed and chopped | 1 |
| or more garlic clove | 2 |
| or more of garlic paste | 1 |
| organic diced tomatoes with basil and garlic, drained, muir glen® | 1 |
| organic garlic powder | 1 |
| package al fresco® all natural roasted garlic chicken sausage | 1 |
| package boursin garlic-herb cheese | 1 |
| package boursin garlic-herb cheese, chilled | 1 |
| package cheese and garlic dry salad dressing mix | 1 |
| package chicken sausage (preferably garlic-flavored), cut into 1-inch pieces | 1 |
| package crumbled garlic and herb feta cheese | 1 |
| package frozen garlic bread | 1 |
| package garlic and herb cheese spread (such as boursin®) | 1 |
| package garlic and herb cheese spread (such as boursin®), crumbled | 1 |
| package garlic and herb crumbled feta (recommended: athenos) | 1 |
| package garlic and herb salad dressing mix | 1 |
| package garlic and mushroom soup mix | 2 |
| package garlic cheese spread | 2 |
| package garlic croutons | 2 |
| package garlic flavored instant mashed potato | 1 |
| package garlic herb cheese spread | 1 |
| package garlic-herb cheese such as boursin, at room temperature | 1 |
| package green giant® garlic & herb mashed cauliflower | 2 |
| package herb and garlic feta, crumbled | 2 |
| package herb and garlic soup mix | 3 |
| package herb and garlic-flavored cream cheese | 1 |
| package idahoan® butter & herb or roasted garlic mashed potato | 1 |
| package idahoan® roasted garlic flavored mashed potato | 1 |
| package idahoan® roasted garlic flavored mashed potatoes, dry | 5 |
| package idahoan® roasted garlic flavored mashed potatoes, prepared | 1 |
| package market pantry™ frozen garlic herb chicken breasts, thawed according to package directions | 1 |
| package pre-cooked rosemary and garlic potatoes (recommended: reeser's) | 1 |
| package pre-cooked sun-dried tomato and garlic polenta, drained and cut into 1/2-inch rounds | 1 |
| package prepared garlic bread | 1 |
| package roasted garlic flavored instant mashed potato | 1 |
| package savory garlic stir fry meal kit* | 1 |
| package semi-soft cheese with garlic and herbs (such as alouette®) | 1 |
| package smithfield® peppercorn & garlic seasoned pork tenderloin | 1 |
| package soft cheese with garlic and herbs (recommended: boursin) | 1 |
| packet (1.6-ounce) garlic herb sauce mix, knorr | 1 |
| packet garlic and basil veggie seasoning (recommended: mccormick) | 1 |
| packet garlic herb sauce mix (recommended: knorr) | 1 |
| packet garlic ranch dressing mix | 1 |
| packet instant roasted garlic mashed potatoes, made according to package directions and cooled completely (recommended: betty crocker) | 1 |
| packet zesty herb and garlic seasoning mix | 1 |
| packs roasted garlic dressing mix | 1 |
| panhandle pepper (recommended: bob tallman's cowboy orange seasoning - gourmet black pepper, garlic, onion, and orange oil) | 1 |
| pappadums, quartered (flavored with garlic, if possible) | 1 |
| parboiled cloves of garlic | 1 |
| parboiled garlic | 1 |
| parboiled garlic cloves, pureed until it is pasty | 1 |
| parsley salad (finely chopped parsley, garlic, pepper and scallions) | 1 |
| parsley, oregano, garlic (optional) | 1 |
| part each ground cumin, crushed red pepper flakes, celery salt, garlic powder, onion powder, dried oregano | 1 |
| parts granulated garlic | 2 |
| pasta sauce (such as classico fire-roasted tomato & garlic sauce), heated | 1 |
| peeled and chopped garlic | 1 |
| peeled and crushed garlic | 1 |
| peeled and loosely packed chopped garlic | 1 |
| peeled clove garlic, passed through a press | 2 |
| peeled cloves garlic | 4 |
| peeled fresh garlic | 1 |
| peeled fresh garlic clove | 1 |
| peeled garlic | 15 |
| peeled garlic clove | 25 |
| peeled garlic cloves (4 large heads) | 1 |
| peeled garlic cloves (about 2 large heads) | 1 |
| peeled garlic cloves (about 30) | 1 |
| peeled garlic cloves (from about 2 heads) | 1 |
| peeled garlic cloves, lightly crushed | 1 |
| peeled garlic cloves, smashed | 1 |
| peeled garlic cloves, store bought | 2 |
| peeled garlic cloves; 2 crushed, 2 minced | 1 |
| peeled garlic cloves; 2 whole, 2 sliced | 1 |
| peeled garlic, boiled for 5 minutes | 1 |
| peeled garlic, crushed fine | 1 |
| peeled garlic, or more to taste (divided) | 1 |
| peeled garlic, thinly sliced | 3 |
| peeled minced fresh garlic root (about a 1 1/2 to 2-inch piece) | 2 |
| peeled smashed garlic | 1 |
| peeled whole clove garlic | 1 |
| peeled whole garlic clove | 1 |
| peeled, crushed garlic | 1 |
| peeled, smashed garlic | 2 |
| peeled, thinly sliced garlic | 1 |
| pepper and garlic salt | 1 |
| peppercorn and garlic marinade (recommended: mccormick's) | 1 |
| philadelphia herb & garlic cooking creme | 1 |
| philadelphia herb & garlic cream cheese spread | 1 |
| philadelphia herb & garlic light cream cheese product | 1 |
| pickled garlic | 2 |
| pickled garlic cloves (such as sonoma farm tex-mex sweet & hot garlic cloves®) | 1 |
| pieces pickled garlic, for garnish | 1 |
| pillsbury® refrigerated garlic butter crescent dinner rolls (8 rolls each) | 1 |
| pinches garlic powder | 1 |
| pinches garlic powder, or to taste | 3 |
| pinches garlic salt | 2 |
| pinches garlic salt, or to taste | 1 |
| pints leftover garlic shrimp | 1 |
| pizza sauce (oregano, salt, black and red pepper, granulated garlic, parmesan and basil) | 1 |
| place the basil, cilantro, mint, evoo, jalapenos, garlic, shallots, lime juice and some salt and pepper in the food processor and pulse to finely chop, about the same as a loose pesto | 1 |
| plump fresh garlic cloves, crushed with the flat blade of a knife | 1 |
| plump garlic clove | 7 |
| plump garlic clove, crushed and peeled | 1 |
| plump heads garlic | 3 |
| plump heads of garlic | 1 |
| plump, fresh cloves garlic | 2 |
| plump, fresh garlic clove | 1 |
| plump, moist head garlic, halved crosswise but not peeled | 1 |
| plus 1 1/2 teaspoons minced garlic | 2 |
| plus 1 head garlic | 1 |
| plus 1 tablespoon minced garlic | 1 |
| plus 1 tablespoon roasted garlic salad dressing | 1 |
| plus 1 teaspoon chopped garlic | 2 |
| plus 1 teaspoon dried minced garlic | 1 |
| plus 1 teaspoon finely chopped fresh garlic, salt made a paste | 1 |
| plus 1 teaspoon finely minced garlic | 1 |
| plus 1 teaspoon garlic | 1 |
| plus 1 teaspoon garlic powder | 3 |
| plus 1 teaspoon minced garlic | 4 |
| plus 1/2 teaspoon chili garlic paste | 1 |
| plus 1/4 teaspoon minced garlic | 1 |
| plus 2 garlic clove | 1 |
| plus 2 tablespoons reserved garlic-pepper oil from macadamia nut-crusted goat cheese recipe | 1 |
| plus 2 teaspoons garlic salt | 1 |
| plus 2 teaspoons roasted, mashed garlic (about 12 cloves) | 1 |
| poached garlic | 1 |
| pod fresh garlic | 1 |
| pouch progresso™ recipe starters™ creamy roasted garlic with chicken stock cooking sauce | 4 |
| pouches (4.5 oz. each) starkist tuna creations®, herb and garlic | 1 |
| pounded garlic | 1 |
| powdered garlic | 2 |
| pre-chopped garlic, recipe follows | 2 |
| pre-crushed garlic | 1 |
| pre-minced garlic | 1 |
| prepared garlic mashed potato | 1 |
| prepared minced garlic | 1 |
| prepared roasted garlic | 2 |
| prepared tomato-basil-garlic soup | 1 |
| pressed fresh garlic | 2 |
| pressed garlic | 9 |
| pressed or finely chopped garlic | 1 |
| pressed or minced garlic | 3 |
| progresso™ recipe starters™ creamy roasted garlic with chicken stock cooking sauce | 1 |
| purchased garlic-flavored croutons, (about 5 ounces) | 1 |
| purchased medium-hot salsa with chipotles and garlic (from about two 16-ounce jars) | 1 |
| pureed fresh garlic | 1 |
| pureed garlic | 31 |
| pureed garlic from 4 whole roasted heads of garlic (see above) | 1 |
| pureed roasted garlic | 4 |
| pureed very fresh garlic | 1 |
| quart turkey stock (mire poix, thyme, garlic, turkey carcass and wings, cold water, black peppercorns, bay leaf: simmered for at least 3 hours), strained | 1 |
| quick garlic pickles, recipe follows | 1 |
| ramps (wild spring leeks) or large green onions or a 1-inch-diameter bunch of garlic chives | 1 |
| ranch rub* (recommended: bob tallman's blend of brown sugar, garlic, onion, gourmet peppers, ground chili, and sea salt) | 1 |
| raw garlic | 3 |
| raw garlic, or 3 cloves roasted garlic | 1 |
| razz cherry garlic glaze, to serve, recipe follows | 1 |
| recipe garlic cilantro lime rice, recipe follows | 1 |
| recipe garlic mojo, recipe follows | 1 |
| recipe garlic-anchovy aioli, recipe follows | 1 |
| recipe garlic-basil dressing, recipe follows | 1 |
| recipe roasted garlic paste, recipe follows (or 2 heads roasted garlic) | 3 |
| recipe roasted garlic pesto, recipe follows | 3 |
| recipe roasted garlic vinaigrette, recipe follows | 1 |
| red curry paste or chili-garlic sauce | 1 |
| rendered duck fat (from garlic confit purée ) | 1 |
| reserved marinade from garlic, lemon, and herb rubbed legs | 2 |
| reserved pork, from garlic and mustard pork roast | 1 |
| roast garlic oil | 1 |
| roast garlic puree | 2 |
| roasted chili garlic sauce | 1 |
| roasted cloves garlic | 1 |
| roasted fingerling potatoes with fresh herbs and garlic, recipe follows | 1 |
| roasted freeze-dried garlic | 1 |
| roasted garlic | 94 |
| roasted garlic (1 head rubbed with olive oil then baked at 350 degrees for 45 minutes) | 1 |
| roasted garlic (about 2 cloves) | 1 |
| roasted garlic (about 6 cloves) | 1 |
| roasted garlic (from roasted tomato recipe), recipe follows | 1 |
| roasted garlic (see below) | 1 |
| roasted garlic (see cook's note) | 1 |
| roasted garlic aioli, for serving, recipe follows | 1 |
| roasted garlic aioli, recipe follows | 1 |
| roasted garlic alfredo sauce (recommended: classico) | 1 |
| roasted garlic and herb tomato sauce | 1 |
| roasted garlic and hot sauce, for garnish | 1 |
| roasted garlic and parmesan cheese sauce | 1 |
| roasted garlic and parmesan cheese sauce (such as ragu®) | 1 |
| roasted garlic and parsley dipping sauce, recipe follows | 1 |
| roasted garlic and sun-dried tomato dressing, recipe follows | 1 |
| roasted garlic beurre blanc, recipe follows | 1 |
| roasted garlic butter, recipe follows | 1 |
| roasted garlic chili sauce | 1 |
| roasted garlic clove | 15 |
| roasted garlic cloves (recommended: christopher ranch) | 1 |
| roasted garlic cloves, pureed | 1 |
| roasted garlic cloves, recipe follows | 3 |
| roasted garlic french bread: | 1 |
| roasted garlic guacamole, recipe follows, or store-bought guacamole | 1 |
| roasted garlic herb sauce or high-quality pesto, plus more for serving | 1 |
| roasted garlic hummus | 2 |
| roasted garlic hummus or other prepared hummus | 1 |
| roasted garlic jus, recipe follows | 1 |
| roasted garlic light cream cheese | 1 |
| roasted garlic mashed potatoes, recipe follows | 1 |
| roasted garlic mayo | 1 |
| roasted garlic oil | 3 |
| roasted garlic oil (page 93) | 1 |
| roasted garlic oil or olive oil | 1 |
| roasted garlic oil, or extra-virgin olive oil | 1 |
| roasted garlic olive oil | 1 |
| roasted garlic paste | 5 |
| roasted garlic paste from jar | 1 |
| roasted garlic paste, recipe follows | 3 |
| roasted garlic pepper | 1 |
| roasted garlic powder | 2 |
| roasted garlic pulp | 1 |
| roasted garlic puree | 10 |
| roasted garlic puree (recipe follows) | 1 |
| roasted garlic puree (see below) | 1 |
| roasted garlic puree, recipe follows | 4 |
| roasted garlic rosemary butter, recipe follows | 1 |
| roasted garlic rub, recipe follows | 1 |
| roasted garlic schmear, recipe follows | 1 |
| roasted garlic seasoning | 1 |
| roasted garlic spice, recipe follows | 1 |
| roasted garlic tomato sauce | 1 |
| roasted garlic vinaigrette | 1 |
| roasted garlic, about 1/2 head | 3 |
| roasted garlic, christopher ranch | 1 |
| roasted garlic, crushed | 1 |
| roasted garlic, dried | 1 |
| roasted garlic, lemon, and thyme vinaigrette, recipe follows | 1 |
| roasted garlic, mashed | 5 |
| roasted garlic, mashed into a paste | 3 |
| roasted garlic, mashed into a paste (optional) | 1 |
| roasted garlic, mashed to a paste | 1 |
| roasted garlic, mashed, or more to taste | 1 |
| roasted garlic, or more to taste | 2 |
| roasted garlic, pan seared brown in olive oil works too | 1 |
| roasted garlic, pureed | 6 |
| roasted garlic, recipe below | 1 |
| roasted garlic, recipe follows | 7 |
| roasted garlic, see cook's note* | 1 |
| roasted garlic, smashed to a paste | 9 |
| roasted garlic, squeezed from skins and finely chopped | 1 |
| roasted garlic-dijon aioli | 1 |
| roasted garlic-flavored olive oil | 1 |
| roasted garlic-herb sauce | 1 |
| roasted garlic-onion jam | 1 |
| roasted granulated garlic | 1 |
| roasted minced garlic | 2 |
| roasted red pepper and garlic seasoning blend | 1 |
| roasted vegetables, such as onions, garlic, and squash (optional) | 1 |
| roasted-garlic oilepi:recipelink</epi:recipelink> | 1 |
| roasted-garlic puree, recipe follows | 2 |
| roasted-garlic vinaigrette | 1 |
| rolls cheese with garlic, or any garlic-cheddar spread | 1 |
| rosemary garlic oil, recipe follows | 1 |
| roughly chopped garlic | 12 |
| roughly chopped garlic (about 3 bulbs) | 1 |
| roughly chopped garlic clove | 1 |
| rouille (4 cloves garlic, 2 egg yolks*, 2 teaspoons cayenne pepper, 1 cup olive oil, salt) | 1 |
| round soft cheese with garlic and herbs, 6 ounces (recommended: boursin) | 1 |
| sabra® roasted garlic greek style veggie dip | 1 |
| sachet (1/2 head of garlic, 6 sprigs parsley, 3 sprigs thyme, 1 bay leaf and 1 tablespoon peppercorns) | 1 |
| sachet: 1/2 bay leaf, 1 thyme sprig, 1/2 garlic clove, 1 whole clove, 1 black peppercorn, tied in cheesecloth | 1 |
| sack chips (recommended: onion and garlic yukon gold chips, terra brand, or other mediterranean flavored gourmet chip), available on snacks aisle of market | 1 |
| sack reduced fat gourmet chips (recommended: terra brand garlic and onion yukon gold flavor potato chips (50 percent less fat than regular chips)) | 1 |
| sacks chips (recommended: onion and garlic flavor terra brand yukon gold chips or other specialty chips of choice) | 1 |
| saffron aioli, for garnish (a mixture of roasted garlic,saffron, mayonnaise, lemon juice and salt and pepper) | 1 |
| salt and garlic powder | 2 |
| salt or garlic salt | 1 |
| salt, garlic and cayenne | 1 |
| salt, pepper and crushed garlic | 1 |
| salt, pepper, garlic | 1 |
| salt, pepper, onion powder, garlic powder and cayenne pepper to taste | 1 |
| salt-free garlic & herb seasoning | 1 |
| salt-free garlic and herb seasoning | 6 |
| salt-free garlic and herb seasoning (such as mrs. dash®) | 2 |
| salt-free garlic and herb seasoning blend | 2 |
| salt-free garlic and herb seasoning blend (such as mrs. dash®) | 2 |
| salt-free garlic and herb seasoning or poultry seasoning | 2 |
| salt-free garlic marinade (such as mrs dash®) | 1 |
| salt-free garlic pepper spice blend | 1 |
| salt-free garlic powder | 1 |
| salt-free roasted garlic seasoning (recommended: mccormick) | 1 |
| samba chili sauce with garlic | 1 |
| sambal (asian chile-garlic sauce) | 1 |
| sambal (chile-garlic paste) | 1 |
| sambal (chili garlic sauce) | 1 |
| sambal (chili-garlic paste) | 1 |
| sambal (garlic chili paste) | 1 |
| sambal oelek (asian chile-garlic sauce) | 1 |
| sambal oelek, garlic chili sauce | 1 |
| sambal or chili-garlic sauce | 1 |
| sambal, garlic-chili condiment | 1 |
| saucisson à l'ail or other fully cooked garlic pork sausage (not cured or dried), casing removed | 1 |
| saute the onions, garlic, and yellow peppers. deglaze the pan with white wine, add the bechamel, cream, smoked salmon, and 4 tablespoons capers. slowly bring to a boil | 1 |
| sauteed shiitake mushrooms (in 1/2 tablespoon minced garlic) | 1 |
| scant 1/8 teaspoon garlic powder | 1 |
| seasoned salt (with onion and garlic) | 1 |
| seasoning mixture: coriander, paprika, salt and pepper, seafood boil, garlic powder and cayenne | 1 |
| seasoning spice: equal amounts coriander, curry powder, cumin, paprika, ground thyme, ground garlic, sage, chili powder, dry mustard, dry ginger, cayenne pepper, salt and pepper | 1 |
| secret thai marinade: mixture soy sauce, sesame oil hoisin, chili paste, ginger and garlic | 1 |
| semi-soft garlic and herb cheese (recommended: alouette or boursin) | 1 |
| semisoft cheese with garlic and herbs, boursin® | 1 |
| serving suggestion: 3 cups cooked brown rice and garlic broccoli, recipe follows | 1 |
| serving suggestion: boiled potatoes and garlic croutons | 1 |
| serving suggestion: crusty bread or garlic bread | 1 |
| serving suggestion: garlic bread | 1 |
| serving suggestion: mediterranean sardines with lemon and garlic, recipe follows | 1 |
| serving suggestion: roasted garlic and mushroom risotto, recipe follows | 1 |
| serving suggestion: sweet and sour or vinegar and garlic dipping sauce, recipes follow | 1 |
| serving suggestions: aioli (garlic mayonnaise) and toasts | 1 |
| serving suggestions: french fries, coleslaw, and garlic bread | 1 |
| serving suggestions: green salad and garlic bread | 1 |
| serving suggestions: serve with garlic aioli | 1 |
| several cloves garlic | 3 |
| several cloves garlic, crushed | 5 |
| shaved garlic | 1 |
| shoots green garlic | 2 |
| simplynature garlic granules | 1 |
| sliced cloves garlic | 1 |
| sliced double-blanched garlic, recipe follows | 1 |
| sliced fresh garlic | 1 |
| sliced garlic | 41 |
| sliced garlic (7 or 8 fat garlic cloves) | 1 |
| sliced garlic chives or green onion | 1 |
| sliced garlic chives or regular chives, plus more for serving | 1 |
| sliced garlic clove | 4 |
| sliced green garlic | 1 |
| sliced peeled garlic cloves (about 1 large head) | 1 |
| sliced ramps, bulbs and leaves (or an equal amount of leeks and 1 garlic clove) | 1 |
| sliced spring garlic whites or ramp whites, plus 1/2 cup sliced garlic greens or ramp greens | 1 |
| slices country bread, toasted and lightly rubbed with garlic | 1 |
| slices french bread, toasted and rubbed with raw garlic clove | 1 |
| slices garlic and herb jack cheese | 1 |
| slices garlic and rosemary focaccia bread | 1 |
| slices garlic texas toast | 1 |
| slices pepperidge farm® garlic texas toast, prepared according to package directions | 1 |
| slices pepperidge farm® garlic texas toast, prepared as directed on package | 1 |
| slices prepared garlic bread | 1 |
| slivered garlic | 9 |
| slow roasted garlic | 1 |
| small bunch chopped garlic chives | 1 |
| small clove fresh garlic | 1 |
| small clove garlic | 199 |
| small clove garlic, cracked from skin | 2 |
| small clove garlic, crushed | 2 |
| small clove garlic, cut into thin slices | 1 |
| small clove garlic, halved | 1 |
| small clove garlic, mashed | 1 |
| small clove garlic, or garlic paste | 1 |
| small clove garlic, pasted | 1 |
| small clove garlic, smashed | 2 |
| small clove garlic, smashed and finely chopped | 1 |
| small clove garlic, thinly sliced | 1 |
| small clove garlic, unpeeled | 1 |
| small clove garlic, very finely chopped | 1 |
| small clove garlic, very thinly sliced | 1 |
| small clove garlic, whole | 1 |
| small clove garlic; peeled and finely chopped | 1 |
| small clove minced garlic | 1 |
| small clove of garlic | 4 |
| small clove of garlic, crushed and chopped | 1 |
| small clove of garlic, pressed | 1 |
| small cloves garlic | 43 |
| small cloves garlic (2 smashed, 1 chopped) | 1 |
| small cloves garlic, crushed | 1 |
| small cloves garlic, roasted and chopped | 1 |
| small cloves garlic, smashed | 3 |
| small cloves garlic, thinly sliced | 1 |
| small cloves garlic, toasted (see note) and peeled | 1 |
| small cloves garlic, whole | 1 |
| small crushed garlic clove | 2 |
| small garlic clove | 251 |
| small garlic clove, crushed | 2 |
| small garlic clove, finely grated1/4 cup toasted hazelnuts | 1 |
| small garlic clove, forced through a garlic press | 1 |
| small garlic clove, halved | 1 |
| small garlic clove, if desired | 1 |
| small garlic clove, pressed | 14 |
| small garlic clove, pressed (optional) | 1 |
| small garlic clove, quartered | 1 |
| small garlic clove, roasted, then minced | 1 |
| small garlic clove, smashed | 2 |
| small garlic clove, smashed to a paste with 1/4 teaspoon salt | 1 |
| small garlic clove, thinly sliced | 2 |
| small garlic clove, very thinly sliced | 1 |
| small garlic cloves, crushed | 1 |
| small garlic cloves, crushed with a garlic press | 1 |
| small garlic cloves, forced through a garlic press | 1 |
| small garlic cloves, pressed | 4 |
| small garlic cloves, pressed or minced | 2 |
| small garlic cloves, smashed | 4 |
| small garlic cloves, thinly slivered | 1 |
| small garlic cloves, unpeeled | 1 |
| small garlic cloves, very thinly sliced | 1 |
| small garlic- or italian-flavored croutons, crushed slightly | 2 |
| small glove garlic, pasted up with some salt | 1 |
| small handful garlic | 1 |
| small head garlic | 6 |
| small head garlic (2 inches in diameter) | 2 |
| small head garlic, cloves peeled and minced | 2 |
| small head garlic, cut in half crosswise | 1 |
| small head garlic, halved crosswise | 1 |
| small head garlic, roasted and mashed | 1 |
| small head of garlic | 2 |
| small heads garlic | 1 |
| small heads garlic, plus 1 clove garlic | 1 |
| small heads garlic, separated into cloves and peeled | 1 |
| small heads garlic, smashed and peeled | 2 |
| small heads garlic, smashed and peeled, plus 3 cloves, thinly sliced | 1 |
| small minced clove of garlic | 2 |
| small peeled garlic clove | 1 |
| small peeled garlic clove, passed through a press | 1 |
| small wheel garlic and herb soft cheese (about 5 to 6 ounces) (recommended: boursin) | 1 |
| smashed clove or two of garlic | 1 |
| smashed garlic | 8 |
| smashed garlic (use the edge of a large, wide-bladed knife) | 1 |
| smashed garlic clove | 8 |
| smashed peeled garlic | 1 |
| smashed peeled garlic cloves, plus 1 finely chopped garlic clove | 1 |
| smashed raw garlic | 1 |
| smashed unpeeled garlic clove | 1 |
| smithfield® garlic & herb or golden rotisserie seasoned pork sirloin roast, cooked and shredded | 1 |
| smithfield® garlic & herb seasoned pork loin filet | 2 |
| smithfield® garlic & herb seasoned pork loin filet, cut into 3/4-inch thick slices | 1 |
| smithfield® garlic & herb seasoned pork sirloin | 2 |
| smithfield® peppercorn & garlic seasoned boneless pork sirloin roast, cut into 3/4-inch cubes | 1 |
| smithfield® peppercorn & garlic seasoned boneless pork sirloin roast, cut into 32 (1-inch) pieces | 1 |
| smithfield® peppercorn & garlic seasoned pork tenderloin | 3 |
| smithfield® peppercorn & garlic seasoned tenderloin | 1 |
| smoked garlic | 1 |
| smoked paprika-hot garlic sauce, recipe follows | 1 |
| sofrito (garlic, cilantro, sweet peppers) | 1 |
| soft garlic and herb cheese (recommended: boursin) | 1 |
| soft garlic-herb cheese (such as boursin) | 1 |
| sour cream garlic biscuits, recipe follows | 1 |
| southwest seasoning (chili powder, mexican oregano, garlic powder, ground chipotles (smoked jalepenos), paprika, ground cumin and ground coriander) | 1 |
| spice islands garlic powder | 3 |
| spice islands® garlic powder | 2 |
| spice islands® garlic salt | 2 |
| spice islands® minced garlic | 1 |
| spicy garlic potatoes and zucchini, recipe follows | 1 |
| spicy garlic sauce, such as t-boys spicy garlic sauce | 1 |
| spinach sauteed with garlic and oil | 1 |
| spinach with garlic: | 1 |
| spinach, cleaned and sauteed in garlic and olive oil | 1 |
| spinach, sauteed with garlic, salt and pepper | 1 |
| sprays fire roasted garlic juice (garlic valley farms 800-424-7990 | 1 |
| spreadable garlic-flavored cheese | 1 |
| spring garlic | 2 |
| sprinkle granulated garlic | 2 |
| squares garlic & herb saute express® saute starter | 1 |
| squashed garlic clove | 1 |
| sriracha (thai garlic-chile paste) | 1 |
| sriracha chile-garlic sauce | 1 |
| sriracha chili garlic sauce | 3 |
| sriracha or other chili-garlic sauce | 1 |
| stalk green garlic | 1 |
| stalk green garlic, white and light green parts | 1 |
| stalks garlic chives | 1 |
| stalks green garlic | 2 |
| stalks green garlic or 2 cloves garlic | 1 |
| stalks green garlic, thinly sliced, or 2 finely chopped leeks, white and light-green parts only | 1 |
| stalks green garlic, white part only | 1 |
| standard sachet of garlic cloves, peppercorns, parsley stems, and bay leaf | 1 |
| steak dust (recommended: bob tallman's cowboy blend of garlic, black pepper, sea salt, onion, and sugar) | 1 |
| steak seasoning (such as kc masterpiece ® steak seasoning with garlic), or to taste | 1 |
| stonemill minced garlic in water | 1 |
| store-bought garlic bread (save other half for pizza) | 1 |
| store-bought roasted garlic salsa | 1 |
| sun-dried tomatoes packed in olive oil with garlic, drained and chopped | 1 |
| supermarket-style garlic and herb seasoning mix | 1 |
| sweet chili garlic sauce* | 1 |
| sweet chili-garlic sauce | 1 |
| sweet garlic chili sauce | 1 |
| sweet garlic soy sauce | 1 |
| t minced garlic | 1 |
| tabasco sauce or chili-garlic sauce (sambal oelek) | 1 |
| tabil (a tunisian spice blend of coriander seed, caraway seed, garlic powder, cayenne pepper) | 1 |
| table spoon garlic powder | 1 |
| tablepsoon minced garlic | 1 |
| tablespooon garlic powder | 1 |
| tbs garlic powder | 1 |
| tbs. finely chopped garlic | 1 |
| tbs. garlic | 1 |
| tbs. garlic powder | 1 |
| tbs. minced garlic | 3 |
| tbs. napastyle roasted garlic paste (optional) | 1 |
| tbs. sliced garlic | 1 |
| teaspooon minced garlic | 2 |
| thai chile garlic sauce | 1 |
| thai chili garlic sauce | 2 |
| thai chili garlic sauce oelek | 1 |
| thai chili-garlic sauce (recommended: sriracha) | 2 |
| thai garlic chile paste | 3 |
| thai garlic-chili paste, see cook's note | 1 |
| thai pepper garlic sauce | 2 |
| thai sweet chili and garlic sauce (recommended: mae ploy now available in most grocery stores) | 1 |
| thin slice of garlic | 1 |
| thin sliced garlic jack cheese | 1 |
| thin slices garlic | 2 |
| thinly shaved garlic | 1 |
| thinly sliced fresh garlic | 1 |
| thinly sliced fresh garlic chives or regular fresh chives | 1 |
| thinly sliced garlic | 24 |
| thinly sliced garlic (10 to 12 cloves) | 1 |
| thinly sliced garlic (8 cloves) | 1 |
| thinly sliced garlic (about 8 cloves) | 1 |
| thinly sliced garlic chives or 2 garlic cloves, thinly sliced | 1 |
| thinly sliced garlic clove | 3 |
| three 8-ounce containers prepared tahini hummus with garlic | 1 |
| to 1 1/2 cups store-bought or homemade garlic croutons (see below) | 1 |
| to 1 1/2 teaspoons chili-garlic paste | 1 |
| to 1 clove garlic | 3 |
| to 1 cup minced green garlic, about 5 small heads | 1 |
| to 1 garlic clove (about 1/2 to 1 teaspoon) | 1 |
| to 1 small clove garlic | 1 |
| to 1/2 cup irvine spices roasted garlic pepper | 1 |
| to 10 cloves fresh garlic | 3 |
| to 10 cloves garlic | 4 |
| to 10 cloves garlic, cracked but left in skins, plus 1 clove peeled and halved | 1 |
| to 10 cloves garlic, crushed | 2 |
| to 10 cloves roasted garlic | 2 |
| to 10 garlic clove | 5 |
| to 10 garlic cloves, roasted and pureed | 1 |
| to 10 unpeeled cloves garlic | 1 |
| to 12 cloves fresh garlic | 1 |
| to 12 cloves garlic | 2 |
| to 12 cloves garlic (about 1 head) | 1 |
| to 12 cloves garlic, smashed | 1 |
| to 12 garlic cloves smashed | 1 |
| to 12 smashed garlic clove | 1 |
| to 12 whole cloves garlic | 1 |
| to 15 cloves garlic | 1 |
| to 15 cloves garlic, cracked away from skins | 1 |
| to 15 garlic clove | 2 |
| to 16 cloves fresh garlic | 1 |
| to 2 1/2 cups cooked white beans with 3/4 cup reserved cooking liquid (see cannellini beans with garlic and sage ) | 1 |
| to 2 cloves garlic | 28 |
| to 2 cloves garlic, crushed | 3 |
| to 2 cloves minced garlic | 1 |
| to 2 cloves, garlic | 1 |
| to 2 cups bestquality tomato sauce or marinara sauce (if storebought, embellish with freshly minced garlic and chopped fresh basil leaves) | 1 |
| to 2 garlic clove | 11 |
| to 2 garlic cloves pressed through a garlic press | 1 |
| to 2 garlic cloves, or to taste | 1 |
| to 2 garlic cloves, pressed | 1 |
| to 2 garlic cloves, smashed and peeled | 1 |
| to 2 garlic cloves, thinly sliced | 1 |
| to 2 large cloves garlic | 2 |
| to 2 large cloves garlic, 1/2 grated and 1/2 sliced | 1 |
| to 2 large garlic clove | 1 |
| to 2 large garlic cloves, halved crosswise | 1 |
| to 2 medium cloves garlic | 1 |
| to 2 medium garlic clove | 1 |
| to 2 plump garlic clove | 1 |
| to 2 slices garlic bread, for serving | 1 |
| to 2 tablespoons chopped garlic | 1 |
| to 2 tablespoons fresh minced garlic | 1 |
| to 2 tablespoons lowry's garlic salt | 1 |
| to 2 teaspoon garlic or onion powder | 2 |
| to 2 teaspoons asian chili garlic sauce | 1 |
| to 2 teaspoons chili-garlic sauce | 1 |
| to 2 teaspoons minced garlic | 1 |
| to 20 cloves garlic | 2 |
| to 20 garlic bulbs | 1 |
| to 20 roasted garlic cloves, recipe follows | 1 |
| to 3 cloves chopped garlic | 2 |
| to 3 cloves garlic | 60 |
| to 3 cloves garlic minced | 1 |
| to 3 cloves garlic, crushed | 6 |
| to 3 cloves garlic, crushed, plus 1 clove | 1 |
| to 3 cloves garlic, smashed | 2 |
| to 3 cloves garlic, smashed with back of knife | 1 |
| to 3 cloves garlic, thinly sliced | 1 |
| to 3 cloves minced garlic | 1 |
| to 3 cloves of garlic | 5 |
| to 3 cloves or peeled garlic | 1 |
| to 3 garlic clove | 17 |
| to 3 garlic cloves, crushed | 2 |
| to 3 garlic cloves, slivered | 1 |
| to 3 garlic cloves, smashed | 2 |
| to 3 garlic cloves, thinly sliced | 1 |
| to 3 grated garlic clove | 1 |
| to 3 large cloves garlic | 5 |
| to 3 large cloves garlic, crushed | 1 |
| to 3 large garlic clove | 2 |
| to 3 large unpeeled cloves garlic | 1 |
| to 3 ounces minced roasted garlic | 2 |
| to 3 peeled garlic cloves, for rubbing | 1 |
| to 3 tablespoons chopped garlic | 1 |
| to 3 tablespoons garlic-infused extra-virgin olive oil | 1 |
| to 3 tablespoons granulated garlic | 1 |
| to 3 tablespoons minced garlic | 1 |
| to 3 teaspoons adobo seasoning, or other comparable mix of garlic powder, dried oregano, salt, black pepper and turmeric | 1 |
| to 3 teaspoons chile garlic sauce, such as vietnamese tuong ot toi | 1 |
| to 3 teaspoons finely chopped fresh garlic | 1 |
| to 3 whole cloves garlic | 2 |
| to 3 whole heads garlic | 3 |
| to 4 cloves chopped garlic or granulated, depending on your preference (c'mon, no spicy finger food is complete without this spice) | 1 |
| to 4 cloves garlic | 120 |
| to 4 cloves garlic, cracked from skin and halved | 1 |
| to 4 cloves garlic, crushed | 3 |
| to 4 cloves garlic, in skins | 1 |
| to 4 cloves garlic, mashed or minced | 1 |
| to 4 cloves garlic, pressed | 1 |
| to 4 cloves garlic, smashed | 3 |
| to 4 cloves garlic, smashed, plus 1 for rubbing bread | 1 |
| to 4 cloves garlic, thinly sliced | 4 |
| to 4 cloves of garlic | 1 |
| to 4 finely minced garlic clove | 1 |
| to 4 garlic clove | 11 |
| to 4 garlic cloves minced (depending on size) | 1 |
| to 4 garlic cloves, crushed | 1 |
| to 4 garlic cloves, cut in half (no peeling necessary) | 1 |
| to 4 garlic cloves, lightly smashed | 1 |
| to 4 garlic cloves, smashed | 1 |
| to 4 garlic cloves, very thinly sliced | 1 |
| to 4 large cloves garlic | 6 |
| to 4 large cloves garlic, thinly sliced | 1 |
| to 4 large cloves garlic, thinly sliced or finely chopped | 2 |
| to 4 roasted garlic clove | 1 |
| to 4 tablespoons chili-garlic sauce or sambal oelek | 1 |
| to 4 tablespoons finely chopped garlic | 1 |
| to 4 whole cloves garlic | 2 |
| to 4 whole garlic clove | 1 |
| to 4 whole garlic cloves, cooked in olive oil | 1 |
| to 5 cloves garlic | 17 |
| to 5 cloves garlic, crushed with the back of a knife | 1 |
| to 5 cloves garlic, mashed | 1 |
| to 5 cloves garlic, smashed | 2 |
| to 5 cloves garlic, thinly sliced | 1 |
| to 5 cloves garlic, unpeeled | 1 |
| to 5 cloves garlic, whole | 1 |
| to 5 cloves minced garlic | 1 |
| to 5 garlic clove | 3 |
| to 5 garlic cloves, crushed | 1 |
| to 5 garlic cloves, thinly sliced | 1 |
| to 5 heads roasted garlic | 1 |
| to 5 large cloves garlic | 2 |
| to 5 ounces garlic-and-herb goat cheese (recommended: montrachet | 1 |
| to 5 peeled cloves garlic | 2 |
| to 5 peeled garlic clove | 1 |
| to 5 teaspoons asian chili paste with garlic | 1 |
| to 6 clove garlic | 1 |
| to 6 cloves garlic | 24 |
| to 6 cloves garlic, crushed | 1 |
| to 6 cloves garlic, quartered lengthwise | 1 |
| to 6 cloves garlic, rubbed to paste | 1 |
| to 6 cloves garlic, separated but unpeeled | 1 |
| to 6 cloves garlic, smashed | 3 |
| to 6 cloves garlic, thinly sliced | 1 |
| to 6 cloves of garlic | 2 |
| to 6 cloves roasted garlic | 1 |
| to 6 fat cloves garlic | 1 |
| to 6 garlic clove | 11 |
| to 6 garlic cloves, pressed | 1 |
| to 6 garlic cloves, unpeeled | 1 |
| to 6 large cloves garlic | 2 |
| to 6 whole garlic cloves in skins | 1 |
| to 7 cloves garlic | 2 |
| to 8 cloves garlic | 11 |
| to 8 cloves garlic, crushed | 3 |
| to 8 cloves garlic, pressed | 1 |
| to 8 cloves garlic, slivered | 1 |
| to 8 cloves garlic, smashed | 1 |
| to 8 cloves garlic, smashed from skins | 1 |
| to 8 cloves garlic, thinly sliced | 1 |
| to 8 cloves garlic, thinly sliced, plus 1 or 2 more whole clove | 1 |
| to 8 cloves garlic, very finely chopped | 1 |
| to 8 cloves of garlic | 2 |
| to 8 cloves roasted garlic | 1 |
| to 8 garlic clove | 9 |
| to 8 garlic cloves, halved if large | 1 |
| to 8 garlic whole clove | 1 |
| to 8 large cloves garlic, crushed and minced | 1 |
| to 8 large cloves garlic, quartered | 1 |
| to 8 ounces garlic-and-herb goat cheese, at room temperature, such as montrachet | 1 |
| to 8 slices crusty bread, toasted, rubbed with garlic cloves and drizzled with olive oil | 1 |
| toast points with roasted garlic, caramelized onions, and goat cheese, recipe follows | 1 |
| toasted baguette slices, buttered and rubbed with garlic | 2 |
| toasted bread and garlic, to serve | 1 |
| toasted country bread, rubbed with garlic and olive oil (for serving) | 1 |
| toasted garlic and herb breadcrumbs, recipe follows | 1 |
| toasted garlic chips, recipe follows | 1 |
| toasted garlic vinaigrette | 1 |
| toasted garlic-beef stock | 1 |
| tomato garlic basil sauce, recipe follows | 1 |
| tomato/garlic oil | 1 |
| toppings such as pepperoni, cooked sausage, garlic, onions and pepper | 1 |
| toulouse sausages or fresh garlic-flavored pork sausages | 1 |
| toulouse sausages, or other garlic pork sausage | 1 |
| tub philadelphia herb & garlic cooking creme cream cheese product | 1 |
| tub philadelphia savory garlic cooking creme cream cheese product | 1 |
| tub philadelphia savoury garlic cooking creme | 1 |
| tubs, 6 ounces each, soft garlic and herb cheese (recommended: alouette brand) | 1 |
| unpeeled cloves garlic | 2 |
| unpeeled cloves of garlic ( 3 heads) | 1 |
| unpeeled garlic bulb | 1 |
| unpeeled garlic clove | 23 |
| unpeeled garlic cloves, as needed | 2 |
| unpeeled garlic cloves, cut in half | 1 |
| unpeeled garlic cloves, roasted in a dry skillet over medium heat for about 15 minutes until soft | 1 |
| unpeeled garlic cloves, smashed | 2 |
| unpeeled garlic, crushed | 1 |
| unpeeled head of garlic, cut crosswise in half | 1 |
| unpeeled heads of garlic, halved horizontally | 1 |
| unpeeled large garlic clove | 1 |
| unpeeled large garlic cloves (about 4 ounces) | 1 |
| unpeeled large garlic cloves plus 1 tablespoon finely chopped garlic | 1 |
| unpeeled large garlic cloves, smashed | 1 |
| unpeeled large garlic leaf | 1 |
| unpeeled small garlic clove, lightly smashed | 1 |
| unpeeled whole head of garlic, cut crosswise in half | 1 |
| vali's skordalia or roasted garlic skordalia | 1 |
| vegetable oil 2 cloves garlic | 1 |
| very finely chopped garlic | 2 |
| very finely chopped garlic (about 2 medium cloves) | 1 |
| very finely chopped garlic, (about 2 cloves) | 1 |
| very finely diced garlic | 1 |
| very finely minced garlic | 4 |
| very finely-chopped garlic | 1 |
| very finely-minced garlic | 1 |
| very fresh garlic | 1 |
| very fresh garlic, thinly sliced | 1 |
| very small garlic clove | 3 |
| very thin slices french bread, toasted and rubbed with a cut garlic clove, for garnish | 1 |
| very thin slices peeled garlic plus 2 tablespoons | 1 |
| very thinly sliced garlic | 1 |
| vh® honey garlic sauce | 1 |
| vietnamese chile-garlic paste, or to taste, or chopped fresh chiles | 1 |
| vietnamese chile-garlic sauce (preferably huy fong brand) | 1 |
| vietnamese chili-garlic sauce | 2 |
| vietnamese garlic chili sauce | 1 |
| vietnamese garlic-chile sauce | 1 |
| vietnamese garlic-chili sauce | 1 |
| vlasic® zesty garlic dill stackers | 1 |
| vodka, infused overnight with garlic cloves (12 peeled, whole cloves per 750 ml of vodka) | 1 |
| wheel boursin (5.4 ounces) or other garlic-and-herb cheese | 1 |
| white portion of green garlic | 1 |
| whole bay leaf, 4 whole peeled garlic clove | 1 |
| whole bulb garlic | 2 |
| whole bulb garlic, unpeeled | 1 |
| whole clove chopped garlic | 1 |
| whole clove garlic | 3 |
| whole clove garlic plus 1/4 teaspoon minced garlic | 1 |
| whole clove garlic, smashed | 1 |
| whole cloves garlic | 27 |
| whole cloves garlic plus 1 clove | 1 |
| whole cloves garlic, crushed | 1 |
| whole cloves garlic, for rubbing bread | 1 |
| whole cloves garlic, plus 1/2 small clove | 1 |
| whole cloves garlic, roasted | 1 |
| whole cloves garlic, smashed | 2 |
| whole cloves garlic, unpeeled | 2 |
| whole cloves peeled garlic | 1 |
| whole garlic | 2 |
| whole garlic bulb, cut in half equatorially | 1 |
| whole garlic bulb, roasted to a golden brown | 1 |
| whole garlic bulb, with roots and base chopped off | 1 |
| whole garlic bulbs | 3 |
| whole garlic clove | 38 |
| whole garlic clove plus 15 cloves garlic, thinly sliced | 1 |
| whole garlic clove, crushed | 1 |
| whole garlic clove, cut in half | 1 |
| whole garlic cloves peeled | 1 |
| whole garlic cloves, crushed | 1 |
| whole garlic cloves, smashed | 5 |
| whole garlic cloves, unpeeled | 4 |
| whole garlic head | 3 |
| whole garlic head, skin on | 1 |
| whole garlic head, top 1/2 inch trimmed | 1 |
| whole garlic heads | 4 |
| whole garlic peeled and chopped coarsely | 1 |
| whole garlic, with peel | 1 |
| whole head garlic | 25 |
| whole head garlic (about 2 1/2 ounces, cloves separated and peeled) | 3 |
| whole head garlic clove | 1 |
| whole head garlic, cloves peeled but left whole | 1 |
| whole head garlic, cloves separated and peeled | 1 |
| whole head garlic, cut in 1/2 crosswise | 1 |
| whole head garlic, cut in half crosswise | 1 |
| whole head garlic, halved widthwise | 1 |
| whole head garlic, separated into cloves (about 15), unpeeled | 1 |
| whole head garlic, separated into cloves - cloves unpeeled and quartered | 1 |
| whole head garlic, separated into cloves, unpeeled | 1 |
| whole head garlic, skin on | 1 |
| whole head garlic, un-peeled, cut crosswise in 1/2 | 1 |
| whole head garlic, unpeeled | 1 |
| whole head garlic, unpeeled and cut in half crosswise | 1 |
| whole head of garlic | 1 |
| whole head of garlic (with about 12 to 14 cloves) | 1 |
| whole head of garlic clove | 1 |
| whole head of garlic, cut in half crosswise | 1 |
| whole head of garlic, halved horizontally | 1 |
| whole head of garlic, unpeeled, plus 4 small cloves garlic | 1 |
| whole head or 6 cloves of garlic | 1 |
| whole head roasted garlic, pulp removed | 1 |
| whole heads garlic | 9 |
| whole heads garlic, about 40 clove | 1 |
| whole heads garlic, halved | 1 |
| whole heads garlic, top third sliced off and discarded | 1 |
| whole heads of garlic | 1 |
| whole heads of garlic, crushed and peeled | 1 |
| whole heads of garlic, papery outside removed, cloves separated, unpeeled | 1 |
| whole heads of garlic, unpeeled | 1 |
| whole medium head garlic | 1 |
| whole peeled and sliced garlic clove | 1 |
| whole peeled clove garlic | 1 |
| whole peeled garlic | 1 |
| whole peeled garlic clove | 5 |
| whole peeled garlic clove, crushed and skewered with a toothpick | 1 |
| whole peeled garlic clove, smashed | 1 |
| whole roasted garlic clove | 1 |
| whole unpeeled heads garlic, halved lengthwise | 1 |
| whole, unpeeled heads garlic, split in half horizontally | 1 |
| whole, unpeeled heads of garlic | 1 |
| whole, unpeeled, garlic clove | 1 |
| wild garlic leaf | 1 |
| young garlic shoots | 1 |
| your choice of: boursin garlic and herb cheese, crumbled, alouette garlic and herb cheese (4 rounded spoonfuls), crumbled feta cheese, crumbled herb goat cheese - again, whatever your preference and whichever you have on hand | 1 |
| your favorite seasoning, such as garlic or onion powder | 1 |
| yucon gold,garlic and bleu cheese mashed potatoes, recipe follows | 1 |
| yukon gold mashed potatoes with green garlic butter, recipe follows | 1 |
| ½ teaspoons fresh minced garlic | 1 |
| ‑2 medium garlic clove | 1 |
| –10 heads of garlic (about 3 cups cloves) | 1 |
| –3 cloves garlic | 1 |

### onion

| Canonical value | Recipes |
|---|---:|
| "-slices red onion | 1 |
| "something oniony," like 1 scallion or 1/4 small red onion | 1 |
| (1.25 oz.) dry onion soup mix | 1 |
| *quail eggs are available at some supermarkets, farmers' markets, and specialty foods stores, but if you can't find them, pickled onions are a delicious stand-in | 1 |
| -1/2 cups frozen o'brien potatoes with onions and pepper | 1 |
| -10 cups simmering lightly salted vegetable broth (made with 1 onion, 1 garlic clove, 1 carrot, 1 celery stalk, and a few parsley stems, cooked for 15 minutes) or simmering water | 2 |
| -3 shredded sweet onions (spanish or vidalia) | 1 |
| -4 green onion | 1 |
| -4 tbsp finely sliced spring onion greens | 1 |
| -cup chopped red onion | 1 |
| -cup diced red onion | 1 |
| -cup onion chopped | 1 |
| -cup onions, spring or scallions (includes tops and bulb), raw | 1 |
| -cup red onion | 1 |
| -cup yellow onion | 1 |
| -inch slice of onion | 1 |
| -inch thick slices of a large red onion, grilled until charred and softened | 1 |
| -inch wedges red onion (from 2 large onions) | 1 |
| -inch-diameter pearl onions, blanched 30 seconds | 1 |
| -inch-thick onion slices | 3 |
| -inch-thick red onion slices | 5 |
| -inch-thick rounds red onion | 1 |
| -inch-thick slice from medium-size white onion | 1 |
| -inch-thick slice red onion | 1 |
| -inch-thick slices red onion | 4 |
| -inch-thick slices sweet onion (such as maui or vidalia) | 1 |
| -lb. spring or small white onions (about 6-8 onions), stems and roots trimmed | 1 |
| -ounce chopped green onion | 2 |
| -ounce chopped onion | 3 |
| -ounce chopped spanish onion | 1 |
| -ounce finely chopped onion | 1 |
| -ounce fried onion | 1 |
| -ounce granulated onion | 1 |
| -ounce large diced red onion | 2 |
| -ounce onion | 7 |
| -ounce package frozen pearl onion | 2 |
| -ounce shredded spanish onion | 1 |
| -ounce. green onion | 1 |
| -ounces green onion | 1 |
| -½ cups sliced assorted fresh vegetables, such as zucchini, onions and red pepper | 1 |
| / 2 plus 1/3 cup minced red onion | 1 |
| / 2 teaspoon onion powder | 1 |
| / 3 1/2 oz fresh chives (or green parts of spring onions/scallions) | 1 |
| /1 3/4 ounces onion, cut into 3/4-inch cubes | 1 |
| /160 g finely chopped onion | 1 |
| /2 cup red onion | 1 |
| /20 g finely chopped red onion | 1 |
| /240 ml caramelized onion | 1 |
| /30 g minced chives or onion | 1 |
| /4 cup finely chopped onion | 1 |
| /4 cup red onion | 1 |
| /40 g coarsely chopped onion | 1 |
| /675 g onions, thinly sliced | 1 |
| 1 1/2-inch-thick onion slices (preferable sweet onion, such as vidalia) | 1 |
| 1-inch boiling onion | 1 |
| 1-inch diced onion | 1 |
| 1-inch pieces red onion (1/3 inch thick) | 1 |
| 1-inch pieces red onion (from 1 large) | 1 |
| 1-inch-diameter pearl onions (from two 10-ounce bags) | 1 |
| 1-inch-thick wedges red onion | 1 |
| 1-pound bag frozen pearl onions, thawed | 1 |
| 1-pound packages frozen potato-and-onion pierogi | 1 |
| 1-pound sweet onion (such as vidalia or maui), cut into 1/2-inch-thick slices | 1 |
| 1/2-inch cubes red onion plus 1/4 cup thinly sliced | 1 |
| 1/2-inch diced onion | 1 |
| 1/2-inch onion pieces (from about 2 large onions) | 1 |
| 1/4-inch chunks onion | 1 |
| 1/4-inch cubed onion | 1 |
| 1/4-inch dice onion | 1 |
| 1/4-inch dice red onion | 1 |
| 1/4-inch diced onion | 2 |
| 1/4-inch diced red onion | 3 |
| 1/4-inch diced red onion (from about 1 large onion) | 2 |
| 1/4-inch- sliced sweet onion (about 1/2 onion) | 1 |
| 1/4-inch-diced red onion | 1 |
| 1/4-inch-sliced sweet onion | 1 |
| 1/4-inch-thick half-moon slices onion | 2 |
| 1/8-inch diced red onion | 1 |
| 1/8-inch julienne white onion | 1 |
| 1/8-inch-thick sliced onion | 1 |
| 1/8-inch-thick slices red onion | 1 |
| 10-ounce bag pearl onion | 1 |
| 10-ounce bag pearl onions, blanched | 1 |
| 10-ounce bag red pearl onion | 1 |
| 10-ounce bags unpeeled pearl onions, root ends trimmed but left intact | 1 |
| 10-ounce basket pearl onion | 1 |
| 10-ounce basket pearl onions or 1 cup frozen | 1 |
| 10-ounce container pearl onions, blanched 1 minute | 1 |
| 10-ounce package frozen pearl onions, thawed | 1 |
| 10-ounce package frozen petite whole onions, thawed, drained | 1 |
| 12- to 13-ounce onion, halved, cut into 1/4-inch-thick slices | 1 |
| 12-ounce bag frozen pearl onions, thawed | 1 |
| 12-ounce onion | 2 |
| 12-ounce red onion | 1 |
| 14 1/2-ounce can diced tomatoes with green pepper and onion | 1 |
| 14 1/2-ounce cans diced tomatoes with caramelized onion, in juice | 1 |
| 2-layer sections of red onion wedges | 1 |
| 3-inch-diameter slice white onion (1/2 inch thick), separated into rings | 1 |
| 3-inch-long green onion bottoms | 1 |
| 6-ounce can french fried onion | 1 |
| 7-to 8-ounce onions, halved through root end, each half cut into 6 wedges | 1 |
| 8- to 10-ounce red onions, cut into 1/3-inch-thick rounds | 1 |
| 8-ounce onion | 1 |
| 8-ounce package mixed stir-fry vegetables (including snow peas, carrots, onion and celery; about 3 cups) | 1 |
| 8-ounce package pearl onion | 1 |
| 8-ounce red onion, thinly sliced | 1 |
| 9-ounce boxes frozen creamed pearl onion | 1 |
| a 1/2-inch-thick from a small onion | 1 |
| a 1/2-inch-thick slice medium white onion | 1 |
| a few green onion | 1 |
| a few lengths of spring onion greens, to garnish | 1 |
| a few tablespoons chopped white onion, for garnish | 1 |
| a medium onion | 1 |
| a medium yellow onion, quartered then thinly sliced may be substituted, but cippolini are | 1 |
| a small red onion | 4 |
| about 1 1/2 ounces or 3 tablespoons/40 g chopped red onion | 1 |
| about 1/3 cup finely chopped white onion | 1 |
| about 1/4 cup chopped onion | 1 |
| about 1/4 cup freshly diced green onion | 1 |
| about 1/4 cup grated onion and its juice | 1 |
| about 1/4 cup onion | 1 |
| about 1/4-ounce tender onion | 1 |
| about 2 cups pink pickled onions (recipe follows) | 2 |
| about 2 cups roasted onion, caper, and tarragon sauce | 1 |
| about 2 tablespoons chopped white onion | 1 |
| about one cup, onion | 1 |
| accompaniment: "epi:recipelink id="238426">honeyed red-onion confit | 1 |
| accompaniment: jalapeño onion marmalade | 1 |
| accompaniment: onion gravy | 1 |
| accompaniment: onion-rye flatbreads | 1 |
| accompaniment: roasted balsamic red onion | 1 |
| accompaniment: thinly sliced red or sweet onion | 1 |
| accompaniment:sweet-onion quesadillas | 1 |
| accompaniments: chopped cilantro; lime wedges; chopped white onion | 1 |
| accompaniments: chopped white or red onion; chopped cilantro | 1 |
| accompaniments: corn flan and onion and orange marmalade | 1 |
| accompaniments: cubed country bread, assorted cooked vegetables such as broccoli, cauliflower, carrots, and pearl onion | 1 |
| accompaniments: cubes of avocado tossed with lime juice; tomatillo salsa; lime wedges; chopped white onion; fresh cilantro sprigs | 1 |
| accompaniments: diced avocado; crema; queso fresco; thinly sliced iceberg or romaine lettuce; chopped white onion; sliced radishes; fried tortilla strips or chips; lime wedges; dried oregano; dried hot red-pepper flakes | 1 |
| accompaniments: fresh bean sprouts; very thinly sliced onion (rinsed and drained); fresh cilantro, mint, and basil (preferably thai) leaves; thinly sliced scallions; lime wedges; thinly sliced fresh thai or serrano chiles; asian fish sauce (preferably nuoc mam) | 1 |
| accompaniments: fresh cilantro leaves; chopped plum tomato; finely chopped white onion; tortilla chips | 1 |
| accompaniments: fried tortilla strips (see cooks' note, below); 1/2-inch cubes of california avocado; thinly sliced cabbage or lettuce; chopped white onion; chopped radishes; lime wedges; crumbled dried oregano (preferably mexican); dried hot red pepper flakes | 1 |
| accompaniments: hot corn tortillas or rice; cooked black beans (rinsed and drained if canned); chopped white onion; lime wedges | 1 |
| accompaniments: mayonnaise; coarse-grain mustard; thinly sliced red onion; thinly sliced sweet gherkin pickles; about 2 cups baby romaine lettuce | 1 |
| accompaniments: sour cream; sliced avocado; chopped white onion; lime wedges | 1 |
| additional chopped green onion | 1 |
| additional chopped green onion tops | 1 |
| additional chopped onion | 1 |
| additional chopped onion, fresh cilantro, radish slices or roses, and/or a little crumbled mexican queso fresco or other fresh cheese like feta or farmer's cheese, for garnish | 2 |
| additional elements, such as one or a combination of: strips of red or green bell pepper or pimiento; hard-boiled eggs; rounds of red onion; sardines, tuna, and/or salami; spinach leaves or salad greens | 1 |
| adobo seasoning (equal parts garlic powder, onion powder, ground cumin, and salt)* | 1 |
| an onion | 1 |
| and we always top with green onions. we love the color and the crunch! | 1 |
| any or all of the following, cut into large chunks if necessary: 1/2 peeled onion, 1 small peeled carrot, 1 celery rib, a garlic clove, a bay leaf, a small tomato, a thyme sprig or two, parsley stems | 1 |
| apple, green onion, and jalapeño salsa | 2 |
| aromatics: 1 bay leaf, several thyme sprigs, 2 thin onion slices | 1 |
| artichoke hearts, quartered and simmered in white wine, onion and water (reserve 1/3 cup cooking liquid | 1 |
| assorted additional toppings (such as tomato and grilled onion slices) | 1 |
| assorted condiments, such as mango chutney, honey mustard, garlic mayonnaise, thinly sliced onion, thinly sliced cucumbers, and hot pepper sauce | 1 |
| assorted cooked vegetables such as broccoli, cauliflower, carrots, and pearl onion | 1 |
| assorted cooked vegetables such as broccoli, small carrots, pearl onions, and potato | 1 |
| assorted cut up veggies for dipping, try baby carrots, celery, radishes, bell peppers, red onion, scallions and cucumbers | 1 |
| assorted cut-up vegetables (broccoli, carrots, tomatoes, bell peppers, cauliflower, onions and mushrooms) | 1 |
| assorted cut-up vegetables (such as carrots, cucumbers, red bell peppers, yellow bell peppers, cherry tomatoes, fennel bulbs, green onions and radishes) | 1 |
| assorted fresh vegetables (peppers, onions, and/or broccoli) | 1 |
| assorted garnishes, such as chopped onion, shredded white cheddar | 1 |
| assorted pearl onions such as red, white, and/or yellow (about 8 cups) | 2 |
| assorted pickled garnishes: cornichons, pickled onions, caper berry | 1 |
| assorted pickled vegetables (onions, pepperoncini) | 1 |
| assorted red and yellow pearl onions (about 2 1/2 cups) | 1 |
| assorted root vegetables (4 ounces each: red potatoes, baby carrots, spring onions, and turnips or any other combination of root vegetables) | 1 |
| assorted sliced vegetables, such as eggplant, carrot, broccoli, zucchini and onions, patted dry | 1 |
| assorted spring vegetables (such as carrots, asparagus, radishes, spring onions, or sugar snap peas), trimmed or peeled if needed, cut into same-size pieces | 1 |
| assorted trimmed baby vegetables (such as halved fingerling and purple potatoes, baby carrots, brussels sprouts, cauliflower, pearl onions, pattypan squash, and/or strips of large vegetables like bell peppers) | 1 |
| assorted vegetables (bell peppers, zucchini, eggplant, tomatoes, asparagus, potatoes, fennel, onions) cleaned and if necessary cut or skewered | 1 |
| assorted vegetables (green pepper, onion, mushrooms, and spinach leaves) | 1 |
| assorted vegetables (shredded carrot, canned baby corn, spinach, bean sprouts, red onion ), steamed or raw | 1 |
| assorted vegetables (such as zucchini, bell peppers, red onions and large mushrooms) | 1 |
| assorted vegetables and seafood (scallops, broccoli, mushrooms, eggplant, squash, onions, scallions, asparagus, shrimp) all vegetables should be sliced thin so they fry quickly | 1 |
| assorted vegetables, such as green or red bell pepper, cherry tomatoes, zucchini, and onion, all cubed except tomatoes, for the kabobs, as desired | 1 |
| at least 1/2 cup chopped red onion | 1 |
| baby green onion | 1 |
| baby onion | 4 |
| baby red onion | 1 |
| bacon and sweet onion marmalade, recipe follows | 1 |
| bacon-green onion vinaigrette, recipe follows | 1 |
| bag (14-ounce) frozen pearl onions, c&w | 1 |
| bag (28 ounces) frozen potato cubes with onions and peppers (recommended: ore-ida o'brien potatoes) | 1 |
| bag birds eye® recipe ready chopped green peppers & onion | 1 |
| bag birds eye® recipe ready chopped onion | 1 |
| bag birds eye® recipe ready tri-color pepper & onion blend | 1 |
| bag frozen onions and peppers such as birds eye pepper stir-fry mix (4 cups) | 1 |
| bag frozen or fresh pearl onions, see note | 1 |
| bag frozen pearl onion | 3 |
| bag frozen pearl onions, thawed | 3 |
| bag frozen small white onions, thawed | 1 |
| bag gourmet chips, preferred brand terra chips in yukon gold onion and garlic flavor | 1 |
| bag pearl onion | 1 |
| bag red or yellow pearl onion | 1 |
| bag reduced fat potato chips (recommended: cape cod brand or terra brand garlic and onion flavor yukon chips) | 1 |
| bags frozen chopped onions, thawed | 1 |
| bags frozen pearl onions, thawed | 2 |
| barbecued onion | 2 |
| barbecued onions, recipe follows | 1 |
| bbq onion | 1 |
| beer battered onion rings, recipe follows | 1 |
| bermuda onion | 7 |
| bermuda red onion | 1 |
| bertolli® vidalia onion with roasted garlic sauce | 1 |
| bias cut green onion | 1 |
| bias-cut green onions, loosely packed | 1 |
| bibb lettuce, caramelized onions, and sliced feta (for serving) | 1 |
| big pinch chopped green onion | 1 |
| big yellow onion | 1 |
| birds eye® recipe ready chopped onions & garlic | 1 |
| blaak onion jam | 1 |
| black onion (nigella) seeds (see tip) | 1 |
| black onion seeds | 1 |
| blanched and peeled pearl onion | 1 |
| blooming onion: | 1 |
| bob's all around dust* (blend of ground chili and onion powder) | 1 |
| boiling onion | 6 |
| boiling onions (1 1/4 to 1 1/2 inches wide, about 1 lb), trimmed and peeled | 1 |
| boiling or pearl onion | 1 |
| bottle (10 oz) cocktail onion | 1 |
| bottled pickled onions and cornichons (french sour gherkins, available at specialty foods shops and some supermarkets) for garnish | 1 |
| bottled sweet vidalia onion dressing (recommended: newman's own) or any vinaigrette dressing | 1 |
| box (8 ounces) frozen petite peas with pearl onions, thawed | 1 |
| box frozen pearl onion | 1 |
| box frozen pearl onions, defrosted | 1 |
| box frozen potato & onion pierogies | 1 |
| braised onion ribbons with celery and sliced baked potatoes with parsley butter as accompaniments | 1 |
| brown onion | 3 |
| brown-skinned onion | 1 |
| brunoise red onion | 1 |
| brunoise-cut red onion | 1 |
| brunoised onion | 1 |
| brunoised red onion | 1 |
| bulb spring onion | 1 |
| bundle green onions, cut into 1-inch sections | 1 |
| bundles green onion | 1 |
| butter, to saute the onion | 1 |
| buttermilk, for coating onion | 1 |
| button mushrooms, trimmed and thinly sliced (or other veggie your kids like: onions, carrots, peas, or green beans) | 1 |
| campbell's® condensed french onion soup | 3 |
| can campbell's® condensed french onion soup | 1 |
| can canned french fried onion | 1 |
| can canned onion | 1 |
| can cheddar-flavored french fried onions (such as french's®) | 1 |
| can chopped tomatoes with onions, drained | 1 |
| can condensed cream of onion soup | 2 |
| can condensed french onion soup | 22 |
| can condensed french onion soup (such as campbell's ®) | 1 |
| can condensed onion soup | 2 |
| can cream of onion soup | 3 |
| can diced tomatoes with garlic and onion | 6 |
| can diced tomatoes with garlic and onion, drained | 1 |
| can diced tomatoes with garlic, onion, and peppers, drained | 1 |
| can diced tomatoes with green pepper and onion, drained | 1 |
| can diced tomatoes with green pepper, celery, and onion | 1 |
| can diced tomatoes with green peppers and onion | 2 |
| can diced tomatoes with green peppers, celery, and onion (recommended: hunt's) | 1 |
| can diced tomatoes with onion and celery, drained | 1 |
| can diced tomatoes with onion, celery, and green pepper | 1 |
| can french fried onion | 12 |
| can french onion soup | 1 |
| can french onion soup (such as campbell's ®) | 1 |
| can french-fried onion | 36 |
| can french-fried onion rings | 2 |
| can french-fried onions (such as french's®) | 1 |
| can french-fried onions, crushed | 1 |
| can fried onion | 1 |
| can peas with mushrooms and pearl onions (such as le sueur®), undrained | 1 |
| can red gold® petite diced tomatoes with onion, celery & green pepper | 1 |
| can stewed tomatoes (such as del monte® stewed tomatoes with onions, celery, and green peppers) | 1 |
| can stewed tomatoes with peppers, onions and celery | 1 |
| can tomato sauce with garlic and onion | 1 |
| candied onions (recipe follows) | 1 |
| canned french fried onion | 1 |
| canned french-fried onion | 3 |
| canned french-fried onion rings, plus additional 1/2 cup | 1 |
| canned fried onion | 2 |
| canned fried onions, for topping | 1 |
| canned pickled jalapenos, carrots and onions, drained and chopped (recommended: la costena) | 1 |
| canola oil, for grilling onion | 1 |
| canola oil, plus more for cooking onion | 1 |
| canola oil1 onion | 1 |
| cans condensed french onion soup | 3 |
| cans cream of onion soup | 1 |
| cans diced tomatoes with green peppers, celery and onion | 1 |
| cans diced tomatoes with seasonings (green pepper and onion or garlic and oregano, or any flavor you want) | 1 |
| cans french fried onion | 1 |
| cans french onion soup | 1 |
| cans petite-cut tomatoes with onions and roasted garlic, undrained | 1 |
| cans tomatoes with green pepper, celery and onion | 1 |
| capers or pickled red onions (recipe below) for garnish | 1 |
| capers, thinly sliced red onions and dill sprigs, for garnish | 1 |
| caramelized cippolline onion | 1 |
| caramelized onion | 16 |
| caramelized onion and cornbread stuffing, recipe follows | 1 |
| caramelized onion dip, recipe follows | 1 |
| caramelized onion dip: | 1 |
| caramelized onion mashed potatoes, recipe follows | 1 |
| caramelized onion petals, recipe follows | 1 |
| caramelized onion sauce, recipe follows | 1 |
| caramelized onion tomato jam, recipe follows | 1 |
| caramelized onion, radicchio, and goat cheese pizzettes, recipe follows | 1 |
| caramelized onion-tomato relish, recipe follows | 1 |
| caramelized onion: | 1 |
| caramelized onions (one sliced onion sauteed in butter until dark brown) | 1 |
| caramelized onions (optional) | 1 |
| caramelized onions (recipe follows) | 1 |
| caramelized onions reserved from chicken | 1 |
| caramelized onions, recipe follows | 8 |
| caramelized onions, recipe follows, or leftover sauteed onion | 1 |
| caramelized onions, recipe follows, or your favorite recipe | 1 |
| caramelized onions: | 1 |
| caramelized red onions (pinch salt, pepper and 1 tablespoon butter) | 1 |
| caramelized red onions, recipe follows | 1 |
| caramelized sliced onion | 1 |
| caramelized sliced onion, plus more to taste | 1 |
| caramelized spanish onion, recipe follows | 1 |
| carmelized onion | 1 |
| carrot pickled onion salad, recipe follows | 1 |
| carrot, onion and celery trimmings | 1 |
| carton campbell's® sweet onion soup | 1 |
| carton red or white pearl onions, blanched in boiling water 2 minutes and peeled | 1 |
| celery, carrot, 1/2 onion, tied together with string | 1 |
| center-cut solid onion rings | 1 |
| charred spring onion and sesame-chile butter | 1 |
| charred three onion dip, for serving, recipe follows | 1 |
| cheddar-flavored french-fried onion | 1 |
| chicken frankfurters or chicken sausage - pick a flavor that sounds like it will pair up well with the kraut, like apple and onion sausage | 1 |
| chicken, stock, peas, butter, onion, lettuce, spinach, herbs, egg yolks, cream | 1 |
| chive and onion cream cheese | 5 |
| chive and onion flavored cream cheese | 1 |
| chive and onion soft cream cheese | 1 |
| chive and onion soft cream cheese spread | 1 |
| chive-and-onion cream cheese spread (from 8-oz container) | 1 |
| chives and onion light cream cheese | 1 |
| chopped assorted vegetables (pepper, zucchini and/or onion) | 1 |
| chopped bermuda onion | 2 |
| chopped chives or green onion | 4 |
| chopped chives or green onion, as a garnish | 1 |
| chopped chives or salad onion | 1 |
| chopped cilantro leaves or sliced green onion | 2 |
| chopped dried onion | 1 |
| chopped flat-leaf parsley and green onions, for garnish | 1 |
| chopped french-fried onions (recommended: french's) | 1 |
| chopped fresh chives or green onion | 10 |
| chopped fresh chives or green onion tops | 11 |
| chopped fresh chives or green onions (green parts only) | 1 |
| chopped fresh chives or thinly sliced green onion | 1 |
| chopped fresh cilantro and green onion, for garnish | 1 |
| chopped fresh cilantro leaves and green onion, for garnish | 1 |
| chopped fresh coriander or green onions (optional) | 1 |
| chopped fresh green onion | 2 |
| chopped fresh onion | 1 |
| chopped fresh or frozen onions (2 medium yellow onions) | 1 |
| chopped green and/or red onion | 1 |
| chopped green onion | 715 |
| chopped green onion (1 medium) | 1 |
| chopped green onion (optional) | 9 |
| chopped green onion (white part only) | 1 |
| chopped green onion and cilantro (optional) | 1 |
| chopped green onion for topping | 3 |
| chopped green onion for topping (optional) | 1 |
| chopped green onion or chives to garnish | 1 |
| chopped green onion or shallot | 1 |
| chopped green onion tops | 17 |
| chopped green onion tops or chives | 1 |
| chopped green onion tops, for garnish | 1 |
| chopped green onion, for garnish | 3 |
| chopped green onion, green parts only | 1 |
| chopped green onion, green tops only | 1 |
| chopped green onion, or more to taste | 1 |
| chopped green onion, or to taste | 8 |
| chopped green onion, or to taste (optional) | 2 |
| chopped green onion, white and green parts | 2 |
| chopped green onion, white and green parts separated | 1 |
| chopped green onion, white part only | 1 |
| chopped green onion, white parts and some of the green parts | 1 |
| chopped green onions (4 medium) | 1 |
| chopped green onions (about 10 large) | 1 |
| chopped green onions (about 14 onions) | 1 |
| chopped green onions (about 2 bunches) | 1 |
| chopped green onions (about 2) | 1 |
| chopped green onions (about 4 large) | 1 |
| chopped green onions (about 4) | 2 |
| chopped green onions (about 6 large) | 1 |
| chopped green onions (about 6) | 3 |
| chopped green onions (about 8 large) | 1 |
| chopped green onions (about 8 small) | 1 |
| chopped green onions (dark green parts only; about 2 bunches) | 1 |
| chopped green onions (green part only) | 2 |
| chopped green onions (green parts only) | 1 |
| chopped green onions (just the greens) | 1 |
| chopped green onions (light parts only) | 1 |
| chopped green onions (optional) | 4 |
| chopped green onions (scallions) | 3 |
| chopped green onions (scallions), white and light green parts | 1 |
| chopped green onions (white and pale green parts only) | 1 |
| chopped green onions (white and pale green parts only; about 2) | 1 |
| chopped green onions - white and light green parts separated from green tops | 1 |
| chopped green onions and chopped fresh cilantro (for garnish) | 1 |
| chopped green onions and cilantro leaves, for garnish | 1 |
| chopped green onions and cilantro, for garnish | 1 |
| chopped green onions and/or sesame seeds (optional) | 1 |
| chopped green onions for garnish | 3 |
| chopped green onions or chives | 3 |
| chopped green onions or chives, for garnish | 1 |
| chopped green onions or scallions, white and green parts | 1 |
| chopped green onions with tops | 1 |
| chopped green onions, (about 5) | 1 |
| chopped green onions, both white and green parts | 1 |
| chopped green onions, for garnish | 6 |
| chopped green onions, for garnish (optional) | 1 |
| chopped green onions, for serving | 2 |
| chopped green onions, garnish | 1 |
| chopped green onions, green and white parts | 1 |
| chopped green onions, green part only | 1 |
| chopped green onions, green part only, for garnish | 1 |
| chopped green onions, if desired | 1 |
| chopped green onions, including green part | 1 |
| chopped green onions, including tops | 1 |
| chopped green onions, plus more for garnish | 2 |
| chopped green onions, white and green part | 1 |
| chopped green onions, white and green parts | 2 |
| chopped green onions, white part only | 2 |
| chopped green onions, white parts only | 1 |
| chopped green scallion onion | 1 |
| chopped greens onion | 1 |
| chopped grilled red onion | 2 |
| chopped large onion | 1 |
| chopped leeks (or onions) | 1 |
| chopped maui onion | 2 |
| chopped maui or other sweet onion | 1 |
| chopped medium onion | 5 |
| chopped medium sized yellow onion | 1 |
| chopped onion | 2,129 |
| chopped onion (1 large) | 5 |
| chopped onion (1 medium) | 9 |
| chopped onion (1 pound) | 1 |
| chopped onion (1 small) | 1 |
| chopped onion (1/2 small) | 1 |
| chopped onion (2 medium) | 1 |
| chopped onion (2 onions) | 3 |
| chopped onion (about 1 large onion), pureed with 1/4 cup water | 1 |
| chopped onion (about 1 large) | 4 |
| chopped onion (about 1 small) | 1 |
| chopped onion (about 1/2 pound) | 1 |
| chopped onion (about 2 medium) | 2 |
| chopped onion (about 2 onions) | 1 |
| chopped onion (about 3 medium onions) | 1 |
| chopped onion (from 1 large) | 1 |
| chopped onion (from 3 medium) | 1 |
| chopped onion (from about 1/2 medium onion) | 1 |
| chopped onion (optional) | 14 |
| chopped onion (white or yellow or red--whatever you have left from dinner) | 1 |
| chopped onion or shallots | 1 |
| chopped onion, about 1 medium onion | 1 |
| chopped onion, for garnish | 1 |
| chopped onion, for serving | 1 |
| chopped onion, or more to taste | 3 |
| chopped onion, or to taste | 4 |
| chopped onion, plus 2 large, quartered | 1 |
| chopped onion, rinsed and drained | 1 |
| chopped onion, sauteed in butter | 1 |
| chopped onion, shredded cheddar cheese, sour cream, and salsa for garnish | 1 |
| chopped onion, such as white or vidalia | 1 |
| chopped onions (2 large) | 2 |
| chopped onions (2 onions) | 2 |
| chopped onions (about 1 1/4 pounds) | 1 |
| chopped onions (about 1 pound) | 5 |
| chopped onions (about 2 3/4 pounds) | 1 |
| chopped onions (about 2 large) | 1 |
| chopped onions (about 2 medium) | 5 |
| chopped onions (about 3 large) | 1 |
| chopped onions, approximately 3 cups | 1 |
| chopped onions, as an accompaniment | 1 |
| chopped onions, corn chips | 1 |
| chopped onions, for serving | 2 |
| chopped onions, leeks or scallion | 4 |
| chopped onions, plus 1 whole onion with skin | 1 |
| chopped onions, scallions, and/or shallots | 1 |
| chopped organic onion, red pepper, yellow pepper, green pepper | 1 |
| chopped pungent red or yellow onion | 1 |
| chopped purple onion | 3 |
| chopped radish or red onion as an accompaniment | 1 |
| chopped raw onion | 3 |
| chopped raw onion or chopped red onion | 1 |
| chopped raw onion or scallion | 1 |
| chopped raw white onion | 1 |
| chopped raw white or red onion | 1 |
| chopped raw yellow onions or red onion | 1 |
| chopped red onion | 392 |
| chopped red onion (1 large) | 1 |
| chopped red onion (1 medium) | 1 |
| chopped red onion (about 1 small) | 1 |
| chopped red onion or scallion | 1 |
| chopped red onion plus 1/2 cup thinly sliced | 1 |
| chopped red onion plus thinly sliced red onion rounds for garnish | 1 |
| chopped red onion, for garnish | 1 |
| chopped red onion, or to taste | 1 |
| chopped red onion, tomato, and lettuce, for serving | 1 |
| chopped red onions (2 onions) | 1 |
| chopped red onions (about 2 large) | 1 |
| chopped red onions, for garnish | 2 |
| chopped red onions, for serving | 1 |
| chopped red or yellow onion | 1 |
| chopped red, yellow, or white onion or scallion | 1 |
| chopped scallions (green onions) | 2 |
| chopped scallions or green onion | 1 |
| chopped shallot or onion | 2 |
| chopped shallots or green onion | 1 |
| chopped shallots or onion | 2 |
| chopped shallots or red onion | 1 |
| chopped shallots or spring onions (scallions) | 1 |
| chopped small onion | 1 |
| chopped spanish onion | 6 |
| chopped spanish onion (1 large) | 1 |
| chopped spanish onion (1 pound) | 1 |
| chopped spanish onion, about 1 large onion | 1 |
| chopped spanish onions (about 1 large) | 1 |
| chopped spring garlic (substitute green onions in off season) | 1 |
| chopped spring onion | 5 |
| chopped sweet onion | 57 |
| chopped sweet onion (1 pound) | 1 |
| chopped sweet onion (such as a walla walla) | 1 |
| chopped sweet onion (such as maui or vidalia) | 1 |
| chopped sweet onion (such as maui) | 2 |
| chopped sweet onion (such as vidalia or maui) | 6 |
| chopped sweet onion (such as vidalia) | 2 |
| chopped sweet onion (such as vidalia®) | 6 |
| chopped sweet onion such as vidalia | 2 |
| chopped sweet onion such as vidalia or walla walla | 1 |
| chopped sweet onion such as vidalia, walla walla, or maui | 1 |
| chopped sweet onion, such as vidalia | 1 |
| chopped sweet onions (such as vidalia or maui; about 2 medium) | 1 |
| chopped sweet onions (such as vidalia or maui; about 3 pounds) | 1 |
| chopped sweet onions (such as vidalia or walla walla) | 1 |
| chopped sweet onions, preferably vidalia | 1 |
| chopped sweet onions, such as vidalia | 1 |
| chopped sweet yellow onion | 2 |
| chopped texas sweet or vidalia onion | 1 |
| chopped vidalia onion | 19 |
| chopped vidalia or maui onion | 1 |
| chopped vidalia or other sweet onion | 3 |
| chopped vidalia or sweet onion | 2 |
| chopped vidalia or sweet onion (from about 1/2 large) | 1 |
| chopped white onion | 133 |
| chopped white onion (about 1 medium) | 1 |
| chopped white onion (about 1/4 onion) | 1 |
| chopped white onion (from 1 large or 2 small onions) | 1 |
| chopped white onion and sliced pickled jalapenos, for topping | 1 |
| chopped white onion chopped | 1 |
| chopped white onion, about 1 medium | 2 |
| chopped white onion, for serving | 1 |
| chopped white onion, if serving in a roll | 1 |
| chopped white onion, or to taste | 1 |
| chopped white onion, serving suggestion | 1 |
| chopped white onion, to serve | 1 |
| chopped white, red, or green onion | 1 |
| chopped yellow cooking onion | 1 |
| chopped yellow onion | 100 |
| chopped yellow onion (1 large onion) | 6 |
| chopped yellow onion (1 large) | 4 |
| chopped yellow onion (1 onion) | 7 |
| chopped yellow onion (1/2 onion) | 1 |
| chopped yellow onion (2 onions) | 7 |
| chopped yellow onion (optional) | 1 |
| chopped yellow onion, drained of excess water | 1 |
| chopped yellow onions (2 large onions) | 3 |
| chopped yellow onions (2 large) | 1 |
| chopped yellow onions (2 onions) | 18 |
| chopped yellow onions (2 small) | 2 |
| chopped yellow onions (3 large onions) | 1 |
| chopped yellow onions (3 large) | 1 |
| chopped yellow onions (3 onions) | 3 |
| chopped yellow onions (4 large onions) | 1 |
| chopped yellow or green onion | 1 |
| chunks yellow onion (about 1/4 small onion total) | 1 |
| cipolini onions, roasted and peeled | 1 |
| cipolinni onions, roasted then peeled | 1 |
| cipolline onion | 3 |
| cipolline onions or 1-inch-diameter pearl onions, blanched 1 minute | 1 |
| cipolline onions or pearl onion | 1 |
| cipolline onions or small boiling onion | 1 |
| cipolline onions* or boiling onion | 2 |
| cipolline onions, unpeeled | 1 |
| cipolline or pearl onion | 2 |
| cipolline or small (1 1/2-inch) white boiling onion | 1 |
| cipollini onion | 21 |
| cipollini onions (about 2 sacks) or 1 1/2 pounds red or yellow pearl onion | 1 |
| cipollini onions, blanched and peeled | 1 |
| cipollini onions, boiled 3 minutes | 1 |
| cipollini onions, cooked in boiling water until tender and peeled | 2 |
| cipollini onions, quartered | 1 |
| cipollini onions, roasted | 1 |
| cipollini onions, trimmed and peeled | 1 |
| cipollini or pearl onions, stemmed and peeled | 1 |
| cipollini or pearl onions, trimmed and peeled | 1 |
| cipollini or small white onion | 1 |
| cipollini or spring onion | 1 |
| cipollini or sweet onions, halved if large | 1 |
| cipollini, boiler, or pearl onion | 1 |
| cippoline onions, skins on | 1 |
| cippolini onion | 8 |
| cippolini onions, ends trimmed and peeled, halve larger onion | 1 |
| cippolini or pearl onion | 1 |
| cippolini, small italian flat-shaped sweet onion | 1 |
| clean scallions cut into 2-inch lengths, using only the pale green and white sections of the onion | 1 |
| cleaned spring onion | 1 |
| coarsely chopped fresh or frozen onions (about 2 medium-large yellow onions) | 1 |
| coarsely chopped green onion | 5 |
| coarsely chopped green onion (scallions) | 1 |
| coarsely chopped green onion or sweet onion (such as maui or vidalia) | 1 |
| coarsely chopped green onions (about 2 large) | 1 |
| coarsely chopped green onions (white parts only) | 1 |
| coarsely chopped green onions, white and green parts | 1 |
| coarsely chopped medium onion | 1 |
| coarsely chopped onion | 40 |
| coarsely chopped onion (1 medium-size onion) | 1 |
| coarsely chopped onion, plus 2 cups chopped, plus 1 medium onion | 1 |
| coarsely chopped onions (about 2 large) | 1 |
| coarsely chopped onions (about 3 medium onions) | 1 |
| coarsely chopped pickled cocktail onions (sour) | 1 |
| coarsely chopped red onion | 22 |
| coarsely chopped red onion (about ½ small onion) | 1 |
| coarsely chopped spanish onion | 1 |
| coarsely chopped sweet onion | 2 |
| coarsely chopped sweet onion (such as maui or vidalia) | 1 |
| coarsely chopped sweet white onion | 2 |
| coarsely chopped white onion | 6 |
| coarsely chopped white onion (1 large) | 1 |
| coarsely grated onion | 4 |
| coarsely grated onion (grated on large holes of box grater) | 1 |
| coarsely grated onion, squeezed of excess moisture | 1 |
| coarsely grated or minced red onion | 1 |
| coarsely grated yellow onion | 1 |
| coarsely minced onion | 1 |
| cocktail onion | 1 |
| cocktail onions, drained | 1 |
| cocktail onions, for garnish | 1 |
| cocktail onions, rinsed | 1 |
| cocktail pearl onions, for serving | 1 |
| coconut rice with green onions, recipe above | 1 |
| combined coarsely chopped: celery, carrots, onions, scallion | 1 |
| container (7 ounces) chopped onion | 1 |
| container (8 oz.) chives-and-onion cream cheese spread | 1 |
| container chive and onion cream cheese | 2 |
| container cream cheese spread with onion and chives | 1 |
| container french fried onion | 1 |
| container reduced-fat cream cheese with onion and chives, at room temperature | 1 |
| containers chive and onion cream cheese | 1 |
| cooked and small-diced onion | 1 |
| cooked baked onion | 1 |
| cooked onions and green pepper | 1 |
| cooked pearl onion | 1 |
| cooked puréed onion | 1 |
| cooking onion | 1 |
| corn chips, black olives and diced onions, if desired | 1 |
| cranberry-onion jam, recipe follows | 1 |
| creamed onions with bacon and herbs | 1 |
| creme fraiche, lemon wedges, capers and diced red onion, for serving | 1 |
| crisp fried onions, for garnish | 2 |
| crispy french-fried onion | 2 |
| crispy fried onion strings, recipe follows | 1 |
| crispy fried onion strips or store-bought fried onions (recommended: french's original french fried onions) | 1 |
| crispy onion strings, for serving, recipe follows | 1 |
| crispy onions (recommended: french's original), for garnish | 1 |
| crispy onions, such as french's french fried onion | 1 |
| crispy topped bacon and green onion baked beans, recipe follows | 1 |
| crosswise slice of a medium white onion | 1 |
| crumbled queso fresco (optional), cilantro leaves, thinly sliced red onion, and lime wedges (for serving) | 1 |
| crushed french-fried onion | 1 |
| crushed french-fried onions, or as needed | 1 |
| cube french onion bouillon | 1 |
| cubed onion | 1 |
| cubed onions, for garnish | 1 |
| cup1/4-inch diced red onion | 1 |
| curry dip or "really" onion dip, recipes follow, or sauce of your choice | 1 |
| dash chopped green onion | 1 |
| dash onion powder | 11 |
| dash onion powder, or more to taste | 1 |
| dash onion salt | 1 |
| dashes onion powder | 1 |
| deep-fried onion rings, for garnish | 1 |
| dehydrated chopped onion | 1 |
| dehydrated mixed vegetables (preferably mushrooms, onion, and carrots) | 1 |
| dehydrated onion | 5 |
| dehydrated onion flakes | 6 |
| desired fillings (such as shredded cooked chicken or pork, stewed black beans with cheese and lime, corn salad with onion and fresh herbs; for serving) | 1 |
| diagonally sliced green onion | 2 |
| diced (1 medium-large) white onion | 1 |
| diced (1/2-inch) onion | 1 |
| diced (1/3-inch) sweet onion such as vidalia or walla walla (2 1/2 ounces) | 1 |
| diced (1/4 inch) onion | 2 |
| diced (1/4 inch) red onion | 7 |
| diced (1/4-inch) onion | 1 |
| diced (1/4-inch) red onion | 4 |
| diced (1/4-inch) spanish onion | 2 |
| diced (1/4-inch) sweet onion (14 oz) such as vidalia | 1 |
| diced (1/8-inch) onion | 1 |
| diced (yellow or purple) onion | 1 |
| diced cup red onion | 1 |
| diced dried onion | 1 |
| diced green onion | 37 |
| diced green onion (optional) | 1 |
| diced green onion, for garnish | 1 |
| diced green onions, for garnish | 1 |
| diced maui onion | 3 |
| diced medium onion | 1 |
| diced mixed vegetables (recommended: onion, green bell peppers, zucchini, carrots, and mushrooms) | 1 |
| diced onion | 518 |
| diced onion (1/2-inch dice) | 1 |
| diced onion (1/4-inch dice) | 2 |
| diced onion (1/4-inch) | 1 |
| diced onion (about 1 extra-large vidalia onion) | 1 |
| diced onion (about 1 large) | 1 |
| diced onion (about 1 medium onion) | 1 |
| diced onion (about 1) | 1 |
| diced onion (about 1/2 a small onion) | 1 |
| diced onion (optional) | 2 |
| diced onion for garnish | 1 |
| diced onion, 1/8-inch thick | 1 |
| diced onion, approximately 1 medium onion | 1 |
| diced onion, or more to taste | 1 |
| diced onions (2 onions) | 1 |
| diced onions (about 1/2 small onion) | 1 |
| diced onions (approximately 1 large onion) | 1 |
| diced onions, approximately 2 small | 2 |
| diced onions, cut 1/4-inch | 1 |
| diced onions, sauteed | 1 |
| diced purple onion | 1 |
| diced red onion | 250 |
| diced red onion (1/4-inch dice) | 1 |
| diced red onion (1/4-inch pieces) | 1 |
| diced red onion (about 1/2 small) | 1 |
| diced red onion diced | 1 |
| diced red onion in 1/2-inch pieces | 1 |
| diced red onion, 1/4-inch dice | 1 |
| diced red onion, approximately 1 cup | 1 |
| diced red onion, for garnish | 1 |
| diced red onion, for serving | 1 |
| diced red onion, if desired | 1 |
| diced red onion, or more to taste | 1 |
| diced red onion, plus 2 ounces, for garnish | 1 |
| diced red onion, sauteed | 1 |
| diced red or white onion | 2 |
| diced shallot, scallion, or red onion | 1 |
| diced spanish onion | 12 |
| diced spanish onion (1/2-inch dice) | 2 |
| diced spanish onion (diced in a food processor) | 1 |
| diced spanish onions (1 large onion) | 1 |
| diced sweet onion | 24 |
| diced sweet onion (from 1 large) | 1 |
| diced sweet onion (such as vidalia or maui) | 2 |
| diced sweet onion (such as vidalia®) | 1 |
| diced sweet onion, such as maui or vidalia | 1 |
| diced sweet onions, such as vidalia | 1 |
| diced sweet yellow onion (texas, vidalia, maui, etc) | 1 |
| diced tomatoes with garlic and onion | 1 |
| diced vidalia onion | 4 |
| diced white onion | 47 |
| diced white onion (about 8 ounces) | 1 |
| diced white onion, for serving | 1 |
| diced white or red onion | 1 |
| diced yellow onion | 75 |
| diced yellow onion (1/2-inch dice) | 1 |
| diced yellow onion (2 onions) | 1 |
| diced yellow onion (from 1 large) | 1 |
| diced yellow onion, approximately 1/2 cup | 1 |
| diced yellow onion, sauteed until translucent | 1 |
| diced yellow onions (3 large) | 1 |
| diced yellow onions (about 4 medium onions) | 1 |
| diced yellow onions, about 2 medium onion | 1 |
| dickinson's® sweet 'n' hot pepper & onion relish | 1 |
| different onions (red, yellow, sweet, etc.) | 1 |
| dole red onion | 2 |
| dole red onion, thinly sliced | 1 |
| dole® onion | 1 |
| dole® red onion, thinly sliced | 1 |
| dozen purchased frozen pierogies (such as potato-and-onion or cheese) | 1 |
| dozen small pearl onion | 1 |
| drained bottled cocktail onion | 3 |
| dried chopped onion | 3 |
| dried granulated onion | 2 |
| dried minced onion | 127 |
| dried minced onion (optional) | 2 |
| dried minced onion flakes | 15 |
| dried minced onion, or more to taste | 1 |
| dried minced onion, or to taste | 3 |
| dried minced onion, rehydrated | 1 |
| dried onion | 3 |
| dried onion flakes | 38 |
| dried onion flakes (optional) | 1 |
| dried onion flakes, or to taste | 2 |
| dried onion granules | 3 |
| dried onion powder | 1 |
| dried onions or garlic, for seasoning | 1 |
| dry onion soup mix | 10 |
| each 1/2-inch diced vegetables: yellow onion, green bell pepper, red bell pepper, and tomato | 1 |
| each carrots, celery and onion | 1 |
| each chopped (1/4 inch) onion and poblano pepper | 1 |
| each chopped onion | 1 |
| each chopped red onions and celery | 1 |
| each chunked roasted beets, roasted pearl onions, chunked roasted zucchini, cubed roasted eggplant | 1 |
| each diced (1/2 inch) onion, celery and fennel | 1 |
| each diced carrot, celery, and onion | 1 |
| each finely chopped onion, bell pepper and mushrooms | 1 |
| each finely chopped onion, green bell pepper, and celery | 1 |
| each finely diced onions and granny smith apples | 1 |
| each finely diced onions, carrots and celery | 1 |
| each garlic and onion powder | 1 |
| each garlic powder and onion powder | 1 |
| each granulated garlic, onion powder, ground ginger | 2 |
| each minced celery, white onion, green bell pepper | 1 |
| each of celery, onions, and carrot | 1 |
| each onion and red bell pepper | 1 |
| each onion salt and ground cumin | 1 |
| each roasted zucchini, eggplant, potatoes, onions, carrots and tomato | 1 |
| echalion or banana shallots, or 2 onions (approx. 8 ounces total) | 1 |
| egg and onion matzo cracker sheets | 1 |
| enoki mushrooms, green onion slivers, cilantro leaf | 1 |
| envelope beef and onion dry soup mix | 1 |
| envelope beefy onion soup mix (recommended: lipton) | 1 |
| envelope dry onion gravy mix | 2 |
| envelope dry onion soup mix | 57 |
| envelope dry onion soup mix (from a 2-ounce package) | 1 |
| envelope golden onion soup mix (recommended: lipton) | 1 |
| envelope lipton recipe secrets onion soup mix | 1 |
| envelope onion soup mix | 10 |
| envelope onion soup mix (1/2 2.4-ounce package) | 1 |
| envelope onion soup mix (such as lipton® beefy onion) | 1 |
| envelopes dry onion soup mix | 4 |
| envelopes onion gravy mix | 1 |
| envelopes onion soup mix | 1 |
| extra large onion | 4 |
| extra large onion, cut into chunks | 1 |
| extra large onion, or 3 medium ones | 1 |
| extra large sweet onion | 1 |
| extra large vidalia onion | 1 |
| extra large yellow onion | 1 |
| extra-large onion | 1 |
| extra-large yellow onion | 2 |
| extra-large yellow onions (the biggest ones you can find!) | 1 |
| extra-virgin olive oil, 1 for onion, 2 tablespoons to fry cakes | 1 |
| favorite burger toppings, such as raw onion, tomato slices and lettuce | 1 |
| favorite onion gravy, heated | 1 |
| favorite spices (garlic, ginger, onion powder, etc.) | 1 |
| fine chopped red onion | 1 |
| fine diced spanish onion | 1 |
| fine diced white onion | 1 |
| fine diced yellow onion | 4 |
| finely chopped (150 grams/1 cup) onion | 1 |
| finely chopped assorted fresh vegetables (peppers, tomatoes and/or green onions) | 2 |
| finely chopped chives or green onion | 1 |
| finely chopped dole red onion | 1 |
| finely chopped fresh chives or green onion tops | 1 |
| finely chopped fresh green onion | 1 |
| finely chopped green onion | 89 |
| finely chopped green onion (optional) | 1 |
| finely chopped green onion (white and light green parts) | 2 |
| finely chopped green onion (white and pale green parts) | 1 |
| finely chopped green onion tops | 4 |
| finely chopped green onion tops (dark green parts) | 1 |
| finely chopped green onion, green part only | 1 |
| finely chopped green onion, or to taste | 2 |
| finely chopped green onions (2 medium) | 1 |
| finely chopped green onions (about 2) | 1 |
| finely chopped green onions (about 3 large) | 1 |
| finely chopped green onions (optional) | 2 |
| finely chopped green onions (white and green parts only) | 1 |
| finely chopped green onions (white parts only) | 1 |
| finely chopped green onions (white portion only) | 1 |
| finely chopped green onions, white and light green parts | 1 |
| finely chopped large onion | 1 |
| finely chopped maui onion | 1 |
| finely chopped medium onion | 1 |
| finely chopped onion | 669 |
| finely chopped onion (1 large) | 8 |
| finely chopped onion (1 medium) | 4 |
| finely chopped onion (1 small) | 2 |
| finely chopped onion (about 1 medium) | 2 |
| finely chopped onion (about 1/2 medium onion) | 1 |
| finely chopped onion (about 2 medium onions) | 1 |
| finely chopped onion (about 2 medium-sized onions) | 1 |
| finely chopped onion (optional) | 4 |
| finely chopped onion (preferably sweet onion, such as vidalia or walla walla) | 1 |
| finely chopped onion 1/2 cup diced or grated | 1 |
| finely chopped onion and green or red pepper (optional) | 1 |
| finely chopped onion if desired | 1 |
| finely chopped onion or 1 tablespoon chopped chives | 1 |
| finely chopped onion or shallots | 1 |
| finely chopped onion, eyeball it | 1 |
| finely chopped onion, or more to taste | 1 |
| finely chopped onion, plus 2 cups roughly chopped | 1 |
| finely chopped onion, thinly sliced scallions, sour cream and chopped fresh cilantro, for serving | 1 |
| finely chopped onions (about 2 medium) | 2 |
| finely chopped onions or shallots | 1 |
| finely chopped red onion | 238 |
| finely chopped red onion (about 1/2 large onion) | 1 |
| finely chopped red onion (about 1/4 small red onion), soaked in cold water 5 minutes | 1 |
| finely chopped red onion (optional) | 1 |
| finely chopped red onion or green onion | 1 |
| finely chopped red onion or scallion | 1 |
| finely chopped red onion or scallions, whites and greens | 1 |
| finely chopped red onion, for garnish | 2 |
| finely chopped red onion, or more to taste | 1 |
| finely chopped red onion, rinsed in cool water and drained | 2 |
| finely chopped red onion, soaked in cold water for 10 minutes if strong | 1 |
| finely chopped red onions (about 1/2 medium onion) | 1 |
| finely chopped red onions (about 5 medium) | 2 |
| finely chopped red onions or scallion | 1 |
| finely chopped red onions, sweated | 1 |
| finely chopped shallot or onion | 3 |
| finely chopped shallot or small white onion | 1 |
| finely chopped shallot, or white parts of green onion | 1 |
| finely chopped shallots or onion | 2 |
| finely chopped shallots or sweet onion | 1 |
| finely chopped small white onion | 1 |
| finely chopped spanish onion | 5 |
| finely chopped spanish red onion | 1 |
| finely chopped spring onion | 1 |
| finely chopped spring onions or green onions (white and pale green parts only) | 1 |
| finely chopped sweet onion | 19 |
| finely chopped sweet onion (such as vidalia®) | 2 |
| finely chopped sweet onion such as vidalia | 4 |
| finely chopped sweet onion such as vidalia or walla walla | 1 |
| finely chopped sweet onion, or to taste | 1 |
| finely chopped sweet onion, such as vidalia | 3 |
| finely chopped sweet onions (such as vidalia®) | 1 |
| finely chopped sweet or vidalia onion | 1 |
| finely chopped sweet white onion | 1 |
| finely chopped vidalia onion | 5 |
| finely chopped vidalia onion (about 1/2 medium onion) | 1 |
| finely chopped vidalia or maui onion | 1 |
| finely chopped vidalia or other sweet onion | 5 |
| finely chopped white onion | 70 |
| finely chopped white onion plus 8 very thin slices | 1 |
| finely chopped white onion, rinsed in a sieve and patted dry | 1 |
| finely chopped white onions (optional) | 1 |
| finely chopped wild onions or yellow onion | 1 |
| finely chopped yellow onion | 33 |
| finely chopped yellow onion (about 1 small) | 1 |
| finely chopped yellow onion (about 1/2 large onion) | 1 |
| finely chopped yellow onion, sauteed | 1 |
| finely chopped yellow onions (2 small onions) | 1 |
| finely diced bermuda onion | 1 |
| finely diced dole® red onion | 1 |
| finely diced green onion | 2 |
| finely diced green onions (scallions) | 2 |
| finely diced maui, vidalia, or other sweet onion | 2 |
| finely diced onion | 86 |
| finely diced onion (about 1 medium onion) | 1 |
| finely diced onion (about 1/2 small onion) | 1 |
| finely diced onion (about 1/4 small onion) | 1 |
| finely diced red onion | 93 |
| finely diced red onion (1 large onion) | 1 |
| finely diced red onion (1 onion) | 1 |
| finely diced red onion (1/2 medium red onion) | 1 |
| finely diced red onion or sliced scallions or chives | 1 |
| finely diced shallots, or 1 white onion | 3 |
| finely diced shallots, or 1 white onion finely diced | 1 |
| finely diced spanish onion | 11 |
| finely diced sweet onion | 9 |
| finely diced sweet onion (such as vidalia®) | 1 |
| finely diced sweet onion, such as vidalia | 1 |
| finely diced sweet or yellow onion | 1 |
| finely diced sweet white onion | 1 |
| finely diced vidalia onion | 3 |
| finely diced white onion | 10 |
| finely diced white onion (about 1/2 onion) | 1 |
| finely diced white onions (about 1 small) | 1 |
| finely diced yellow onion | 14 |
| finely diced yellow onion (about 1 small) | 2 |
| finely diced yellow onion or shallot | 1 |
| finely grated onion | 8 |
| finely grated red onion | 3 |
| finely grated white onion (using small teardrop holes of a box grater) | 1 |
| finely julienned (1-inch long) red onion | 1 |
| finely julienned red onion | 2 |
| finely minced fresh onion | 1 |
| finely minced maui onion | 1 |
| finely minced onion | 24 |
| finely minced onion (about 2 medium onions) | 1 |
| finely minced onion (about 2 medium) | 1 |
| finely minced onion or 1/2 teaspoon dried minced onion | 1 |
| finely minced red onion | 10 |
| finely minced shallot or green onion | 2 |
| finely minced shallots or onion | 1 |
| finely minced sweet onion (about 2 small onions) | 1 |
| finely minced vidalia onion | 1 |
| finely minced white onion | 4 |
| finely minced yellow onion | 3 |
| finely shredded green onion | 1 |
| finely sliced chives or green onions, for garnish | 2 |
| finely sliced green onion | 15 |
| finely sliced green onions, plus more for garnish if desired | 1 |
| finely sliced lettuce and chopped onion, for garnish | 1 |
| finely sliced onion | 5 |
| finely sliced onions cooked in 2 tablespoons olive oil | 1 |
| finely sliced red onion | 4 |
| finely sliced spring onion greens | 1 |
| finely sliced spring onions (green) | 1 |
| finely sliced spring onions (scallions) | 1 |
| finely sliced sweet onion | 3 |
| finely sliced wadmalaw sweets or other sweet onions, such as vidalia or maui (about 3 pounds) | 1 |
| finely slivered red onion | 1 |
| finely-chopped onions, sauteed in 2 tablespoons vegetable oil until crispy brown | 1 |
| finely-minced onion | 1 |
| finley chopped raw white, red or green onion | 1 |
| flaked cooked cod (such as from roast cod with potatoes, onions and olives | 1 |
| for serving: tomato slices, lettuce leaves, red onion slices and dill pickle rounds | 1 |
| for the caramelized onions: | 1 |
| for the onions: | 1 |
| four 1/3-inch-thick slices red onion, secured with wooden picks | 1 |
| freeze-dried onion | 1 |
| french fried onion | 8 |
| french fried onion pieces | 1 |
| french fried onions (1 1/3 cups) | 1 |
| french fried onions or crushed potato chips (optional) | 1 |
| french fried onions, recipe follows | 1 |
| french onion dip | 1 |
| french onion soup | 2 |
| french onion soup (may use canned french onion or homemade) | 1 |
| french onion soup bowls or 8-ounce ramekins | 1 |
| french's fried onion | 1 |
| french's® french fried onion | 2 |
| french's® french fried onions (2 2/3 cups) | 1 |
| french-fried onion | 19 |
| french-fried onion rings | 2 |
| french-fried onions (i like french's), crushed | 1 |
| french-fried onions (such as french's®) | 2 |
| french-fried onions (such as french's®) (optional) | 1 |
| french-fried onions, crushed | 2 |
| french-fried onions, lightly hand-crushed (recommended: french's) | 1 |
| french-fried onions, or to taste | 1 |
| french-fried onions, slightly crumbled | 1 |
| fresh chives or 1 bunch green onion | 1 |
| fresh chives or green onions, cut into 2-inch pieces | 1 |
| fresh chopped, steaming hot, grilled onion | 1 |
| fresh cilantro and diced white onion and radishes, for topping | 1 |
| fresh cilantro and diced white onion, for topping | 1 |
| fresh green onion | 6 |
| fresh green onion; chopped (yields approximately 1 cup) | 1 |
| fresh green onions, grilled and chopped fine | 1 |
| fresh ground onion | 1 |
| fresh italian sausage, removed from casings and sauteed in extravirgin olive oil with minced onion and garlic | 1 |
| fresh minced chives or green onion | 1 |
| fresh onion rolls, buttered and toasted until golden | 1 |
| fresh onion, pureed | 2 |
| fresh or frozen chopped onion (about 1 medium-large yellow onion) | 2 |
| fresh or frozen chopped onions (2 medium-large yellow onions) | 1 |
| fresh or frozen pearl onion | 1 |
| fresh or frozen yuca (1 large), cut crosswise into 2-inch sections for pickled onion | 1 |
| fresh pearl onion | 3 |
| fresh red onion | 1 |
| fresh red pearl onion | 1 |
| fresh sliced white onion | 1 |
| fresh small cipolline onions or pearl onion | 1 |
| fresh sweet yellow onion | 1 |
| fresh white onion | 1 |
| freshly chopped green onion | 5 |
| freshly chopped green onion, green parts only, plus more for garnish | 1 |
| freshly chopped green onions, for garnish | 1 |
| freshly grated onion | 1 |
| freshly peeled or defrosted drained pearl onion | 1 |
| freshly sliced green onion | 2 |
| fried onion | 5 |
| fried onion rings | 1 |
| fried onion snacks (recommended: french's fried onions) | 1 |
| fried onion strings | 1 |
| fried onions (1 1/2 cups) | 1 |
| fried onions (one 2.8-ounce can) | 2 |
| fried onions (one 6-ounce can) | 1 |
| fried onions, for garnish | 1 |
| fried onions, homemade or store-bought, recipe follows | 1 |
| fried onions, or to taste | 1 |
| fried onions, recipe follows | 1 |
| fried onions, such as durkee, or chinese fried noodles, for garnish | 1 |
| fried onions, such as french's | 1 |
| frozen bell pepper and onion mix | 1 |
| frozen chopped fire-roasted peppers and onion blend, thawed | 1 |
| frozen chopped onion | 20 |
| frozen chopped onion (recommended: ore-ida) | 2 |
| frozen chopped onion, thawed | 2 |
| frozen chopped onion, thawed (recommended: ore-ida) | 1 |
| frozen chopped onions (from a 12-oz bag) such as ore ida brand | 1 |
| frozen chopped onions (recommended: ore-ida) | 1 |
| frozen chopped onions - ore-ida | 1 |
| frozen chopped onions and bell peppers, thawed | 1 |
| frozen chopped onions, ore-ida | 2 |
| frozen chopped onions, thawed | 9 |
| frozen chopped onions, thawed and drained | 1 |
| frozen chopped white onion | 1 |
| frozen cipollini onion | 1 |
| frozen cipollini or pearl onions, thawed | 1 |
| frozen diced onion | 1 |
| frozen diced onions (recommended: c&w) | 1 |
| frozen diced onions, thawed | 1 |
| frozen onion | 1 |
| frozen onion rings | 1 |
| frozen onion rings, prepared according to package directions | 1 |
| frozen onions, thawed | 1 |
| frozen or jarred pearl onion | 1 |
| frozen pearl onion | 14 |
| frozen pearl onions (12 ounces), thawed | 1 |
| frozen pearl onions (from 10-ounce bag) | 1 |
| frozen pearl onions (recommended: c and w) | 1 |
| frozen pearl onions, a large handful | 1 |
| frozen pearl onions, blanched and drained | 1 |
| frozen pearl onions, defrosted | 1 |
| frozen pearl onions, defrosted and drained | 1 |
| frozen pearl onions, thawed | 11 |
| frozen pearl onions, thawed (6 ounces) | 1 |
| frozen pearl onions, thawed (they can be left to thaw overnight during prep) | 1 |
| frozen pearl onions, thawed and drained | 1 |
| frozen pearl onions, thawed slightly | 1 |
| frozen pearl onions, thawed, halved | 1 |
| frozen peas and baby onion | 1 |
| frozen peas with pearl onion | 1 |
| frozen peas, corn, onion, red pepper and black bean blend | 1 |
| frozen pepper and onion blend | 1 |
| frozen potato-onion pierogies | 2 |
| frozen seasoning blend (mixed diced vegetables including onion, celery, red and green peppers, parsley) | 1 |
| frozen seasoning blend: chopped onion, green and red pepper combination (recommended: pictsweet) | 1 |
| frozen small whole onion | 5 |
| frozen small whole onions (1/2 pound) | 1 |
| frozen vegetable blend (no garlic or onions) | 1 |
| frozen vegetable blend (peppers, onions, celery, and parsley) | 1 |
| frozen white pearl onions, thawed | 1 |
| frozen whole onion | 1 |
| frozen whole petite onions (about 2 1/2 cups; do not thaw) | 1 |
| gallon chopped celery, onions and carrot | 1 |
| gallon mirepoix (2 parts onion, 1 part carrots and 1 part celery) | 1 |
| gallons chopped onion | 1 |
| garlic and onion seasoning | 1 |
| garlic cloves and/or an onion | 1 |
| garnish options: sharp cheddar, pepper or monterey jack, cotija, oaxaca or other flavorful cheese, shredded or crumbled; salsa of any sort (i make fresh pico de gallo in the summer); green onion | 1 |
| garnish: about 6 finely-chopped tablespoons each green bell pepper, red bell pepper, onion, cucumber, hard-boiled egg and olives; 3/4 cup small croutons | 1 |
| garnish: celery sticks, trimmed green onions, and skewered cherry tomato | 1 |
| garnish: chopped raw onion | 1 |
| garnish: fresh small fennel bulbs, (sometimes called anise), quartered with fronds attached, fresh small white onions with greens attached, fresh thyme sprigs | 1 |
| garnish: julienne carrots, celery and onion (just a few for presentation) | 1 |
| garnish: olive, cherry tomato, and cocktail onion on a swizzle stick or toothpick | 1 |
| garnish: shredded cheddar, red onion, scallions, sour cream | 1 |
| garnish: slivered red onion | 1 |
| garnish: small dark seeds such as nigella* (black onion seeds), cumin seeds, or caraway seeds for ghosts' "eyes" | 1 |
| garnishes – choose from whatever you have on hand: chopped cilantro or parsley and finely chopped scallions, chives or red onions, sour cream or yogurt | 1 |
| garnishes: thinly sliced avocado dressed with lime, thinly sliced rings of red onion | 1 |
| generous cup pearl onion | 1 |
| generous pinch onion powder | 1 |
| good-sized onion | 1 |
| grain bread with sprouts, tomato and red onion | 2 |
| grand marnier seasoning, 5 cloves garlic; 2 small onion | 1 |
| granulated onion | 82 |
| granulated onion powder | 8 |
| granulated onion, 1/3 palmful | 1 |
| granulated onion, a palmful | 2 |
| granulated onion, half a palmful | 1 |
| granulated onion, plus 1 teaspoon | 1 |
| granulated or powdered onion | 3 |
| grapeseed oil (1 tablespoon to saute the leeks, 1 tablespoon to saute the onion and garlic for the sauce, and 1 tablespoon to sear the scallops) | 1 |
| grapeseed oil (as needed to saute the onion and rissole cakes, respectively) | 2 |
| grated onion | 124 |
| grated onion (optional) | 1 |
| grated onion (use a box grater on the largest side) | 1 |
| grated onion (use a rasp or box grater) | 1 |
| grated onion (use the smallest side on a box grater, or use a rasp) | 1 |
| grated onion and juice grate directly over meat | 1 |
| grated onion pulp, made with the biggest side of box grater | 1 |
| grated onion, drained | 1 |
| grated onion, or to taste | 1 |
| grated or very finely chopped onion | 1 |
| grated red onion | 10 |
| grated red onion pulp (use a box grater or rasp) | 1 |
| grated shallot or onion, squeezed dry | 1 |
| grated spanish onion | 7 |
| grated sweet onion | 1 |
| grated sweet onion (or finely | 1 |
| grated sweet onion (such as vidalia or maui) | 1 |
| grated sweet onion such as vidalia | 1 |
| grated sweet onion such as vidalia or walla walla (use large holes of a box grater) | 1 |
| grated vidalia onion | 2 |
| grated vidalia or other sweet onion (use the largest holes on a box grater) | 1 |
| grated vidalia or sweet onion | 1 |
| grated white onion and juice | 1 |
| grated yellow onion | 3 |
| grated yellow onion (about 1/2 medium onion) | 1 |
| green (spring) onions, thinly sliced, plus more for garnish | 1 |
| green beans with red onion and mustard vinaigrette, recipe follows | 2 |
| green diced onion | 1 |
| green onion | 3,362 |
| green onion (dark green part only) | 1 |
| green onion (green and pale green parts), thinly sliced | 1 |
| green onion (green portion only) for garnish | 1 |
| green onion (green tops only) | 1 |
| green onion (scallion) | 2 |
| green onion (scallion) tops, thinly sliced | 1 |
| green onion (white and pale green parts) | 1 |
| green onion and top | 1 |
| green onion bunch, thinly sliced | 1 |
| green onion bunches | 1 |
| green onion chopped | 2 |
| green onion dressing | 1 |
| green onion flakes, dried | 1 |
| green onion for garnish | 1 |
| green onion honey dip, recipe follows | 1 |
| green onion pesto mashed potatoes, recipe follows | 1 |
| green onion pesto, recipe follows | 1 |
| green onion pork sausage, removed from casings | 1 |
| green onion sliced on the bias, for garnish | 1 |
| green onion slices | 1 |
| green onion sour cream, recipe follows | 1 |
| green onion stalks | 2 |
| green onion top, thinly sliced, or as desired | 1 |
| green onion tops | 6 |
| green onion with top, thinly sliced | 1 |
| green onion, both green and white portions | 1 |
| green onion, bruised with a rolling pin | 1 |
| green onion, cleaned and finely minced | 1 |
| green onion, cut into 1-inch pieces | 1 |
| green onion, cut into 1-inch pieces, or more to taste | 1 |
| green onion, cut into 2- to 2 1/2-inch pieces | 1 |
| green onion, cut into matchsticks | 1 |
| green onion, cut on bias | 1 |
| green onion, cut on bias, in quill like shapes | 1 |
| green onion, cut on the diagonal | 1 |
| green onion, cut the white part into 1/2 -inch pieces, julienne the green parts | 1 |
| green onion, fine julienne | 1 |
| green onion, green part only | 2 |
| green onion, green part only cut in 1-inch lengths | 1 |
| green onion, greens sliced | 1 |
| green onion, roots removed and chopped | 2 |
| green onion, slivered lengthwise, as needed for garnish | 1 |
| green onion, thinly sliced | 39 |
| green onion, thinly sliced (about 2 tablespoons) | 1 |
| green onion, thinly sliced diagonally | 1 |
| green onion, thinly sliced, for garnish | 2 |
| green onion, trimmed and finely chopped | 1 |
| green onion, trimmed and thinly sliced | 1 |
| green onion, washed and chopped fine | 1 |
| green onion, white and green part | 2 |
| green onion, white and light green parts | 1 |
| green onion, white and pale green part | 1 |
| green onion, white and tender green parts, thinly sliced on the diagonal (see "it's that easy") | 1 |
| green onion, white part only, crushed | 1 |
| green onion-jalapeño cornbread | 1 |
| green onion-mustard slaw, recipe follows | 1 |
| green onion-parmesan popovers | 1 |
| green onions (2 minced, 4 cut into 4-inch lengths) | 1 |
| green onions (about 12), dark green tops trimmed | 1 |
| green onions (about 6), trimmed | 1 |
| green onions (dark and pale green part) thinly sliced | 1 |
| green onions (dark green and light green parts only), thinly sliced | 1 |
| green onions (green and pale green part), thinly sliced | 3 |
| green onions (green and pale green parts), thinly sliced | 2 |
| green onions (green part only) | 3 |
| green onions (green portion only) | 1 |
| green onions (green tops only) | 1 |
| green onions (including tops) minced | 1 |
| green onions (optional) | 2 |
| green onions (root tips and tough green ends removed) coarsely chopped | 1 |
| green onions (scallions) | 6 |
| green onions (scallions), cut into 1-inch lengths | 1 |
| green onions (scallions), cut into pieces | 1 |
| green onions (scallions), green part only, thinly sliced | 1 |
| green onions (scallions), trimmed, white bottoms and green tops separated | 1 |
| green onions (scallions), white and light green parts, trimmed and chopped | 1 |
| green onions (white and green part) finely chopped | 1 |
| green onions (white and green parts) | 4 |
| green onions (white and light green parts only) | 1 |
| green onions (white and pale green parts only) | 3 |
| green onions (white and pale green parts only), cut into 3- to 4-inch-long matchstick-size strips | 1 |
| green onions (white and pale green parts only), cut into matchstick-size strips | 1 |
| green onions (white and pale green parts only), thinly sliced | 3 |
| green onions (white bulb and 3 inches of green) | 1 |
| green onions (white part only) | 3 |
| green onions (white parts only), cut into 1-inch pieces | 1 |
| green onions and 3 inches of the top | 1 |
| green onions and tops | 3 |
| green onions chopped, white and some of the green, about 2 green onion | 1 |
| green onions cut diagonally into thin slices | 1 |
| green onions cut into 1-inch pieces | 2 |
| green onions cut into 2-inch pieces | 1 |
| green onions julienned, matchstick size to about 1/2 cup | 1 |
| green onions or garlic scapes, thinly sliced | 1 |
| green onions or scallions, cut into 1/2-inch pieces | 1 |
| green onions or scallions, white and green parts, cut on the bias into thin strips or julienned | 1 |
| green onions with tops | 1 |
| green onions with tops, thinly sliced | 2 |
| green onions, 1/4 cup (1/4 oz/20 g) sliced | 1 |
| green onions, 2, thinly sliced | 1 |
| green onions, all but 3 inches of green tops trimmed | 1 |
| green onions, blanched in boiling water for 15 seconds and cooled | 1 |
| green onions, both white and green parts, julienned | 1 |
| green onions, both white and green parts, trimmed | 1 |
| green onions, bottom 4 inches, thinly sliced | 1 |
| green onions, cleaned well | 1 |
| green onions, cut 3 inches in length | 1 |
| green onions, cut crosswise into quarters, then cut lengthwise into thin strips | 1 |
| green onions, cut diagonally into 1 1/2-inch lengths | 1 |
| green onions, cut diagonally into 1-inch lengths | 1 |
| green onions, cut in 1/3-inch pieces | 1 |
| green onions, cut in 2-inch lengths | 1 |
| green onions, cut in half | 2 |
| green onions, cut in half crosswise | 1 |
| green onions, cut into 1-inch lengths | 3 |
| green onions, cut into 1-inch lengths (about 30 pieces) | 1 |
| green onions, cut into 1-inch pieces | 6 |
| green onions, cut into 1-inch pieces (about 1/3 cup) | 1 |
| green onions, cut into 1-inch strips | 1 |
| green onions, cut into 1-inch-long pieces | 1 |
| green onions, cut into 1/2-inch lengths | 1 |
| green onions, cut into 1/2-inch pieces | 7 |
| green onions, cut into 1/4-inch pieces | 6 |
| green onions, cut into 1/4-inch pieces, plus more chopped small for garnish | 1 |
| green onions, cut into 1/4-inch pieces, white and green parts separated | 1 |
| green onions, cut into 1/4-inch slices | 1 |
| green onions, cut into 2 inch pieces | 3 |
| green onions, cut into 2-inch bias | 1 |
| green onions, cut into 2-inch lengths | 6 |
| green onions, cut into 2-inch lengths and halved lengthwise | 1 |
| green onions, cut into 2-inch matchsticks | 1 |
| green onions, cut into 2-inch pieces | 4 |
| green onions, cut into 2-inch slices | 1 |
| green onions, cut into 3 inch lengths | 3 |
| green onions, cut into 3-inch pieces (white and some of green) and soaked | 1 |
| green onions, cut into matchstick-size strips | 3 |
| green onions, cut into thin strips | 3 |
| green onions, cut on the bias | 1 |
| green onions, cut on the bias, all of white part and half of the green | 2 |
| green onions, cut thinly on a diagonal | 1 |
| green onions, dark and pale green part thinly sliced, white part minced | 1 |
| green onions, dark and pale green parts finely chopped | 1 |
| green onions, dark and pale green parts thinly sliced, plus more for garnish | 1 |
| green onions, dark green and pale green part, thinly sliced | 1 |
| green onions, dark green and pale green parts, thinly sliced | 1 |
| green onions, dark green and white parts chopped separately | 1 |
| green onions, dark green parts only | 2 |
| green onions, dark green parts only, thinly sliced on the diagonal | 1 |
| green onions, diagonally sliced | 2 |
| green onions, ends trimmed | 6 |
| green onions, fine dice | 1 |
| green onions, for garnish | 2 |
| green onions, green and light green parts only | 1 |
| green onions, green and light green parts only, thinly sliced | 1 |
| green onions, green and pale green part finely chopped | 1 |
| green onions, green and pale green part, thinly sliced | 3 |
| green onions, green and pale green parts | 2 |
| green onions, green and pale green parts halved lengthwise and thinly sliced crosswise | 1 |
| green onions, green and pale green parts only, thinly sliced | 6 |
| green onions, green and pale green parts only, thinly sliced, plus more for garnish | 1 |
| green onions, green and pale green parts thinly sliced | 2 |
| green onions, green and pale green parts, thinly sliced | 2 |
| green onions, green and pale-green parts only, thinly sliced | 2 |
| green onions, green and white parts | 2 |
| green onions, green and white parts kept separate | 1 |
| green onions, green and white parts, thinly sliced on diagonal | 1 |
| green onions, green part blanched | 1 |
| green onions, green part only | 3 |
| green onions, green part only, grilled and chopped, plus additional thinly sliced green onions, for garnish | 1 |
| green onions, green part only, very thinly sliced | 1 |
| green onions, green parts cut into even slivers | 1 |
| green onions, green parts only | 16 |
| green onions, green parts only, cut into 5-inch long pieces | 1 |
| green onions, green tops included | 1 |
| green onions, greens only | 1 |
| green onions, greens parts only | 1 |
| green onions, greens sliced | 2 |
| green onions, greens thinly sliced | 1 |
| green onions, grilled | 1 |
| green onions, grilled and thinly sliced | 1 |
| green onions, halved | 1 |
| green onions, halved and thinly sliced | 1 |
| green onions, halved lengthwise | 1 |
| green onions, halved lengthwise and cut into 1 1/2-in / 4cm segments | 1 |
| green onions, halved lengthwise and thin sliced crosswise | 1 |
| green onions, halved lengthwise and thinly sliced crosswise | 1 |
| green onions, including green tops, thinly sliced | 1 |
| green onions, julienne | 1 |
| green onions, julienned | 2 |
| green onions, julienned for garnish | 1 |
| green onions, light and dark green parts only | 1 |
| green onions, light and dark green parts only, thinly sliced on the diagonal | 1 |
| green onions, light and dark green parts sliced on the bias, whites reserved for another use | 1 |
| green onions, light green and dark green parts | 1 |
| green onions, light green and medium green parts, thinly sliced | 1 |
| green onions, lighter half chopped thin and darker green half discarded | 1 |
| green onions, or 1 medium yellow onion | 1 |
| green onions, or to taste | 1 |
| green onions, pale green and white parts only | 1 |
| green onions, pressed flat with a knife | 1 |
| green onions, quartered | 1 |
| green onions, rinsed, ends trimmed | 1 |
| green onions, roasted and diced | 1 |
| green onions, root ends trimmed, dark green tops cut off and discarded | 1 |
| green onions, roots and 4 inches of green tops trimmed | 1 |
| green onions, roots cut off | 1 |
| green onions, roots removed | 1 |
| green onions, slivered | 1 |
| green onions, split in 1/2, cut in 2-inch sections | 1 |
| green onions, thin sliced | 1 |
| green onions, thinly chopped | 1 |
| green onions, thinly chopped on the bias | 1 |
| green onions, thinly sliced | 253 |
| green onions, thinly sliced (4 tablespoons) | 1 |
| green onions, thinly sliced (about 1/2 cup) | 1 |
| green onions, thinly sliced (about 3/4 cup) | 2 |
| green onions, thinly sliced (everything but the bulb), for garnish | 1 |
| green onions, thinly sliced (optional) | 2 |
| green onions, thinly sliced (reserve half for garnish) | 1 |
| green onions, thinly sliced (white and green parts) | 1 |
| green onions, thinly sliced (white and pale green parts only) | 1 |
| green onions, thinly sliced (white and pale green parts only; about 1 1/2 cups) | 1 |
| green onions, thinly sliced 1 lemon, cut into 6 wedges | 1 |
| green onions, thinly sliced crosswise | 1 |
| green onions, thinly sliced diagonally | 3 |
| green onions, thinly sliced diagonally (about 2) | 1 |
| green onions, thinly sliced including tops | 1 |
| green onions, thinly sliced on an angle | 1 |
| green onions, thinly sliced on bias, for serving | 1 |
| green onions, thinly sliced on diagonal | 5 |
| green onions, thinly sliced on diagonal (about 1 cup) | 1 |
| green onions, thinly sliced on the bias | 1 |
| green onions, thinly sliced on the diagonal | 2 |
| green onions, thinly sliced, dark green part reserved for garnish | 1 |
| green onions, thinly sliced, for garnish | 6 |
| green onions, thinly sliced, for serving | 2 |
| green onions, thinly sliced, or to taste | 3 |
| green onions, thinly sliced, or to taste (optional) | 1 |
| green onions, thinly sliced, plus additional for garnish | 1 |
| green onions, thinly sliced, plus more for garnish | 2 |
| green onions, thinly sliced, white and pale green parts separated from dark green parts | 1 |
| green onions, top 1/3 sliced for garnish, and middle 1/3 kept whole* | 1 |
| green onions, tops thinly sliced | 2 |
| green onions, tops trimmed a few inches | 1 |
| green onions, trimmed | 15 |
| green onions, trimmed and chopped | 4 |
| green onions, trimmed and coarsely chopped | 1 |
| green onions, trimmed and cut in half lengthwise | 1 |
| green onions, trimmed and cut into strips (about 1 cup) | 1 |
| green onions, trimmed and cut into thirds | 1 |
| green onions, trimmed and minced | 1 |
| green onions, trimmed and roughly chopped | 1 |
| green onions, trimmed and sliced lengthwise (for planking only) | 1 |
| green onions, trimmed and sliced thin | 1 |
| green onions, trimmed and sliced thinly on the diagonal | 1 |
| green onions, trimmed and thinly sliced | 2 |
| green onions, trimmed and thinly sliced on the diagonal | 1 |
| green onions, trimmed to 4 inches from root end | 1 |
| green onions, trimmed, cut into 1-inch lengths | 1 |
| green onions, trimmed, cut into thin matchstick-size strips | 1 |
| green onions, very thinly sliced | 3 |
| green onions, white and bright green parts, thinly sliced (about 6) | 1 |
| green onions, white and green part | 2 |
| green onions, white and green parts | 14 |
| green onions, white and green parts included | 1 |
| green onions, white and green parts separated | 1 |
| green onions, white and green parts separated and sliced | 1 |
| green onions, white and green parts separated, and chopped | 1 |
| green onions, white and green parts sliced | 1 |
| green onions, white and green parts sliced separately | 1 |
| green onions, white and green parts thinly sliced | 1 |
| green onions, white and green parts, thinly sliced | 2 |
| green onions, white and green parts, thinly sliced, plus chopped green onion tops, for garnish | 1 |
| green onions, white and light green parts | 1 |
| green onions, white and light green parts only | 5 |
| green onions, white and light green parts only, thinly sliced | 2 |
| green onions, white and light green parts only, thinly sliced on the diagonal | 1 |
| green onions, white and light tender parts only | 1 |
| green onions, white and pale green parts only | 1 |
| green onions, white and pale green parts only, thinly sliced | 1 |
| green onions, white and pale green parts thinly sliced, tops cut into 1/2-inch lengths and reserved | 1 |
| green onions, white and some green part, thinly sliced on the diagonal | 1 |
| green onions, white and tender green parts only, thinly sliced | 1 |
| green onions, white and tender green parts, thinly sliced | 1 |
| green onions, white part only | 1 |
| green onions, white part only (optional) | 1 |
| green onions, white parts and green parts chopped separately | 1 |
| green onions, white parts and green tops chopped separately | 1 |
| green onions, white parts cut into thin strips, green parts chopped | 1 |
| green onions, white parts finely chopped, green parts thinly sliced | 1 |
| green onions, white parts only | 3 |
| green onions, white tips removed | 1 |
| green onions, white, light green, and a little of the dark green part | 1 |
| green onions, whites and light green parts sliced | 1 |
| green onions, whites cut thinly across and greens sliced into thin lengths - divided | 1 |
| green onions, whites minced and green tops cut into thin rings | 1 |
| green onions, whites minced, greens thinly sliced and reserved for garnish | 1 |
| green onions, whites portion only, smashed and coarsely chopped | 1 |
| green onions, with tops flared | 1 |
| green onions; 2 chopped, 8 trimmed | 1 |
| green onions; root ends trimmed, onions left whole | 1 |
| green onions; white and pale green parts finely chopped, dark green parts thinly sliced | 1 |
| green onions; white and pale green parts finely chopped, green parts thinly sliced | 1 |
| grilled onion | 3 |
| grilled onion blue cheese dressing, recipe follows | 1 |
| grilled onion relish, recipe follows | 2 |
| grilled onions, recipe follows | 3 |
| grilled red onions, for serving | 1 |
| grilled red onions, recipe follows | 1 |
| grilled sliced onions, as needed | 1 |
| grilled sweet onion | 1 |
| grilled vegetables (eggplant, zucchini, onions, red bell peppers) coarsely chopped | 1 |
| grilled vegetables from the salad bar (peppers, squash, zucchini, red onions) | 1 |
| grilled vidalia onions, recipe follows | 2 |
| grilled yellow and red onion | 1 |
| grilled yellow onion | 1 |
| grilled zucchini, eggplant and red onion fusilli with parmesan cheese | 1 |
| grind the seafood seasoning, paprika, salt, celery seeds, chili powder, garlic powder, onion powder and pepper. mix together | 1 |
| ground beef, reserved from ale house burgers with red onion compote, recipe follows | 1 |
| ground onion | 3 |
| habanero onion puree, recipe follows | 1 |
| half a medium red onion | 1 |
| half cut plus 1 tablespoon finely chopped red onion | 1 |
| half medium onion | 1 |
| half moon shaped sliced red onion | 1 |
| half reserved red onion, from crispy wonton cups with tuna salad | 1 |
| half reserved red onion, from crispy wonton cups with tuna salad, thinly sliced | 1 |
| halved and sliced lengthwise yellow onion | 2 |
| halved peeled onion | 1 |
| halved thinly sliced red onion | 1 |
| hamburger buns, preferably onion flavored | 1 |
| happy farms onion & chive soft spread cream cheese | 1 |
| heaping 1/4 cup diced spanish onion | 1 |
| heaping cup chopped onion | 1 |
| heaping tablespoon finely minced onion of your choice | 1 |
| heaping tablespoon onion powder | 1 |
| heaping tablespoon pickled onions, recipe follows | 1 |
| heat the oil in a medium saute pan over medium high heat. add the onions and cook until soft, about 4 minutes. add the garlic and cook for 30 seconds. stir in the piquillo peppers, season with salt and pepper, and cook 5 minutes | 1 |
| heated tablespoon finely chopped white onion | 1 |
| herb salad with pickled red onion and preserved lemon (for serving) | 1 |
| homemade sour cream and onion chips, recipe follows | 1 |
| honey mustard and onion pretzels, crushed | 1 |
| i red onion, thinly sliced into rings | 1 |
| i tablespoon finely chopped onion | 1 |
| i yellow onion | 1 |
| in a bowl, combine the tomatoes, onion, garlic, olive oil, lemon juice, basil, tarragon, salt, and pepper. add the croutons and toss well | 1 |
| in a medium saucepan, add the onions, vinegar, wine, sugar and salt and pepper. cook over low heat until reduced by half. the liquid will become syrupy. stir in the lemon juice and season with more salt and pepper, if needed | 1 |
| ingredient info: cipolline onions, small flat onions, are available at italian markets, specialty foods stores, and some supermarkets | 1 |
| instant chopped onion | 1 |
| instant minced onion | 2 |
| jar (6-7 ounces) roasted red peppers or fried sweet peppers with onion | 1 |
| jar baby pearl onions, drained | 1 |
| jar chunky tomato sauce with onion and garlic | 1 |
| jar dickinson's® sweet 'n' hot pepper & onion relish | 4 |
| jar garlic and onion spaghetti sauce (such as ragu® robusto® sauteed onion & garlic pasta sauce) | 1 |
| jar holland-style pearl onions, drained | 1 |
| jar marinated cocktail onions, with liquid | 1 |
| jar of extra chunky spaghetti sauce with mushrooms and diced onion | 1 |
| jar onion and garlic spaghetti sauce | 1 |
| jar patak's rich tomato & onion cooking sauce (dopiaza) | 1 |
| jar picked cipollini onion | 1 |
| jar pickled onion | 1 |
| jar pickled onions, drained | 1 |
| jar pickled pearl onions, drained | 1 |
| jar pickled red onion | 1 |
| jar pushcart-style onions in sauce | 1 |
| jar ragu® chunky tomato, garlic & onion sauce | 1 |
| jars tomato, onion, and garlic spaghetti sauce (such as prego®) | 1 |
| julienne green onion | 3 |
| julienne green onions, white and light green | 1 |
| julienne of the following: pineapple, mango, coconut, onion, sweet peppers, and celery | 1 |
| julienne onion | 4 |
| julienne red onion | 3 |
| julienne strips red onion | 1 |
| julienne yellow onion | 1 |
| julienned fried ginger or paper thin fried onion rings, for garnish | 1 |
| julienned green onion | 2 |
| julienned green onion (hay cut), 2 to 3 inches in length | 1 |
| julienned onion | 5 |
| julienned onion, rinsed in cold water | 1 |
| julienned pickled red onions, recipe follows | 1 |
| julienned red onion | 19 |
| julienned red onion (about 1/2 onion) | 2 |
| julienned spanish onion | 1 |
| julienned yellow onion | 3 |
| julienned yellow onions, caramelized | 1 |
| jumbo organic yellow onion | 1 |
| jumbo sweet onion such as vidalia | 1 |
| jumbo sweet onion such as vidalia (1 lb), halved lengthwise and thinly sliced crosswise | 1 |
| jumbo sweet onions, thinly sliced | 1 |
| jumbo texas yellow onion | 1 |
| jumbo vidalia onion | 1 |
| jumbo yellow onion | 1 |
| kaiser rolls, onion or poppy seed | 1 |
| lamb sausage and caramelized onions, recipe follows | 1 |
| large (10- to 12-ounce) onion | 1 |
| large (about 12 ounces) walla walla onion or other sweet onion (such as vidalia or maui), cut into 1/3-inch-thick rounds, separated into rings | 1 |
| large (or 1 small) onion | 1 |
| large (or 1 small) yellow onion | 1 |
| large bermuda onion | 3 |
| large bermuda onion, cut into 2-inch squares | 1 |
| large bunch green onion | 1 |
| large butternut or onion squash | 1 |
| large chopped onion | 7 |
| large cipollini onion | 2 |
| large cold onion, thinly sliced | 1 |
| large dice onion | 1 |
| large dice spanish onion | 1 |
| large diced onion | 3 |
| large diced red onion | 2 |
| large diced vidalia onion | 1 |
| large finely chopped onion | 1 |
| large firm red onion | 1 |
| large green onion | 34 |
| large green onion, cut into 1-inch pieces | 2 |
| large green onion, green part chopped, plus more for garnish | 1 |
| large green onion, green part only | 1 |
| large green onion, thinly sliced (about 1/4 cup) | 1 |
| large green onion, white and green part minced and chopped | 1 |
| large green onions (green and pale green parts), thinly sliced | 1 |
| large green onions (see note), or baby leeks | 1 |
| large green onions (white and pale green parts only) | 1 |
| large green onions or scallions, tops and roots trimmed | 1 |
| large green onions, dark green and pale green parts, thinly sliced | 1 |
| large green onions, dark green tops trimmed | 1 |
| large green onions, green and light green parts only | 1 |
| large green onions, halved lengthwise and finely sliced | 1 |
| large green onions, thinly sliced | 9 |
| large green onions, trimmed | 1 |
| large green onions, trimmed to 8-inch length | 1 |
| large green onions, trimmed, cut into 1inch lengths | 1 |
| large green onions, white and light green part only | 1 |
| large green onions, white and pale green part only | 1 |
| large green onions, white and pale green parts minced, tops cut into 1-inch pieces | 1 |
| large green onions, white and tender green parts only | 1 |
| large green onions; 4 coarsely chopped, 1 thinly sliced for garnish | 1 |
| large leeks (white and pale green parts only), thinly sliced or 1 large onion | 1 |
| large maui onion (or other sweet onion), thinly sliced | 1 |
| large maui sweet onion | 1 |
| large maui sweet onion, cubed | 1 |
| large mesh bags (such as onions or citrus fruit come in) or 4 pouches made from several wide layers cheesecloth | 1 |
| large minced onion | 2 |
| large onion | 2,267 |
| large onion (1 pound) | 1 |
| large onion (1/2 pound) | 1 |
| large onion (1/2 pound), halved lengthwise, then thinly sliced crosswise | 1 |
| large onion (10 ounces), cut into 1/2-inch dice | 1 |
| large onion (10 to 12 ounces), cut into 1/2-inch dice | 1 |
| large onion (10 to 12 ounces), large dice (3/4-inch) | 1 |
| large onion (12 ounces), cut into 1/2-inch dice | 1 |
| large onion (3/4 lb), halved lengthwise | 1 |
| large onion (3/4 pound) | 1 |
| large onion (9 ounces) | 1 |
| large onion (about 1 pound) | 3 |
| large onion (about 1 pound), halved lengthwise, thinly sliced crosswise | 1 |
| large onion (about 1/2 pound) | 1 |
| large onion (about 3/4 pound) | 3 |
| large onion (chopped) | 1 |
| large onion (or leek), 1 stalk celery and 1 large carrot | 1 |
| large onion (or more), cut into 1- to 2-in/2.5- to 5-cm chunks (or 3 leeks, thickly sliced) | 1 |
| large onion (vidalia are the best) | 1 |
| large onion buns or rolls | 1 |
| large onion chopped | 2 |
| large onion coarsely chopped | 2 |
| large onion cut into 4 pieces | 1 |
| large onion diced | 1 |
| large onion diced in 2-inch cubes | 1 |
| large onion finely chopped | 2 |
| large onion finely diced | 1 |
| large onion or 1 medium onion, quartered | 2 |
| large onion or 1 small onion | 1 |
| large onion or 2 medium onion | 2 |
| large onion or 2 small, cut into 1-inch dice | 1 |
| large onion or lemon | 1 |
| large onion or red onion, quartered lengthwise and thinly sliced | 1 |
| large onion peeled | 1 |
| large onion rolls, split, toasted | 1 |
| large onion sliced | 1 |
| large onion sliced in 1/2 inch slices | 1 |
| large onion stuck with 1 whole clove | 1 |
| large onion stuck with 2 clove | 1 |
| large onion studded with 1 clove | 2 |
| large onion studded with 2 whole clove | 1 |
| large onion yellow | 1 |
| large onion, 1-inch dice | 1 |
| large onion, 1/2 cut into 1/2-inch dice and the other half left whole | 1 |
| large onion, 1/2 onion diced and 1/2 onion finely sliced | 1 |
| large onion, 1/2-inch dice (about 2 cups) | 1 |
| large onion, 1/2-inch slices | 2 |
| large onion, 1/4 onion finely chopped, 3/4 thinly sliced | 1 |
| large onion, 1/4-inch dice | 4 |
| large onion, caramelized | 1 |
| large onion, cubed | 2 |
| large onion, cut in 1/2-inch dice | 1 |
| large onion, cut in half and into 1/2-inch-thick slices | 1 |
| large onion, cut in half and sliced | 2 |
| large onion, cut in rings | 1 |
| large onion, cut into 1 inch chunks | 1 |
| large onion, cut into 1- to 2-inch pieces | 1 |
| large onion, cut into 1-inch chunks | 1 |
| large onion, cut into 1-inch chunks (about 2 cups) | 1 |
| large onion, cut into 1-inch cubes | 3 |
| large onion, cut into 1-inch dice | 1 |
| large onion, cut into 1-inch pieces | 4 |
| large onion, cut into 1-inch pieces, or more to taste | 1 |
| large onion, cut into 1-inch wedges | 1 |
| large onion, cut into 1/2-inch cubes | 2 |
| large onion, cut into 1/2-inch dice | 16 |
| large onion, cut into 1/2-inch pieces | 4 |
| large onion, cut into 1/2-inch slices | 2 |
| large onion, cut into 1/2-inch squares (about 2 cups) | 1 |
| large onion, cut into 1/2-inch wedges | 2 |
| large onion, cut into 1/2-inch wide slices | 1 |
| large onion, cut into 1/2-inch-thick slices | 1 |
| large onion, cut into 1/4-inch dice | 7 |
| large onion, cut into 1/4-inch pieces (about 2 cups) | 1 |
| large onion, cut into 1/4-inch slices | 3 |
| large onion, cut into 1/4-inch strips | 1 |
| large onion, cut into 1/4-inch thick rings | 1 |
| large onion, cut into 1/4-inch-thick rings | 1 |
| large onion, cut into 1/8-inch pieces | 1 |
| large onion, cut into 2-inch squares | 1 |
| large onion, cut into 3/4-inch pieces | 1 |
| large onion, cut into 4 pieces | 1 |
| large onion, cut into 4 wedges | 1 |
| large onion, cut into 6 pieces | 1 |
| large onion, cut into 8 pieces | 4 |
| large onion, cut into 8 wedges | 4 |
| large onion, cut into a large dice | 1 |
| large onion, cut into big cubes | 2 |
| large onion, cut into bite-sized pieces | 1 |
| large onion, cut into chunks | 9 |
| large onion, cut into eighths | 2 |
| large onion, cut into fine dice | 2 |
| large onion, cut into large chunks | 5 |
| large onion, cut into large dice | 11 |
| large onion, cut into large pieces | 1 |
| large onion, cut into large squares | 1 |
| large onion, cut into large wedges | 1 |
| large onion, cut into long slices | 1 |
| large onion, cut into matchstick-size pieces | 1 |
| large onion, cut into medium dice | 2 |
| large onion, cut into medium dice (2 cups) | 1 |
| large onion, cut into rings | 7 |
| large onion, cut into slices | 1 |
| large onion, cut into small cubes | 1 |
| large onion, cut into small dice | 2 |
| large onion, cut into strips | 2 |
| large onion, cut into thick slices and separated into rings | 1 |
| large onion, cut into thick wedges | 1 |
| large onion, cut into thin rings | 1 |
| large onion, cut into thin rounds | 1 |
| large onion, cut into thin strips | 3 |
| large onion, cut into thin wedges | 1 |
| large onion, cut into thirds | 2 |
| large onion, cut into three or four 1-inch-wide rings | 1 |
| large onion, cut into wedges | 8 |
| large onion, cut into wedges, leaving root ends intact | 1 |
| large onion, cut julienne | 1 |
| large onion, cut lengthwise into 1/4-inch thick strips | 1 |
| large onion, cut lengthwise into 1/4-inch-thick slices | 1 |
| large onion, ends trimmed and skin removed | 1 |
| large onion, halved | 12 |
| large onion, halved - unpeeled | 1 |
| large onion, halved and cut into slices | 1 |
| large onion, halved and quartered | 1 |
| large onion, halved and skin left on | 1 |
| large onion, halved and sliced | 9 |
| large onion, halved and sliced 1/2 inch thick | 1 |
| large onion, halved and sliced lengthwise | 2 |
| large onion, halved and sliced lengthwise 1/4 inch thick | 1 |
| large onion, halved and slivered | 1 |
| large onion, halved and thinly sliced | 10 |
| large onion, halved and unpeeled | 1 |
| large onion, halved lengthwise | 1 |
| large onion, halved lengthwise and cut into thick slices | 1 |
| large onion, halved lengthwise and sliced into half-moons | 1 |
| large onion, halved lengthwise and sliced thin lengthwise | 1 |
| large onion, halved lengthwise and thinly sliced | 3 |
| large onion, halved lengthwise and thinly sliced crosswise | 1 |
| large onion, halved lengthwise and thinly sliced crosswise (2 cups) | 1 |
| large onion, halved lengthwise and thinly sliced lengthwise | 2 |
| large onion, halved lengthwise, one half cut lengthwise into 1/4-inch-thick slices and the other half chopped | 1 |
| large onion, halved lengthwise, then cut crosswise into thin slices (3 cups) | 1 |
| large onion, halved lengthwise, then cut lengthwise into 1/4-inch slices | 1 |
| large onion, halved lengthwise, then cut lengthwise into 1/4-inch-thick slices | 2 |
| large onion, halved lengthwise, then cut lengthwise into 1/4-inch-thick slices (2 cups) | 1 |
| large onion, halved lengthwise, then cut lengthwise into 1/4-inch-wide strips | 1 |
| large onion, halved lengthwise, then cut lengthwise into1/4-inch-wide strips | 1 |
| large onion, halved lengthwise, then sliced crosswise 1/2 inch thick | 1 |
| large onion, halved lengthwise, then sliced lengthwise (1/4 inch thick) | 1 |
| large onion, halved lengthwise, then thinly sliced crosswise | 3 |
| large onion, halved lengthwise, then thinly sliced lengthwise | 2 |
| large onion, halved lengthwise, thinly sliced | 2 |
| large onion, halved lengthwise, thinly sliced crosswise | 1 |
| large onion, halved, cut into 1-inch-wide wedges | 1 |
| large onion, halved, plus 1 cup chopped | 1 |
| large onion, halved, thinly sliced | 7 |
| large onion, halved, thinly sliced crosswise | 1 |
| large onion, halved, thinly sliced lengthwise | 1 |
| large onion, julienned | 6 |
| large onion, left unpeeled | 1 |
| large onion, medium dice | 3 |
| large onion, medium diced | 5 |
| large onion, or 2 small ones-- peeled and cut into eighths | 1 |
| large onion, preferably red | 1 |
| large onion, preferably walla walla, maui or other sweet onion | 1 |
| large onion, preferably yellow | 1 |
| large onion, quartered | 31 |
| large onion, quartered - divided | 1 |
| large onion, quartered and cut into 2-inch pieces | 1 |
| large onion, quartered and halved | 1 |
| large onion, quartered and separated into pieces | 1 |
| large onion, quartered and sliced | 1 |
| large onion, quartered and thinly sliced | 3 |
| large onion, quartered lengthwise then sliced | 1 |
| large onion, quartered lengthwise then sliced 1/4-inch thick | 1 |
| large onion, quartered lengthwise then thinly sliced | 1 |
| large onion, quartered then thinly sliced | 1 |
| large onion, quartered through root end | 1 |
| large onion, quartered with root end attached | 3 |
| large onion, quartered with the root end attached | 2 |
| large onion, quartered, cut crosswise into 1/4-inch-thick slices | 1 |
| large onion, quartered, root end intact | 1 |
| large onion, root end left intact, then cut lengthwise into 1/2-inch-wide wedges | 1 |
| large onion, rough diced | 1 |
| large onion, roughly chop | 2 |
| large onion, shredded | 1 |
| large onion, skin on | 1 |
| large onion, small dice | 4 |
| large onion, small diced | 1 |
| large onion, split vertically and sliced thin | 1 |
| large onion, squeezed through a garlic press | 1 |
| large onion, studded with 3 clove | 2 |
| large onion, thickly sliced | 1 |
| large onion, thinly slice | 1 |
| large onion, thinly sliced | 121 |
| large onion, thinly sliced (2 1/4 cups) | 2 |
| large onion, thinly sliced (about 2 cups) | 1 |
| large onion, thinly sliced (about 3 cups) | 1 |
| large onion, thinly sliced into rings | 1 |
| large onion, thinly sliced into rounds | 1 |
| large onion, thinly sliced, or to taste | 1 |
| large onion, trimmed | 1 |
| large onion, unpeeled and cut in eighths | 1 |
| large onion, unpeeled and quartered | 1 |
| large onion, unpeeled, halved lengthwise | 1 |
| large onion, unpeeled, quartered | 1 |
| large onion, very coarsely chopped | 1 |
| large onion, very thinly sliced | 3 |
| large onion, white or brown skinned | 1 |
| large onions (1 1/2 lb total), halved lengthwise and cut crosswise into 1/4-inch slices | 1 |
| large onions (1 1/2 lb total), halved lengthwise and cut lengthwise into 1/4-inch strips | 1 |
| large onions (1 1/2 lb total), quartered lengthwise and thinly sliced crosswise | 1 |
| large onions (1 1/2 pounds), cut lengthwise into 1/4-inch-thick slices | 1 |
| large onions (1 cut into wedges, 1 diced) | 1 |
| large onions (1 pound total) | 1 |
| large onions (1 pound) | 3 |
| large onions (12 ounces each), 1 unpeeled | 1 |
| large onions (2 pounds total) | 1 |
| large onions (2 pounds total), thinly sliced (7 cups) | 1 |
| large onions (2 white, 2 red, 2 yellow), halved and thinly sliced | 1 |
| large onions (about 1 1/2 pounds) | 2 |
| large onions (about 1 1/3 pounds total), halved through root end, thinly sliced lengthwise | 1 |
| large onions (about 1 3/4 pounds) | 1 |
| large onions (about 1 pound) | 1 |
| large onions (about 2 1/2 pounds), cut into 1/4-inch -thick slices | 1 |
| large onions (about 2 cups when grated; don't tamp it down) | 1 |
| large onions (about 2 pounds), halved, thinly sliced | 1 |
| large onions (about 2 pounds), thinly sliced | 1 |
| large onions (about 3 1/2 pounds), halved, thinly sliced | 1 |
| large onions (about 3/4 pound each) | 2 |
| large onions (about 3/4 pound each), unpeeled and untrimmed | 1 |
| large onions (about 5 pounds), thinly sliced | 2 |
| large onions (preferably white) | 1 |
| large onions - sliced | 1 |
| large onions chopped | 2 |
| large onions diced | 1 |
| large onions or leeks, white and pale-green parts only | 1 |
| large onions, 1 chopped, 1 quartered | 1 |
| large onions, 1-inch dice | 1 |
| large onions, cubed | 1 |
| large onions, cut crosswise into 1/4-inch-thick slices | 1 |
| large onions, cut in 1/2-inch dice | 1 |
| large onions, cut in half and sliced | 2 |
| large onions, cut in half and thinly sliced | 1 |
| large onions, cut into 1-inch pieces | 2 |
| large onions, cut into 1-inch squares | 1 |
| large onions, cut into 1/2 inch chunks | 1 |
| large onions, cut into 1/2-inch dice | 3 |
| large onions, cut into 1/4 inch dice | 1 |
| large onions, cut into 1/4 inch thick slices | 1 |
| large onions, cut into 1/4-inch thick slices and separated into rings | 1 |
| large onions, cut into 1/4-inch-thick slices, separated into rings | 1 |
| large onions, cut into 2-inch pieces | 1 |
| large onions, cut into 3/4-inch-thick rings | 1 |
| large onions, cut into 8 (1/4-inch) slices | 1 |
| large onions, cut into a small dice | 1 |
| large onions, cut into bite-size pieces | 1 |
| large onions, cut into chunks | 1 |
| large onions, cut into large chunks | 2 |
| large onions, cut into large dice | 1 |
| large onions, cut into medium dice | 3 |
| large onions, cut into rings | 1 |
| large onions, cut into small cubes | 1 |
| large onions, cut into small dice | 1 |
| large onions, cut into thin slices | 1 |
| large onions, cut into very thin rings | 1 |
| large onions, cut into wedges | 2 |
| large onions, each cut into 8 wedges through root end, leaving root ends intact | 1 |
| large onions, halved | 3 |
| large onions, halved and cut 1/4-inch thick | 1 |
| large onions, halved and cut into short strips | 1 |
| large onions, halved and sliced | 1 |
| large onions, halved and sliced about 1/4-inch thick | 1 |
| large onions, halved and sliced thin | 1 |
| large onions, halved and thinly sliced | 5 |
| large onions, halved lengthwise | 1 |
| large onions, halved lengthwise and sliced thin lengthwise | 1 |
| large onions, halved lengthwise, then cut crosswise into 1/2-inch slices (4 cups) | 1 |
| large onions, halved lengthwise, then cut lengthwise into 1/4-inch-wide strips | 1 |
| large onions, halved lengthwise, then sliced (1/4 inch thick; 4 cups) | 1 |
| large onions, halved through core, cut crosswise into 1/4- to 1/3-inch slices | 1 |
| large onions, halved, thinly sliced | 3 |
| large onions, julienned | 2 |
| large onions, large dice | 2 |
| large onions, left unpeeled and coarsely chopped | 1 |
| large onions, medium chopped | 1 |
| large onions, medium dice | 1 |
| large onions, one quartered and one chopped | 1 |
| large onions, quartered | 25 |
| large onions, quartered and cut into 1-inch pieces | 1 |
| large onions, quartered and thinly sliced | 1 |
| large onions, quartered lengthwise through root end | 1 |
| large onions, quartered, (about 1 1/2 cups grated) | 1 |
| large onions, skin removed, hairy end left on, cut in 1/2 | 1 |
| large onions, skin removed, root end left on, cut in 1/2 | 1 |
| large onions, thickly sliced | 6 |
| large onions, thinly sliced | 49 |
| large onions, thinly sliced (about 2 pounds) | 1 |
| large onions, thinly sliced (about 3 pounds) | 1 |
| large onions, thinly sliced (about 8 cups) | 1 |
| large onions, thinly sliced from stem to root end | 1 |
| large onions, thinly sliced, about 1 1/2 cups | 2 |
| large onions, unpeeled | 2 |
| large onions, unpeeled and quartered | 3 |
| large onions, unpeeled, quartered | 1 |
| large onions, very thinly sliced | 3 |
| large onions, white, yellow, or red, thinly sliced | 1 |
| large onions, with skins, quartered | 1 |
| large onions, yellow or red, thinly sliced | 1 |
| large or 1 small onion | 1 |
| large or 2 medium onion | 11 |
| large or 2 medium onions (about 1 pound) | 1 |
| large or 2 medium onions, thinly sliced | 1 |
| large or 2 medium onions, thinly sliced in half-moons (about 2 cups) | 1 |
| large or 2 medium spanish onion | 2 |
| large or 2 medium sweet onions, such as vidalia, thinly sliced | 1 |
| large or 2 medium unpeeled onion | 1 |
| large or 2 regular vidalia or sweet onions, halved and sliced | 1 |
| large or 2 small onion | 1 |
| large or 2 small onions, cut into 1/2-inch dice | 3 |
| large or 2 small to medium onion | 1 |
| large or 2 small yellow onion | 1 |
| large or 2 small yellow onions, halved and thinly sliced | 1 |
| large or 3 medium onion | 1 |
| large or 3 medium onions, cut into eighths | 2 |
| large or 3 medium red onions, halved and thinly sliced | 1 |
| large or medium onion | 1 |
| large paper-thin red onion slices, separated into rings | 1 |
| large pearl onion | 2 |
| large pearl onions, about 1/2 pound | 1 |
| large purple onion, cut into chunks | 1 |
| large purple onion, thinly sliced | 1 |
| large purple or red onion, thinly sliced | 1 |
| large red bermuda onion | 4 |
| large red onion | 300 |
| large red onion (1/2 lb), trimmed and cut lengthwise into 6 wedges | 1 |
| large red onion (12 ounces), cut crosswise into 1/3-inch thick slices | 1 |
| large red onion (3/4 pound) | 1 |
| large red onion (about 1 pound) | 1 |
| large red onion (about 8 ounces) | 1 |
| large red onion minced | 1 |
| large red onion rings (each 3 1/2 to 4 inches in diameter and 1/2 inch thick) | 1 |
| large red onion thinly sliced | 1 |
| large red onion, 1-inch dice | 1 |
| large red onion, 1/4-inch dice | 1 |
| large red onion, 1/4-inch slices pulled into rings | 1 |
| large red onion, cut crosswise into 1/3-inch-thick rounds | 1 |
| large red onion, cut crosswise into 1/4-inch-thick slices and separated into rings | 2 |
| large red onion, cut crosswise into 1/8-inch-thick slices, rings separated | 1 |
| large red onion, cut in half | 1 |
| large red onion, cut in very small dice | 1 |
| large red onion, cut into 1 1/2-inch pieces | 1 |
| large red onion, cut into 1 1/2-inch-wide wedges, trimmed, layers separated (32 pieces total) | 1 |
| large red onion, cut into 1 inch cubes | 1 |
| large red onion, cut into 1 inch pieces | 1 |
| large red onion, cut into 1-inch cubes | 1 |
| large red onion, cut into 1-inch pieces | 3 |
| large red onion, cut into 1-inch squares | 1 |
| large red onion, cut into 1-inch wedges (keep stem end intact) | 1 |
| large red onion, cut into 1-inch-thick rounds | 1 |
| large red onion, cut into 1/2-inch cubes | 1 |
| large red onion, cut into 1/2-inch dice | 5 |
| large red onion, cut into 1/2-inch rounds | 1 |
| large red onion, cut into 1/2-inch thick slices | 3 |
| large red onion, cut into 1/2-inch wedges | 1 |
| large red onion, cut into 1/2-inch wide rings | 1 |
| large red onion, cut into 1/2-inch-thick rounds, separated into rings | 1 |
| large red onion, cut into 1/2-inch-thick slices | 2 |
| large red onion, cut into 1/3-inch rounds | 1 |
| large red onion, cut into 1/3-inch-thick slices | 1 |
| large red onion, cut into 1/4-inch dice | 2 |
| large red onion, cut into 1/4-inch slices | 1 |
| large red onion, cut into 1/4-inch thick slices | 2 |
| large red onion, cut into 1/4-inch wedges | 1 |
| large red onion, cut into 12 wedges | 1 |
| large red onion, cut into 2 inch strips | 1 |
| large red onion, cut into 2-inch chunks | 1 |
| large red onion, cut into 2-inch pieces | 1 |
| large red onion, cut into 3/4-inch-thick wedges | 1 |
| large red onion, cut into 4 (1/2-inch) thick rounds, each stuck with a wooden pick to keep it together | 1 |
| large red onion, cut into 4 thick rounds | 1 |
| large red onion, cut into 4 thick slices | 1 |
| large red onion, cut into 6 wedges | 1 |
| large red onion, cut into 8 wedges | 2 |
| large red onion, cut into chunks | 2 |
| large red onion, cut into four 1/3-inch thick slices | 1 |
| large red onion, cut into large pieces | 1 |
| large red onion, cut into quarters vertically | 1 |
| large red onion, cut into rounds | 1 |
| large red onion, cut into small dice | 4 |
| large red onion, cut into small slivers | 1 |
| large red onion, cut into strips | 2 |
| large red onion, cut into thick wedges | 1 |
| large red onion, cut into thin rounds, then quartered (about 2 cups) | 1 |
| large red onion, cut into thin wedges | 1 |
| large red onion, cut into wedges | 4 |
| large red onion, cut julienne | 1 |
| large red onion, cut lengthwise into 1/3-inch-wide wedges and layers separated | 1 |
| large red onion, cut through root end into 6 wedges | 1 |
| large red onion, cut through root end into thin wedges | 1 |
| large red onion, frenched | 1 |
| large red onion, half finely chopped and half thinly sliced | 1 |
| large red onion, halved | 3 |
| large red onion, halved and cut into 1/4-inch-wide slices (about 3 cups) | 1 |
| large red onion, halved and finely chopped | 1 |
| large red onion, halved and sliced | 1 |
| large red onion, halved and sliced 1/4 inch thick | 1 |
| large red onion, halved and thinly sliced | 11 |
| large red onion, halved and thinly sliced (about 1 1/2 cups) | 1 |
| large red onion, halved lengthwise and cut into strips | 1 |
| large red onion, halved lengthwise and sliced | 1 |
| large red onion, halved lengthwise through root end, thinly sliced (about 3 cups) | 1 |
| large red onion, halved lengthwise, cut into thin wedges | 1 |
| large red onion, halved lengthwise, cut thinly crosswise | 1 |
| large red onion, halved lengthwise, thinly sliced crosswise | 1 |
| large red onion, halved through core, thinly sliced | 1 |
| large red onion, halved through core, thinly sliced crosswise | 2 |
| large red onion, halved through root end, cut into 3/4-inch-thick wedges with some root left intact | 1 |
| large red onion, halved through root end, thinly sliced | 1 |
| large red onion, halved, thinly sliced | 1 |
| large red onion, julienned | 2 |
| large red onion, julienned, plus 1 large red onion | 1 |
| large red onion, jullienned | 1 |
| large red onion, medium dice | 2 |
| large red onion, quartered | 3 |
| large red onion, quartered and sliced | 1 |
| large red onion, quartered and sliced thin | 1 |
| large red onion, quartered and thinly sliced | 3 |
| large red onion, quartered and thinly sliced crosswise | 1 |
| large red onion, quartered lengthwise and separated into layers | 1 |
| large red onion, quartered, halved, and cut crosswise | 1 |
| large red onion, roughly chop | 1 |
| large red onion, skin removed, cut in 1/2 and cut into slices | 1 |
| large red onion, small diced | 1 |
| large red onion, thickly sliced | 1 |
| large red onion, thickly sliced (about 1 cup) | 1 |
| large red onion, thinly sliced | 42 |
| large red onion, thinly sliced and rings separated | 1 |
| large red onion, thinly sliced and separated into rings | 1 |
| large red onion, thinly sliced into rings | 1 |
| large red onion, thinly sliced into rounds | 1 |
| large red onion, thinly sliced lengthwise | 1 |
| large red onion, thinly sliced plus 3 tablespoons chopped red onion | 1 |
| large red onion, thinly sliced* | 1 |
| large red onion, very thinly sliced | 1 |
| large red onion,cut into 3/4-inch-thick rounds | 1 |
| large red onion; 1/2 chopped, 1/2 sliced | 1 |
| large red onions (1 1/2 to 1 3/4 pounds), halved, thinly sliced | 1 |
| large red onions or 15 cipolline or boiling onion | 1 |
| large red onions, 1/8-inch slices | 1 |
| large red onions, caramelized and sweated to 2 cups | 1 |
| large red onions, cut in half lengthwise and sliced thin | 1 |
| large red onions, cut into 1-inch rings | 1 |
| large red onions, cut into 1/4-inch-thick rings | 1 |
| large red onions, cut into rounds, 3/8-inch thick | 1 |
| large red onions, cut into wedges | 1 |
| large red onions, cut lengthwise into 1/2-inch wedges (keep root ends intact) | 1 |
| large red onions, each cut into 8 wedges | 1 |
| large red onions, each cut into 8 wedges, keeping root ends intact | 1 |
| large red onions, each cut through root end into 8 wedges | 1 |
| large red onions, halved | 3 |
| large red onions, halved and thinly sliced | 2 |
| large red onions, halved lengthwise, cut crosswise into 1/3-inch-thick slices (about 6 cups) | 1 |
| large red onions, halved, thinly sliced | 1 |
| large red onions, halved, thinly sliced crosswise (about 6 cups) | 1 |
| large red onions, thinly sliced | 10 |
| large red onions, thinly sliced into rings | 1 |
| large red onions, unpeeled | 1 |
| large red or white onion, quartered and thinly sliced crosswise | 1 |
| large red or yellow onion | 2 |
| large red or yellow onion, thinly sliced | 1 |
| large red, yellow, or white onion, (3/4 pound) | 1 |
| large scallions (green onions) | 1 |
| large shallot or 1/2 small red onion | 1 |
| large shallot or 1/4 red onion | 1 |
| large shallots or 1 medium onion | 1 |
| large shallots or 1 small onion | 1 |
| large shallots or 1/2 small onion | 1 |
| large shallots or green onion | 1 |
| large shallots or medium onions, quartered | 1 |
| large shallots, or 2 small onion | 1 |
| large sliced onion | 1 |
| large slices white onion | 2 |
| large spanish onion | 122 |
| large spanish onion (about 12 ounces), cut into large chunks (about 3 cups) | 2 |
| large spanish onion (chopped) | 1 |
| large spanish onion or 2 small yellow onions, cut into 1-inch dice | 1 |
| large spanish onion, cut in half | 1 |
| large spanish onion, cut in half and each half in thirds | 1 |
| large spanish onion, cut into 1-inch dice | 1 |
| large spanish onion, cut into 1/2-inch dice | 1 |
| large spanish onion, cut into 1/2-inch pieces | 1 |
| large spanish onion, cut into 1/4-inch dice | 2 |
| large spanish onion, cut into brunoise | 1 |
| large spanish onion, cut into chunks | 1 |
| large spanish onion, cut into wedges | 1 |
| large spanish onion, halved and sliced 1/4 inch thick | 1 |
| large spanish onion, halved, cut into eighths | 1 |
| large spanish onion, julienned | 2 |
| large spanish onion, quartered | 1 |
| large spanish onion, thickly sliced | 1 |
| large spanish onion, thinly sliced | 6 |
| large spanish onion, thinly sliced into rings and halved | 1 |
| large spanish onions (1 pound) | 1 |
| large spanish onions (2 lb total) | 1 |
| large spanish onions (about 1 pound each), skin-on | 1 |
| large spanish onions (about 2 pounds), left whole and unpeeled | 2 |
| large spanish onions (or 3 yellow onions) | 1 |
| large spanish onions, cut into 1/2- thick inch rings, separated | 1 |
| large spanish onions, cut into 1/4-inch dice | 5 |
| large spanish onions, cut into thin wedges | 1 |
| large spanish onions, halved and thinly sliced | 6 |
| large spanish onions, halved lengthwise and cut into thin half-moon slices | 1 |
| large spanish onions, medium diced | 1 |
| large spanish onions, quartered | 1 |
| large spanish onions, quartered (skin left on) | 4 |
| large spanish onions, roughly cut into 2.5 cm (1 inch) dice | 1 |
| large spanish onions, thinly sliced | 5 |
| large spanish onions, trimmed and cut into 1 inch wedges | 1 |
| large spanish onions, trimmed and cut into 1-inch wedges | 2 |
| large spanish or sweet (vidalia) onion, halved and thinly sliced | 1 |
| large spanish or sweet onion | 1 |
| large spanish or vidalia onion | 2 |
| large spanish or yellow onion | 1 |
| large spanish red onion | 1 |
| large spanish yellow onion | 1 |
| large spring onion | 2 |
| large spring onion (green) | 2 |
| large spring onions (green) | 2 |
| large sweet bermuda onion | 1 |
| large sweet onion | 94 |
| large sweet onion (such as maui or vidalia), cut into 1-inch squares | 1 |
| large sweet onion (such as vidalia or maui) | 1 |
| large sweet onion (such as vidalia or maui), halved, thickly sliced crosswise | 1 |
| large sweet onion (such as vidalia or maui), thinly sliced | 2 |
| large sweet onion (such as vidalia) | 5 |
| large sweet onion (such as vidalia®) | 9 |
| large sweet onion (such as vidalia®), cut into chunks | 1 |
| large sweet onion (such as walla walla) | 1 |
| large sweet onion or red onion, thickly sliced | 1 |
| large sweet onion, 1/2 chopped and 1/2 in wedges | 1 |
| large sweet onion, 1/2 diced and 1/2 chopped | 1 |
| large sweet onion, 1/2-inch dice | 1 |
| large sweet onion, cubed | 1 |
| large sweet onion, cut into 1 1/2 to 2-inch dice | 1 |
| large sweet onion, cut into 1 1/2-2-inch dice | 1 |
| large sweet onion, cut into 1 inch pieces | 2 |
| large sweet onion, cut into 1-inch rings | 1 |
| large sweet onion, cut into 1/2-inch slices | 2 |
| large sweet onion, cut into 1/4-inch dice | 1 |
| large sweet onion, cut into slivers | 1 |
| large sweet onion, halved | 1 |
| large sweet onion, halved and sliced | 1 |
| large sweet onion, halved and sliced thin | 1 |
| large sweet onion, halved and thinly sliced | 2 |
| large sweet onion, quartered and sliced (about 2 cups) | 1 |
| large sweet onion, quartered and thinly sliced | 1 |
| large sweet onion, such as vidalia | 2 |
| large sweet onion, such as vidalia (about 1 pound) | 1 |
| large sweet onion, such as vidalia or maui, thickly sliced | 1 |
| large sweet onion, such as vidalia, halved and thinly sliced | 1 |
| large sweet onion, thinly sliced | 6 |
| large sweet onion, thinly sliced, separated into rings | 1 |
| large sweet onion, unpeeled and cut in half | 1 |
| large sweet onion, very thinly sliced | 1 |
| large sweet onions (2 pounds total) such as vidalia | 1 |
| large sweet onions (such as maui or walla walla), very thinly sliced | 1 |
| large sweet onions (such as vidalia®), thinly sliced | 1 |
| large sweet onions (such as vidalia®), very thinly sliced and separated into rings | 1 |
| large sweet onions (such as walla walla, vidalia, or maui) | 1 |
| large sweet onions such as vidalia, walla walla, or oso sweet (3 to 4 lb total) | 1 |
| large sweet onions, (walla walla, vidalia) | 2 |
| large sweet onions, cut into 1/2-inch thick rings, thin skins removed | 1 |
| large sweet onions, cut into 1/2-inch-thick rings | 1 |
| large sweet onions, cut into 1/4 inch slices and separated into rings | 1 |
| large sweet onions, cut into chunks | 1 |
| large sweet onions, cut into large dice | 1 |
| large sweet onions, cut into thin strips | 1 |
| large sweet onions, halved and thinly sliced | 1 |
| large sweet onions, thinly sliced | 6 |
| large sweet onions, thinly sliced and grilled | 1 |
| large sweet onions/vidalias | 1 |
| large sweet red onion, cut into 1/2-inch-thick rings | 1 |
| large sweet red onion, or to taste | 1 |
| large sweet vidalia onion | 3 |
| large sweet white onions, such as vidalia | 1 |
| large sweet yellow onion | 2 |
| large sweet yellow onion, thinly sliced | 1 |
| large sweet yellow onions (about 1 1/2 pounds), cut into 1/4-inch-thick rounds | 1 |
| large sweet, vidalia or maui onion | 1 |
| large sweet/mild onion | 1 |
| large thin red onion slices | 1 |
| large unpeeled onion | 1 |
| large unpeeled onion, quartered | 1 |
| large unpeeled onions (1 1/4 to 1 1/2 pounds total), cut into 1-inch cubes | 1 |
| large unpeeled yellow onion, cut in half lengthwise through the root | 1 |
| large vidalia onion | 52 |
| large vidalia onion fine chopped | 1 |
| large vidalia onion, cubed | 1 |
| large vidalia onion, cut into 1/2-inch slices | 1 |
| large vidalia onion, cut into 1/4-inch dice | 1 |
| large vidalia onion, cut into 3/4-inch thick wedges | 1 |
| large vidalia onion, cut into chunks | 1 |
| large vidalia onion, cut into wedges | 1 |
| large vidalia onion, halved (through the core) and thinly sliced (1/4-inch) | 1 |
| large vidalia onion, halved and thinly sliced | 2 |
| large vidalia onion, halved vertically | 1 |
| large vidalia onion, medium dice | 1 |
| large vidalia onion, thinly sliced | 2 |
| large vidalia onion, very thinly sliced | 1 |
| large vidalia onion, wedged | 1 |
| large vidalia onions (about 2 pounds), cut into 1/4-inch-thick rounds, separated into rings | 1 |
| large vidalia onions (or other sweets) | 1 |
| large vidalia onions or other sweet variety, thinly sliced | 1 |
| large vidalia onions, cut into 1-inch thick slices | 1 |
| large vidalia onions, cut into 1/2-inch-thick-slices | 1 |
| large vidalia onions, cut into 1/4-inch slices, and separated into rings | 1 |
| large vidalia onions, cut into wedges through the root so they stay attached | 1 |
| large vidalia onions, halved and thinly sliced | 1 |
| large vidalia onions, medium dice | 1 |
| large vidalia onions, thinly sliced | 1 |
| large vidalia or other sweet onion | 5 |
| large vidalia or other sweet onion, cut into 1/4-inch-thick slices | 1 |
| large vidalia or other sweet onion, thinly sliced | 1 |
| large vidalia or spanish onion | 1 |
| large vidalia or spanish onions, thinly sliced | 1 |
| large vidalia or sweet onion | 2 |
| large vidalia or sweet onion, thinly sliced | 1 |
| large vidalia sweet onion, 1/2 cut into large dice, 1/2 reserved | 1 |
| large vidalia, or other sweet onion sliced into rings | 1 |
| large vidalia, or other sweet onion, thinly sliced | 1 |
| large walla walla onion | 2 |
| large while onion | 1 |
| large white boiling onions or small spanish onion | 1 |
| large white cooking onions, thinly sliced | 1 |
| large white onion | 203 |
| large white onion (10 oz), trimmed and cut lengthwise into 6 wedges | 1 |
| large white onion diced | 1 |
| large white onion thinly sliced | 1 |
| large white onion with skin, quartered through core with some core still attached to each piece | 1 |
| large white onion, cut crosswise into 1/2-inch-thick rounds | 1 |
| large white onion, cut crosswise into 4 thick slices | 1 |
| large white onion, cut into 1 1/2-inch pieces | 2 |
| large white onion, cut into 1-inch chunks | 1 |
| large white onion, cut into 1-inch pieces | 1 |
| large white onion, cut into 1/2" rings | 1 |
| large white onion, cut into 1/2-inch cubes | 2 |
| large white onion, cut into 1/2-inch dice | 1 |
| large white onion, cut into 1/2-inch pieces (about 2 1/2 cups) | 1 |
| large white onion, cut into 2-inch-thick wedges | 1 |
| large white onion, cut into 4 wedges | 2 |
| large white onion, cut into 6 wedges | 1 |
| large white onion, cut into 8 wedges | 1 |
| large white onion, cut into 8 wedges and layers separated | 1 |
| large white onion, cut into chunks | 4 |
| large white onion, cut into large chunks | 2 |
| large white onion, cut into large wedges | 1 |
| large white onion, cut into rings | 1 |
| large white onion, cut into small dice | 3 |
| large white onion, cut lengthwise into 1/4-inch-wide strips (1 3/4 cups) | 1 |
| large white onion, halved | 1 |
| large white onion, halved and thinly sliced | 2 |
| large white onion, halved lengthwise, then cut crosswise into 1/2-inch slices | 1 |
| large white onion, halved with some root end attached | 1 |
| large white onion, julienned | 1 |
| large white onion, medium dice | 1 |
| large white onion, medium diced | 2 |
| large white onion, quartered | 7 |
| large white onion, quartered through root end | 1 |
| large white onion, shredded | 1 |
| large white onion, thinly sliced | 10 |
| large white onion, thinly sliced into rings | 1 |
| large white onion; 2/3 diced, 1/3 sliced into rings | 1 |
| large white onions finely chopped | 2 |
| large white onions, cut into 1/2-inch dice | 1 |
| large white onions, cut into 2-inch squares | 2 |
| large white onions, halved | 1 |
| large white onions, halved (do not peel) | 1 |
| large white onions, julienne | 1 |
| large white onions, quartered | 3 |
| large white onions, thickly sliced | 1 |
| large white onions, thinly sliced | 4 |
| large whole onion | 3 |
| large whole onion, unpeeled | 1 |
| large whole onion, unpeeled (find one with a firm, golden-brown peel) | 1 |
| large yellow cooking onion | 1 |
| large yellow mexican onion | 2 |
| large yellow onion | 260 |
| large yellow onion (about 8 ounces) | 1 |
| large yellow onion julienned | 1 |
| large yellow onion, 1/2-inch dice | 1 |
| large yellow onion, 1/4-inch dice | 1 |
| large yellow onion, 1/4-inch dice (about 2 cups) | 1 |
| large yellow onion, cut in eighths | 1 |
| large yellow onion, cut into 1 1/2-inch cubes | 1 |
| large yellow onion, cut into 1/2 inch pieces | 1 |
| large yellow onion, cut into 1/2-inch dice(about 2 cups) | 1 |
| large yellow onion, cut into 1/4-inch strips | 1 |
| large yellow onion, cut into 1/8 inch dice | 1 |
| large yellow onion, cut into 1/8-inch dice | 1 |
| large yellow onion, cut into 3/4-inch thick rounds | 1 |
| large yellow onion, cut into cubes | 1 |
| large yellow onion, cut into large dice | 1 |
| large yellow onion, cut into medium dice | 2 |
| large yellow onion, cut into small dice | 2 |
| large yellow onion, cut into three or four 1/2-inch rounds | 1 |
| large yellow onion, cut into wedges | 1 |
| large yellow onion, cut to 1/2-inch dice | 1 |
| large yellow onion, halved | 1 |
| large yellow onion, halved and cut into 1/4-inch-thick slices | 1 |
| large yellow onion, halved and sliced | 1 |
| large yellow onion, halved and sliced 1/4-inch-thick (about 2 cups) | 1 |
| large yellow onion, halved and sliced thin | 1 |
| large yellow onion, halved and thinly sliced | 2 |
| large yellow onion, halved and thinly sliced (about 2 cups) | 2 |
| large yellow onion, halved and very thinly sliced (about 2 cups) | 1 |
| large yellow onion, julienned | 1 |
| large yellow onion, quartered | 8 |
| large yellow onion, quartered and sliced | 1 |
| large yellow onion, quartered and thinly sliced | 1 |
| large yellow onion, root removed | 1 |
| large yellow onion, small dice | 1 |
| large yellow onion, small diced | 2 |
| large yellow onion, small diced (about 1 1/2 cups) | 1 |
| large yellow onion, small-diced | 1 |
| large yellow onion, thickly sliced | 1 |
| large yellow onion, thickly sliced lengthwise | 1 |
| large yellow onion, thinly sliced | 10 |
| large yellow onion, thinly sliced into half moons | 1 |
| large yellow onion, thinly sliced, caramelized | 1 |
| large yellow onion, unpeeled and cut in eighths | 2 |
| large yellow onions (about 1 1/2 pounds), quartered and thinly sliced | 1 |
| large yellow onions (about 2 pounds total) | 1 |
| large yellow onions (about 4 pounds) | 2 |
| large yellow onions (spanish) | 1 |
| large yellow onions cut in half and sliced 1/2 inch thick | 1 |
| large yellow onions, cut in 1/2 through the root and sliced into 1/8-inch-thick slices | 1 |
| large yellow onions, cut in 2-inch-thick slices | 1 |
| large yellow onions, cut in half and sliced | 1 |
| large yellow onions, cut into 1-inch squares | 1 |
| large yellow onions, cut into 1/2-inch pieces (about 5 cups or 3 pounds) | 1 |
| large yellow onions, cut into 1/8"-thick wedges | 1 |
| large yellow onions, cut into very thin slivers | 1 |
| large yellow onions, cut into very thin wedges | 1 |
| large yellow onions, cut into wedges | 1 |
| large yellow onions, halved | 4 |
| large yellow onions, halved and thinly sliced | 1 |
| large yellow onions, halved and thinly sliced (about 6 cups) | 1 |
| large yellow onions, halved and very thinly sliced | 1 |
| large yellow onions, halved lengthwise and each half sliced about 3/8 inch thick | 1 |
| large yellow onions, in 1/4-inch slices from root to tip | 1 |
| large yellow onions, large dice | 1 |
| large yellow onions, large diced (about 3 cups) | 1 |
| large yellow onions, medium dice | 1 |
| large yellow onions, medium diced | 1 |
| large yellow onions, quartered | 1 |
| large yellow onions, rough cut | 1 |
| large yellow onions, thinly sliced | 5 |
| large yellow onions, thinly sliced in rounds | 1 |
| large yellow onions, thinly sliced into rings | 1 |
| large yellow onions, thinly sliced lengthwise | 1 |
| large yellow onions, unpeeled and quartered | 2 |
| large yellow onions, unpeeled, quartered | 4 |
| large yellow onions, very thinly sliced | 1 |
| large yellow onions, very thinly sliced with a mandoline | 1 |
| large yellow or spanish onion, halved and thinly sliced | 1 |
| large yellow or white onion | 4 |
| large yellow or white onions, thinly sliced | 1 |
| large yellow skinned onion | 3 |
| large yellow skinned onion, cubed, 1-inch pieces | 1 |
| large yellow skinned onions, thinly sliced | 2 |
| large yellow sweet onions, such as maui | 1 |
| large, 1-inch slice sweet onion, cut from the middle | 2 |
| large, red onion | 1 |
| large, sweet onion | 1 |
| large, thin red onion slices | 1 |
| large, yellow onions, 1/4-inch slices | 1 |
| large, yellow skinned onion | 1 |
| large-chopped onion | 1 |
| large-diced onion | 1 |
| large-diced red onion | 1 |
| large-size yellow onion | 1 |
| large/jumbo yellow onion | 1 |
| leek (white and light green parts only) or white onion, very thinly sliced | 1 |
| leek or large onion | 1 |
| leek, cleaned and chopped, or substitute 1 large yellow onion | 2 |
| leeks (white and light green parts only) or 1 onion | 1 |
| left over mashed potatoes, or chive and onion mashed potatoes, recipe follows | 1 |
| leftover chopped onions from chicken souvlaki recipe | 1 |
| leftover pearl onions, creamed or plain | 2 |
| leftover pieces of raw veggies: green or red pepper, onion, mushroom | 1 |
| leftover red onion compote from aale house burgers with red onion compote, recipe follows | 1 |
| leftover roasted vegetables, such as potatoes, carrots, parsnips and onion | 1 |
| leftover sauteed sliced onion | 1 |
| lemon cucumbers and torpedo onion | 1 |
| lemon-pepper seasoning with garlic and onion | 1 |
| lettuce leaves, red onion slices, tomato slices (optional) | 1 |
| lettuce tomato slices, and red onion slices | 1 |
| lettuce, tomato, onion | 1 |
| lettuce, tomato, onion and pickle, for garnish | 1 |
| lettuce, tomato, onion, for serving | 1 |
| lettuce, tomato, onion, pickles, for dressing the burger | 1 |
| lettuce, tomato, onions, for garnish | 1 |
| lettuce, tomato, onions, ketchup, mustard, for serving or whatever else you like on a burger | 1 |
| lettuce, tomato, red onion and tartar sauce, for serving | 1 |
| lettuce, tomatoes, onion | 1 |
| little onion | 1 |
| long onions, or 8 to 10 scallions, cut diagonally into 1 1/2-inch lengths | 1 |
| mango-pineapple salsa or spicy caramelized onion | 1 |
| marie poix of vegetable (celery, onions and fennel) | 1 |
| marinated cocktail onion | 1 |
| marinated cocktail onions, cut in half | 1 |
| marinated red onions, recipe follows | 2 |
| matchstick-size strips green onion | 1 |
| matchstick-size strips green onions (about 8) | 1 |
| maui onion | 14 |
| maui onion cut into thick 1/2-inch rings | 1 |
| maui onion or other sweet onion | 1 |
| maui onion slices | 1 |
| maui onion, julienned | 2 |
| maui onion, thinly sliced | 1 |
| maui onion, very thinly sliced | 1 |
| maui onions or any sweet onion | 1 |
| maui onions, julienned | 1 |
| maui onions, slide thin, for caramelizing | 1 |
| maui or other sweet onion, thinly sliced | 1 |
| maui or vidalia onions, cut into 1/2-inch-thick rounds | 1 |
| mayonnaise, thinly sliced chives, french fried onions (such as french's), drained canned corn kernels, and/or chopped pickles (for serving) | 1 |
| meatless bacon and onion seasoning (such as tastefully simple® bacon bacon®) | 1 |
| med. onion | 1 |
| medium (1-inch) boiling onion | 1 |
| medium (3 oz | 90 g) yellow or red onion, thinly sliced against the grain and soaked in water for 10 minutes | 1 |
| medium (5 ounces) onion | 1 |
| medium (about 1 cup) vidalia onion | 1 |
| medium bermuda onion | 1 |
| medium bermuda onion, thinly sliced | 1 |
| medium chopped onion | 3 |
| medium chopped red onion | 1 |
| medium chopped yellow onion | 2 |
| medium cipollini onions (about 8 ounces) | 1 |
| medium dice onion | 1 |
| medium dice onion, yellow or white | 1 |
| medium dice red onion | 2 |
| medium dice sweet onion | 1 |
| medium dice yellow onion | 2 |
| medium diced onion | 7 |
| medium diced onions (2 to 3 large onions) | 1 |
| medium diced red onion | 2 |
| medium diced white onion | 1 |
| medium diced yellow onion | 1 |
| medium green onion | 12 |
| medium green onions, cut into 2" pieces | 1 |
| medium green onions, thinly sliced | 4 |
| medium green onions, thinly sliced (1/4 cup) or 1/3 cup chopped green or red bell pepper | 1 |
| medium green onions, thinly sliced diagonally | 1 |
| medium large sweet onion | 2 |
| medium leeks or 1 yellow onion, halved and sliced 1/4-inch thick | 1 |
| medium maui onion, small diced | 1 |
| medium new white onion | 1 |
| medium onion | 2,353 |
| medium onion (2 ounces) finely sliced | 1 |
| medium onion (4 ounces), cut into 1/2-inch dice | 1 |
| medium onion (5 to 6 ounces) | 2 |
| medium onion (6 oz) | 1 |
| medium onion (7 ounces) cut into 3/4-inch dice | 1 |
| medium onion (7 to 8 ounces), cut into 1/2-inch dice | 1 |
| medium onion (8 ounces), cut into 3/4-inch dice | 1 |
| medium onion (8 ounces), thinly sliced | 1 |
| medium onion (about 6 ounces) | 1 |
| medium onion (about 6 ounces), thinly sliced | 1 |
| medium onion (about 8 ounces) | 2 |
| medium onion (preferably white) | 2 |
| medium onion (small dice) | 1 |
| medium onion chopped | 6 |
| medium onion diced | 3 |
| medium onion diced small | 1 |
| medium onion or 1/2 large onion | 1 |
| medium onion or leek | 1 |
| medium onion or leek, or 2 shallots | 1 |
| medium onion or leek, thinly sliced | 1 |
| medium onion peeled | 1 |
| medium onion peeled and chopped | 1 |
| medium onion, 1-inch dice | 1 |
| medium onion, 1/2-inch dice | 2 |
| medium onion, 1/4 onion grated and juiced, 3/4 onion | 1 |
| medium onion, 1/4-inch dice | 1 |
| medium onion, about 1/2 cup | 1 |
| medium onion, about 1/2 pound | 1 |
| medium onion, about 8 ounces | 1 |
| medium onion, chunked | 1 |
| medium onion, cubed | 1 |
| medium onion, cut crosswise into 1/4-inch-thick rings | 1 |
| medium onion, cut crosswise into 1/4-inch-thick slices | 1 |
| medium onion, cut in 1/2 | 1 |
| medium onion, cut in 1/2 lengthwise and then into 1/4-inch-thick slices | 1 |
| medium onion, cut in 1/2, then thinly sliced into 1/2 moons | 1 |
| medium onion, cut in 4 wedges | 1 |
| medium onion, cut in 8 wedges | 1 |
| medium onion, cut in ?-inch dice | 1 |
| medium onion, cut in eighths | 1 |
| medium onion, cut in half | 10 |
| medium onion, cut in half and sliced (about 1 cup) | 1 |
| medium onion, cut in half, then sliced | 1 |
| medium onion, cut in strips | 1 |
| medium onion, cut into 1 inch slices | 1 |
| medium onion, cut into 1-inch dice | 1 |
| medium onion, cut into 1-inch pieces | 4 |
| medium onion, cut into 1/2 -inch wedges | 1 |
| medium onion, cut into 1/2-inch cubes | 2 |
| medium onion, cut into 1/2-inch dice | 1 |
| medium onion, cut into 1/2-inch pieces | 2 |
| medium onion, cut into 1/2-inch slices | 2 |
| medium onion, cut into 1/2-inch wedges | 2 |
| medium onion, cut into 1/2-inch-thick rounds | 1 |
| medium onion, cut into 1/3-inch pieces | 1 |
| medium onion, cut into 1/4-inch dice | 5 |
| medium onion, cut into 1/4-inch slices | 2 |
| medium onion, cut into 1/4-inch wedges | 1 |
| medium onion, cut into 1/4inch dice | 1 |
| medium onion, cut into 3/4-inch pieces | 2 |
| medium onion, cut into 3/4-inch pieces (about 1 3/4 cups) | 1 |
| medium onion, cut into 6 wedges | 1 |
| medium onion, cut into 8 wedges | 1 |
| medium onion, cut into chunks | 5 |
| medium onion, cut into fine dice | 1 |
| medium onion, cut into fine julienne | 1 |
| medium onion, cut into julienne strips | 1 |
| medium onion, cut into large chunks | 1 |
| medium onion, cut into large dice | 1 |
| medium onion, cut into large pieces | 1 |
| medium onion, cut into medium dice | 1 |
| medium onion, cut into medium dice (about 2 cups) | 1 |
| medium onion, cut into paper-thin half-moons | 1 |
| medium onion, cut into rings | 2 |
| medium onion, cut into small dice | 3 |
| medium onion, cut into small dice (about 1 1/2 cups) | 1 |
| medium onion, cut into small dice (about 3/4 cup) | 1 |
| medium onion, cut into thin wedges | 1 |
| medium onion, cut into thirds | 1 |
| medium onion, cut into wedges | 5 |
| medium onion, cut into wedges, keeping root intact | 1 |
| medium onion, cut lengthwise into 6 wedges, leaving root ends intact | 1 |
| medium onion, finely choppe | 1 |
| medium onion, finely food processed | 1 |
| medium onion, halved | 15 |
| medium onion, halved and cut lengthwise into julienne | 1 |
| medium onion, halved and sliced | 8 |
| medium onion, halved and thinly sliced | 5 |
| medium onion, halved and thinly sliced (but not too thin) | 1 |
| medium onion, halved and thinly sliced, plus 1 large onion | 1 |
| medium onion, halved from pole to pole; each half cut into 6 wedges | 1 |
| medium onion, halved lengthwise | 2 |
| medium onion, halved lengthwise and thinly sliced | 2 |
| medium onion, halved lengthwise and thinly sliced crosswise | 2 |
| medium onion, halved lengthwise through core end | 1 |
| medium onion, halved lengthwise, then cut crosswise into 1/2-inch-thick slices | 1 |
| medium onion, halved lengthwise, then cut crosswise into 1/4-inch-thick slices | 1 |
| medium onion, halved lengthwise, then sliced crosswise (1 cup) | 1 |
| medium onion, halved lengthwise, then thinly sliced crosswise | 2 |
| medium onion, halved lengthwise, then thinly sliced lengthwise | 2 |
| medium onion, halved lengthwise, thinly sliced | 1 |
| medium onion, halved then cut into chunks | 1 |
| medium onion, halved, plus 1 medium onion, halved | 1 |
| medium onion, halved, thinly sliced | 1 |
| medium onion, halved, very thinly sliced | 1 |
| medium onion, in large chunks | 1 |
| medium onion, julienne | 1 |
| medium onion, julienned | 8 |
| medium onion, large dice | 2 |
| medium onion, left unpeeled and cut into 8 wedges | 1 |
| medium onion, left unpeeled, trimmed, and halved | 1 |
| medium onion, medium dice | 4 |
| medium onion, medium diced | 2 |
| medium onion, plus 1 cup chopped | 1 |
| medium onion, poked with a fork | 1 |
| medium onion, pureed in blender | 1 |
| medium onion, quartered | 39 |
| medium onion, quartered and left unpeeled | 1 |
| medium onion, quartered and thinly sliced | 6 |
| medium onion, quartered but left unpeeled | 1 |
| medium onion, quartered lengthwise, and cut crosswise into 1/4-inch-thick slices | 1 |
| medium onion, quartered through core | 1 |
| medium onion, quartered through core end | 1 |
| medium onion, quartered, then thinly sliced | 1 |
| medium onion, red or yellow | 2 |
| medium onion, roasted then minced | 1 |
| medium onion, rough chopped | 1 |
| medium onion, skin on | 2 |
| medium onion, skin removed and cut in half | 1 |
| medium onion, slivered | 1 |
| medium onion, small dice | 5 |
| medium onion, small diced | 6 |
| medium onion, small diced (about 1 1/2 cups) | 1 |
| medium onion, small diced (about 1 cup) | 1 |
| medium onion, small diced (about 2 cups) | 1 |
| medium onion, small to medium dice | 1 |
| medium onion, stuck with 1 clove | 1 |
| medium onion, stuck with 1 whole clove | 1 |
| medium onion, thickly sliced | 1 |
| medium onion, thinly sliced | 104 |
| medium onion, thinly sliced (about 2 cups) | 1 |
| medium onion, thinly sliced and soaked for 30 minutes in ice water | 1 |
| medium onion, thinly sliced into rings | 1 |
| medium onion, thinly sliced, separated into rings | 1 |
| medium onion, unpeeled, cut into 1" pieces | 1 |
| medium onion, unpeeled, cut into eighths | 1 |
| medium onion, unpeeled, halved | 1 |
| medium onion, unpeeled, quartered | 1 |
| medium onion, very finely chopped | 7 |
| medium onion, very thinly sliced | 4 |
| medium onion, yellow skinned | 1 |
| medium onions (1 1/4 pounds total) | 1 |
| medium onions (1 1/4 to 1 1/2 pounds total) | 1 |
| medium onions (12 to 14 ounces), cut into 1/2-inch pieces | 1 |
| medium onions (14 ounces), cut into 3/4-inch dice | 1 |
| medium onions (about 1 1/4 pounds), thinly sliced | 1 |
| medium onions (about 1 pound) peeled and sliced into 1/4-inch-thick rounds | 1 |
| medium onions (about 1/2 pound each), halved lengthwise, cut into 3/4-inch-wide wedges with some core still attached | 1 |
| medium onions (about 12 ounces), cut in 1/4-inch dice | 1 |
| medium onions (about 14 ounces) | 1 |
| medium onions (about 2 1/2 pounds) | 1 |
| medium onions (about 6 ounces each), thinly sliced | 1 |
| medium onions (cut into 1/2 inch slices) | 1 |
| medium onions (preferably 1 red and 1 sweet), cut into 1/4-inch-wide wedges | 1 |
| medium onions 1/4-inch sliced | 1 |
| medium onions chopped | 2 |
| medium onions cut into 2-inch pieces | 1 |
| medium onions cut into chunks | 2 |
| medium onions diced | 1 |
| medium onions julienned | 1 |
| medium onions peeled and cut into small cubes | 1 |
| medium onions peeled, each cut into 6 wedges, root end intact | 1 |
| medium onions per person | 1 |
| medium onions sliced crosswise 1/2 inch thick | 1 |
| medium onions, 1 halved, 1 thinly sliced | 1 |
| medium onions, 1 sliced into rings, the other finely diced | 1 |
| medium onions, 1/2-inch dice | 1 |
| medium onions, 2 left in their skin, and 1 peeled | 1 |
| medium onions, 2 left in their skins, and 1 peeled | 2 |
| medium onions, chopped1 fresh bay leaf | 1 |
| medium onions, cut crosswise into 1/8 inch slices and separated into rings | 1 |
| medium onions, cut in half and then sliced 1/4-inch-thick | 1 |
| medium onions, cut in large chunks (about 3 cups) | 1 |
| medium onions, cut into 1" pieces | 1 |
| medium onions, cut into 1-inch cubes | 1 |
| medium onions, cut into 1-inch pieces | 1 |
| medium onions, cut into 1-inch wedges | 1 |
| medium onions, cut into 1/2" slices | 1 |
| medium onions, cut into 1/2-inch dice | 1 |
| medium onions, cut into 1/2-inch-thick slices | 1 |
| medium onions, cut into 1/4-inch dice (2 cups) | 1 |
| medium onions, cut into 1/4-inch dice (about 3 cups) | 1 |
| medium onions, cut into 1/4-inch slices | 1 |
| medium onions, cut into 1/4-inch-thick rounds, separated into rings | 1 |
| medium onions, cut into 2-by-1/2-inch matchsticks | 1 |
| medium onions, cut into 2-inch chunks | 1 |
| medium onions, cut into 3/4-inch dice | 1 |
| medium onions, cut into 3/4-inch wedges with some core attached | 1 |
| medium onions, cut into 6ths | 1 |
| medium onions, cut into bite-size pieces | 1 |
| medium onions, cut into chunks | 3 |
| medium onions, cut into large dice | 1 |
| medium onions, cut into medium dice | 3 |
| medium onions, cut into quarters | 1 |
| medium onions, cut into quarters, keeping the root end intact | 1 |
| medium onions, cut into sixths | 1 |
| medium onions, cut into thick slices | 1 |
| medium onions, cut into thin wedges | 1 |
| medium onions, cut into thin wedges, root end attached | 1 |
| medium onions, cut into wedges | 3 |
| medium onions, cut into wedges with root end attached | 1 |
| medium onions, cut lengthwise into 1-inch-thick wedges | 1 |
| medium onions, each cut into 4 wedges | 1 |
| medium onions, each stuck with 3 whole clove | 1 |
| medium onions, halved | 6 |
| medium onions, halved and cut in 1/4-inch slices lengthwise | 1 |
| medium onions, halved and cut in 1/4-inch slices, lengthwise | 1 |
| medium onions, halved and cut into thin rings | 1 |
| medium onions, halved and sliced | 4 |
| medium onions, halved and sliced thin lengthwise | 1 |
| medium onions, halved and thinly sliced | 2 |
| medium onions, halved lengthwise and cut crosswise into 1/4-inch-thick slices | 1 |
| medium onions, halved lengthwise and sliced thin | 1 |
| medium onions, halved lengthwise and then cut lengthwise into 1/4-inch slices | 1 |
| medium onions, halved lengthwise and then sliced crosswise 1/4 inch thick | 1 |
| medium onions, halved lengthwise and thickly sliced | 1 |
| medium onions, halved lengthwise and thinly sliced | 2 |
| medium onions, halved lengthwise and thinly sliced crosswise | 1 |
| medium onions, halved lengthwise and thinly sliced crosswise (4 cups) | 1 |
| medium onions, halved lengthwise and thinly sliced lengthwise | 1 |
| medium onions, halved lengthwise, then cut lengthwise into 1/4-inch slices | 1 |
| medium onions, halved lengthwise, then cut lengthwise into 1/4-inch-wide strips | 1 |
| medium onions, halved lengthwise, then thinly sliced crosswise | 2 |
| medium onions, halved lengthwise, then thinly sliced crosswise (2 cups) | 1 |
| medium onions, halved lengthwise, then thinly sliced lengthwise | 1 |
| medium onions, halved, cut into 1/2-inch thick wedges | 1 |
| medium onions, halved, cut lengthwise into strips (about 3 cups) | 1 |
| medium onions, halves and sliced thin lengthwise (about 1 1/2 cups) | 1 |
| medium onions, in large dice | 1 |
| medium onions, in medium dice | 1 |
| medium onions, julienned | 1 |
| medium onions, left unpeeled, trimmed and halved | 3 |
| medium onions, left unpeeled, trimmed, and halved | 4 |
| medium onions, medium dice | 1 |
| medium onions, or 4 cups smoked onion | 1 |
| medium onions, quartered | 16 |
| medium onions, quartered lengthwise | 3 |
| medium onions, quartered lengthwise then very thinly sliced | 1 |
| medium onions, quartered; plus 2 cups | 1 |
| medium onions, red or yellow | 1 |
| medium onions, roughly cut | 1 |
| medium onions, small dice | 1 |
| medium onions, thickly sliced | 1 |
| medium onions, thinly sliced | 51 |
| medium onions, thinly sliced (3 cups) | 1 |
| medium onions, thinly sliced (4 cups) | 1 |
| medium onions, thinly sliced (about 2 cups) | 1 |
| medium onions, unpeeled | 1 |
| medium onions, unpeeled but trimmed, and each cut into 4 wedges | 1 |
| medium onions, unpeeled, cut into 1" pieces | 1 |
| medium onions, unpeeled, halved through root | 1 |
| medium onions, unpeeled, quartered | 1 |
| medium onions, unpeeled, quartered lengthwise | 1 |
| medium onions, unpeeled, quartered through root ends | 1 |
| medium onions, very finely chopped | 1 |
| medium onions, very thinly sliced | 2 |
| medium or 1 large onion | 2 |
| medium or 1 large vidalia onion | 2 |
| medium or 1 large yellow skinned onion, quartered and sliced | 1 |
| medium or 12 baby onion | 1 |
| medium or 2 small onions, cut into 1/4-inch dice (about 1 1/2 cups) | 1 |
| medium or 3 large onions, halved and sliced as thinly as possible | 1 |
| medium or 4 large onion | 1 |
| medium or large onion, french cut | 1 |
| medium peeled red onions cut into 8 rounds | 1 |
| medium red and yellow onions (4 lb) | 1 |
| medium red and/or yellow onions, halved, stem ends intact | 1 |
| medium red onion | 340 |
| medium red onion (1/2 roughly chopped, 1/2 thinly sliced) | 1 |
| medium red onion (about 6 ounces) | 1 |
| medium red onion (you can use the rest of the onion you grated for the brine, recipe above) | 1 |
| medium red onion coarsely chopped | 1 |
| medium red onion diced | 1 |
| medium red onion, 1/2 finely chopped, 1/2 thinly sliced | 1 |
| medium red onion, cored and cut into 1-inch cubes* | 1 |
| medium red onion, cut crosswise into 1/2-inch thick slices | 1 |
| medium red onion, cut in 1-inch dice | 1 |
| medium red onion, cut in 1/2, then into 1/4-inch slivers | 1 |
| medium red onion, cut in small dice | 1 |
| medium red onion, cut into 1-inch chunks | 1 |
| medium red onion, cut into 1-inch pieces | 1 |
| medium red onion, cut into 1-inch-thick rings | 1 |
| medium red onion, cut into 1-inch-thick wedges | 1 |
| medium red onion, cut into 1/2 inch chunks | 1 |
| medium red onion, cut into 1/2" wedges | 2 |
| medium red onion, cut into 1/2-inch pieces | 1 |
| medium red onion, cut into 1/2-inch rings | 2 |
| medium red onion, cut into 1/2-inch thick slices | 1 |
| medium red onion, cut into 1/2-inch wedges | 1 |
| medium red onion, cut into 1/4"-thick rounds | 1 |
| medium red onion, cut into 1/4-inch cubes | 2 |
| medium red onion, cut into 1/4-inch dice | 2 |
| medium red onion, cut into 1/4-inch slices | 1 |
| medium red onion, cut into 1/4-inch thick slices | 1 |
| medium red onion, cut into 1/8-inch dice | 1 |
| medium red onion, cut into 16 slices | 1 |
| medium red onion, cut into 2-inch chunks and sections separated | 1 |
| medium red onion, cut into 2-inch chunks* | 1 |
| medium red onion, cut into 3/4-inch-wide wedges, then very thinly sliced crosswise | 1 |
| medium red onion, cut into 4 slices | 1 |
| medium red onion, cut into 4 wedges, then crosswise into paper-thin slices | 1 |
| medium red onion, cut into 6 thick slices | 1 |
| medium red onion, cut into 8 wedges | 1 |
| medium red onion, cut into 8 wedges (from root to tip) | 1 |
| medium red onion, cut into julienne strips | 1 |
| medium red onion, cut into small dice | 2 |
| medium red onion, cut into thin slices | 1 |
| medium red onion, cut into wedges | 4 |
| medium red onion, cut lengthwise into 1/2-inch-thick wedges | 1 |
| medium red onion, cut lengthwise into 1/2-inch-wide strips | 1 |
| medium red onion, halved | 1 |
| medium red onion, halved and cut into 1/4-inch-thick slices | 1 |
| medium red onion, halved and sliced | 3 |
| medium red onion, halved and sliced into half moons | 2 |
| medium red onion, halved and thinly sliced | 11 |
| medium red onion, halved lengthwise and cut lengthwise into 1/2-inch-thick slices | 1 |
| medium red onion, halved lengthwise and sliced paper thin | 1 |
| medium red onion, halved lengthwise, then thinly sliced | 1 |
| medium red onion, halved lengthwise, then thinly sliced crosswise | 2 |
| medium red onion, halved lengthwise, then very thinly sliced lengthwise | 1 |
| medium red onion, halved lengthwise, very thinly sliced lengthwise, and soaked in cold water 20 minutes | 1 |
| medium red onion, halved through core, cut lengthwise into 1/2-inch-thick strips | 1 |
| medium red onion, halved through root end, thinly sliced | 1 |
| medium red onion, halved, cut into 1/3-inch-thick wedges with some core attached | 1 |
| medium red onion, halved, then sliced 1/4 inch thick | 1 |
| medium red onion, halved, thinly sliced (about 2 cups) | 1 |
| medium red onion, julienned | 5 |
| medium red onion, large dice | 3 |
| medium red onion, quartered | 2 |
| medium red onion, quartered and separated | 1 |
| medium red onion, quartered and sliced crosswise 1/2-inch thick | 1 |
| medium red onion, root intact and thinly sliced lengthwise into wedges | 1 |
| medium red onion, shaved thin with a mandoline | 1 |
| medium red onion, shredded | 1 |
| medium red onion, small dice | 3 |
| medium red onion, small diced | 1 |
| medium red onion, thinly sliced | 90 |
| medium red onion, thinly sliced (about 1 1/2 cups) | 1 |
| medium red onion, thinly sliced (about 1 1/4 cups) | 1 |
| medium red onion, thinly sliced (about 1 cup) | 1 |
| medium red onion, thinly sliced (about 2 cups) | 1 |
| medium red onion, thinly sliced (about 3/4 cup) | 1 |
| medium red onion, thinly sliced crosswise | 2 |
| medium red onion, thinly sliced into rings | 1 |
| medium red onion, thinly sliced into rounds | 1 |
| medium red onion, thinly sliced, soaked in ice water for 10 minutes and drained | 1 |
| medium red onion, thinly slicied | 1 |
| medium red onion, unpeeled, thickly sliced | 1 |
| medium red onion, very finely diced | 1 |
| medium red onion, very small diced | 1 |
| medium red onion, very thinly sliced | 2 |
| medium red onion, very, very thinly sliced | 1 |
| medium red onions (1 pound total) | 1 |
| medium red onions (about 1 1/2 pounds total) | 1 |
| medium red onions (about 1 1/2 pounds total), each cut into 6 wedges, leaving enough of root ends attached to keep wedges intact | 1 |
| medium red onions (about 1 pound total), each cut into 8 wedges | 1 |
| medium red onions (about 10 ounces each), halved, thinly sliced (about 5 1/2 cups) | 1 |
| medium red onions (about 5) | 1 |
| medium red onions (about 7 ounces each) | 1 |
| medium red onions (about 9) | 1 |
| medium red onions cut crosswise 1/3-inch thick | 1 |
| medium red onions cut into slices | 1 |
| medium red onions or sweet onions (such as walla walla), skin on, roots intact | 1 |
| medium red onions, 2 whole, 1 minced | 1 |
| medium red onions, about 2 pounds | 1 |
| medium red onions, cut crosswise into 1/4-inch-thick rounds | 1 |
| medium red onions, cut in 1/2 lengthwise | 1 |
| medium red onions, cut into 1-inch pieces | 2 |
| medium red onions, cut into 1/2" wedges | 1 |
| medium red onions, cut into 1/2-inch cubes | 1 |
| medium red onions, cut into 1/4-inch slices | 1 |
| medium red onions, cut into 1/4-inch-thick slices | 1 |
| medium red onions, cut into 3/4-inch dice | 1 |
| medium red onions, cut into large chunks | 1 |
| medium red onions, cut into wedges | 1 |
| medium red onions, cut through root ends into 1/2-inch-thick wedges | 1 |
| medium red onions, each cut through root end into 6 wedges | 1 |
| medium red onions, halved | 1 |
| medium red onions, halved and cut into wedges | 1 |
| medium red onions, halved and sliced paper thin | 1 |
| medium red onions, halved and thinly sliced | 4 |
| medium red onions, halved lengthwise and cut into 1/2-inch rings | 1 |
| medium red onions, julienned | 1 |
| medium red onions, quartered | 1 |
| medium red onions, quartered through stem end | 1 |
| medium red onions, rough chopped | 1 |
| medium red onions, small dice | 1 |
| medium red onions, thinly sliced | 13 |
| medium red onions, trimmed, leaving root ends intact, and cut lengthwise into 1-inch-wide wedges | 1 |
| medium red onions, very thinly julienned | 1 |
| medium red onions, very thinly sliced | 3 |
| medium red onions, wide around the middle | 1 |
| medium red onions; 1 grated, 1 halved and thinly sliced | 1 |
| medium red or white onion | 1 |
| medium red or white onions (3 1/2 lb) | 1 |
| medium red or yellow onion, quartered and thinly sliced | 1 |
| medium red or yellow onions, quartered | 1 |
| medium round onion | 1 |
| medium shallot or 1/2 small red onion | 2 |
| medium shallots (or 1 small red onion) | 1 |
| medium size onion | 3 |
| medium size red onion | 1 |
| medium size yellow onion | 2 |
| medium sized onion | 5 |
| medium sized onions, quartered | 1 |
| medium sized red onion | 2 |
| medium slice yellow onion | 1 |
| medium sliced onion | 1 |
| medium slices onion | 2 |
| medium spanish onion | 68 |
| medium spanish onion, cut in 1/2, thinly sliced (3 cups) | 1 |
| medium spanish onion, cut into 1/8-inch dice | 1 |
| medium spanish onion, cut into small dice | 1 |
| medium spanish onion, halved | 1 |
| medium spanish onion, halved and thinly sliced | 5 |
| medium spanish onion, thinly sliced | 1 |
| medium spanish onions (about 12 ounces), cut into large chunks | 1 |
| medium spanish onions, cut into large chunks | 1 |
| medium spanish onions, cut into medium dice | 1 |
| medium spanish onions, quartered | 1 |
| medium spanish or red onion | 1 |
| medium spring onion, thinly sliced | 1 |
| medium spring onions, cleaned and trimmed to 2-inches | 1 |
| medium spring onions, stems cut into 2-inch pieces, bulbs quartered | 1 |
| medium sweet onion | 21 |
| medium sweet onion (1/2 lb), thinly sliced crosswise and separated into rings | 1 |
| medium sweet onion (such as vidalia), thinly sliced | 1 |
| medium sweet onion, cubed | 1 |
| medium sweet onion, cut into 1/2-inch-thick rings | 1 |
| medium sweet onion, cut into 1/4-inch pieces | 1 |
| medium sweet onion, cut into large chunks | 1 |
| medium sweet onion, halved | 1 |
| medium sweet onion, halved and thinly sliced | 1 |
| medium sweet onion, halved lengthwise and thinly sliced crosswise | 1 |
| medium sweet onion, such as vidalia | 5 |
| medium sweet onion, such as vidalia or walla walla, thinly sliced | 1 |
| medium sweet onion, such as vidalia, cut in half | 1 |
| medium sweet onion, such as vidalia, maui, or walla walla, thinly sliced | 1 |
| medium sweet onion, such as vidalia, thinly sliced | 1 |
| medium sweet onion, thinly sliced in rings | 1 |
| medium sweet onion, thinly sliced into rings | 1 |
| medium sweet onion, very finely chopped | 1 |
| medium sweet onions (such as vidalia) | 1 |
| medium sweet onions (vidalia or walla walla, for example), thinly sliced | 1 |
| medium sweet onions, cut into medium dice | 1 |
| medium sweet onions, such as vidalia | 1 |
| medium sweet onions, such as vidalia, quartered | 1 |
| medium sweet onions, such as vidalia, thinly sliced | 1 |
| medium sweet onions, thinly sliced | 1 |
| medium sweet vidalia onion | 1 |
| medium sweet white onions, thinly sliced | 1 |
| medium sweet yellow onion | 1 |
| medium sweet yellow onion, thinly sliced | 2 |
| medium thinly sliced red onion | 1 |
| medium to large onion | 12 |
| medium to large onion, thinly sliced | 1 |
| medium to large red onion | 2 |
| medium to large white onion | 1 |
| medium to large yellow onion, quartered then thinly sliced | 1 |
| medium to large yellow skinned onion | 1 |
| medium to large yellow skinned onion, thinly sliced | 1 |
| medium unpeeled yellow onion | 1 |
| medium vidalia onion | 16 |
| medium vidalia onion or any sweet variety onion, thinly sliced | 1 |
| medium vidalia onion, julienned | 1 |
| medium vidalia onion, quartered | 1 |
| medium vidalia onion, small dice | 2 |
| medium vidalia onion, small dice (about 1 1/2 cups) | 1 |
| medium vidalia onion, thinly sliced | 1 |
| medium vidalia onions or other sweet onions (about 1 pound) | 1 |
| medium vidalia or maui onions (about 1 1/4 pounds total), very thinly sliced on a mandoline (about 3 packed cups) | 1 |
| medium vidalia or other sweet onion | 1 |
| medium vidalia or other sweet onion, thinly sliced | 1 |
| medium vidalia or other sweet onions, cut in 1-inch chunks | 1 |
| medium vidalia or yellow onion | 1 |
| medium vidalia, yellow, or brown onions (about 2) | 1 |
| medium white onion | 124 |
| medium white onion (about 7 ounces), cut into 1/4-inch cubes | 1 |
| medium white onion (about 8 ounces), halved lengthwise, thinly sliced | 1 |
| medium white onion chopped | 1 |
| medium white onion cut into 1/2-inch dice | 1 |
| medium white onion, (about 2 cups), trimmed and cut into small dice | 1 |
| medium white onion, chunked into 1/2-inch pieces | 1 |
| medium white onion, cut into 1-inch chunks | 1 |
| medium white onion, cut into 1/4-inch pieces | 1 |
| medium white onion, cut into 1/4-inch-thick slices | 1 |
| medium white onion, grilled and chopped | 1 |
| medium white onion, halved | 3 |
| medium white onion, halved and thinly sliced | 1 |
| medium white onion, halved, plus 1 onion | 1 |
| medium white onion, halved, thinly sliced | 2 |
| medium white onion, medium dice | 1 |
| medium white onion, quartered | 11 |
| medium white onion, small dice | 1 |
| medium white onion, thickly sliced | 1 |
| medium white onion, thinly sliced | 10 |
| medium white onion, very thinly sliced | 1 |
| medium white onion, very thinly sliced and soaked in ice water for 20 minutes | 1 |
| medium white onions, cut into 1/2-inch slices | 1 |
| medium white onions, each cut into 6 wedges with some root attached | 1 |
| medium white onions, thickly sliced | 1 |
| medium white onions, thinly sliced, or a combination of onions and fennel bulbs (about 3 cups) | 1 |
| medium white onions, unpeeled | 1 |
| medium white or yellow onion | 3 |
| medium white spanish onion, thinly sliced | 1 |
| medium yellow medium onion | 1 |
| medium yellow onion | 281 |
| medium yellow onion (about 6 ounces) | 1 |
| medium yellow onion (about 8 ounces) | 2 |
| medium yellow onion (about 8 ounces) cut into 1/4-inch thick rings | 1 |
| medium yellow onion chopped | 1 |
| medium yellow onion cut into 1/4-inch dice | 1 |
| medium yellow onion diced | 1 |
| medium yellow onion, 1 peeled | 2 |
| medium yellow onion, 1/2 grated and 1/2 thinly sliced | 1 |
| medium yellow onion, cut from root to tip into 1/4-inch-thick slices | 1 |
| medium yellow onion, cut in small dice | 1 |
| medium yellow onion, cut into 1-inch-thick rings or strips | 1 |
| medium yellow onion, cut into chunks | 1 |
| medium yellow onion, frenched | 1 |
| medium yellow onion, halved | 1 |
| medium yellow onion, halved and thinluy sliced | 1 |
| medium yellow onion, halved and thinly sliced | 2 |
| medium yellow onion, halved and very finely chopped | 1 |
| medium yellow onion, halved lengthwise and thinly sliced | 1 |
| medium yellow onion, julienned and sauteed | 1 |
| medium yellow onion, quartered | 4 |
| medium yellow onion, quartered (about 1 cup) | 1 |
| medium yellow onion, quartered and very thinly sliced (about 3 cups) | 1 |
| medium yellow onion, quartered lengthwise, root end intact | 1 |
| medium yellow onion, quartered, plus 1/2 yellow onion, thinly sliced | 1 |
| medium yellow onion, rough chopped | 1 |
| medium yellow onion, small dice | 4 |
| medium yellow onion, small-diced | 1 |
| medium yellow onion, thinly sliced | 22 |
| medium yellow onion, thinly sliced (about 4 ounces) | 1 |
| medium yellow onion, thinly sliced into half moons | 1 |
| medium yellow onions (1 cup) finely chopped (not minced) | 1 |
| medium yellow onions diced | 1 |
| medium yellow onions or sweet onions, when available | 1 |
| medium yellow onions, cut into 1 inch pieces | 1 |
| medium yellow onions, cut into 1-inch pieces | 1 |
| medium yellow onions, cut into 1/4-inch slices | 1 |
| medium yellow onions, cut into eighths | 1 |
| medium yellow onions, cut into quarters | 1 |
| medium yellow onions, cut into thin wedges with root end attached | 1 |
| medium yellow onions, either sliced with the grain in 1/2-inch-thick pieces (if using as an accompaniment to meat) or cut into 12 wedges, with the root ends intact to keep the wedges together (if using as a main fajita filling) | 1 |
| medium yellow onions, ends removed | 1 |
| medium yellow onions, halved | 1 |
| medium yellow onions, halved and sliced | 2 |
| medium yellow onions, halved and sliced (3 to 4 cups) | 1 |
| medium yellow onions, halved and thinly sliced | 1 |
| medium yellow onions, julienned | 1 |
| medium yellow onions, left unpeeled, then trimmedand halved | 1 |
| medium yellow onions, left unpeeled, trimmed and halved | 1 |
| medium yellow onions, left unpeeled, trimmed and quartered | 1 |
| medium yellow onions, quartered | 4 |
| medium yellow onions, quartered and sliced | 1 |
| medium yellow onions, quartered and thinly sliced crosswise | 1 |
| medium yellow onions, quartered lengthwise | 1 |
| medium yellow onions, small dice (about 2 1/2 cups) | 2 |
| medium yellow onions, thinly sliced | 9 |
| medium yellow onions, thinly sliced (about 14 cups) | 1 |
| medium yellow onions, trimmed, leaving root ends intact, and cut lengthwise into 1-inch-wide wedges | 1 |
| medium yellow onions, unpeeled | 1 |
| medium yellow or red onion | 1 |
| medium yellow or white onion | 1 |
| medium yellow skinned onion | 12 |
| medium yellow skinned onion, thinly sliced | 1 |
| medium yellow skinned onion, thinly sliced lengthwise, reserve 1/4 of a piece, uncut | 1 |
| medium yellow skinned onions, 1 finely chopped | 1 |
| medium yellow spanish onion | 1 |
| medium yellow-skinned spanish onion, cut into thin strips | 1 |
| medium(1 1/2 cups chopped) onion | 1 |
| medium-dice mixed carrots, celery and onion | 3 |
| medium-diced onion | 6 |
| medium-diced yellow onion (1 onion) | 1 |
| medium-diced yellow onion (2 large) | 1 |
| medium-diced yellow onion (2 onions) | 3 |
| medium-large onion | 7 |
| medium-large onion chopped | 1 |
| medium-large onion, cut into medium dice | 1 |
| medium-large onion, halved lengthwise and sliced thin | 1 |
| medium-large onion, thinly sliced | 1 |
| medium-large onions, thinly sliced | 1 |
| medium-large red onion | 2 |
| medium-large red onions, thinly sliced (about 2 pounds) | 1 |
| medium-large sweet onions, about 1/2 each (such as vidalia, walla walla, maui, texas sweet) | 1 |
| medium-size cooking onion | 1 |
| medium-size onion | 13 |
| medium-size onion, cut into 8 thin wedges | 1 |
| medium-size onion, halved and sliced | 1 |
| medium-size onions, halved and thinly sliced | 1 |
| medium-size onions, thickly sliced | 1 |
| medium-size red onion | 10 |
| medium-size red onion, cut into 1/4-inch-thick rounds | 1 |
| medium-size red onion, cut into paper-thin slices | 1 |
| medium-size red onion, cut into thin wedges | 1 |
| medium-size red onion, cut lengthwise into 1/3-inch-thick slices | 1 |
| medium-size red onion, halved, thinly sliced lengthwise | 1 |
| medium-size red onion, thinly sliced | 2 |
| medium-size red onion, thinly sliced (2 cups) | 1 |
| medium-size red onion, thinly sliced (about 2 cups) | 1 |
| medium-size red onion, thinly sliced into rounds | 1 |
| medium-size red onion, very thinly sliced | 1 |
| medium-size spanish onion, halved and sliced | 1 |
| medium-size sweet onion | 2 |
| medium-size sweet onion (such as vidalia or maui), thinly sliced | 1 |
| medium-size sweet onions (such as maui), cut into 1/2-inch-wide slices | 1 |
| medium-size sweet onions (such as vidalia or maui), halved, thinly sliced | 1 |
| medium-size white onion | 2 |
| medium-size white onion, thickly sliced | 1 |
| medium-size yellow onion | 4 |
| medium-size yellow onion, halved and thinly sliced (2 cups) | 1 |
| medium-size yellow onions 4 sprigs fresh or 1 tablespoon dried rosemary | 1 |
| medium-sized onion | 11 |
| medium-sized onion, halved | 1 |
| medium-sized onion, unpeeled, studded with 4 whole clove | 1 |
| medium-sized onions (1 coarsely chopped, 1 for garnishing) | 1 |
| medium-sized onions, each coarsely chopped but kept separate | 1 |
| medium-sized red onion | 4 |
| medium-sized red onion, thinly sliced | 1 |
| medium-sized vidalia onions, thinly sliced | 1 |
| medium-sized white onion | 1 |
| medium-sized white onion, medium dice | 1 |
| medium-sized white onion, small dice | 1 |
| medium-sized yellow onion, thinly sliced | 1 |
| medium-sized yellow onion, very finely chopped (about 1/2 cup) | 1 |
| medium-small onion, cut in half and thinly sliced | 1 |
| medium-sweet organic onions, unpeeled | 1 |
| mexican scallions (like small spring onions) | 1 |
| minced (onions, various colored bell peppers) | 1 |
| minced chives or green onion | 2 |
| minced chives or onion | 2 |
| minced fresh chives or green onion | 1 |
| minced fresh chives or green onion tops | 2 |
| minced fresh onion | 7 |
| minced green onion | 93 |
| minced green onion (garnish) | 1 |
| minced green onion (including green tops) | 1 |
| minced green onion (white and pale green parts only) | 1 |
| minced green onion (white part only) | 1 |
| minced green onion tops | 2 |
| minced green onion, for garnish | 1 |
| minced green onion, or to taste | 1 |
| minced green onion, plus 1/4 cup | 1 |
| minced green onion, to garnish | 1 |
| minced green onion, white and light green part only | 1 |
| minced green onions (about 3) | 1 |
| minced green onions (optional) | 1 |
| minced green onions (scallions) | 1 |
| minced green onions with tops | 1 |
| minced green onions, for garnish | 2 |
| minced green onions, green and white parts | 1 |
| minced green onions, plus some for garnish | 1 |
| minced green onions, with tops | 1 |
| minced maui onion (sweet onion) | 1 |
| minced maui onion or other sweet onion | 1 |
| minced onion | 546 |
| minced onion (1 small) | 1 |
| minced onion (about 1 medium) | 1 |
| minced onion (about 1/2 small onion) | 1 |
| minced onion (optional) | 1 |
| minced onion flakes | 2 |
| minced onion or onion powder | 1 |
| minced onion, celery and carrot (mix together) | 2 |
| minced onion, or more to taste | 1 |
| minced onion, or to taste | 2 |
| minced or grated onion | 1 |
| minced organic spring onion | 1 |
| minced raw onion | 1 |
| minced raw onion, for garnish | 1 |
| minced red onion | 176 |
| minced red onion (1 onion) | 1 |
| minced red onion (about 1/2 medium onion) | 1 |
| minced red onion (optional) | 2 |
| minced red onion cannellini beans, drained | 1 |
| minced red onion or shallot | 1 |
| minced red onion plus additional for garnish | 1 |
| minced red onion, soaked in cold water for 5 minutes and drained | 4 |
| minced red onion, soaked in cold water for 5 minutes, drained | 2 |
| minced red onions, for serving | 1 |
| minced scallions or green onion | 4 |
| minced shallot or onion | 4 |
| minced shallot or red onion | 4 |
| minced shallots or green onion | 2 |
| minced shallots or onion | 1 |
| minced shallots or red onion | 2 |
| minced spanish onion | 4 |
| minced sweet onion | 11 |
| minced sweet white onion | 1 |
| minced texas yellow onion | 1 |
| minced vidalia onion | 1 |
| minced white onion | 34 |
| minced white onion, rinsed, drained | 1 |
| minced whole green onion | 1 |
| minced yellow onion | 41 |
| minced yellow or white onion | 1 |
| minces onion | 1 |
| mirepoix (1 small diced onion, 1/2 cup small diced carrots, 1/2 cup small diced celery) | 1 |
| mirepoix (carrots, onions, celery, leeks) small dice | 1 |
| mirepoix (diced celery, carrot and onion) | 1 |
| mirepoix (diced celery, carrots and onion) | 1 |
| mirepoix (equal parts chopped celery, carrots and onions) | 1 |
| mirepoix (mix of chopped celery, onions, and carrots) | 1 |
| mirepoix (onion, carrot, and celery) | 2 |
| mirepoix, small dice carrots, celery and onion | 1 |
| mix-ins of your choice, such as sauteed onions, crumbled feta or chopped smoked salmon | 1 |
| mixed chopped seasonal fresh vegetables, such as squash, broccoli, cauliflower, zucchini, red onion, tomato, and carrot | 1 |
| mixed colorful vegetables (such as spring onions, radishes, rainbow baby carrots and asparagus), halved lengthwise if thick | 1 |
| mixed cut-up vegetables (such as bell peppers, broccoli florets, onion, mushrooms and cauliflower florets) | 1 |
| mixed grilled vegetables, 1/2-inch dice (1 zucchini, 1 eggplant, 1 red bell pepper, 1 large red onion, 1 fennel, 1/4-inch thick sliced and grilled with olive oil, salt and pepper) | 1 |
| mixed pickled vegetables: carrot, cauliflower, cornichon, onion, and celery root | 1 |
| mixed roughly chopped carrots and onion | 1 |
| mixed scallion, garlic and onion | 1 |
| mixed small and medium onions (such as vidalia or yellow) | 1 |
| mixed sweet onions, large shallots, baby leeks, and green onion | 1 |
| mixed winter vegetables such as carrots, brussels sprouts, rutabagas, turnips, onions, leeks or savoy cabbage | 1 |
| mop the meat a couple of times on either side with a mix of water, butter, onion, worcestershire sauce, and dry mustard | 1 |
| mrs. dash® onion and herb seasoning blend | 1 |
| mushroom and onions, reserved from mushroom walnut tarts | 1 |
| mushroom onion gravy, recipe follows | 1 |
| mushrooms, quartered 3 onion | 1 |
| negi (long green onion), white part only | 1 |
| new onions (1 inch in diameter), trimmed, or 1/2 pound boiling onion | 1 |
| nigella (black onion seed) | 1 |
| nigella seeds (also called black onion seeds) | 1 |
| nigella seeds (also called kalonji or black onion seeds) | 1 |
| nigella seeds (sometimes mislabeled "black onion seeds") or caraway seeds for garnish | 1 |
| nigella seeds* (sometimes called black onion seeds) | 1 |
| of a fist-sized white onion | 1 |
| of a large white onion, cut into large chunks | 1 |
| of a medium yellow onion | 1 |
| of a red onion | 2 |
| of a small red onion | 1 |
| of a small red onion, thinly sliced | 2 |
| of any combination sauteed peppers and onion | 1 |
| of chopped onion | 1 |
| of chopped red onion | 1 |
| of diced onion | 2 |
| of finely chopped green onion | 2 |
| of finely chopped onion | 1 |
| of green onion | 3 |
| of green onions, cut into 1-inch lengths | 1 |
| of green onions, white parts only, plus more for garnish | 1 |
| of hand chopped onions (chunky) | 1 |
| of minced onion | 2 |
| of onion | 1 |
| of onion (1/4 inch dice) | 1 |
| of onion (chop 1/4 inch dice) | 1 |
| of red onion | 1 |
| of red onions, small diced | 1 |
| of sliced white onion | 2 |
| of thinly sliced yellow onion | 1 |
| of white onion, thinly sliced | 2 |
| okra, onion and tomato stew, recipe follows | 1 |
| olive oil (to saute white onion) | 1 |
| olive oil 1 small onion | 1 |
| olive oil for brushing on onion and avocado | 1 |
| olive oil for brushing onion | 1 |
| olive oil, enough to sauté garlic and onion | 1 |
| olive oil, for sauteing the onion | 1 |
| olive oil, plus extra for brushing the potatoes and green onion | 1 |
| olive or canola oil, for boiling potatoes and cooking onion | 1 |
| one 1-ounce packet onion soup mix (recommended: lipton) | 2 |
| one 10-ounce bag frozen roasted peppers and onion | 1 |
| one 10-ounce box frozen pearl onions, defrosted | 1 |
| one 10-ounce can diced tomatoes and onions with lime juice and cilantro | 2 |
| one 12-ounce bag frozen onion | 2 |
| one 14-ounce bag frozen fire-roasted or charred onions and pepper | 1 |
| one 14-ounce bag frozen pearl onions, thawed | 1 |
| one 14-ounce package frozen pearl onion | 1 |
| one 15-ounce can french onion soup | 2 |
| one 16-ounce bag frozen pearl onions, thawed | 3 |
| one 16-ounce jar onion-stuffed olives | 1 |
| one 16-ounce package frozen onion rings | 1 |
| one 2.8-ounce can french fried onions (about 1 1/4 cups) | 1 |
| one 3-ounce jar pickled pearl onions, drained | 1 |
| one 6-ounce can french-fried onions, crushed | 2 |
| one large yellow onion | 1 |
| one medium onion | 1 |
| onion | 5,309 |
| onion (1/4 grated, 3/4 chopped) | 1 |
| onion (about 1/2 pound) | 2 |
| onion (nigella) seeds | 1 |
| onion (not peeled), quartered | 1 |
| onion ,halved | 1 |
| onion and chive-flavored whipped cream cheese | 1 |
| onion and garlic mix | 5 |
| onion and garlic yukon gold potato chips, (preferred brand: terra chips) | 1 |
| onion and garlic-flavored croutons | 1 |
| onion base | 1 |
| onion blossom sauce, recipe follows, for serving | 1 |
| onion buns | 2 |
| onion buns, lightly toasted | 1 |
| onion chopped | 4 |
| onion chopped small | 1 |
| onion cilantro salad: | 1 |
| onion cut into large dice | 1 |
| onion cut into quarters | 3 |
| onion diced | 4 |
| onion diced into 1/4-inch pieces | 1 |
| onion filling, recipe follows | 1 |
| onion finely diced | 2 |
| onion flakes | 7 |
| onion flakes (optional) | 1 |
| onion flakes, for sprinkling | 1 |
| onion flakes, or to taste | 1 |
| onion flavored pita bread pockets | 1 |
| onion granules | 6 |
| onion grass (or chives) finely minced | 1 |
| onion jam, recipe follows | 2 |
| onion jam, recipe follows, for serving | 1 |
| onion jam: | 1 |
| onion juice | 9 |
| onion juice (from 1 grated medium-size onion) | 1 |
| onion juice (optional) | 1 |
| onion kaiser rolls | 1 |
| onion kaiser rolls, split and toasted | 1 |
| onion minced | 1 |
| onion oil | 1 |
| onion oil* | 1 |
| onion or 1 shallot | 1 |
| onion or 2 shallots, very finely sliced | 1 |
| onion or 3 shallots | 1 |
| onion or beef broth | 1 |
| onion or chive blossoms (optional) | 1 |
| onion or fig jam | 1 |
| onion or large shallot | 1 |
| onion peeled and quartered | 1 |
| onion pickling liquid | 1 |
| onion powder | 1,411 |
| onion powder (optional) | 4 |
| onion powder 8 extra-large egg | 1 |
| onion powder or flakes | 6 |
| onion powder teaspoon garlic powder | 1 |
| onion powder to taste | 12 |
| onion powder to taste (optional) | 1 |
| onion powder with green onion and parsley | 1 |
| onion powder* | 1 |
| onion powder, 2/3 palmful | 1 |
| onion powder, or 1/4 small onion | 1 |
| onion powder, or more to taste | 5 |
| onion powder, or to taste | 19 |
| onion powder, or to taste (optional) | 1 |
| onion powder, plus more for seasoning tomato | 1 |
| onion power | 1 |
| onion puree (2 tablespoons olive oil, 1 onion, very thinly sliced, 1 tablespoon sherry vinegar, salt & pepper) | 1 |
| onion relish, recipe follows | 2 |
| onion rings, for topping | 2 |
| onion roll | 1 |
| onion roll, split | 1 |
| onion rolls | 4 |
| onion rolls or hamburger buns | 1 |
| onion rolls or hamburger buns, split | 1 |
| onion rolls or sesame-seed hamburger buns, split | 1 |
| onion rolls, buttered and toasted until golden | 1 |
| onion rolls, halved | 3 |
| onion rolls, halved horizontally | 1 |
| onion rolls, split | 3 |
| onion rolls, split, buttered and griddled | 1 |
| onion rolls, toasted | 2 |
| onion roughly chopped | 3 |
| onion salt | 88 |
| onion salt to taste | 2 |
| onion salt to taste (optional) | 1 |
| onion salt, or to taste | 6 |
| onion sauce | 1 |
| onion sauce, recipe follows | 1 |
| onion seeds (kalonji) | 1 |
| onion skins | 1 |
| onion sliced | 3 |
| onion slices | 6 |
| onion slices (1/2 inch thick) | 1 |
| onion slices from 2 large onions, 2/3-inch thick | 1 |
| onion slices, separated into rings | 1 |
| onion small diced | 1 |
| onion soup mix | 8 |
| onion soup, prepared from a packet of dry onion soup mix | 1 |
| onion sprouts or garlic chive sprouts (2 cups) | 1 |
| onion sprouts, for garnish | 1 |
| onion straws, recipe follows | 1 |
| onion stuck with 2 clove | 2 |
| onion studded with 1 clove | 1 |
| onion thinly sliced | 1 |
| onion wedge | 1 |
| onion wedge, studded with clove | 1 |
| onion whole, with a bay leaf attached with 2 clove | 1 |
| onion yellow | 1 |
| onion, 1 half left intact, the other chopped | 1 |
| onion, 1/2 diced, 1/2 cut into wedges | 1 |
| onion, 1/2-inch diced | 1 |
| onion, 1/3 thinly sliced, remaining finely chopped | 1 |
| onion, 1/4 dice | 1 |
| onion, 1/4-inch dice | 3 |
| onion, about 1/3 pound | 1 |
| onion, about 2 small | 1 |
| onion, brunoise | 1 |
| onion, caramelized | 1 |
| onion, carrot and celery, each finely chopped | 1 |
| onion, chunked | 3 |
| onion, cleaned and sliced thin, then roughly chopped | 1 |
| onion, cubed | 2 |
| onion, cut crosswise into 1/4-inch-thick slices | 1 |
| onion, cut in half | 8 |
| onion, cut in half and sliced | 1 |
| onion, cut in half and stuck with 2 clove | 1 |
| onion, cut in large dice | 1 |
| onion, cut in rings | 1 |
| onion, cut in small dice | 1 |
| onion, cut into 1 inch pieces | 1 |
| onion, cut into 1-inch chunks | 2 |
| onion, cut into 1-inch cubes | 3 |
| onion, cut into 1-inch dice | 1 |
| onion, cut into 1-inch pieces | 8 |
| onion, cut into 1-inch squares | 1 |
| onion, cut into 1/2-inch dice | 4 |
| onion, cut into 1/2-inch pieces | 4 |
| onion, cut into 1/2-inch slices | 1 |
| onion, cut into 1/2-inch-thick wedges | 1 |
| onion, cut into 1/4 inch dice | 1 |
| onion, cut into 1/4-inch chunks | 1 |
| onion, cut into 1/4-inch dice | 13 |
| onion, cut into 1/4-inch slices | 5 |
| onion, cut into 1/4-inch slices and separated into rings | 1 |
| onion, cut into 1/4-inch strips | 1 |
| onion, cut into 1/4-inch thick rings | 1 |
| onion, cut into 1/8-inch julienne strips | 1 |
| onion, cut into 2 inch pieces | 1 |
| onion, cut into 2-inch pieces | 1 |
| onion, cut into 3/4 inch squares | 2 |
| onion, cut into 3/4-inch pieces | 2 |
| onion, cut into 4 wedges | 1 |
| onion, cut into 6 wedges | 2 |
| onion, cut into 8 pieces, layers separated | 1 |
| onion, cut into 8 wedges | 3 |
| onion, cut into bite-size pieces | 3 |
| onion, cut into chunks | 27 |
| onion, cut into chunks, or to taste | 1 |
| onion, cut into eighths | 1 |
| onion, cut into half-moon slices | 1 |
| onion, cut into large chunks | 3 |
| onion, cut into large dice | 4 |
| onion, cut into large slices | 1 |
| onion, cut into matchstick-size pieces | 2 |
| onion, cut into matchstick-sized pieces | 1 |
| onion, cut into medium dice | 2 |
| onion, cut into noodle shapes | 1 |
| onion, cut into quarters | 3 |
| onion, cut into rings | 2 |
| onion, cut into rings (optional) | 1 |
| onion, cut into slices and separated | 1 |
| onion, cut into small dice | 8 |
| onion, cut into small pieces | 1 |
| onion, cut into strips | 5 |
| onion, cut into thick slices | 2 |
| onion, cut into thick wedges | 1 |
| onion, cut into thin julienne | 1 |
| onion, cut into thin rounds | 1 |
| onion, cut into thin slivers | 2 |
| onion, cut into thin strips | 3 |
| onion, cut into thin wedges | 3 |
| onion, cut into very thin slices | 1 |
| onion, cut into wedges | 14 |
| onion, cut into wedges and separated | 1 |
| onion, cut julienne | 1 |
| onion, cut julienne style | 1 |
| onion, cut lengthwise in half, then sliced crosswise | 1 |
| onion, cut thinly | 1 |
| onion, dice small | 1 |
| onion, granulated | 1 |
| onion, grilled | 1 |
| onion, halved | 30 |
| onion, halved (skin on) | 1 |
| onion, halved - unpeeled | 1 |
| onion, halved and cut into 1/4-inch slices | 1 |
| onion, halved and each half cut into quarters | 1 |
| onion, halved and sliced | 11 |
| onion, halved and sliced into rings | 1 |
| onion, halved and thickly sliced | 1 |
| onion, halved and thinly sliced | 18 |
| onion, halved and thinly sliced - divided | 1 |
| onion, halved lengthwise and sliced thin crosswise | 2 |
| onion, halved lengthwise and sliced thin lengthwise | 1 |
| onion, halved lengthwise, cut into thin wedges | 1 |
| onion, halved or quarter | 1 |
| onion, halved, but not peeled | 1 |
| onion, halved, plus 1 onion | 1 |
| onion, halved, skin on | 1 |
| onion, halved, thinly sliced | 2 |
| onion, julienne | 5 |
| onion, julienned | 21 |
| onion, large | 1 |
| onion, large dice | 3 |
| onion, large, cut into eighths (about 1/2 pound) | 1 |
| onion, left unpeeled, quartered | 3 |
| onion, medium dice | 6 |
| onion, medium diced | 1 |
| onion, poked with 2 clove | 1 |
| onion, preferably vidalia | 1 |
| onion, pulverized like an onion smoothie | 1 |
| onion, quarterd | 1 |
| onion, quartered | 118 |
| onion, quartered and sliced | 1 |
| onion, quartered and then quarters halved crosswise | 1 |
| onion, quartered and thinly sliced | 2 |
| onion, quartered and very thinly sliced | 1 |
| onion, quartered lengthwise | 2 |
| onion, quartered lengthwise and then sliced | 1 |
| onion, quartered lengthwise then thinly sliced | 1 |
| onion, quartered then halved | 2 |
| onion, quartered then sliced | 1 |
| onion, quartered then thinly sliced | 1 |
| onion, quartered through root end | 1 |
| onion, quartered, cut crosswise into 1/4" slices | 1 |
| onion, quartered, root end attached | 2 |
| onion, quartered, thinly sliced | 1 |
| onion, quartered, with a bay leaf attached with a clove | 1 |
| onion, red (grilled if you like) | 1 |
| onion, roasted and chopped | 1 |
| onion, root end attached and sliced into thin wedges | 1 |
| onion, rough chopped | 2 |
| onion, shredded | 5 |
| onion, skin on | 1 |
| onion, skin on, halved and quartered | 1 |
| onion, slivered | 1 |
| onion, small dice | 11 |
| onion, small diced | 5 |
| onion, spiked with 2 cloves and 1bay leaf | 1 |
| onion, thickly sliced | 2 |
| onion, thinly sliced | 208 |
| onion, thinly sliced (optional) | 1 |
| onion, thinly sliced across the width | 1 |
| onion, thinly sliced and divided | 1 |
| onion, thinly sliced into rings | 1 |
| onion, thinly sliced lengthwise | 1 |
| onion, tomato, and cucumber slices, for garnish | 1 |
| onion, trimmed | 1 |
| onion, trimmed and minced | 1 |
| onion, unchopped | 1 |
| onion, unpeeled, quartered | 2 |
| onion, vertically sliced | 1 |
| onion, very finely chopped | 4 |
| onion, very thinly sliced | 2 |
| onion, whole | 1 |
| onion-and garlic-seasoned croutons | 1 |
| onion-flavored soy crisps, crushed | 1 |
| onions (2 large) | 1 |
| onions (2 large), halved and thinly sliced | 1 |
| onions (2 large), halved lengthwise and thinly sliced | 1 |
| onions (2 medium) | 1 |
| onions (2 pounds), cut into 1/4-inch dice | 1 |
| onions (2 to 3 medium onions), thinly sliced | 1 |
| onions (3 large), thinly sliced | 1 |
| onions (3 medium), halved lengthwise, then thinly sliced crosswise | 1 |
| onions (4 to 6 medium), halved lengthwise and thinly sliced | 1 |
| onions (5 or 6 medium), halved lengthwise, then cut lengthwise into 1/4-inch-thick slices | 2 |
| onions (6 to 8 medium) | 1 |
| onions (6 to 8 medium), halved lengthwise, then thinly sliced lengthwise | 1 |
| onions (about 1 1/2 pounds total) | 1 |
| onions (about 1 pound) | 1 |
| onions (about 1 pound), thinly sliced | 1 |
| onions (about 2 large) | 1 |
| onions (about 2 medium), cut into 1/3-inch-thick wedges through root ends | 1 |
| onions (about 3 medium) | 2 |
| onions (about 3 medium), thinly sliced | 1 |
| onions (large) | 1 |
| onions (left unpeeled), quartered | 1 |
| onions (red, white, and yellow, making sure at least one onion is of a sweet variety such as vidalia or maui), thinly sliced | 1 |
| onions (small diced) | 1 |
| onions (yellow or white) | 1 |
| onions chopped | 3 |
| onions chopped fine | 1 |
| onions chopped, about 1 1/2 cups | 1 |
| onions cut into 16 pieces | 1 |
| onions finely chopped | 1 |
| onions finely diced | 1 |
| onions or scallion | 1 |
| onions or shallots, thinly sliced | 1 |
| onions quartered | 1 |
| onions quartered and not peeled | 1 |
| onions sliced | 2 |
| onions, (2 pounds) | 1 |
| onions, 1 chopped, 1 thinly sliced | 1 |
| onions, 1 diced, 1 left whole | 1 |
| onions, 1 diced, 1 sliced | 1 |
| onions, 1 inch dice | 1 |
| onions, 1 peeled and sliced, 1 cut in 1/2 with the skin-on | 1 |
| onions, 1 quartered and thinly sliced, 1 chopped | 1 |
| onions, 1 quartered at the root end and 1 chopped | 1 |
| onions, 1 sliced and 1 minced | 1 |
| onions, 1/2 peeled, 1 1/2 chopped | 1 |
| onions, 1/4-inch dice | 2 |
| onions, 2 ounces each, quartered and petals separated | 1 |
| onions, caramelized | 1 |
| onions, carrots and celery cut into 3 to 4-inch pieces | 1 |
| onions, cut crosswise into thin slices and separated into rings | 1 |
| onions, cut in 1/2 lengthwise and sliced thinly | 1 |
| onions, cut in half | 1 |
| onions, cut in wedges | 1 |
| onions, cut into 1-inch dice | 1 |
| onions, cut into 1-inch pieces | 4 |
| onions, cut into 1-inch thick slices | 1 |
| onions, cut into 1/2-inch pieces | 1 |
| onions, cut into 1/2-inch slices | 1 |
| onions, cut into 1/2-inch-thick slices | 1 |
| onions, cut into 1/3-inch slices | 1 |
| onions, cut into 1/4 inch thick slices | 3 |
| onions, cut into 1/4-inch-thick rounds | 1 |
| onions, cut into 1/4-inch-thick slices | 1 |
| onions, cut into 2 inch pieces | 1 |
| onions, cut into 2-inch chunks | 1 |
| onions, cut into 3 slices each, plus 2 onions diced | 1 |
| onions, cut into 3/4- to 1-inch pieces | 1 |
| onions, cut into 3/4-inch pieces | 1 |
| onions, cut into 8 wedges | 1 |
| onions, cut into 8 wedges each | 1 |
| onions, cut into bite-size pieces | 2 |
| onions, cut into chunks | 8 |
| onions, cut into fine dice | 1 |
| onions, cut into half | 1 |
| onions, cut into large chunks | 6 |
| onions, cut into large dice | 1 |
| onions, cut into large pieces | 1 |
| onions, cut into quarters | 1 |
| onions, cut into rings | 1 |
| onions, cut into thin rings | 2 |
| onions, cut into thin wedges, root end attached | 1 |
| onions, cut into very thin rings | 1 |
| onions, cut into wedges | 4 |
| onions, cut into wedges and sliced | 1 |
| onions, cut into wedges with root end attached | 2 |
| onions, cut into wedges, root end attached | 1 |
| onions, cut into wide slices | 1 |
| onions, cut lengthwise into 1/4-inch strips | 1 |
| onions, each studded with 3 whole clove | 1 |
| onions, for grilling | 1 |
| onions, for serving | 1 |
| onions, ground | 2 |
| onions, halved | 13 |
| onions, halved (use skins too, if clean) | 1 |
| onions, halved and bruleed (cut sides seared in a hot skillet) | 1 |
| onions, halved and cut into thin slices | 1 |
| onions, halved and sliced | 3 |
| onions, halved and sliced into strips | 1 |
| onions, halved and thinly sliced | 5 |
| onions, halved but not peeled | 1 |
| onions, halved crosswise | 1 |
| onions, halved lengthwise | 1 |
| onions, halved lengthwise and cut crosswise into 1/2-inch-thick slices | 1 |
| onions, halved lengthwise and cut crosswise into 1/4 inch slices | 1 |
| onions, halved lengthwise and cut crosswise into 1/4-inch slices | 1 |
| onions, halved lengthwise and sliced thin | 2 |
| onions, halved lengthwise and thinly sliced | 1 |
| onions, halved lengthwise and thinly sliced lengthwise (6 cups) | 1 |
| onions, halved lengthwise, then thinly sliced lengthwise (6 cups) | 1 |
| onions, halved lengthwise, thinly sliced crosswise (about 6 cups) | 1 |
| onions, halved lengthwise, thinly sliced crosswise (about 7 cups) | 1 |
| onions, halved through the root end and thinly sliced, core still attached | 1 |
| onions, halved, cut into 1/4-inch-thick slices | 1 |
| onions, halved, thinly sliced | 3 |
| onions, julienne | 2 |
| onions, julienned | 1 |
| onions, julienned, caramelized | 1 |
| onions, large | 1 |
| onions, left unpeeled, quartered | 1 |
| onions, medium chop | 2 |
| onions, medium chopped | 1 |
| onions, medium dice | 3 |
| onions, medium diced | 2 |
| onions, medium sized, tips removed, skin left on and cut in half widthwise | 1 |
| onions, pearl | 1 |
| onions, preferably vidalia, quartered | 1 |
| onions, quartered | 45 |
| onions, quartered and left unpeeled | 1 |
| onions, quartered and roasted | 1 |
| onions, quartered and thinly sliced | 1 |
| onions, quartered, peels still on | 1 |
| onions, roasted | 1 |
| onions, rough chopped | 1 |
| onions, shallots and garlic | 1 |
| onions, shaved (use a mandoline or a very sharp knife to make the thinnest possible slices) | 1 |
| onions, shredded | 1 |
| onions, small dice | 2 |
| onions, spring or scallions (includes tops and bulb) | 1 |
| onions, stuck with clove | 1 |
| onions, thickly sliced | 6 |
| onions, thinly shaved | 1 |
| onions, thinly sliced | 93 |
| onions, thinly sliced (about 4 cups) | 1 |
| onions, thinly sliced into rounds | 1 |
| onions, thinly sliced kosher salt and freshly ground pepper | 1 |
| onions, thinly sliced root to tip | 1 |
| onions, trimmed and sliced on the slant | 1 |
| onions, unpeeled and chopped | 1 |
| onions, unpeeled and cut in wedges | 1 |
| onions, unpeeled, ends removed | 1 |
| onions, very finely chopped | 1 |
| onions, very thinly sliced | 6 |
| onions, very thinly sliced (4 cups) | 1 |
| onions, whole | 2 |
| onions, with skins | 1 |
| optional additions: pearl onions and lettuce, freshly chopped tarragon, chives, mint, parsley, soaked and chopped dried wild mushrooms or chopped prosciutto | 1 |
| optional garnish: cucumber and red onion salad (recipe follows | 1 |
| optional toppings: lettuce, onion, tomato, salsa, cheese, avocado | 1 |
| or 1/2 (if very large) walla walla onion | 1 |
| or 2 medium onions, trimmed | 1 |
| or 2 onion slices | 1 |
| or 3 large onions, thinly slivered | 1 |
| or 3 medium onions, whole | 1 |
| or 4 thinly sliced green onions, green parts only | 1 |
| or 5 green onion | 1 |
| or 5 large onions, halved and thinly sliced (use the slicing blade on your food processor, or a mandoline if you have one) | 1 |
| organic grilled sweet onion | 1 |
| organic onion buns | 1 |
| package beef with onion soup mix | 4 |
| package chive and onion-flavored goat cheese | 1 |
| package dry french onion soup mix | 1 |
| package dry onion and mushroom soup mix | 3 |
| package dry onion soup mix | 105 |
| package dry onion soup mix (optional) | 1 |
| package dry onion soup mix (such as lipton®) | 11 |
| package dry onion soup mix, or more to taste | 1 |
| package dry onion soup mix, or to taste | 1 |
| package french onion dip | 1 |
| package french onion soup mix | 2 |
| package french-fried onion | 2 |
| package frozen bell pepper and onion mix, thawed | 1 |
| package frozen bell peppers with onion | 1 |
| package frozen chopped bell peppers and onion | 1 |
| package frozen chopped onion | 1 |
| package frozen chopped onions, thawed and squeezed | 1 |
| package frozen diced potatoes (hash browns) with onions and peppers, thawed | 1 |
| package frozen green bell peppers and onion | 1 |
| package frozen green, red and yellow peppers and onions* | 1 |
| package frozen pearl onion | 1 |
| package frozen pearl onions or small whole white onion | 1 |
| package frozen pearl onions, thawed | 1 |
| package frozen peas and onions, thawed | 1 |
| package frozen pepper and onion stir fry mix | 1 |
| package frozen pepper and onion stir fry vegetable blend | 1 |
| package frozen pepper and onion stir-fry blend | 1 |
| package frozen vegetable blend (peppers, onions, celery, and parsley) | 1 |
| package frozen, breaded onion rings | 1 |
| package mccormick® french onion dip seasoning mix | 1 |
| package onion dip | 1 |
| package onion soup mix | 6 |
| package pearl onion | 1 |
| package prepared french onion dip | 1 |
| package simply potatoes® diced potatoes with onion | 1 |
| package sour cream and onion dip | 1 |
| packaged french-fried onion | 1 |
| packaged fried onions (recommended: french's) | 1 |
| packaged fried shallots or onion | 2 |
| packages beef with onion soup mix | 1 |
| packages dry onion soup mix | 19 |
| packages fresh pearl onion | 1 |
| packages simply potatoes® diced potatoes with onion | 1 |
| packed thinly sliced onion | 1 |
| packet (0.7-ounce) onion recipe mix, lipton(r) carb options(tm) | 1 |
| packet (1.0-ounce) onion soup mix, lipton | 1 |
| packet beef and onion dry soup mix | 1 |
| packet beefy onion soup mix | 1 |
| packet beefy onion soup mix (recommended: lipton) | 1 |
| packet dried onion soup mix | 1 |
| packet dry french onion soup mix | 1 |
| packet dry onion gravy mix | 1 |
| packet dry onion soup mix | 15 |
| packet dry onion soup mix (such as knorr® french onion soup mix) | 1 |
| packet dry onion soup/dip mix | 1 |
| packet french onion soup mix | 1 |
| packet onion mushroom soup mix | 1 |
| packet onion soup mix | 4 |
| packet onion soup mix (recommended: lipton's) | 1 |
| pan-seared onion and apples, recipe follows | 1 |
| pan-seared rib-eye with french onion confit, for serving | 1 |
| panhandle pepper (recommended: bob tallman's cowboy orange seasoning - gourmet black pepper, garlic, onion, and orange oil) | 1 |
| paper-thin onion slice | 1 |
| paper-thin onion slices | 1 |
| paper-thin red onion slices | 4 |
| paper-thin red onion slices, separated into rings | 2 |
| paper-thin slices red onion | 5 |
| paper-thin slices red onion (optional) | 1 |
| paprika-braised peppers and onion | 1 |
| paprika-braised peppers and onions: | 1 |
| parboiled pearl onions (frozen are fine) | 2 |
| part each ground cumin, crushed red pepper flakes, celery salt, garlic powder, onion powder, dried oregano | 1 |
| part onion powder | 1 |
| pearl onion | 108 |
| pearl onions (5 ounces) | 1 |
| pearl onions (about 1 cup), unpeeled | 2 |
| pearl onions (about 1 inch in diameter) | 1 |
| pearl onions (about 15), blanched in boiling water for 2 minutes, drained, and peeled | 1 |
| pearl onions (about 16) | 1 |
| pearl onions (about 2 1/4 cups) | 1 |
| pearl onions (about 2 cups) | 1 |
| pearl onions (about 2 cups), blanched in boiling water 2 minutes and peeled | 1 |
| pearl onions (about 24) | 2 |
| pearl onions (preferably red; 2 cups) | 1 |
| pearl onions (see note, above) | 1 |
| pearl onions, blanched | 2 |
| pearl onions, blanched 1 minute | 1 |
| pearl onions, blanched and carefully peeled | 2 |
| pearl onions, blanched and peeled | 3 |
| pearl onions, blanched for 2 minutes in boiling water and skins slipped off | 1 |
| pearl onions, blanched in boiling water 1 minute | 1 |
| pearl onions, blanched in boiling water 2 minutes, drained | 1 |
| pearl onions, blanched in boiling water for 1 minute | 2 |
| pearl onions, blanched in boiling water for 1 minute, drained, and peeled | 1 |
| pearl onions, blanched in boiling water for 2 minutes and skins slipped off | 1 |
| pearl onions, blanched in boiling water for 3 minutes, drained, and peeled | 2 |
| pearl onions, boiled | 1 |
| pearl onions, carefully peeled | 1 |
| pearl onions, cleaned | 1 |
| pearl onions, cooked | 2 |
| pearl onions, fresh or frozen | 1 |
| pearl onions, frozen | 1 |
| pearl onions, glazed with sugar | 1 |
| pearl onions, halved | 1 |
| pearl onions, root ends trimmed | 1 |
| pearl onions, thinly sliced | 1 |
| pearl onions, unpeeled | 1 |
| pearl onions. peeled | 1 |
| pearl or cipollini onion | 1 |
| pearl white onion | 1 |
| peeled and chopped (1/4 inch) onion | 1 |
| peeled and chopped onion | 1 |
| peeled and diced onion | 1 |
| peeled and julienned spanish onion | 1 |
| peeled and quartered cipollini onion | 1 |
| peeled and small diced yellow onion (about 1/2 onion) | 1 |
| peeled onions, quartered | 1 |
| peeled onions; 1 halved, 1 chopped (about 2 cups) | 1 |
| peeled pearl onion | 1 |
| peeled pearl onions, thawed if frozen | 1 |
| peeled red pearl onion | 1 |
| peeled small shallots, preferably asian, or very small red onions, halved lengthwise and thinly sliced with the grain (about 1/4 cup, lightly packed) | 1 |
| peeled, halved, and thinly sliced onion | 1 |
| petite-cut diced tomatoes with sweet onions, drained and juice reserved | 1 |
| philadelphia chive & onion 1/3 less fat than cream cheese | 3 |
| philadelphia chive & onion cream cheese product | 1 |
| pickled beets and onion | 1 |
| pickled cippolini onion | 1 |
| pickled cocktail onion | 1 |
| pickled cocktail onions, plus some for garnish | 1 |
| pickled cocktail onions, trimmed and finely chopped | 1 |
| pickled jalapeno peppers (including the onions and carrots from the jar or can) | 1 |
| pickled jalapenos with carrots and onions, drained and chopped, plus 1 tablespoon of the brine | 1 |
| pickled jalapenos, including the carrots and onions that come in the jar | 1 |
| pickled jalapenos, including the onions and carrots that come in the jar or can | 1 |
| pickled onion | 6 |
| pickled onion for garnish | 1 |
| pickled onion slices | 1 |
| pickled onions or chiles or a combination | 1 |
| pickled onions, 14 to 18 ounce jar | 1 |
| pickled onions, for garnish | 2 |
| pickled onions, for serving, recipe follows | 1 |
| pickled onions, for topping | 1 |
| pickled onions, recipe follows | 2 |
| pickled pearl onion | 2 |
| pickled pearl onions, drained | 3 |
| pickled pink onions, recipe follows | 1 |
| pickled red onion | 12 |
| pickled red onion, recipe follows | 2 |
| pickled red onions (optional) | 1 |
| pickled red onions (recipe follows) | 1 |
| pickled red onions and fresno chiles, for serving, recipe follows | 2 |
| pickled red onions, for garnish | 1 |
| pickled red onions, for serving | 1 |
| pickled red onions, for serving, recipe follows | 2 |
| pickled red onions, for topping (below) | 1 |
| pickled red onions, recipe follows | 10 |
| pickled red onions, recipe follows, for garnish | 1 |
| pickled red onions, recipe follows, for topping | 1 |
| pickled red onions, recipe follows: | 1 |
| pickled red onions: | 2 |
| pickling liquid reserved from <pickled pearl onion | 1 |
| piece sliced red onion | 1 |
| pieces green onion | 1 |
| pieces red onion | 1 |
| pimientos, tomato, red onion and/or lettuce, for topping | 1 |
| pink pickled onions, recipe follows | 1 |
| pint pearl onion | 1 |
| pint pearl onions, blanched and peeled | 1 |
| pint pearl onions, parboiled for 5 minutes and peeled | 1 |
| pint red pearl onion | 1 |
| plain yogurt and fried onions, for garnish | 1 |
| plus 1 1/2 teaspoons red onion | 1 |
| plus 1 medium sized onion | 1 |
| plus 1 tablespoon chopped green onion | 1 |
| plus 1 teaspoon minced spanish onion | 1 |
| plus 1 teaspoon onion powder | 2 |
| plus 1/2 cup minced red onion | 1 |
| plus 1/4 cup chopped green onion | 2 |
| plus 2 tablespoons diced onion | 1 |
| plus 2 tablespoons minced red onion | 1 |
| plus 2 teaspoons pickled red onion | 1 |
| plus 3 tablespoons onion | 1 |
| plus thinly sliced red onion rounds for garnish | 1 |
| possible garnishes: 1 (8-ounce) container sour cream, 2 cups grated cheddar, 2 cups grated pepper jack cheese, 1 large onion | 1 |
| potato-onion cakes | 1 |
| potatoes with chorizo and onions, recipe follows | 1 |
| pouch campbell's® dry onion soup and recipe mix | 1 |
| pounded onion | 1 |
| powdered onion | 1 |
| pre-sliced green onion | 1 |
| prepared fried onion | 1 |
| prepared fried onions or fried shallots, for topping | 1 |
| prepared fried shallots, scallions or onion | 2 |
| prepared onion confit | 1 |
| pureed shallot (onion works fine too) | 1 |
| purple onion | 9 |
| purple onion, skin removed | 1 |
| purple onion, thinly sliced | 2 |
| purple pearl onion | 1 |
| purple pearl onions, blanched and peeled | 1 |
| quart coarsely chopped yellow onion | 2 |
| quart diced onion | 1 |
| quart small white onion | 1 |
| quart spanish onion | 1 |
| quart thinly sliced spanish onion | 2 |
| quart water simmering with 1 bay leaf, 2 onion slices, 2 thyme sprigs, juice of 1 lemon | 1 |
| quartered and thin sliced red onion | 1 |
| quartered and thinly sliced red onion | 1 |
| quartered onion | 4 |
| quarts chopped onion | 1 |
| quick-pickled onion and cucumber, recipe follows | 1 |
| quick-pickled onions, recipe follows | 1 |
| quick-pickled red onions, for serving, recipe follows | 1 |
| rajun' cajun onion rings, recipe follows | 1 |
| ramekin chopped onion | 2 |
| ramps (wild spring leeks) or large green onions or a 1-inch-diameter bunch of garlic chives | 1 |
| ranch rub* (recommended: bob tallman's blend of brown sugar, garlic, onion, gourmet peppers, ground chili, and sea salt) | 1 |
| raw onion rings | 1 |
| raw red onion rings, for garnish | 1 |
| red bermuda onion | 1 |
| red boiling onion | 1 |
| red chile onion rings, recipe follows | 1 |
| red medium onion, thinly sliced | 1 |
| red onion | 1,345 |
| red onion (1 small), very thinly sliced | 1 |
| red onion (1/2 grated, 1/2 sliced) | 1 |
| red onion (6 ounce) | 1 |
| red onion (about 12 ounces), halved lengthwise, cut thinly crosswise | 1 |
| red onion (julienne) | 1 |
| red onion (or more) | 1 |
| red onion (sliced in 1/8-inch rings), grilled | 1 |
| red onion , thinly sliced in rings | 1 |
| red onion - sliced 1/2 inch thick | 1 |
| red onion chopped | 1 |
| red onion chunks | 2 |
| red onion core | 1 |
| red onion cut in small dice | 1 |
| red onion cut into small dice | 1 |
| red onion cut into wedges, then in half and separated | 1 |
| red onion diced | 3 |
| red onion fined diced | 1 |
| red onion finely chopped | 2 |
| red onion finely diced | 2 |
| red onion finely minced | 2 |
| red onion finely sliced | 2 |
| red onion for topping and cucumber | 1 |
| red onion marmalade | 1 |
| red onion marmalade, recipe follows | 2 |
| red onion minced | 3 |
| red onion or 2 to 3 scallion | 1 |
| red onion relish, recipe follows | 1 |
| red onion rings (1/4-inch thick) | 1 |
| red onion sauteed (without oil) | 1 |
| red onion shaved julienne | 1 |
| red onion sliced | 1 |
| red onion sliced 1/2 inch thick | 1 |
| red onion sliced thin | 1 |
| red onion slices | 10 |
| red onion slices, cut 1/8-inch thick | 1 |
| red onion slices, for serving | 1 |
| red onion slices, for topping | 1 |
| red onion slices, or to taste | 1 |
| red onion slivers (recommended: ready pac) | 1 |
| red onion thinly sliced and chopped | 1 |
| red onion thinly sliced into half moons | 1 |
| red onion, 1 1/2-inch diced | 1 |
| red onion, 1-inch dice | 1 |
| red onion, 1/2 chopped, 1/2 thinly sliced | 1 |
| red onion, 1/4-inch dice | 2 |
| red onion, 1/4-inch diced | 1 |
| red onion, 1/4-inch slices | 1 |
| red onion, brunoise | 1 |
| red onion, cleaned and chopped | 1 |
| red onion, cubed | 1 |
| red onion, cut in 1/2 and thinly sliced | 1 |
| red onion, cut in 1/2 lengthwise and sliced thin | 1 |
| red onion, cut in 1/2-inch thick slices | 1 |
| red onion, cut in a fine brunoise | 1 |
| red onion, cut in half | 2 |
| red onion, cut in half and thinly sliced | 1 |
| red onion, cut in half through the root end (do not peel) | 1 |
| red onion, cut in large pieces | 1 |
| red onion, cut in rings | 1 |
| red onion, cut in small dice | 3 |
| red onion, cut into 1 1/2-inch pieces | 1 |
| red onion, cut into 1 inch cubes | 1 |
| red onion, cut into 1 inch pieces | 1 |
| red onion, cut into 1-inch dice | 1 |
| red onion, cut into 1-inch pieces | 11 |
| red onion, cut into 1-inch rounds | 1 |
| red onion, cut into 1-inch squares | 3 |
| red onion, cut into 1/2 by 2-inch strips, about 2 cups | 1 |
| red onion, cut into 1/2" slices | 1 |
| red onion, cut into 1/2-inch cubes | 1 |
| red onion, cut into 1/2-inch dice | 4 |
| red onion, cut into 1/2-inch pieces | 2 |
| red onion, cut into 1/2-inch rounds | 1 |
| red onion, cut into 1/2-inch slices | 2 |
| red onion, cut into 1/2-inch wedges | 3 |
| red onion, cut into 1/2-inch-thick rounds | 1 |
| red onion, cut into 1/2-inch-thick slices | 1 |
| red onion, cut into 1/4 inch-thick rings | 1 |
| red onion, cut into 1/4-inch dice | 7 |
| red onion, cut into 1/4-inch dice (about 1 small) | 1 |
| red onion, cut into 1/4-inch pieces, approximately 1 cup | 1 |
| red onion, cut into 1/4-inch slices | 2 |
| red onion, cut into 1/4-inch thick rings | 2 |
| red onion, cut into 1/4-inch thick rounds, grilled and finely diced | 1 |
| red onion, cut into 1/4-inch-dice | 1 |
| red onion, cut into 1/4-inch-thick slices | 1 |
| red onion, cut into 1/4-inch-thick slices (1/2 cup) | 1 |
| red onion, cut into 12 pieces | 1 |
| red onion, cut into 16 chunks | 1 |
| red onion, cut into 8 equal wedges | 1 |
| red onion, cut into 8 pieces | 1 |
| red onion, cut into a small dice | 1 |
| red onion, cut into chunks | 2 |
| red onion, cut into eighths | 2 |
| red onion, cut into half moons | 1 |
| red onion, cut into large chunks | 2 |
| red onion, cut into large dice (about 1 1/2 cups) | 1 |
| red onion, cut into medium dice | 4 |
| red onion, cut into rings | 2 |
| red onion, cut into slivers | 2 |
| red onion, cut into small dice | 7 |
| red onion, cut into spirals | 1 |
| red onion, cut into strips | 6 |
| red onion, cut into thick slices | 1 |
| red onion, cut into thin 1-inch-long strips | 1 |
| red onion, cut into thin half-moon slices | 1 |
| red onion, cut into thin half-moons | 1 |
| red onion, cut into thin rings and soaked in ice water | 1 |
| red onion, cut into thin rounds, soaked in ice and cold water for 1 hour, and patted dry | 1 |
| red onion, cut into thin slices through the stem end to make crescent shapes (about 1/3 cup) | 1 |
| red onion, cut into thin wedges | 2 |
| red onion, cut into twenty-four 1-inch pieces | 1 |
| red onion, cut into very thin rings | 1 |
| red onion, cut into wedges | 6 |
| red onion, cut julienne | 2 |
| red onion, cut through stem end into 8 wedges | 2 |
| red onion, cut vertically into sixths, sections separated | 1 |
| red onion, fine chopped | 2 |
| red onion, grilled and thinly sliced | 2 |
| red onion, halved | 6 |
| red onion, halved and cut into wedges | 1 |
| red onion, halved and sliced | 4 |
| red onion, halved and sliced thin | 1 |
| red onion, halved and sliced thinly into half moons | 1 |
| red onion, halved and thinly sliced | 13 |
| red onion, halved and thinly sliced into half-moons | 1 |
| red onion, halved lengthwise and sliced into 1/4-inch-thick half-rounds | 1 |
| red onion, halved lengthwise and sliced thin lengthwise | 1 |
| red onion, halved through stem, thinly sliced crosswise, rinsed, drained well | 1 |
| red onion, halved, cut into 1-inch wedges | 1 |
| red onion, halved, thinly sliced | 6 |
| red onion, halved; 1 half chopped and the other half whole | 1 |
| red onion, julienne | 7 |
| red onion, julienne, plus 1/2 red onion | 1 |
| red onion, julienned | 32 |
| red onion, large dice | 2 |
| red onion, large diced | 1 |
| red onion, large, cut in 1/8-inch rounds | 1 |
| red onion, large-diced | 1 |
| red onion, medium chop | 1 |
| red onion, medium dice | 4 |
| red onion, medium diced | 4 |
| red onion, medium-diced | 1 |
| red onion, or 3/4-cup, small diced | 1 |
| red onion, pulled apart into circles | 1 |
| red onion, quartered | 19 |
| red onion, quartered and cut in 1-inch strips | 2 |
| red onion, quartered and separated into 3-layer pieces | 1 |
| red onion, quartered and thinly sliced | 5 |
| red onion, quartered lengthwise then thinly sliced | 1 |
| red onion, quartered through root end | 1 |
| red onion, quartered with stem intact | 1 |
| red onion, quartered, root end left intact | 1 |
| red onion, roasted and coarsely chopped | 1 |
| red onion, rood end trimmed but left on, cut into thin wedges | 1 |
| red onion, shaved | 5 |
| red onion, shaved in slices | 1 |
| red onion, shaved julienned | 1 |
| red onion, shaved paper thin | 1 |
| red onion, shaved thin and soaked in ice water for 10 minutes | 1 |
| red onion, shredded | 1 |
| red onion, skin on, cut into 1/2-inch thick rounds | 1 |
| red onion, slivered | 2 |
| red onion, small dice | 4 |
| red onion, small dice, caramelized | 1 |
| red onion, small diced | 7 |
| red onion, super finely sliced with a mandoline | 1 |
| red onion, thickly sliced | 4 |
| red onion, thinly sliced | 286 |
| red onion, thinly sliced (1/2 cup) | 1 |
| red onion, thinly sliced (about 1 cup) | 1 |
| red onion, thinly sliced (about 2 cups) | 1 |
| red onion, thinly sliced (optional) | 1 |
| red onion, thinly sliced (soaked in ice water for 10 minutes) | 1 |
| red onion, thinly sliced and separated into rings | 1 |
| red onion, thinly sliced and slices quartered | 1 |
| red onion, thinly sliced and soaked in ice water for 10 minutes | 1 |
| red onion, thinly sliced crescents | 1 |
| red onion, thinly sliced for garnish (or as preferred) | 1 |
| red onion, thinly sliced into half moons | 1 |
| red onion, thinly sliced into half-moons | 1 |
| red onion, thinly sliced into rings | 4 |
| red onion, thinly sliced lengthwise | 1 |
| red onion, thinly sliced on a mandolin | 2 |
| red onion, thinly sliced rings, for garnish | 1 |
| red onion, thinly sliced, for topping | 1 |
| red onion, trimmed and cut into 4 wedges, layers separated | 1 |
| red onion, unpeeled, quartered lengthwise | 1 |
| red onion, very finely chopped | 2 |
| red onion, very thinly sliced | 17 |
| red onion, very thinly sliced and cut into 1-inch pieces | 1 |
| red onion, very thinly sliced on a mandoline (about 1/3 cup) | 1 |
| red onion, very thinly sliced onion-soup style | 1 |
| red onion: 1, julienned | 1 |
| red onions (1 pound total), cut into 1/4-inch dice (about 3 cups) | 1 |
| red onions (about 3 medium), each cut into 8 wedges | 1 |
| red onions (about 3 medium), halved lengthwise, cut crosswise into 1/4-inch-thick slices | 1 |
| red onions (about 4 medium), halved, thinly sliced | 1 |
| red onions chopped | 1 |
| red onions quartered, skins on | 1 |
| red onions sliced | 1 |
| red onions thinly sliced | 2 |
| red onions with peel, halved | 1 |
| red onions, 1 cut into 1/4-inch dice and 1 sliced for garnish | 1 |
| red onions, 1 cut into 1/4-inch dice and 1 sliced, forgarnish | 1 |
| red onions, cut crosswise into 1/2inch thick slices | 1 |
| red onions, cut crosswise into 1/3- to 1/2-inch-thick rounds | 1 |
| red onions, cut in 1/2 to make 2 rounds | 1 |
| red onions, cut in eighths | 1 |
| red onions, cut into 1-inch cubes | 1 |
| red onions, cut into 1-inch dice | 1 |
| red onions, cut into 1-inch pieces | 1 |
| red onions, cut into 1-inch wedges | 3 |
| red onions, cut into 1/2-inch dice | 1 |
| red onions, cut into 1/2-inch thick slices | 1 |
| red onions, cut into 1/2-inch wedges | 2 |
| red onions, cut into 1/4-inch rings | 1 |
| red onions, cut into 2-inch pieces | 1 |
| red onions, cut into 8 pieces each | 1 |
| red onions, cut into chunks | 1 |
| red onions, cut into quarters | 3 |
| red onions, cut into small dice | 1 |
| red onions, cut into strips | 2 |
| red onions, cut into thick rings | 1 |
| red onions, cut into wedges | 4 |
| red onions, cut into wedges, stem end attached | 1 |
| red onions, cut julienne | 1 |
| red onions, each cut into 6 wedges | 1 |
| red onions, each halved and cut into 6 or 8 wedges through the root end | 1 |
| red onions, halved | 5 |
| red onions, halved and peeled | 1 |
| red onions, halved and sliced | 1 |
| red onions, halved and thinly sliced | 1 |
| red onions, halved lengthwise, then cut lengthwise into 1/4-inch-thick slices | 1 |
| red onions, halved lengthwise, then thinly sliced | 1 |
| red onions, halved through the root end (unpeeled) | 1 |
| red onions, julienne | 1 |
| red onions, julienne thinly | 1 |
| red onions, julienned | 10 |
| red onions, quartered | 7 |
| red onions, quartered and each quarter cut in half | 1 |
| red onions, quartered lengthwise | 1 |
| red onions, quartered lengthwise, cored, and fine julienned | 1 |
| red onions, quartered through the root | 2 |
| red onions, quartered with roots intact | 1 |
| red onions, skins on, halved | 1 |
| red onions, slivered | 1 |
| red onions, small diced | 1 |
| red onions, thinly sliced | 21 |
| red onions, thinly sliced (3 cups) | 1 |
| red onions, thinly sliced (4 cups) | 1 |
| red onions, thinly sliced into rounds | 1 |
| red onions, thinly sliced, separated into rings | 1 |
| red onions, with skin | 1 |
| red onions; 1 quartered, 1 diced | 1 |
| red or green onion | 1 |
| red or maui onion | 1 |
| red or mild yellow onion | 1 |
| red or sweet onions, thinly sliced | 1 |
| red or white boiling onion | 1 |
| red or white pearl onion | 1 |
| red or white pearl onions (about 6 ounces) | 1 |
| red or yellow onion | 2 |
| red or yellow onion, thinly sliced | 1 |
| red pearl onion | 11 |
| red pearl onion, thinly sliced | 1 |
| red pearl onions (available at specialty produce markets) or white pearl onions, blanched in boiling water for 3 minutes, drained, and peeled | 1 |
| red pearl onions or 1/4 small red onion, thinly sliced | 1 |
| red pearl onions, blanched 1 minute | 1 |
| red pearl onions, blanched and peeled | 4 |
| red pearl onions, roasted and peeled | 1 |
| red pearl onions, roasted then peeled | 1 |
| red pearl onions, scored, blanched and peeled | 1 |
| red pearl onions, thinly sliced and soaked in small amount of olive oil | 1 |
| red pearl onions, unpeeled | 2 |
| red raw onion | 2 |
| red-onion mojo | 1 |
| relish and chopped onion, for garnish | 2 |
| reserved 1 cup onion and pepper mixture from spicy fajita soup | 1 |
| reserved 1/2 red onion | 1 |
| reserved 1/2 vidalia onion, thinly sliced, with a mandoline | 1 |
| reserved chopped onions from cuban chicken and rice | 1 |
| reserved cooked onion from spinach and pasta pie, recipe follows | 1 |
| reserved diced 1/2 medium onion from corn salsa recipe | 1 |
| reserved lobster shells, oiled annatto seed, reserved onion 1/2, and fresh culantro | 1 |
| reserved onion from chicken burritos with pineapple salsa | 1 |
| reserved red onion core | 1 |
| reserved red onion from steamed mahi mahi with vegetables | 1 |
| reserved sausage, onion, and fennel mixture | 1 |
| rings onion | 1 |
| rings thinly sliced red onion (about 1/4 medium onion) | 1 |
| rinsed unpeeled large onion, quartered | 1 |
| roasted cipolini onion | 1 |
| roasted garlic-onion jam | 1 |
| roasted onion | 1 |
| roasted onions, stem end removed and thinly sliced | 1 |
| roasted pearl onion | 2 |
| roasted red onion | 2 |
| roasted red pepper-and-vidalia onion gravy, recipe follows | 1 |
| roasted sweet potato, pureed with portion of onion liquid | 1 |
| roasted sweet-and-sour onion | 1 |
| roasted tomato and onion dipping sauce, recipe follows | 1 |
| roasted vegetables, such as onions, garlic, and squash (optional) | 1 |
| roasted yellow onion, julienned | 2 |
| rough, largely chopped root vegetables (most root vegetables - i used potatoes - will roast just fine with the pork...red onions, sweet potatoes and carrots are a few i've tried and been greatly pleased!) | 1 |
| roughly chopped (1/8 inch) onion | 1 |
| roughly chopped green onion | 2 |
| roughly chopped green onion, green part only | 1 |
| roughly chopped onion | 12 |
| roughly chopped onions (about 2 medium size onions) | 1 |
| roughly chopped raw vegetables (i like a combination of carrots, red onions, cucumbers, tomatoes, green or red bell peppers, and zucchini) | 1 |
| roughly chopped red onion | 2 |
| roughly chopped white onion | 1 |
| roughly chopped yellow onion | 2 |
| roughly chopped yellow onion, rinsed in cool water, drained | 1 |
| roughly cut onion | 1 |
| round bread loaves (preferably a dill/onion bread) | 1 |
| rounds of red onion (cut from 1 large) | 1 |
| rounds sliced red onion (about 1/4-inch thick) | 1 |
| sack chips (recommended: onion and garlic yukon gold chips, terra brand, or other mediterranean flavored gourmet chip), available on snacks aisle of market | 1 |
| sack gourmet potato chips, such as terra chips onion and herb yukon gold or blue potato chips | 1 |
| sack purple pearl onions or 1 jar pickled pearl onions, drained | 1 |
| sack reduced fat gourmet chips (recommended: terra brand garlic and onion yukon gold flavor potato chips (50 percent less fat than regular chips)) | 1 |
| sacks chips (recommended: onion and garlic flavor terra brand yukon gold chips or other specialty chips of choice) | 1 |
| sage and onion stuffing (not from a packet) | 1 |
| sage and onion stuffing mix (such as pepperidge farm®) | 1 |
| salt and freshly ground black pepper1 medium chopped onion | 1 |
| salt, pepper, onion powder, garlic powder and cayenne pepper to taste | 1 |
| salt-free onion and herb seasoning (such as mrs. dash®) | 1 |
| salt-free onion and herb seasoning blend | 1 |
| salted pickled onion | 2 |
| saute the onions, garlic, and yellow peppers. deglaze the pan with white wine, add the bechamel, cream, smoked salmon, and 4 tablespoons capers. slowly bring to a boil | 1 |
| sauteed chopped onion | 1 |
| sauteed mushrooms and onions, recipe follows | 1 |
| sauteed onion | 6 |
| sauteed onions, about 1 cup | 1 |
| sauteed onions, for garnish | 1 |
| sauteed onions, recipe follows | 1 |
| sauteed peppers and onions, recipe follows | 1 |
| sauteed sliced onion | 1 |
| sauteed swiss chard with red onion and serrano chile vinegar, recipe follows | 1 |
| scallion (green onion) trimmed | 1 |
| scallion (green onion) trimmed of 2 inches of green | 2 |
| scallion (spring onion) | 1 |
| scallion (spring onion), thinly sliced on an angle | 1 |
| scallion, both white and green parts, trimmed and finely chopped, or 3 tablespoons diced sweet onion | 1 |
| scallions (green onion) | 1 |
| scallions (green onions) | 9 |
| scallions (green onions), thinly sliced | 2 |
| scallions (green onions), trimmed, thinly sliced | 1 |
| scallions (green onions), white and tender green parts only | 3 |
| scallions (shallots/spring onions), dark green tops removed | 1 |
| scallions (spring onions) | 1 |
| scallions or spring onions, cut on the bias | 1 |
| scallions, cut into 1/4-inch slices, or 1 cup sliced spring onion | 1 |
| scallions, trimmed and thinly sliced or 1/4 cup sweet onion cut into 1/4-inch dice | 4 |
| scallions, white only or use pearl onions, roasted | 1 |
| scant 1/2 cup finely chopped green onions (about 6) | 1 |
| scant 1/4 cup finely chopped onion | 1 |
| scant tablespoon onion powder | 1 |
| seasoned salt (with onion and garlic) | 1 |
| seasonings (possible suggestions: onion, parsley, black pepper, or other) | 1 |
| serving suggestion: composed salad of red onions, orange segments, and avocado slices | 1 |
| serving suggestion: diced raw onions and vinegar | 1 |
| serving suggestion: grilled cheese with caramelized onions, recipe follows | 1 |
| serving suggestion: onion and spinach dip, recipe follows | 1 |
| serving suggestion: polenta and glazed onions or roasted shallots | 1 |
| serving suggestions: corn tortillas, shredded cabbage, pickled red onion, crumbled queso fresco, cilantro leaves and lime wedges | 1 |
| serving suggestions: diced red onion | 1 |
| serving suggestions: fresh baked brat buns with sauerkraut, onions, green peppers, ketchup, and/or mustard | 2 |
| serving suggestions: green leaf lettuce, halved cherry tomatoes, thinly sliced red onions, shredded carrots and sliced celery | 1 |
| serving suggestions: lettuce, tomato slices and red onion slices | 1 |
| serving suggestions: mashed potatoes, sauteed mushrooms and onion, and a side of freshly grated horseradish | 1 |
| serving suggestions: pickled red onions, warm corn tortillas and salsa | 1 |
| serving suggestions: rolls with ketchup, tomato, fried onions, feta cheese | 1 |
| serving suggestions: serve with grilled onions, grilled portobello mushroom slices, and mixed greens, or, burger style with mango ketchup | 1 |
| serving suggestions: sour cream, shredded cheddar cheese and diced red onion | 1 |
| serving suggestions: tortillas, salsas, cilantro, limes, onions and sea salt | 1 |
| sesame hamburger buns or onion rolls, split and toasted | 1 |
| several large vidalia onion | 1 |
| several thin slices red onion (sliced on a mandolin) | 1 |
| shallot or 1/4 red onion | 1 |
| shallot or 1/4 red onion, thinly sliced | 1 |
| shallot or boiling onion | 1 |
| shallot or onion | 1 |
| shallot or small onion | 1 |
| shallot or small yellow onion | 1 |
| shallots or 1 medium onion | 2 |
| shallots or 1 small onion | 2 |
| shallots or 1 small onion, very finely chopped | 1 |
| shallots or 1 small red onion | 1 |
| shallots or 1/2 red onion | 1 |
| shallots or mild onion, thinly sliced or minced | 1 |
| shallots or onion | 1 |
| shallots or small onion | 1 |
| shallots or white onion | 1 |
| shallots, or 1/2 onion | 1 |
| shaved green onions, for garnish | 1 |
| shaved green onions, or more to taste | 1 |
| shaved maui onion | 1 |
| shaved onion | 1 |
| shaved red onion | 3 |
| shaved vidalia onion | 1 |
| shoestring onion rings, see recipe | 1 |
| shredded iceberg lettuce, quick pickled onions , thinly sliced radishes | 1 |
| shredded iceberg lettuce, thinly sliced white onion, crema (mexican salted cream) or sour cream, queso fresco, cilantro leaves with tender stems (for serving) | 1 |
| shredded iceberg lettuce, thinly sliced white onion, queso fresco, cilantro leaves with tender stems (for serving) | 1 |
| shredded lettuce and/or diced red onion, for topping | 1 |
| silver dollar onion rolls, halved | 1 |
| six 1-inch sections green onion | 1 |
| slice from middle of a large white onion | 1 |
| slice large white onion | 1 |
| slice onion | 8 |
| slice onion, separated into rings | 1 |
| slice red onion | 2 |
| slice red onion, cut into a julienne | 1 |
| slice red onion, separated into rings | 1 |
| slice white onion | 2 |
| slice yellow onion | 1 |
| sliced (1/4-inch) yellow onion | 1 |
| sliced assorted vegetables, such as peppers, onions and mushrooms | 1 |
| sliced avocado, cilantro leaves, sour cream, and/or finely chopped onion (for serving; optional) | 1 |
| sliced bell peppers and onion, for topping | 1 |
| sliced carrots, green onions, jalapenos, fresno chiles, basil, cilantro and limes, for serving | 1 |
| sliced cippolini onion | 1 |
| sliced dole red onion | 1 |
| sliced fresh chives or green onion | 1 |
| sliced fresh green onion | 1 |
| sliced garlic chives or green onion | 1 |
| sliced green onion | 173 |
| sliced green onion (1-inch) | 1 |
| sliced green onion (green part only) | 2 |
| sliced green onion (optional) | 1 |
| sliced green onion, for garnish | 3 |
| sliced green onion, green and pale green part | 1 |
| sliced green onion, white and green parts | 1 |
| sliced green onion, white and green parts, for serving | 1 |
| sliced green onion, white part only | 1 |
| sliced green onions (4 medium) | 1 |
| sliced green onions (4 medium), if desired | 1 |
| sliced green onions (about 1 small bunch) | 1 |
| sliced green onions (about 3) | 1 |
| sliced green onions (about 5) | 1 |
| sliced green onions (about 8) | 1 |
| sliced green onions (green part only) | 1 |
| sliced green onions (less to taste) | 1 |
| sliced green onions (optional) | 1 |
| sliced green onions (white and light green parts only) | 1 |
| sliced green onions (with some green tops) | 1 |
| sliced green onions and diced red peppers, for garnish | 1 |
| sliced green onions, cut on the bias | 1 |
| sliced green onions, for garnish | 5 |
| sliced green onions, for serving | 1 |
| sliced green onions, for topping | 1 |
| sliced green onions, green only (about 3) | 1 |
| sliced green onions, green part only | 2 |
| sliced green onions, mostly white and lighter green parts | 1 |
| sliced green onions, tops only | 1 |
| sliced green onions, white and green parts separated | 1 |
| sliced green onions, with green | 1 |
| sliced medium onion | 1 |
| sliced nacho japapeños, 1 to 2 seeded and minced fresh chilies, 1 bunch sliced scallions (green onions), or drops of hot sauce or tabasco | 1 |
| sliced onion | 138 |
| sliced onion (1 large) | 1 |
| sliced onion (about 1/4th of an onion) | 1 |
| sliced onion (about one large onion) | 1 |
| sliced onion wedges | 1 |
| sliced onion, or to taste | 1 |
| sliced onions (about 1 1/4 pounds) | 1 |
| sliced onions (about 2 large onions) | 1 |
| sliced onions (about 2 onions) | 1 |
| sliced onions (about 2) | 1 |
| sliced onions (about 3 large) | 1 |
| sliced onions (about 4 large) | 1 |
| sliced onions* | 1 |
| sliced onions, 1/4-inch thick | 1 |
| sliced or chopped onion | 2 |
| sliced pickled cocktail onion | 1 |
| sliced pickled red onions, for garnish | 1 |
| sliced purple onion | 1 |
| sliced radishes and chopped red onion, for topping | 1 |
| sliced red onion | 61 |
| sliced red onion (1/8 inch thick; 1 small) | 1 |
| sliced red onion (about 1 small) | 1 |
| sliced red onion (for serving) | 1 |
| sliced red onion (optional) | 2 |
| sliced red onion and pickles, for serving | 1 |
| sliced red onion and sliced yellow and plum tomato | 1 |
| sliced red onion, as desired | 1 |
| sliced red onion, as needed | 1 |
| sliced red onion, bean sprouts, cilantro sprigs, crispy fried onions or shallots, chili oil, and lime wedges (for serving) | 1 |
| sliced red onion, cut lengthwise | 1 |
| sliced red onion, for serving | 2 |
| sliced red onion, for topping | 1 |
| sliced red onion, tomato and avocado, for serving | 1 |
| sliced red onions, "pickled" in lemon juice for 2 hours | 1 |
| sliced red onions, for serving | 3 |
| sliced red or sweet onion | 1 |
| sliced red or yellow onion, pulled into rings | 1 |
| sliced seared onion | 1 |
| sliced small red onion, for topping | 1 |
| sliced spanish onion | 3 |
| sliced spring onion | 2 |
| sliced sweet onion | 3 |
| sliced sweet yellow onion | 1 |
| sliced thin sweet onions in 1/16-inch slices | 1 |
| sliced tomato, cucumber, lettuce, red onion and some plain yogurt | 1 |
| sliced tomato, cucumber, lettuce, red onion, and some plain yogurt, for serving | 1 |
| sliced tomatoes and thinly sliced red onion | 1 |
| sliced vidalia onion | 2 |
| sliced white onion | 7 |
| sliced white onion, separated into rings | 1 |
| sliced yellow onion | 11 |
| sliced yellow onion (1 large) | 1 |
| sliced yellow onions (2 onions) | 2 |
| sliced yellow onions (3 onions) | 1 |
| sliced yellow onions, 1/4-inch thick (3 pounds) | 1 |
| slices chopped onion | 1 |
| slices green onion | 1 |
| slices of monterey jack cheese, lettuce, tomato, onion, avocado, red onion, etc | 1 |
| slices of red onion (keep intact so they are large disks) | 1 |
| slices onion | 10 |
| slices onion (optional) | 1 |
| slices onion slices | 1 |
| slices onion, or to taste | 1 |
| slices raw onion | 1 |
| slices raw red onion | 1 |
| slices red onion | 15 |
| slices red onion (optional) | 1 |
| slices red onion, 1/2-inch thick | 1 |
| slices red onion, 1/2inch thick | 1 |
| slices red onion, 1/4-inch thick | 1 |
| slices red onion, for serving | 1 |
| slices red onion, quartered | 1 |
| slices red onion, separated into rings | 1 |
| slices small red onion | 1 |
| slices sweet onion, 1/2 inch thick | 1 |
| slices sweet onion, such as vidalia or maui | 1 |
| slices thin-sliced pumpernickel, onion, or plain white bread | 1 |
| slices vidalia or other sweet onion, grilled | 1 |
| slivered green onion | 1 |
| slivered green onion tops, for garnish (optional) | 1 |
| slivered red onion | 4 |
| small (1 1/2-inch) boiling onions or pearl onion | 1 |
| small (1 1/2-inch) onion | 1 |
| small (1-inch) white boiling onions (not peeled) | 1 |
| small (1/4 to 1/3 pound) onion | 1 |
| small (4-ounce) white onion | 1 |
| small (6-ounce) onion | 1 |
| small (golf-ball sized) onion | 1 |
| small (or 1/2 large) white onion, cut into 1/4" cubes, rinsed with cool water, patted dry | 1 |
| small and thin green onions, cut into 1 1/4-inch segments | 1 |
| small boiling onion | 2 |
| small boiling onions (about 20), left unpeeled | 1 |
| small boiling onions, trimmed | 1 |
| small bunch green onion | 1 |
| small bunch green onions, green tops only, thinly sliced (about 3 tablespoons) | 1 |
| small bunches green onions, trimmed | 1 |
| small can french fried onions, for topping | 1 |
| small chopped onion | 2 |
| small chopped onion (about 1 cup) | 1 |
| small chopped red onion | 1 |
| small chopped yellow onion | 2 |
| small cipolline onion | 1 |
| small cipolline onions or small boiling onions, blanched | 1 |
| small cipolline or pearl onion | 2 |
| small cipolline, shallots, or boiling onion | 1 |
| small cipollini onion | 2 |
| small cipollini onions, (if you can't find cipollini onions, pearl onions are a good substitute) | 1 |
| small cup onion | 1 |
| small dark seeds such as nigella (black onion seeds), cumin seeds, or caraway seeds for ghosts; "eyes | 1 |
| small dark seeds such as nigella (black onion seeds), cumin seeds, or caraway seeds for ghosts; "eyes" | 1 |
| small dice mirepoix (celery, carrot and onion) | 2 |
| small dice red onion | 6 |
| small dice spanish onion | 1 |
| small dice sweet onion | 1 |
| small dice vidalia onion | 1 |
| small dice white onion | 2 |
| small dice yellow onion | 1 |
| small diced onion | 17 |
| small diced onion (approximately 1 cup) | 1 |
| small diced or chopped onion | 1 |
| small diced red onion | 10 |
| small diced red onion (1 small onion) | 2 |
| small diced white onion | 4 |
| small diced yellow onion | 7 |
| small finely diced onion | 1 |
| small fresh onion bulbs, halved | 1 |
| small green onion | 10 |
| small green onion, thinly sliced | 1 |
| small green onions, cut into 1-inch pieces | 1 |
| small green onions, greens parts only, thinly sliced | 1 |
| small green onions, pale green and white parts only | 1 |
| small green onions, thinly sliced | 2 |
| small jar pickled onions, also available on condiments aisle | 1 |
| small jar pickled onions, available on vegetable aisle | 2 |
| small jarred onions, quartered (about 4 ounces or 1 cup) | 1 |
| small maui onion | 2 |
| small maui onions or other sweet onions, thinly sliced and separated into rings | 1 |
| small maui sweet onion - sliced | 1 |
| small minced onion | 1 |
| small minced red onion | 1 |
| small new onions, with tops attached | 1 |
| small onion | 1,996 |
| small onion (1/2 sliced into rings, 1/2 diced) | 1 |
| small onion (1/4 pound), cut into 1/2-inch-thick slices | 1 |
| small onion (1/4 pound), thinly sliced | 1 |
| small onion (5 ounces), small dice | 1 |
| small onion (about 3 ounces) | 2 |
| small onion (about 4 ounces) | 1 |
| small onion (about 7 ounces), thinly sliced | 1 |
| small onion (any kind) | 1 |
| small onion (sliced thin) | 1 |
| small onion chopped | 3 |
| small onion chopped fine | 1 |
| small onion cut in large wedges | 1 |
| small onion finely chopped | 5 |
| small onion finely chopped (about 1 cup) | 1 |
| small onion finely diced | 1 |
| small onion minced | 2 |
| small onion or 1/2 large onion | 1 |
| small onion or 1/2 medium onion | 2 |
| small onion or large shallot | 1 |
| small onion pierced with 3 whole clove | 1 |
| small onion spiked with 10 clove | 1 |
| small onion thinly sliced | 1 |
| small onion, 1/2-inch dice | 2 |
| small onion, chopped1can (10 3/4 ounce) condensed tomato soup | 1 |
| small onion, cubed | 2 |
| small onion, cut in half | 3 |
| small onion, cut in half and sliced | 1 |
| small onion, cut in half and thinly sliced | 1 |
| small onion, cut in half, thinly sliced, rinsed, and drained | 1 |
| small onion, cut in pieces, plus 3 medium onion | 1 |
| small onion, cut into 1-inch pieces | 1 |
| small onion, cut into 1/2-inch cubes | 1 |
| small onion, cut into 1/2-inch dice | 2 |
| small onion, cut into 1/2-inch pieces | 1 |
| small onion, cut into 1/2-inch thick slices | 1 |
| small onion, cut into 1/2-inch wedges | 1 |
| small onion, cut into 1/2-inch-thick rounds | 1 |
| small onion, cut into 1/2-inch-thick slices | 1 |
| small onion, cut into 1/4-inch cubes | 1 |
| small onion, cut into 1/4-inch dice | 8 |
| small onion, cut into 1/4-inch dice (1/2 cup) | 1 |
| small onion, cut into 1/4-inch dice (3/4 cup) | 1 |
| small onion, cut into 1/4-inch pieces | 1 |
| small onion, cut into 1/4-inch slices | 2 |
| small onion, cut into 1/4-inch-thick slices | 1 |
| small onion, cut into 16 small pieces | 1 |
| small onion, cut into 3/4" rounds | 1 |
| small onion, cut into 3/4-inch dice (about 1 cup) | 1 |
| small onion, cut into 6 wedges | 1 |
| small onion, cut into 8 wedges | 1 |
| small onion, cut into bite-size pieces | 1 |
| small onion, cut into chunks | 5 |
| small onion, cut into large chunks | 1 |
| small onion, cut into large dice | 1 |
| small onion, cut into long slices | 1 |
| small onion, cut into matchstick-sized pieces | 1 |
| small onion, cut into medium dice | 1 |
| small onion, cut into pieces | 2 |
| small onion, cut into quarters | 3 |
| small onion, cut into small dice | 3 |
| small onion, cut into strips | 1 |
| small onion, cut into thick slices | 2 |
| small onion, cut into thin strips (about 1 cup) | 1 |
| small onion, cut into thin wedges | 3 |
| small onion, cut into wedges | 2 |
| small onion, cut lengthwise in 1/2 and thinly sliced crosswise | 1 |
| small onion, cut lengthwise into 1/4-inch-thick slices | 1 |
| small onion, fine dice | 1 |
| small onion, grilled and chopped | 1 |
| small onion, halved | 22 |
| small onion, halved and peeled | 1 |
| small onion, halved and sliced | 4 |
| small onion, halved and sliced root to tip | 1 |
| small onion, halved and sliced thin from root to tip | 1 |
| small onion, halved and thinly sliced | 13 |
| small onion, halved but not peeled | 1 |
| small onion, halved lengthwise and sliced thin | 1 |
| small onion, halved lengthwise and thinly sliced crosswise | 1 |
| small onion, halved lengthwise and thinly sliced lengthwise | 1 |
| small onion, halved, plus | 1 |
| small onion, halved, then very thinly sliced | 1 |
| small onion, julienned | 3 |
| small onion, medium dice | 1 |
| small onion, medium diced | 3 |
| small onion, or to taste | 1 |
| small onion, peeled1 teaspoon baking soda | 1 |
| small onion, quartered | 33 |
| small onion, quartered and peeled | 1 |
| small onion, quartered and sliced | 1 |
| small onion, quartered and thinly sliced | 1 |
| small onion, quartered through core, thinly sliced crosswise (1 scant cup) | 1 |
| small onion, quartered through root end | 1 |
| small onion, red or white | 1 |
| small onion, roasted, then chopped | 1 |
| small onion, shredded | 2 |
| small onion, slivered | 1 |
| small onion, small dice | 1 |
| small onion, small diced | 1 |
| small onion, studded with 1 clove | 1 |
| small onion, the rest chopped for garnish | 1 |
| small onion, thickly sliced | 3 |
| small onion, thinly slice | 1 |
| small onion, thinly sliced | 73 |
| small onion, thinly sliced (about 1/3 cup) | 1 |
| small onion, thinly sliced and quartered | 1 |
| small onion, thinly sliced into rings | 1 |
| small onion, thinly sliced lengthwise | 1 |
| small onion, unpeeled | 1 |
| small onion, very finely chopped | 3 |
| small onion, very thinly sliced | 2 |
| small onion, yellow or red, thinly sliced | 1 |
| small onions (1 left unpeeled and halved lengthwise, and 1 peeled and chopped) | 1 |
| small onions (about 1 pound total), unpeeled but chopped | 1 |
| small onions (about 12 ounces total) | 1 |
| small onions (approximately 1 1/2-inch diameter) | 1 |
| small onions (or 1 cup pearl onions) | 1 |
| small onions or 1 large, quartered lengthwise and thinly sliced | 1 |
| small onions, 1 finely chopped and 1 cut into half-moon slices | 2 |
| small onions, 1 roughly chopped, 1 cut in medium dice | 1 |
| small onions, 1 roughly chopped, 2 thinly sliced | 1 |
| small onions, cut into 1-inch cubes | 1 |
| small onions, cut into 1/4-inch-thick slices | 1 |
| small onions, cut into 2 inch pieces | 1 |
| small onions, cut into 6 quarters | 2 |
| small onions, cut into wedges | 3 |
| small onions, each cut into 6 wedges | 1 |
| small onions, each quartered | 1 |
| small onions, finley chopped | 1 |
| small onions, halved | 1 |
| small onions, halved lengthwise and thinly sliced | 1 |
| small onions, medium diced | 1 |
| small onions, quartered | 6 |
| small onions, thinly sliced | 7 |
| small onions, thinly sliced across width | 1 |
| small or 1/2 large onion | 1 |
| small or 1/2 large onion, small dice | 1 |
| small or 1/2 large red onion | 2 |
| small or 1/2 medium red onion | 1 |
| small or medium red onion, 1/4 finely chopped, the remainder thinly sliced | 1 |
| small pearl onion | 2 |
| small peeled onion | 1 |
| small purple onion, thinly sliced | 1 |
| small purple or white spring onion bulbs, thinly sliced crosswise | 1 |
| small red bermuda onion | 1 |
| small red onion | 650 |
| small red onion (1/2 cut into large chunks, 1/2 thinly sliced) | 1 |
| small red onion (1/4 lb), thinly sliced | 1 |
| small red onion (5 ounces) thinly slivered lengthwise | 1 |
| small red onion (about 4 ounces), thinly sliced into rings | 1 |
| small red onion (about 6 ounces) | 1 |
| small red onion chopped | 2 |
| small red onion cut into 4 slices | 1 |
| small red onion finely chopped | 1 |
| small red onion finely diced | 2 |
| small red onion or 1 shallot | 1 |
| small red onion or 1/2 large | 1 |
| small red onion or 1/2 large red onion | 1 |
| small red onion or 1/2 medium | 1 |
| small red onion or 1/2 medium onion, very thinly sliced or chopped | 1 |
| small red onion or 1/2 medium red onion, thinly sliced | 1 |
| small red onion or 1/2 medium, very thinly sliced | 1 |
| small red onion or 2 to 3 scallion | 1 |
| small red onion or white, halved | 1 |
| small red onion sliced paper thin into circles | 1 |
| small red onion sliced very thin | 1 |
| small red onion, 1/2 finely chopped, 1/2 thinly sliced | 1 |
| small red onion, 1/4 inch dice | 1 |
| small red onion, 1/4" dice | 2 |
| small red onion, cut in 1/2, then into thin slivers (about 1/4 cup) | 1 |
| small red onion, cut in 1/2-inch dice (about 1 cup) | 1 |
| small red onion, cut in half and thinly sliced | 2 |
| small red onion, cut in half lengthwise and then into 1/2-inch cubes | 1 |
| small red onion, cut into 1-inch dice | 1 |
| small red onion, cut into 1-inch pieces | 1 |
| small red onion, cut into 1/2-inch pieces | 3 |
| small red onion, cut into 1/2-inch rings | 1 |
| small red onion, cut into 1/2-inch rounds | 1 |
| small red onion, cut into 1/2-inch slices | 1 |
| small red onion, cut into 1/2-inch wedges, soaked in cold water for 5 minutes and drained | 2 |
| small red onion, cut into 1/3-inch dice (about 1/2 cup) | 1 |
| small red onion, cut into 1/4"-thick rings | 1 |
| small red onion, cut into 1/4-inch cubes | 2 |
| small red onion, cut into 1/4-inch dice | 8 |
| small red onion, cut into 1/4-inch pieces | 1 |
| small red onion, cut into 1/4-inch-thick slices | 2 |
| small red onion, cut into 2" pieces | 1 |
| small red onion, cut into 3/4 inch slices | 1 |
| small red onion, cut into 4 wedges, each wedge halved crosswise, layers kept intact | 1 |
| small red onion, cut into 8 thin wedges | 1 |
| small red onion, cut into matchstick-size pieces | 1 |
| small red onion, cut into medium wedges | 1 |
| small red onion, cut into rings | 2 |
| small red onion, cut into slivers | 3 |
| small red onion, cut into small dice | 7 |
| small red onion, cut into thin rings | 1 |
| small red onion, cut into thin rings and grilled | 2 |
| small red onion, cut into thin slices | 1 |
| small red onion, cut into thin slivers | 1 |
| small red onion, cut into thin strips | 1 |
| small red onion, cut into thin wedges | 2 |
| small red onion, cut into tiny dice (about 1/2 cup) | 1 |
| small red onion, cut into very small dice | 1 |
| small red onion, cut into wedges | 2 |
| small red onion, cut lengthwise into 1/2-inch-thick wedges (keeping root end intact) | 1 |
| small red onion, extra thinly sliced | 1 |
| small red onion, fine dice | 1 |
| small red onion, finely julienned | 1 |
| small red onion, halved | 5 |
| small red onion, halved and julienne | 1 |
| small red onion, halved and minced | 1 |
| small red onion, halved and sliced | 2 |
| small red onion, halved and sliced into thin half-moons | 3 |
| small red onion, halved and sliced root to stem | 1 |
| small red onion, halved and thinly sliced | 40 |
| small red onion, halved lengthwise | 1 |
| small red onion, halved lengthwise and sliced crosswise 1/8 inch thick (1 cup) | 1 |
| small red onion, halved lengthwise and sliced thin | 1 |
| small red onion, halved lengthwise and sliced thin lengthwise | 1 |
| small red onion, halved lengthwise and sliced very thin | 1 |
| small red onion, halved lengthwise and thinly sliced crosswise | 4 |
| small red onion, halved lengthwise and thinly sliced crosswise (1 cup) | 1 |
| small red onion, halved lengthwise and thinly sliced crosswise (1/2 cup) | 1 |
| small red onion, halved lengthwise and very thinly sliced crosswise | 1 |
| small red onion, halved lengthwise, then thinly sliced crosswise (1 cup) | 1 |
| small red onion, halved lengthwise, then thinly sliced crosswise (1/2 cup) | 2 |
| small red onion, halved lengthwise, then thinly sliced lengthwise (1 cup) | 1 |
| small red onion, halved lengthwise, then very thinly sliced crosswise | 2 |
| small red onion, halved lengthwise, then very thinly sliced lengthwise | 1 |
| small red onion, halved, thinly sliced | 1 |
| small red onion, halved, very thinly sliced | 1 |
| small red onion, in small dice | 2 |
| small red onion, julienne | 2 |
| small red onion, julienned | 16 |
| small red onion, julienned thin | 1 |
| small red onion, medium diced | 2 |
| small red onion, quartered | 2 |
| small red onion, quartered and thinly sliced | 6 |
| small red onion, quartered lengthwise | 1 |
| small red onion, quartered lengthwise and thinly sliced crosswise | 1 |
| small red onion, shaved | 3 |
| small red onion, shaved julienne | 1 |
| small red onion, shredded and squeezed dry (about 1/2 cup) | 1 |
| small red onion, slivered | 1 |
| small red onion, small dice | 4 |
| small red onion, small diced | 1 |
| small red onion, thinly julienned | 1 |
| small red onion, thinly sliced | 209 |
| small red onion, thinly sliced (1/2 cup) | 1 |
| small red onion, thinly sliced (about 1 cup) | 2 |
| small red onion, thinly sliced (about 1/2 cup) | 2 |
| small red onion, thinly sliced (about 3/4 cup) | 1 |
| small red onion, thinly sliced against the grain | 1 |
| small red onion, thinly sliced and rinsed in cold water | 1 |
| small red onion, thinly sliced and separated into rings (about 12 rings) | 1 |
| small red onion, thinly sliced by hand or with mandoline | 1 |
| small red onion, thinly sliced crosswise | 1 |
| small red onion, thinly sliced crosswise, separated into rings | 1 |
| small red onion, thinly sliced into rings | 3 |
| small red onion, thinly sliced into rounds | 1 |
| small red onion, thinly sliced on a mandolin | 1 |
| small red onion, thinly sliced on a mandoline | 1 |
| small red onion, thinly sliced, for garnish | 1 |
| small red onion, thinly sliced, pulled into rings | 1 |
| small red onion, thinly sliced, rinsed | 1 |
| small red onion, thinly slivered | 1 |
| small red onion, unpeeled, cut into quarters | 1 |
| small red onion, very finely diced | 3 |
| small red onion, very thinly sliced | 23 |
| small red onion, very thinly sliced (about 1 1/2 cups) | 1 |
| small red onion, very thinly sliced into circles | 1 |
| small red onion, very thinly sliced into rings | 3 |
| small red onion, very thinly sliced or 1/2-inch dice | 1 |
| small red onion, very thinly sliced, rinsed, patted dry | 1 |
| small red onion,thinly sliced | 1 |
| small red onions (10 oz total), each cut into 6 wedges | 1 |
| small red onions (11/2 thickly sliced, 1/2 thinly sliced) | 1 |
| small red onions (3/4 lb total) | 1 |
| small red onions (3/4 pound total), quartered lengthwise, leaving root end intact | 1 |
| small red onions (about 1/2 pound) | 1 |
| small red onions (about 12 ounces total), halved | 1 |
| small red onions (about 9), halved through root end, then cut into 3/4-inch-wide wedges with some of core attached to each | 1 |
| small red onions, (about 5, each about 1 1/2 inches in diameter) | 1 |
| small red onions, cut into 1/3-inch wedges | 1 |
| small red onions, cut into 3/4-inch-thick rounds | 1 |
| small red onions, cut into quarters | 2 |
| small red onions, cut into strips | 1 |
| small red onions, cut into thin wedges | 1 |
| small red onions, halved and thinly sliced | 1 |
| small red onions, quartered | 2 |
| small red onions, thinly sliced | 8 |
| small red onions, thinly sliced in half rounds | 1 |
| small red or sweet onion, cut into 12 (1/2-inch) pieces | 1 |
| small red or white onion | 1 |
| small red or yellow onion | 1 |
| small scallion (green onion), trimmed and finely sliced | 1 |
| small shallot or 3 tablespoons red onion | 1 |
| small shallot or onion | 1 |
| small shallots, or 2 tablespoons white onion | 1 |
| small sliced onion | 2 |
| small slices white onion | 1 |
| small small onion | 2 |
| small spanish onion | 62 |
| small spanish onion or 1/2 large | 1 |
| small spanish onion, cut into 1/2-inch thick slices | 1 |
| small spanish onion, cut into medium dice | 1 |
| small spanish onion, cut into small dice | 1 |
| small spanish onion, halved | 1 |
| small spanish onion, halved and thinly sliced | 3 |
| small spanish onion, halved lengthwise and thinly sliced | 1 |
| small spanish onion, quartered | 2 |
| small spanish onion, thinly sliced | 4 |
| small spring onion | 1 |
| small spring onion (green) | 1 |
| small spring onion, julienned | 1 |
| small spring onion, thinly sliced | 1 |
| small spring onions or scallions, white part only, trimmed | 2 |
| small spring onions, bulbs only | 1 |
| small spring onions, julienned | 1 |
| small sweet onion | 39 |
| small sweet onion (such as maui or walla walla), very thinly sliced | 1 |
| small sweet onion (such as maui), very thinly sliced | 1 |
| small sweet onion (such as vidalia or maui), quartered | 1 |
| small sweet onion (such as vidalia or maui), thinly sliced | 1 |
| small sweet onion (such as vidalia) | 2 |
| small sweet onion (such as vidalia®) | 3 |
| small sweet onion (such as vidalia®), cut in half and sliced | 1 |
| small sweet onion (such as vidalia®), thinly sliced | 2 |
| small sweet onion such as vidalia | 1 |
| small sweet onion, cut into 1/4-inch pieces | 1 |
| small sweet onion, cut lengthwise into quarters, thinly sliced crosswise | 1 |
| small sweet onion, or to taste | 1 |
| small sweet onion, rough chopped | 1 |
| small sweet onion, such as vidalia | 2 |
| small sweet onion, such as vidalia or walla walla | 2 |
| small sweet onion, such as vidalia, thinly sliced | 1 |
| small sweet onion, thinly sliced | 6 |
| small sweet onions (such as vidalia or maui; about 1 pound), cut crosswise into 1/2-inch-thick slices | 1 |
| small sweet onions (such as vidalia®) | 1 |
| small sweet onions, thinly sliced | 2 |
| small sweet red onion, cut into strips | 1 |
| small sweet white onion | 1 |
| small sweet yellow onion | 1 |
| small sweet yellow onion, thinly sliced | 1 |
| small to medium onion | 7 |
| small to medium onion, cut into 1 1/2 inch chunks | 1 |
| small to medium onion, thinly sliced | 1 |
| small to medium onion, very thinly sliced | 1 |
| small to medium onions, cut into thin wedges with the root ends attached | 1 |
| small to medium red onion | 2 |
| small to medium red onion, very thinly sliced | 1 |
| small to medium red onions, halved and thinly sliced (about 3 1/2 cups) | 1 |
| small to medium white or yellow onions, 1 quartered and 1 chopped | 1 |
| small to medium yellow onion | 3 |
| small to medium yellow onion, 1 grated and 1 finely chopped | 1 |
| small to medium yellow skinned onion | 4 |
| small to medium yellow skinned onion, thinly sliced | 1 |
| small to medium-sized onion | 1 |
| small torpedo or red onion, thinly sliced into rings | 1 |
| small unpeeled onion, quartered and separated | 1 |
| small vidalia onion | 13 |
| small vidalia onion (or other sweet onion) | 1 |
| small vidalia onion, cut in half through the root | 1 |
| small vidalia onion, cut into a medium dice | 2 |
| small vidalia onion, thinly sliced | 3 |
| small vidalia or other sweet onion | 1 |
| small vidalia or sweet onion, thinly sliced | 1 |
| small white boiling onion | 2 |
| small white onion | 165 |
| small white onion (6 to 8 ounces), quartered | 1 |
| small white onion (about 2 ounces) | 1 |
| small white onion (boiling onion) | 1 |
| small white onion (finely chopped) | 1 |
| small white onion or a 1-inch-thick slice of a large white onion | 1 |
| small white onion, cut into 1/2-inch dice | 2 |
| small white onion, cut into 1/4-inch dice | 1 |
| small white onion, cut into 1/8-inch dice | 1 |
| small white onion, cut into pieces | 1 |
| small white onion, half finely chopped, half chunked | 1 |
| small white onion, halved and thinly sliced | 3 |
| small white onion, halved lengthwise, keeping root intact | 1 |
| small white onion, halved, cut into 1/4-inch-thick slices (about 1/2 cup) | 1 |
| small white onion, quartered | 5 |
| small white onion, quartered, cooked and peeled | 1 |
| small white onion, small dice | 1 |
| small white onion, thinly sliced | 6 |
| small white onion, thinly sliced and separated into rings | 1 |
| small white onion, thinly sliced and soaked in ice water for 20 minutes | 1 |
| small white onion, thinly sliced into half moons | 1 |
| small white onion, thinly sliced or finely chopped, for garnish | 1 |
| small white onion, unpeeled, plus 1 medium-sized white onion | 1 |
| small white onion, very finely chopped | 1 |
| small white onion, very thinly sliced into rings | 1 |
| small white onion, wedge with root attached | 1 |
| small white onions, about 1-inch in diameter | 1 |
| small white onions, blanched in boiling water for 2 minutes, drained, and peeled | 1 |
| small white onions, cleaned and scored | 1 |
| small white onions, halved lengthwise | 1 |
| small white onions, parboiled for 15 minutes | 1 |
| small white onions, quartered | 1 |
| small white onions, with green tops if possible | 1 |
| small white or red onion | 2 |
| small white or sweet onion | 2 |
| small white or vidalia onion, julienned | 1 |
| small white or yellow onion | 2 |
| small white or yellow onion, very thinly sliced | 1 |
| small white skinned onion | 3 |
| small whole onion | 4 |
| small whole red onion | 1 |
| small whole unpeeled onions (1/2 pound total) | 1 |
| small yellow onion | 204 |
| small yellow onion (about 5 ounces) | 1 |
| small yellow onion or 1/2 red onion | 1 |
| small yellow onion, cut into 1/2-inch dice | 1 |
| small yellow onion, cut into 1/4-inch dice | 2 |
| small yellow onion, cut into 1/4-inch slices | 1 |
| small yellow onion, cut into 1/4inch dice | 1 |
| small yellow onion, cut into medium dice | 1 |
| small yellow onion, cut into small dice | 2 |
| small yellow onion, cut into wedges | 1 |
| small yellow onion, finley chopped | 1 |
| small yellow onion, halved | 2 |
| small yellow onion, halved through root | 1 |
| small yellow onion, halved vertically and cut into half moons | 1 |
| small yellow onion, julienne | 1 |
| small yellow onion, julienned | 2 |
| small yellow onion, medium dice | 1 |
| small yellow onion, or to taste | 1 |
| small yellow onion, quartered | 3 |
| small yellow onion, skin and root intact, quartered | 2 |
| small yellow onion, skin removed and quartered | 1 |
| small yellow onion, small dice | 2 |
| small yellow onion, small dice (about 1 cup) | 1 |
| small yellow onion, thinly sliced | 7 |
| small yellow onion, thinly sliced (about 1/2 cup) | 1 |
| small yellow onion, thinly sliced (optional) | 1 |
| small yellow onion, thinly sliced into rings | 1 |
| small yellow onion, very thinly sliced | 1 |
| small yellow onions (each about 2 inches in diameter) | 1 |
| small yellow onions, cut in 1/2 and sliced thin | 1 |
| small yellow onions, cut into 24 very thin rounds | 1 |
| small yellow or 1/4 red onion | 3 |
| small yellow or red onion | 1 |
| small yellow or white onion, halved and thinly sliced | 1 |
| small yellow or white onion, thinly sliced | 1 |
| small yellow or1/4 red onion | 1 |
| small yellow skinned onion | 9 |
| small yellow-skinned onion | 1 |
| small-dice sweet onion | 1 |
| small-dice yellow onion | 1 |
| small-diced onion | 7 |
| small-diced onion (about 1 medium onion) | 1 |
| small-diced red onion | 7 |
| small-diced red onion (1 small onion) | 12 |
| small-diced red onion (2 onions) | 1 |
| small-diced red onion (about 2 pounds) | 1 |
| small-diced sweet onion | 2 |
| small-diced white onion | 2 |
| small-diced yellow onion | 4 |
| small-medium onion | 1 |
| small-size yellow onion | 1 |
| smallish red onion | 1 |
| smashed new potatoes with peas, lemon, and pearl onions, recipe follows | 1 |
| smoked salmon, crème fraîche, and sliced spring onions (optional) | 1 |
| smothered onions or sour cream (accompaniments) | 1 |
| soak the red onion in cold water, 10 minutes; drain and pat dry | 1 |
| soft rolls (such as onion, egg, sesame, or whole wheat) | 1 |
| sour cream and onion dip , saffron mayonnaise , ginger-sesame sauce , roasted red pepper-walnut dip , and/or chipotle-tomatillo sauce | 1 |
| sour cream-and-onion potato chips (about 7 ounces) | 1 |
| spanish onion | 154 |
| spanish onion - peeled, cut in half, and thinly sliced | 1 |
| spanish onion finely chopped | 1 |
| spanish onion sliced very thin | 1 |
| spanish onion thinly sliced | 1 |
| spanish onion, 1/2-inch dice | 1 |
| spanish onion, 1/4-inch dice | 2 |
| spanish onion, 1/4-inch sliced root to tip | 1 |
| spanish onion, cut in small dice | 1 |
| spanish onion, cut into 1-inch dice | 1 |
| spanish onion, cut into 1/2-inch slices | 1 |
| spanish onion, cut into 1/4-inch dice | 10 |
| spanish onion, cut into 1/4-inch slices | 2 |
| spanish onion, cut into 3/4-inch dice | 1 |
| spanish onion, cut into brunoise | 1 |
| spanish onion, cut into medium dice | 1 |
| spanish onion, halved and thinly sliced | 3 |
| spanish onion, julienne | 2 |
| spanish onion, julienne cut | 1 |
| spanish onion, julienned | 1 |
| spanish onion, quartered | 3 |
| spanish onion, sauteed in butter | 1 |
| spanish onion, small dice | 6 |
| spanish onion, small diced | 4 |
| spanish onion, thickly sliced | 1 |
| spanish onion, thinly sliced | 8 |
| spanish onion, very thinly sliced | 1 |
| spanish onions (1 quartered, 1 thinly sliced) | 1 |
| spanish onions, cut into 1-inch dice | 1 |
| spanish onions, cut into 1/2-inch dice | 1 |
| spanish onions, cut into 1/4-inch dice | 2 |
| spanish onions, cut into 1/8inch ribbons | 1 |
| spanish onions, halved and thinly sliced | 1 |
| spanish onions, julienne | 1 |
| spanish onions, julienne cut | 1 |
| spanish onions, medium dice | 2 |
| spanish onions, quartered | 2 |
| spanish onions, quartered, in the skins | 1 |
| spanish onions, skin on | 1 |
| spanish onions, small dice | 2 |
| spanish onions, thinly sliced | 7 |
| spanish onions: | 1 |
| spanish or sweet onion, thickly sliced | 1 |
| spanish sweet onion | 1 |
| spanish yellow onion | 1 |
| spanish yellow onion, medium | 1 |
| spice islands onion powder | 1 |
| spice rubbed grilled vidalia onions, recipe follows | 1 |
| spiced onion marmalade | 1 |
| spinach salad with apple and red onion, as an accompaniment, recipe follows | 1 |
| sprigs green onion | 1 |
| sprigs spring onion | 1 |
| spring (green) onion | 1 |
| spring (pearl) onion | 1 |
| spring onion (green part only) | 1 |
| spring onion (green) | 2 |
| spring onion oil | 2 |
| spring onion or baby leek | 1 |
| spring onion or green onion, white part only | 1 |
| spring onion stalks | 1 |
| spring onion, cut into 2-inch lengths | 1 |
| spring onion, julienned | 1 |
| spring onion, thinly sliced on diagonal | 1 |
| spring onion, very finely chopped | 1 |
| spring onion, white part only, crushed slightly | 1 |
| spring onions (about 1 pound), root ends trimmed | 1 |
| spring onions (green part only) | 2 |
| spring onions (green) | 4 |
| spring onions (scallions) | 6 |
| spring onions (scallions), cut into 2 inch-lengths | 1 |
| spring onions (scallions), cut into 2-inch/ 5 cm lengths | 1 |
| spring onions (scallions), cut into 2-inch/5 cm lengths | 1 |
| spring onions (scallions), thinly sliced | 1 |
| spring onions (white part only) | 1 |
| spring onions or 1 medium yellow onion | 1 |
| spring onions or 12 scallion | 1 |
| spring onions or 4 scallions, trimmed and thinly sliced | 1 |
| spring onions or 4 scallions, white and pale-green parts only, thinly sliced | 1 |
| spring onions or 6 scallions, bulbs halved, dark-green parts discarded | 1 |
| spring onions or 6 scallions, whites only, thinly sliced | 1 |
| spring onions or green onion | 1 |
| spring onions or green onions (dark green parts discarded); white parts cut into 1/4-inch-thick slices, pale green parts cut into 1/2-inch-thick slices | 1 |
| spring onions or green onions (dark green parts discarded); white parts cut into 1/4-inch-thick slices, pale green parts cut into 1/2-inchthick slices (scant 2 cups) | 1 |
| spring onions or large scallions (about 8 bunches) | 1 |
| spring onions or large scallions, bulbs separated from tops | 1 |
| spring onions or scallion | 2 |
| spring onions or scallions (white and light green parts only), thinly sliced | 1 |
| spring onions or scallions, halved lengthwise | 1 |
| spring onions or scallions, thinly sliced | 1 |
| spring onions or scallions, whites halved and sliced; greens sliced on a diagonal | 1 |
| spring onions or small regular onions trimmed and halved | 1 |
| spring onions or white onion, thinly sliced | 1 |
| spring onions with enough vegetable stock to cover | 1 |
| spring onions, (white part only) sliced | 1 |
| spring onions, bashed | 1 |
| spring onions, cut in half | 1 |
| spring onions, cut into 1 1/2-inch/4 cm lengths | 1 |
| spring onions, cut into 1/2-inch dice | 1 |
| spring onions, cut into 2-inch pieces | 2 |
| spring onions, halved if large | 1 |
| spring onions, halved lengthwise, or 8 scallions (left whole) | 1 |
| spring onions, root and stem trimmed | 1 |
| spring onions, root trimmed off | 1 |
| spring onions, stems removed, cut in 1/2 | 1 |
| spring onions, thinly chopped on the bias | 1 |
| spring onions, thinly sliced | 6 |
| spring onions, thinly sliced including green tops | 1 |
| spring onions, thinly sliced on the bias | 1 |
| spring onions, trimmed | 1 |
| spring onions, trimmed and chopped | 1 |
| spring onions, very finely sliced | 1 |
| spring onions, white part only | 1 |
| spring onions, white part only, thinly sliced | 1 |
| spring onions, white part only, very finely chopped | 1 |
| spring onions, white parts only, thinly sliced | 1 |
| stalk green onion | 1 |
| stalk spring onion (optional) | 1 |
| stalks fresh green onion | 1 |
| stalks green onion | 7 |
| stalks green onions, julienned | 1 |
| stalks green onions, thinly sliced | 1 |
| stalks spring onions or scallions, green tops thinly sliced and bottom white half sliced in half lengthwise | 1 |
| steak dust (recommended: bob tallman's cowboy blend of garlic, black pepper, sea salt, onion, and sugar) | 1 |
| stems green onion | 1 |
| stonemill minced onion | 1 |
| store-bought caramelized onion | 1 |
| store-bought crispy shallots or onions, to serve | 1 |
| store-bought fried onion | 2 |
| store-bought fried shallots or onion | 2 |
| strips bacon (about 8 ounces), cut into 1/2-inch pieces 1 medium vidalia onion, halved and thinly sliced 1 stick butter | 1 |
| strips green onion | 1 |
| strips of green onion, for garnish | 1 |
| sugar (helps the onions to brown) | 1 |
| suggested toppings: crispy bacon, french-fried onions, crushed tortilla chips | 1 |
| summer pearl onion | 1 |
| sweet (vidalia or maui) onion | 1 |
| sweet and sour onion compote, recipe follows | 1 |
| sweet and sour onions, plus more for serving, recipe follows | 1 |
| sweet maui onion | 2 |
| sweet maui onion, 1/2 whole, 1/2 diced | 1 |
| sweet maui or vidalia onion | 1 |
| sweet onion | 195 |
| sweet onion (1/2 pound) | 1 |
| sweet onion (3/4 pound) such as vidalia, ososweet, or walla walla, halved lengthwise and thinly sliced | 1 |
| sweet onion (maui or vidalia) | 2 |
| sweet onion (recommended: walla walla) chopped | 1 |
| sweet onion (such as maui or vidalia), halved lengthwise, thinly sliced | 1 |
| sweet onion (such as maui or vidalia), thinly sliced | 1 |
| sweet onion (such as vidalia or walla walla), cut into 1/3-inch-thick slices | 1 |
| sweet onion (such as vidalia or walla walla), halved and thinly sliced | 1 |
| sweet onion (such as vidalia) | 1 |
| sweet onion (such as vidalia), thinly sliced | 1 |
| sweet onion (such as vidalia®) | 20 |
| sweet onion (such as vidalia®), thinly sliced | 2 |
| sweet onion (such as walla walla) | 1 |
| sweet onion and sage gratin, recipe follows | 1 |
| sweet onion crepe filling, recipe follows | 1 |
| sweet onion cut in 1/4-inch-thick rounds | 1 |
| sweet onion cut into 1/2-inch slices | 1 |
| sweet onion diced | 1 |
| sweet onion jam, recipe follows | 1 |
| sweet onion such as vidalia | 1 |
| sweet onion such as vidalia (1/2 lb), trimmed and cut crosswise into 6 slices | 1 |
| sweet onion such as vidalia or walla walla, thinly sliced | 1 |
| sweet onion, cut in half lengthwise and then crosswise into 1/4-inch slices | 2 |
| sweet onion, cut into 1-inch chunks | 1 |
| sweet onion, cut into 1-inch rings | 1 |
| sweet onion, cut into 1/2-inch dice | 1 |
| sweet onion, cut into 1/2-inch pieces | 1 |
| sweet onion, cut into 1/2-inch wedges | 1 |
| sweet onion, cut into 1/4-inch dice | 2 |
| sweet onion, cut into 1/4-inch dice (2 cups) | 1 |
| sweet onion, cut into 1/4-inch rings | 1 |
| sweet onion, cut into 1/4-inch slices | 1 |
| sweet onion, cut into 1/4-inch wide rings | 1 |
| sweet onion, cut into bite-size pieces | 2 |
| sweet onion, cut into julienne strips | 1 |
| sweet onion, cut into large dice | 1 |
| sweet onion, cut into strips | 1 |
| sweet onion, cut into thin slivers | 1 |
| sweet onion, cut into wedges | 4 |
| sweet onion, half rough chopped and half finely diced | 1 |
| sweet onion, halved and cut into slices (the size and shape of the fortune in a fortune cookie) | 1 |
| sweet onion, halved and sliced | 1 |
| sweet onion, like maui or vidallia, rough chopped | 1 |
| sweet onion, preferably vidalia | 1 |
| sweet onion, quartered | 3 |
| sweet onion, rough chopped, medium/large size pieces | 1 |
| sweet onion, small dice | 1 |
| sweet onion, such as a walla walla, cubed | 1 |
| sweet onion, such as vidalia | 5 |
| sweet onion, such as vidalia, thinly sliced | 1 |
| sweet onion, such as walla walla | 1 |
| sweet onion, thinly sliced | 13 |
| sweet onion, thinly sliced (about 1 cup) | 1 |
| sweet onion, thinly sliced or chopped | 1 |
| sweet onion, very finely chopped | 2 |
| sweet onion, very thinly sliced | 1 |
| sweet onions (like vidalias) or a combination of sweet and red onion | 1 |
| sweet onions (like vidalias) or a combination of sweet and red onions (about 4 pounds) | 1 |
| sweet onions (such as maui) | 1 |
| sweet onions (such as vidalia or maui), halved, thinly sliced | 1 |
| sweet onions (such as vidalia or walla walla), thinly sliced into rounds, then separated into rings | 1 |
| sweet onions (such as vidalia) | 1 |
| sweet onions (such as vidalia, walla walla, or maui onions) | 1 |
| sweet onions (such as vidalia; about 2 1/2 pounds total) | 1 |
| sweet onions (such as vidalia®) | 3 |
| sweet onions (such as vidalia®), cut into wedges | 1 |
| sweet onions (such as vidalia®), quartered | 1 |
| sweet onions (vidalia or walla walla) | 1 |
| sweet onions, (such as vidalia, walla walla or maui) | 1 |
| sweet onions, cut into 1/2-inch slices | 1 |
| sweet onions, cut into 3/4-inch chunks | 1 |
| sweet onions, cut into thin strips | 1 |
| sweet onions, skin-on, and cut into 1/4-inch thick slices | 1 |
| sweet onions, thickly sliced | 1 |
| sweet onions, thinly sliced | 1 |
| sweet onions, very thinly sliced | 1 |
| sweet onions, vidalia or texas sweets, thinly sliced | 1 |
| sweet or red onion | 1 |
| sweet red onion | 6 |
| sweet red onion, shaved or sliced paper thin | 1 |
| sweet red onion, thinly sliced | 1 |
| sweet spanish onion, thinly sliced | 1 |
| sweet vidalia onion | 4 |
| sweet vidalia or maui onion | 1 |
| sweet white onion | 3 |
| sweet white onion (maui or vidalia) | 1 |
| sweet yellow onion | 9 |
| sweet yellow onion (such as vidalia®), thinly sliced | 1 |
| sweet yellow onion, cut into wedges | 1 |
| sweet yellow onion, quartered | 1 |
| sweet yellow onion, thinly sliced | 2 |
| t minced fresh onion | 1 |
| t. chopped onion | 1 |
| tablespoosn minced onion | 1 |
| tangerine-green onion relish, recipe follows | 1 |
| tangy red onions, recipe follows | 1 |
| tarator sauce ; chopped tomatoes; chopped onion; pita bread | 1 |
| tartar sauce, such as pike place fish smoked walla walla onion tartar sauce | 1 |
| tbs finely minced onions or scallion | 1 |
| tbs onion powder | 1 |
| tbs. chopped onion | 1 |
| tbs. finely diced red onion | 1 |
| tbs. fried onion | 1 |
| tbs. minced onion | 1 |
| tbs.minced white onion | 1 |
| tbsp.crisp-fried onion | 1 |
| tehina onion sauce, recipe follows | 1 |
| tempura onions, recipe follows | 1 |
| texas onions (spring onions) | 1 |
| texas sweet onion diced | 1 |
| thawed frozen pearl onion | 1 |
| the pearl onions reserved from the herbed roast leg of lamb | 1 |
| thick onion slices | 1 |
| thick slice onion | 1 |
| thick slice red onion, all rings intact | 1 |
| thick sliced onion | 1 |
| thick slices red onion | 2 |
| thickly sliced white onion | 1 |
| thin green onion | 1 |
| thin onion slice | 1 |
| thin onion slices | 1 |
| thin onion slices, separated in rings | 1 |
| thin onion slices, separated into rings | 1 |
| thin red onion rings | 1 |
| thin red onion slices | 3 |
| thin red onion slices, cut in half | 1 |
| thin red onion slices, rings separated | 1 |
| thin slice onion | 2 |
| thin slice red onion | 3 |
| thin slice red onion, separated into rings | 1 |
| thin sliced red onion | 2 |
| thin sliced red onion (1/6-inch half rounds) | 1 |
| thin slices of red onion | 4 |
| thin slices of red onion, cut into thin half moons | 1 |
| thin slices onion, separated into rings | 2 |
| thin slices red onion | 11 |
| thin slices red onion (from 1 medium onion) | 1 |
| thin slices red onion (optional) | 1 |
| thin slices red onion, separated into rings | 1 |
| thin slices sweet onion | 2 |
| thin slices sweet onion, separated into rings | 1 |
| thin slices vidalia onion | 1 |
| thin slices white onion | 3 |
| thin slices white onion, separated into rings | 1 |
| thin slices yellow onion | 1 |
| thin slivers red onion | 1 |
| thin strips green onion | 1 |
| thin-sliced (height wise) red or vidalia onion | 1 |
| thin-sliced green onion | 1 |
| thin-sliced green onion (optional) | 1 |
| thin-sliced red onion | 2 |
| thin-sliced red onion, separated into rings | 1 |
| thinly chopped napa valley spring onions, about 2, green and white portion | 1 |
| thinly cut yellow onion half | 1 |
| thinly sliced caramelized onion | 1 |
| thinly sliced dole red onion | 3 |
| thinly sliced green onion | 166 |
| thinly sliced green onion (green and pale green part) | 1 |
| thinly sliced green onion (optional) | 1 |
| thinly sliced green onion for garnish | 2 |
| thinly sliced green onion or spring onion | 1 |
| thinly sliced green onion tops | 1 |
| thinly sliced green onion, for garnish | 3 |
| thinly sliced green onion, including green part | 1 |
| thinly sliced green onion, white and pale green portions | 1 |
| thinly sliced green onions (about 1/2 cup) | 1 |
| thinly sliced green onions (about 4 green onions) | 1 |
| thinly sliced green onions (about 4) | 1 |
| thinly sliced green onions (about 5) | 1 |
| thinly sliced green onions (about 6) | 2 |
| thinly sliced green onions (green part only) | 1 |
| thinly sliced green onions (optional) | 1 |
| thinly sliced green onions (white and pale green parts only) | 1 |
| thinly sliced green onions, crumbled crisp bacon, sour cream, sieved hard-cooked egg, and thin lemon slices, for garnish | 1 |
| thinly sliced green onions, for garnish | 4 |
| thinly sliced green onions, green part only | 1 |
| thinly sliced green onions, including tops | 1 |
| thinly sliced green onions, plus more for serving | 1 |
| thinly sliced green onions, white and green parts | 1 |
| thinly sliced green onions, white part only (from about 3) | 1 |
| thinly sliced green onions, whites and green parts | 1 |
| thinly sliced green onions, with some of the green tops | 1 |
| thinly sliced green or red onion | 1 |
| thinly sliced large onion | 1 |
| thinly sliced leeks or finely chopped onion | 1 |
| thinly sliced medium onion | 2 |
| thinly sliced medium red onion | 1 |
| thinly sliced onion | 89 |
| thinly sliced onion (1 large) | 1 |
| thinly sliced onion (about 1 small onion) | 1 |
| thinly sliced onions (2 1/2 pounds) | 1 |
| thinly sliced onions (2 medium) | 1 |
| thinly sliced onions (about 1 1/2 pounds) | 1 |
| thinly sliced onions (about 1 pound) | 1 |
| thinly sliced onions (about 2) | 1 |
| thinly sliced onions (about 2-1/2 pounds) | 1 |
| thinly sliced onions (about 5 3/4 pounds) | 1 |
| thinly sliced pickled red onion | 1 |
| thinly sliced raw onion | 1 |
| thinly sliced red onion | 163 |
| thinly sliced red onion (about 1 pound) | 1 |
| thinly sliced red onion (about 1/2 large onion) | 1 |
| thinly sliced red onion (about 1/2 medium) | 1 |
| thinly sliced red onion (garnish) | 1 |
| thinly sliced red onion (like paper thin!) | 1 |
| thinly sliced red onion (optional) | 2 |
| thinly sliced red onion or coarsely grated radishes | 1 |
| thinly sliced red onion rings | 2 |
| thinly sliced red onion rounds | 1 |
| thinly sliced red onion, (julienne) | 2 |
| thinly sliced red onion, for garnish | 2 |
| thinly sliced red onion, for serving | 1 |
| thinly sliced red onion, for topping | 2 |
| thinly sliced red onion, rinsed and drained if desired | 1 |
| thinly sliced red onions (about 3 1/4 pounds) | 1 |
| thinly sliced red onions (about 4 medium) | 1 |
| thinly sliced red onions or sweet onions, for topping | 1 |
| thinly sliced red onions, for garnish | 1 |
| thinly sliced red onions, for serving | 1 |
| thinly sliced red onions, soaked in cold water to cover for 10 minutes, drained, and patted dry | 1 |
| thinly sliced red onions, soaked in ice water for 15 min utes and drained | 1 |
| thinly sliced red pearl onions or shallots | 1 |
| thinly sliced rings red onion | 1 |
| thinly sliced shallots or onion | 1 |
| thinly sliced small red onion | 4 |
| thinly sliced spanish onion (reserve other 1/2 for pasta water) | 1 |
| thinly sliced spring onions or scallion | 1 |
| thinly sliced strips red onion | 1 |
| thinly sliced sweet onion | 4 |
| thinly sliced sweet onion (about 2 onions) | 1 |
| thinly sliced sweet onion (such as maui or vidalia) | 1 |
| thinly sliced sweet onion (such as vidalia or maui; optional) | 1 |
| thinly sliced sweet onion, for garnish | 1 |
| thinly sliced sweet red or vidalia onion | 1 |
| thinly sliced vidalia onion | 2 |
| thinly sliced vidalia onions or other sweet onion | 1 |
| thinly sliced vidalia onions, see cook note* | 1 |
| thinly sliced vidalia or spanish onion | 1 |
| thinly sliced vidalia or texas sweet onion | 1 |
| thinly sliced white onion | 9 |
| thinly sliced yellow onion | 13 |
| thinly sliced yellow onion (about 2 large onions) | 1 |
| thinly sliced yellow onion (about 2 medium yellow onions) | 1 |
| thinly sliced yellow onion (about 2 small onions) | 1 |
| thinly sliced yellow onions (2 large onions) | 2 |
| thinly sliced yellow onions or leeks, sauteed in butter or extravirgin olive oil | 1 |
| thinly sliced, dehydrated, and crushed maui onion | 1 |
| thinly slivered red onion | 1 |
| thinly-sliced onion | 2 |
| thinly-sliced red onion | 1 |
| thinly-sliced white onion | 1 |
| three 1/4-inch slices red onion | 1 |
| three-onion cherry jam, recipe follows | 1 |
| three-onion marmalade, recipe follows | 1 |
| tiny scallions or spring onion | 1 |
| tiny spring onion | 1 |
| to 1 1/4 pounds red onions, thinly sliced | 1 |
| to 1 small or medium red onion | 2 |
| to 1 teaspoon onion powder | 1 |
| to 1 teaspoon onion powder or to taste | 1 |
| to 1 whole large onion | 1 |
| to 1/2 cup diced maui onions or red onion | 1 |
| to 1/2 cup diced onion | 1 |
| to 1/2 cup sauteed sliced red onion | 1 |
| to 1/2 red onion | 1 |
| to 10 cipollini onion | 1 |
| to 10 pearl onion | 1 |
| to 12 pearl onions or 1 large onion | 1 |
| to 12 slices red onion | 1 |
| to 12 small white onions (pearl or boiling onions), very thinly sliced | 1 |
| to 12 super-thin slices red onion | 1 |
| to 15 onion slider rolls | 1 |
| to 15 thinly sliced pieces red onion | 1 |
| to 16 knob onions, or calcots | 1 |
| to 2 cups bagged frozen onions and red bell pepper mixture | 1 |
| to 2 cups canola oil, as needed, for frying the onion rings | 1 |
| to 2 cups vegetable broth (carrot, celery, onion, parsley stems, 1 clove, 2 bay leaves) | 1 |
| to 2 green onion | 2 |
| to 2 large vidalia onion | 1 |
| to 2 rings red onion | 1 |
| to 2 sweet onion | 1 |
| to 2 tablespoons diced onion | 1 |
| to 2 tablespoons minced shallots or green onion | 1 |
| to 2 teaspoon garlic or onion powder | 2 |
| to 2 teaspoons onion powder | 1 |
| to 2 vidalia onions (available seasonally at specialty produce markets and some supermarkets) | 1 |
| to 20 baby onion | 1 |
| to 20 cornichon and/or pickled onion | 1 |
| to 20 pearl onion | 1 |
| to 20 vidalia onion | 1 |
| to 24 brown-braised onions, recipe follows | 1 |
| to 24 large shallots, about 1 pound (small onions may be substituted) | 1 |
| to 24 pearl onion | 1 |
| to 24 pearl white and/or red onions, oven roasted and peeled | 1 |
| to 24 peeled white onions, about 1-inch in diameter | 1 |
| to 24 small white onions, brown-braised in stock | 1 |
| to 3 cups prepared vegetables, such as braised leeks, broccoli, sauteed onions, mushrooms, spinach, peppers, tomato | 1 |
| to 3 cups very coarsely chopped onion | 1 |
| to 3 cups vidalia onions cut into 1-inch slivers | 1 |
| to 3 fresh spring onions or 2 cups very thinly sliced medium white onion | 1 |
| to 3 green onion | 1 |
| to 3 green onions, (dark and pale green part) thinly sliced | 1 |
| to 3 green onions, thinly sliced on the diagonal | 1 |
| to 3 green onions, white and pale green parts only | 3 |
| to 3 green onions/scallions | 1 |
| to 3 large yellow onions (about 2 lb), halved, thinly sliced, then halved again | 1 |
| to 3 medium sweet onions, such as vidalia | 2 |
| to 3 medium white onion | 1 |
| to 3 onion | 3 |
| to 3 onions, thinly sliced | 1 |
| to 3 peeled whole onion | 1 |
| to 3 scallions or spring onion | 1 |
| to 3 tablespoons minced onion (optional) | 1 |
| to 3 tablespoons minced shallot or onion | 1 |
| to 3 teaspoons freshly chopped green onion | 1 |
| to 3 white onion | 1 |
| to 3/4 cup caramelized onion-tomato jam | 1 |
| to 30 pearl onion | 1 |
| to 4 green onions, green parts only | 1 |
| to 4 green onions, thinly sliced | 2 |
| to 4 green onions, trimmed and sliced crosswise into 1/2-inch pieces | 1 |
| to 4 pounds onions, thinly sliced | 1 |
| to 4 tablespoons grated onion | 2 |
| to 4 tablespoons grated red onion | 1 |
| to 4 thin rings red onion | 1 |
| to 4 very thin slices red or sweet onion | 1 |
| to 4.5 lbs yellow onions, thinly sliced | 1 |
| to 5 green onion | 1 |
| to 5 green onions (up to the middle of the dark green part) | 1 |
| to 5 green onions, thinly sliced | 1 |
| to 5 green onions, white and green parts | 1 |
| to 5 spanish onion | 1 |
| to 5 whole baby onions (optional) | 1 |
| to 6 cups medium-dice mixed carrots, celery and red onion | 1 |
| to 6 tablespoons minced onion | 1 |
| to 6 yellow onions (small dice) | 1 |
| to 7 cups spinach, bacon, and cashew stuffing (see stuffed onions ) | 1 |
| to 8 medium whole shallots or 1 large onion cut into 6 wedges | 1 |
| to 8 ounces of shallots (about 7 or 8 large ones) -if you can?t find shallots, use an equal amount of sweet onion | 1 |
| to 8 pickled onion | 1 |
| to 8 small onion | 1 |
| to 8 stalks green onion | 1 |
| toast points with roasted garlic, caramelized onions, and goat cheese, recipe follows | 1 |
| toasted breadcrumbs or fried onion | 1 |
| toasted sesame seeds and fresh daikon radish or onion sprouts, as garnish | 1 |
| toasted sesame seeds and sliced green onions (optional) | 1 |
| tomato and onion salad, as an accompaniment | 1 |
| tomato and onion salad, recipe under this show number: tm1a04 | 1 |
| tomato and red onion chutney | 1 |
| tomato onion chutney | 1 |
| tomatoes and onions, recipe follows | 1 |
| toppings such as pepperoni, cooked sausage, garlic, onions and pepper | 1 |
| toppings: cubed avocado, cubed mango, thinly sliced red onion, crumbled queso fresco, cilantro and lime wedges | 1 |
| toppings: lettuce, tomato, red onion, and sliced avocado | 1 |
| toppings: lettuce, tomato, red onion, thinly sliced fresh mozzarella and torn fresh basil leaf | 1 |
| toppings: tortilla chips; sour cream; grated cheddar; chopped red onions; chopped jalapenos; diced avocado; minced cilantro; etc | 1 |
| trimmed thinly sliced green onion | 1 |
| tub philadelphia chive & onion cream cheese spread | 2 |
| turmeric, ground cumin, ground coriander, smoked sweet or sweet paprika, granulated onion or onion powder* | 1 |
| twelve 1/4-inch-thick lengthwise slices of red onion with root ends intact (about 4 onions) | 1 |
| two 10-ounce cans french onion soup | 1 |
| two large sweet onions thin sliced | 1 |
| two white cocktail onion | 1 |
| unpeeled medium onion | 1 |
| unpeeled onion | 1 |
| unpeeled onions, quartered | 1 |
| variety of pickles such as regular, pickled red onions and pickled jalapenos | 1 |
| vegetable mix, (sauteed zucchini, bell pepper and onion) | 1 |
| vertically sliced onion | 1 |
| very finely chopped onion | 1 |
| very finely chopped yellow onion | 1 |
| very finely minced onion | 1 |
| very large (14- to 16-ounce) red onion | 1 |
| very large onion | 2 |
| very large onion, halved through root end, cut lengthwise into 1/3-inch-thick slices (about 4 cups) | 1 |
| very large onions (2 pound total), cut crosswise into 1/4-inch-thick slices | 1 |
| very large red onion, halved | 1 |
| very large red onion, halved and sliced 1/3 inch thick | 1 |
| very large red onion, thinly sliced (about 3 cups) | 1 |
| very large red onions, halved lengthwise, thinly sliced crosswise (about 5 cups) | 1 |
| very large spanish onion | 1 |
| very large sweet onions (such as vidalia®), thinly sliced | 1 |
| very large yellow onion | 1 |
| very small onion, cut into 1/2-inch rounds | 1 |
| very small purple onion | 1 |
| very small red onion | 1 |
| very small red onion, thinly sliced | 1 |
| very thin onion slices | 1 |
| very thin slices green onion tops | 1 |
| very thin slices red onion | 2 |
| very thin slices red onion, rings separated | 1 |
| very thin slices red onion, separated | 1 |
| very thinly sliced green onion | 2 |
| very thinly sliced green onions, white and green parts | 1 |
| very thinly sliced maui, or another sweet, onion | 1 |
| very thinly sliced onion | 6 |
| very thinly sliced onion (about 2 onions) | 1 |
| very thinly sliced red onion | 12 |
| very thinly sliced red onion (about 1/4 onion) | 1 |
| very thinly sliced red onion (from 1 small) | 1 |
| very thinly sliced red onions, for serving | 1 |
| very thinly sliced spanish onion | 1 |
| very thinly sliced sweet onion | 1 |
| very thinly sliced white onion | 1 |
| very, very finely chopped onion, almost grated (use a food processor) | 1 |
| vidahlia onion | 1 |
| vidalia (or other sweet variety) onion | 1 |
| vidalia onion | 76 |
| vidalia onion (available seasonally at specialty produce markets and some supermarkets) | 1 |
| vidalia onion dressing | 1 |
| vidalia onion or other sweet onion | 1 |
| vidalia onion or other sweet yellow onion, halved and sliced | 1 |
| vidalia onion, cut in rings | 1 |
| vidalia onion, cut into 1/2-inch disks | 1 |
| vidalia onion, cut into 1/4-inch dice | 1 |
| vidalia onion, cut into 1/4-inch thick slices | 1 |
| vidalia onion, cut into bite-size pieces | 1 |
| vidalia onion, cut julienne style | 1 |
| vidalia onion, grilled and thinly sliced | 1 |
| vidalia onion, halved lengthwise and cut crosswise into 1/4-inch slices | 1 |
| vidalia onion, julienned | 1 |
| vidalia onion, medium dice | 1 |
| vidalia onion, rough chopped | 1 |
| vidalia onion, shaved | 1 |
| vidalia onion, skin removed | 1 |
| vidalia onion, thickly sliced | 1 |
| vidalia onion, thin julienne | 1 |
| vidalia onion, thinly sliced | 7 |
| vidalia onion, thinly sliced and divided into rings | 1 |
| vidalia onion, thinly sliced on a mandoline | 1 |
| vidalia onion, very finely sliced | 2 |
| vidalia onions (about 4 medium), halved lengthwise | 1 |
| vidalia onions (or other sweet onion, such as maui), cut into 1/4-inch thick slices and separated into rings | 1 |
| vidalia onions, cut into 1/4-inch thick slices | 1 |
| vidalia onions, cut into large dice | 1 |
| vidalia onions, cut into rings | 1 |
| vidalia onions, cut into thin strips | 1 |
| vidalia onions, halved and thinly sliced | 1 |
| vidalia onions, julienned (if not in season, any sweet onion will do) | 2 |
| vidalia onions, thickly sliced | 1 |
| vidalia onions, thinly sliced | 9 |
| vidalia or another sweet onion | 1 |
| vidalia or bermuda onion | 1 |
| vidalia or other sweet onion | 2 |
| vidalia or other sweet onion, halved and thinly sliced | 1 |
| vidalia or other sweet onion, medium dice (3 cups) | 1 |
| vidalia or other sweet onion, such as walla walla or maui | 1 |
| vidalia or other sweet onions, skin on | 1 |
| vidalia or red onion, cut in 1/2 and thinly sliced into half-moons | 1 |
| vidalia or sweet onion | 4 |
| vidalia or sweet onion pulp (grated on the large holes of a box grater) | 1 |
| vidalia or white onion | 1 |
| vidalia or white onion, cut into 1/4-inch thick rings | 1 |
| vidalia spring onion | 1 |
| vidalia sweet onions, quartered | 1 |
| vidalia, texas sweet or other sweet onion variety, cut in thin strips | 1 |
| vinegar (steve uses white vinegar with jalepeno peppers, onions, etc.) | 1 |
| vinegar-pickled onion | 1 |
| walla walla onion | 1 |
| wasabi fried onions, recipe follows | 1 |
| water, plus 2 cups3 tablespoons finely chopped red onion | 1 |
| wedge large white onion | 1 |
| wedge of large white onion | 1 |
| while onion | 1 |
| white and/or purple pearl onions (about 7 ounces) | 1 |
| white boiling onions (about 9 ounces total), thinly sliced | 1 |
| white colossal onion | 2 |
| white onion | 372 |
| white onion (about 3 1/2 ounces) | 1 |
| white onion (about 4 ounces) | 1 |
| white onion (diced small) | 1 |
| white onion chopped | 1 |
| white onion coarsely chopped, covered and microwaved for 1 minute | 2 |
| white onion diced | 2 |
| white onion sliced | 2 |
| white onion sliced thin | 2 |
| white onion small diced | 1 |
| white onion, 1-inch dice | 1 |
| white onion, cut into 1/4-inch dice | 1 |
| white onion, cut into eighths | 1 |
| white onion, cut into large chunks | 1 |
| white onion, cut into large dice | 1 |
| white onion, cut into large dice, plus 1 white onion, cut into small dice | 1 |
| white onion, cut into large diced | 1 |
| white onion, cut into matchstick-size pieces | 1 |
| white onion, cut into small dice | 2 |
| white onion, cut into thin strips | 1 |
| white onion, cut julienne | 1 |
| white onion, finely dice | 1 |
| white onion, finely shaved on a mandoline | 1 |
| white onion, half roughly chopped, half finely diced | 1 |
| white onion, halved | 5 |
| white onion, halved again | 1 |
| white onion, halved and sliced 1/4-inch thick | 1 |
| white onion, halved and sliced into 1/2-inch rings | 1 |
| white onion, halved and thinly sliced | 3 |
| white onion, julienned | 1 |
| white onion, large | 1 |
| white onion, large dice | 2 |
| white onion, medium diced | 1 |
| white onion, medium slice (1/8 inch) | 1 |
| white onion, quartered | 12 |
| white onion, quartered and sliced | 1 |
| white onion, quartered, plus 1 white onion | 1 |
| white onion, quartered, plus 1/2 cup | 1 |
| white onion, sauteed | 2 |
| white onion, small dice | 3 |
| white onion, small diced | 1 |
| white onion, such as maui onion, julienned | 1 |
| white onion, thickly sliced | 1 |
| white onion, thinly cut julienne | 1 |
| white onion, thinly julienned | 1 |
| white onion, thinly sliced | 13 |
| white onion, thinly sliced (about 1 pound) | 1 |
| white onion, thinly sliced and blanched in boiling water | 1 |
| white onion, thinly sliced, or more to taste | 1 |
| white onion, very finely diced | 1 |
| white onion, very thinly sliced | 2 |
| white onions (average size) | 1 |
| white onions (not too big) | 1 |
| white onions chopped | 1 |
| white onions finely chopped | 1 |
| white onions slices | 1 |
| white onions, 1 halved, 1 quartered | 1 |
| white onions, halved and sliced into 1/2 rings | 1 |
| white onions, halved and thinly sliced | 1 |
| white onions, halved lengthwise, thinly sliced crosswise | 1 |
| white onions, halved lengthwise, thinly sliced crosswise (about 5 cups) | 1 |
| white onions, halved through core, thinly sliced crosswise (about 8 cups) | 1 |
| white onions, julienned | 2 |
| white onions, large dice | 1 |
| white onions, medium diced | 1 |
| white onions, quartered | 5 |
| white onions, quartered lengthwise, then cut lengthwise into 1/4-inch-wide wedges | 1 |
| white onions, quartered through the root end (unpeeled) | 1 |
| white onions, thickly sliced | 1 |
| white onions, thinly sliced | 7 |
| white or red onion | 1 |
| white or red onion, thinly sliced | 1 |
| white or yellow onion | 2 |
| white pearl onion | 5 |
| white pearl onions, blanched and peeled | 2 |
| white pearl onions, left unpeeled | 1 |
| white pearl onions, scored, blanched and peeled | 1 |
| white spanish onion | 1 |
| white spring onion heads | 1 |
| whole green onion | 10 |
| whole green onion plus 2 green onion | 1 |
| whole green onions (white and light green parts) | 1 |
| whole green onions, trimmed, plus 2 cups chopped green onions (for garnish) | 1 |
| whole large (or 2 small) onion | 1 |
| whole large onion | 1 |
| whole large onion, halved and sliced | 1 |
| whole medium onion | 3 |
| whole medium white onion | 1 |
| whole onion | 19 |
| whole onion, halved and thinly sliced (or diced if you prefer) | 1 |
| whole onion, whatever kind you prefer | 1 |
| whole onions (large) | 1 |
| whole red onion | 4 |
| whole small red onions, halved and sliced | 1 |
| whole small to medium onion | 2 |
| whole wheat or onion pita breads, cut in half crosswise | 1 |
| whole white onion | 1 |
| whole yellow onion | 1 |
| wide onion rings | 1 |
| yellow (brown) onions, thinly sliced | 1 |
| yellow onion | 654 |
| yellow onion (10/15 if possible) | 1 |
| yellow onion (about 1/4 of a small onion) | 1 |
| yellow onion (chopped) | 1 |
| yellow onion - ends trimmed off | 1 |
| yellow onion charred (see chef's tip, below) | 1 |
| yellow onion peeled and chopped | 1 |
| yellow onion peeled plus 1 medium yellow onion | 1 |
| yellow onion shredded and sauteed | 1 |
| yellow onion slice | 1 |
| yellow onion sliced | 1 |
| yellow onion sliced thin in 1/2-inch circles | 1 |
| yellow onion slices | 1 |
| yellow onion, 1 small | 1 |
| yellow onion, 1/4-inch dice | 1 |
| yellow onion, 1/4-inch diced | 2 |
| yellow onion, 1/8-inch diced | 3 |
| yellow onion, brunoise | 1 |
| yellow onion, cubed | 1 |
| yellow onion, cut crosswise into 1/2-inch thick slices | 1 |
| yellow onion, cut in 1/2 and thinly sliced | 2 |
| yellow onion, cut in half | 1 |
| yellow onion, cut in small pieces | 1 |
| yellow onion, cut into 1-inch chunks | 1 |
| yellow onion, cut into 1-inch pieces | 1 |
| yellow onion, cut into 1/2-inch chunks | 1 |
| yellow onion, cut into 1/2-inch dice | 2 |
| yellow onion, cut into 1/2-inch strips | 1 |
| yellow onion, cut into 1/4-inch slices | 1 |
| yellow onion, cut into 1/4-inch wedges | 1 |
| yellow onion, cut into 1/8-inch slices | 2 |
| yellow onion, cut into 8 wedges | 1 |
| yellow onion, cut into a very small dice | 1 |
| yellow onion, cut into chunks | 1 |
| yellow onion, cut into large chunks | 4 |
| yellow onion, cut into large dice | 1 |
| yellow onion, cut into strips | 1 |
| yellow onion, cut into thick slices | 1 |
| yellow onion, cut into thirds | 1 |
| yellow onion, cut into wedges | 6 |
| yellow onion, finely ground | 1 |
| yellow onion, halved | 3 |
| yellow onion, halved and quartered | 1 |
| yellow onion, halved and sliced | 1 |
| yellow onion, halved and sliced 1/2-inch-thick | 1 |
| yellow onion, halved and sliced 1/4 inch thick | 1 |
| yellow onion, halved and thickly sliced | 1 |
| yellow onion, halved and thinly sliced | 1 |
| yellow onion, halved, with the skin left on | 1 |
| yellow onion, julienned | 4 |
| yellow onion, medium dice | 1 |
| yellow onion, quartered | 15 |
| yellow onion, quartered and sliced | 1 |
| yellow onion, quartered lengthwise | 1 |
| yellow onion, skin on, quartered | 1 |
| yellow onion, slivered | 1 |
| yellow onion, small dice | 3 |
| yellow onion, small diced, about 1/4 cup | 1 |
| yellow onion, thinly sliced | 32 |
| yellow onion, thinly sliced (1/2 cup) | 2 |
| yellow onion, thinly sliced into strips | 1 |
| yellow onion, unpeeled | 1 |
| yellow onion, whole, plus 1 onion | 1 |
| yellow onions (3 large or 4 medium) | 1 |
| yellow onions (about 1 3/4 pounds), thinly sliced with the grain to hold their shape | 1 |
| yellow onions (about 2 medium onions) | 1 |
| yellow onions (about 4 medium) cut into 1/4-inch dice | 1 |
| yellow onions (about 6 medium), halved and thinly sliced lengthwise | 1 |
| yellow onions cut into 1 1/2-inch pieces | 1 |
| yellow onions minced | 1 |
| yellow onions, 1 roughly chopped and 3 finely diced | 1 |
| yellow onions, 2 sliced and 2 finely diced | 1 |
| yellow onions, cubed | 1 |
| yellow onions, cut crosswise into 1/2-inch thick slices | 1 |
| yellow onions, cut in 1/2 and sliced (3 large) | 2 |
| yellow onions, cut in half lengthwise and crosswise into 1/4-inch slices | 2 |
| yellow onions, cut into 1-inch cubes | 1 |
| yellow onions, cut into 1-inch sections | 1 |
| yellow onions, cut into 1-inch wedges | 1 |
| yellow onions, cut into small dice | 1 |
| yellow onions, cut into wedges, plus 1 medium yellow or sweet onion | 1 |
| yellow onions, halved | 1 |
| yellow onions, halved and sliced | 4 |
| yellow onions, halved and sliced 1/2 inch thick | 2 |
| yellow onions, halved and sliced 1/4-inch thick | 1 |
| yellow onions, halved and thinly cut lengthwise | 1 |
| yellow onions, halved and thinly sliced | 2 |
| yellow onions, halved, and sliced 1/4-inch thick (8 cups) | 1 |
| yellow onions, julienne | 2 |
| yellow onions, large diced (about 4 cups) | 2 |
| yellow onions, medium dice | 1 |
| yellow onions, quartered | 3 |
| yellow onions, skins removed and reserved | 1 |
| yellow onions, small dice | 1 |
| yellow onions, sweeter the better, vidalia or texas sweets | 1 |
| yellow onions, thickly sliced | 1 |
| yellow onions, thickly sliced lengthwise | 1 |
| yellow onions, thinly sliced | 11 |
| yellow or red onion | 5 |
| yellow or white onion | 6 |
| yellow or white onion, quartered | 2 |
| yellow pearl onion | 1 |
| yellow skinned onion | 1 |
| yellow spanish onion | 2 |
| yellow sweet onion | 1 |
| your favorite condiments, such as ketchup, mustard, mayonnaise, lettuce, tomato slices, onion slices, and pickles | 1 |
| your favorite pizza toppings: sliced peppers, onions, mushrooms, etc | 1 |
| your favorite seasoning, such as garlic or onion powder | 1 |
| yucatecan pickled onion | 2 |
| ½ cups sliced yellow onion | 1 |
| ½ pounds medium or small red onion | 1 |
| ¾ cups sliced onion | 1 |

## Family-mode vs raw-regex gap details

Samples use `random.Random(20261111)` from `config/gap_audit.yaml`; each side contributes up to 30 recipe IDs.
Raw regex scans original ingredient lines for the token, including excluded products and mentions outside the ingredient head. Each sample includes its triggering source line.

### tomato

Family-not-regex recipes: **0**. Regex-not-family recipes: **5,735**. Net canonical-family minus raw-regex gap: **-5,735**.

Largest configured product exclusions observed in regex-not-family causes:

- `\btomato(?:es)?\s+(?:paste|sauce|juice|puree|purée|powder|ketchup|soup)\b`: 2,953 recipe causes
- `\btomatillos?\b`: 7 recipe causes

#### Top 20 Family-not-regex canonical variants

| Canonical variant | Recipes |
|---|---:|

#### Random sample: Family-not-regex (up to 30)

| Recipe ID | Triggering raw ingredient line | Canonical value |
|---|---|---|

#### Top 20 Regex-not-family canonical variants

| Canonical variant | Recipes |
|---|---:|
| tomato paste | 1,066 |
| can tomato sauce | 298 |
| tomato sauce | 266 |
| can tomato paste | 118 |
| tomato juice | 104 |
| tomato puree | 96 |
| cans tomato sauce | 85 |
| can condensed tomato soup | 68 |
| can diced tomatoes with green chile pepper | 59 |
| can diced tomatoes with juice | 56 |
| can tomato puree | 39 |
| tomato slices | 36 |
| can diced tomatoes with green chile peppers (such as ro*tel®) | 31 |
| can whole tomatoes in juice | 30 |
| cans condensed tomato soup | 23 |
| tomato ketchup | 23 |
| can diced tomatoes in juice | 22 |
| 14 1/2-ounce can diced tomatoes in juice | 21 |
| 28-ounce can diced tomatoes in juice | 21 |
| can diced tomatoes with green chile peppers, drained | 18 |

#### Random sample: Regex-not-family (up to 30)

| Recipe ID | Triggering raw ingredient line | Canonical value |
|---|---|---|
| `fn:N2LOCSJcZa7Fw/DKOdhFoKPVCbWHSpe` | 2 tablespoons tomato paste | tomato paste |
| `fn:o8CKGLLF9YvfxyPxUbE/6qbeeeJsIlC` | 2 tablespoons tomato paste | tomato paste |
| `epi:dqDi72Jpu6sIaXPZ3REFB5G0ARKyI6i` | 1 cup peeled, seeded, and chopped tomatoes | peeled, seeded, and chopped tomato |
| `ar:NS/sp3p61tVXcID7DHE.jczZn8Ns8d2` | 4 sun-dried tomatoes (not packed in oil), snipped into small pieces ADVERTISEMENT | sun-dried tomatoes (not packed in oil), snipped into small pieces |
| `ar:wsJIW2lk5Y1pQ7RwwMRjDGD.F9sBwMG` | 1 large tomato-flavored tortilla ADVERTISEMENT | large tomato-flavored tortilla |
| `epi:BP7mM4ey2fuQUdnthhnFtfDVVMbhXZ.` | 2 tablespoons tomato paste | tomato paste |
| `fn:XSf8/ZieWkNduj5M3FaAAP2adxH/dZG` | 20 ounces tomato juice | tomato juice |
| `ar:DDYOfbEts7DSUU22qGDQ8C7b79qJ3Cm` | 1 (14.5 ounce) can diced tomatoes with juice ADVERTISEMENT | can diced tomatoes with juice |
| `fn:CP3QB8MNFyNkZpBK0yN/hi1ot/cKlNq` | One 14-ounce can tomato sauce | one 14-ounce can tomato sauce |
| `ar:dIiihIUcd1kcd0dvCR4WIoZPUiysvsC` | 2 tablespoons tomato paste ADVERTISEMENT | tomato paste |
| `fn:Kzag2aoO5QNrA8QfZzUzVRYgHbi2khO` | 1 tablespoon tomato paste | tomato paste |
| `epi:eFIC7q.SxkKfOkkavijaA7uhy6UpM7i` | 2 pounds ripe plum tomatoes (preferably San Marzano-style), coarsely chopped, or one 28-ounce can San Marzano tomatoes in juice with basil leaves | ripe plum tomatoes (preferably san marzano-style) |
| `ar:aD74GbVslm9ekYK19b6sqLP2.h4a4Um` | 5 peeled, seeded, and chopped tomatoes ADVERTISEMENT | peeled, seeded, and chopped tomato |
| `fn:Gi0FmJ3xWWdY9QtuQ/Z28fFhDY3Rtoi` | 3 large ripe tomatoes (about 1 1/2 pounds) | large ripe tomatoes (about 1 1/2 pounds) |
| `epi:6/SmDkFN9glPtrkIhQO/YBh0lYyaXXK` | 1 1/2 tablespoons tomato paste | tomato paste |
| `ar:ZvOgs5ytLNg7YSBwOwJYqTswyO65ES.` | 2 teaspoons tomato salsa ADVERTISEMENT | tomato salsa |
| `ar:qNstvOzfG.4xjbvt9mkhQ1PCjzYN5Le` | 1 (8 ounce) can tomato sauce ADVERTISEMENT | can tomato sauce |
| `fn:13YdNsSFk6k5cFFQVbObn9XLDPCiD0a` | 4 large tomatoes cut into wedges | large tomatoes cut into wedges |
| `fn:K5zo4tIwEIJ/q7a1SmhJeiFli7QLzVm` | 1/2 cup tomato sauce | tomato sauce |
| `epi:wT3mbTnrhltU42jjmb7O9i4sABU8wQ.` | 2 (28-ounce) cans whole, peeled San Marzano tomatoes, drained and seeded | cans whole |
| `fn:qXhEORnTueHKwoIyu.PiO4x9y9yfLXu` | One 14.5-ounce can crushed tomatoes in thick puree | one 14.5-ounce can crushed tomatoes in thick puree |
| `fn:oi5C8h1tsMCChgKW.y6tZXrg01ke8A.` | 2 medium ripe tomatoes (12 ounces) | medium ripe tomatoes (12 ounces) |
| `ar:WVluoQBveLXrCaAxpjspSziOAUdapdG` | 1 (10.75 ounce) can tomato soup ADVERTISEMENT | can tomato soup |
| `ar:ZrDDXV5/ch22I4T5WQfOKhcerZUKbOi` | 1 (8 ounce) can tomato sauce ADVERTISEMENT | can tomato sauce |
| `ar:ZttBUqsl35GQ9MSDgwyQFLLXefbBrue` | 1 (28 ounce) can whole tomatoes with juice, lightly crushed with hands and pulp removed ADVERTISEMENT | can whole tomatoes with juice, lightly crushed with hands and pulp removed |
| `fn:pXFw9lDMqh2MIUCohw.9rdXkhgywHHC` | 2 tablespoons tomato paste | tomato paste |
| `fn:OHh65t2oRloU/ZzCQ.eNe36u/RKRcKS` | Two 28-ounce cans pomodori pelati tomatoes (whole peeled tomatoes), blended smooth | two 28-ounce cans pomodori pelati tomatoes (whole peeled tomatoes), blended smooth |
| `ar:.zcOYoZ1E0VEidPAUctxuPYRH0vh.Eq` | 4 large tomatoes - peeled, seeded and chopped ADVERTISEMENT | large tomatoes - peeled, seeded and chopped |
| `ar:SA1c2TPH8dK1.32UtrLPgf9L4/6G0Te` | 1 (15 ounce) can tomato sauce ADVERTISEMENT | can tomato sauce |
| `fn:T1RyitrPQ2apZgCwDdDHCzReun14DIO` | One 14-ounce can diced tomatoes with juices | one 14-ounce can diced tomatoes with juices |

### garlic

Family-not-regex recipes: **1**. Regex-not-family recipes: **4,911**. Net canonical-family minus raw-regex gap: **-4,910**.

Largest configured product exclusions observed in regex-not-family causes:

- `\b(?:garlic|granulated garlic|dried garlic) (?:powder|salt|paste|sauce)\b`: 3,799 recipe causes
- `\b(?:chili|chile|chilli)[ -]garlic sauce\b`: 84 recipe causes

#### Top 20 Family-not-regex canonical variants

| Canonical variant | Recipes |
|---|---:|
| garlic clove | 1 |

#### Random sample: Family-not-regex (up to 30)

| Recipe ID | Triggering raw ingredient line | Canonical value |
|---|---|---|
| `fn:m0JRZL9q/l70zx8640/fMK/TaSkdvVS` | 1garlic clove | garlic clove |

#### Top 20 Regex-not-family canonical variants

| Canonical variant | Recipes |
|---|---:|
| garlic powder | 2,658 |
| garlic salt | 488 |
| garlic powder, or to taste | 99 |
| garlic powder to taste | 77 |
| garlic salt to taste | 41 |
| garlic salt, or to taste | 41 |
| garlic paste | 38 |
| minced garlic (3 cloves) | 28 |
| dash garlic powder | 26 |
| garlic minced | 20 |
| granulated garlic powder | 18 |
| minced garlic (2 cloves) | 18 |
| chili garlic sauce | 15 |
| garlic powder (optional) | 15 |
| minced garlic (4 cloves) | 15 |
| chili-garlic sauce | 14 |
| ginger garlic paste | 14 |
| garlic pepper | 12 |
| garlic scapes | 12 |
| ginger-garlic paste | 12 |

#### Random sample: Regex-not-family (up to 30)

| Recipe ID | Triggering raw ingredient line | Canonical value |
|---|---|---|
| `ar:5UclQTiZrCFARtIDqwTPVgDEh.ED4CO` | 1 dash garlic salt ADVERTISEMENT | dash garlic salt |
| `fn:aj8qSHzOgV0CxKWXawfPVnCQjaARBIe` | 1/4 cup garlic flavored olive oil, divided | garlic flavored olive oil |
| `fn:bWwj0nojR2gB0/boNigZKPFaB3NrwVy` | 2 cloves finely chopped garlic (about 2 teaspoons) | finely chopped garlic (about 2 teaspoons) |
| `epi:cq4jKEPYaSvC9WJYHd4ESk31ID.oEra` | 1/4 cup Roasted Garlic Herb Sauce or high-quality pesto, plus more for serving | roasted garlic herb sauce or high-quality pesto, plus more for serving |
| `ar:9TmeXnJ007dWW2wQ4H41bU8vK1UspRS` | 1/2 teaspoon garlic powder ADVERTISEMENT | garlic powder |
| `epi:4eeDfFSeepxmGFavcIGzYmOZtsQ1syS` | 1 5.3-ounce package basil and roasted garlic goat cheese or 6 ounces soft fresh goat cheese (such as Montrachet), room temperature | 5.3-ounce package basil and roasted garlic goat cheese or 6 ounces soft fresh goat cheese (such as montrachet) |
| `ar:te6YbiDKO9FMYunSjwNzckhGc21U4UG` | 1/4 teaspoon garlic salt ADVERTISEMENT | garlic salt |
| `fn:/3ND/NfjcwIyYtYVVO3bqGHCSL2b0xK` | 2 cloves garlic (1 minced) | garlic (1 minced) |
| `epi:cCWlx19o/rPqATePhveXCIpQ585JhDu` | 1/4 cup garlic powder | garlic powder |
| `ar:pUThBWf4VQDaOyXdIH7C5x2ngFWBiau` | 1 teaspoon garlic salt ADVERTISEMENT | garlic salt |
| `ar:rm9vtbZcKMIhuO9GVXFp19Qihv.i26a` | 1 pinch garlic powder, or to taste ADVERTISEMENT | garlic powder, or to taste |
| `fn:V5TKKGj/32bkAwKMNho0bzYXQO4vQFe` | 1/2 teaspoon garlic powder | garlic powder |
| `ar:L0gzdmDxxm6hIjrMn3OGgWa5bZZzrI.` | 1 1/2 teaspoons garlic powder ADVERTISEMENT | garlic powder |
| `ar:cxYaW03fFsp7sTJY3DKHcyS43/DE396` | 3/4 teaspoon garlic powder ADVERTISEMENT | garlic powder |
| `ar:a/iQ5J27pdS4Jw7Di4LiiyIV6wjAWom` | 2 teaspoons garlic powder ADVERTISEMENT | garlic powder |
| `fn:vA9ddmYQke7nOZDGI4Jh1ubnWPaAkFu` | 1 tablespoon garlic powder | garlic powder |
| `fn:MzhOkQBDovi7up9.SKIsrbjKIglR3.6` | 4 garlic cloves crushed | garlic cloves crushed |
| `fn:Id3/AZx/FlAdWNTJrrxVoiDhHNW4zMO` | 1/2 teaspoon garlic powder | garlic powder |
| `fn:khi0HysQp9.P4ldbkjCYNbOUVXXx0Hq` | 1 teaspoon garlic powder | garlic powder |
| `ar:AyiT0yrx3uro7dDLUb68f8R4TPFJVRa` | garlic powder to taste ADVERTISEMENT | garlic powder to taste |
| `fn:vzxsDpT0n1CJOoZs4ggH9i/G7hFv1PC` | 1 tablespoon Vietnamese chili-garlic sauce | vietnamese chili-garlic sauce |
| `ar:EWpkzuajh4COi1XpZ4JBU/cHkCAc8xa` | 1/4 teaspoon garlic powder ADVERTISEMENT | garlic powder |
| `fn:uN0PFyh5IbsKyNxWqhzn.FZHCuW32cG` | garlic salt | garlic salt |
| `epi:8Opj6mX0njnXOTzhaAaAwPKY8ZPIv8O` | 1/4 teaspoon garlic powder | garlic powder |
| `ar:ktyAr1r5npJNcstRscsLCG.RbTl.xa2` | 1/4 teaspoon garlic salt ADVERTISEMENT | garlic salt |
| `fn:TmU/xvGvoHLnBLeuLJ7E2KvhZaljtEm` | 2 teaspoon sambal or chili-garlic sauce | sambal or chili-garlic sauce |
| `ar:tYKsG9emjJY9ne5vsj3ussGPnU8C0..` | 1 dash garlic powder ADVERTISEMENT | dash garlic powder |
| `fn:kKPLmi9DhK1eGOkI4YSMckKKqscrfx.` | 1 teaspoon garlic salt | garlic salt |
| `ar:W307deKtqMnBZOOcJMa1lDHuw.6Wrwm` | 1 tablespoon garlic powder ADVERTISEMENT | garlic powder |
| `ar:43/FFvLJtcysYie8KQFd1iBgK/4I7mm` | 1/2 teaspoon garlic powder ADVERTISEMENT | garlic powder |

### onion

Family-not-regex recipes: **1,089**. Regex-not-family recipes: **3,014**. Net canonical-family minus raw-regex gap: **-1,925**.

Largest configured product exclusions observed in regex-not-family causes:

- `\b(?:onion|granulated onion|dried onion) (?:powder|salt|flakes)\b`: 1,167 recipe causes
- `\bonion soup mix\b`: 191 recipe causes
- `\b(?:dry|dried) onion soup mix\b`: 168 recipe causes

#### Top 20 Family-not-regex canonical variants

| Canonical variant | Recipes |
|---|---:|
| green onion | 1,089 |

#### Random sample: Family-not-regex (up to 30)

| Recipe ID | Triggering raw ingredient line | Canonical value |
|---|---|---|
| `epi:3JOr5Hjh2/.fkOal6wBDbaxz.DCRHY6` | 1 scallion, sliced thin | green onion |
| `fn:otefgrfxVbCktZ9mKy.loigMNB3/GAe` | 2 scallions, finely chopped | green onion |
| `ar:06l/7ZWqbNij6aAM9vjN0s.Pg5sGbim` | 4 scallions, chopped ADVERTISEMENT | green onion |
| `fn:ZFtwCXslsQbyWUoRKkLw.EGaiPdaygO` | 1 bunch scallions, sliced | green onion |
| `epi:2mA5uGrULstY/cd3gF.N7NubryZ/BOi` | 1 scallion, chopped fine | green onion |
| `fn:Vl.aKe.7y60UUvoQ1CVKeClBWRtWLn2` | 2 scallions, minced | green onion |
| `fn:qxmVqcM94es9Q95A1Grrq3iPswiz/jy` | 1 bunch scallions, sliced, white and greens parts separated | green onion |
| `epi:6nt01QcfSieDjDc31HK6Ucx5gbJu/Ia` | 3 scallions, sliced | green onion |
| `fn:7tIOvOJ2tLR5Eu8PlpTBDiE3OgJqbb.` | 6 scallions, roughly chopped | green onion |
| `fn:CKPYxvrXQK/pMER91eTu3vU8J/jFgq.` | 3 scallions, finely chopped | green onion |
| `fn:qFXmphXZ0fr7AzGm1/J97ZT3Pctg4HS` | 2 scallions, sliced | green onion |
| `fn:Yno2EDe7UkhHzHSnWfZXqiFJn1a7H8i` | 4 scallions, chopped | green onion |
| `epi:ZafDQxb3QnCui9ibyIvUlSZeIsMum7e` | 2 scallions, chopped (about 1/2 cup) | green onion |
| `fn:AM9UZP.n0hGP/XtnTOqK4wjuRUN5aq2` | 3 scallions, chopped | green onion |
| `fn:wstaL9SPfFoxx5SUglX2E9pM0uQijli` | 2 scallions, sliced | green onion |
| `fn:LFgfPHcFF2aEdXEcJas16dFaB.8e7Hi` | 1/2 cup scallions, sliced | green onion |
| `fn:uOyvav.Br5mGMJWHNh3IHIFh8IRekra` | 2 scallions, roughly chopped | green onion |
| `epi:Pve8iAiwAHw2nnYtTi5RFPYCxlA921y` | 1 bunch scallions, chopped | green onion |
| `fn:3AIxqdd7Iud6zYqsSABMtDBMqqTdv0C` | 1 bunch scallions, chopped | green onion |
| `epi:tPCwPLX7kQ8uC9QbOdEyEIpwEpzycx6` | 2 scallions | green onion |
| `fn:3wHInuaORgNqIo651FPUWx4sZ2waOq.` | 2 scallions, finely chopped | green onion |
| `fn:tY895PKz9zJOxo2M9Q7fTO5mveuHWHW` | 3 scallions, sliced, whites and greens kept separate | green onion |
| `fn:bcVuFlP1P0qF3B1O6XxidEE79Md9NH6` | 1 scallion, minced | green onion |
| `fn:BAco/xaz//dpgXCfvkVXstfcME4Vfy6` | 2 scallions, chopped | green onion |
| `epi:mFPT6aC20mXH4nM1K3nooYTV06KfUIi` | 1 bunch scallions | green onion |
| `epi:uGfu0gl14ZtuvxQSQaU/DsoWIlPUP8K` | 1 scallion, minced | green onion |
| `fn:zWOhCCfigj8kmD7lC8setik9U2NL4oO` | 1 bunch scallions, roughly chopped | green onion |
| `fn:fRh38nYw3aaQoy/prJqUgiIEFiKM2Wm` | 3 scallions, sliced | green onion |
| `fn:AtfSiirWL1eUPnGQJg8zSZC3505Ukta` | 2 scallions, sliced | green onion |
| `fn:AblMs/64mf6q2TJmZBYBbWBL74Yj652` | 8 scallions | green onion |

#### Top 20 Regex-not-family canonical variants

| Canonical variant | Recipes |
|---|---:|
| onion powder | 970 |
| package dry onion soup mix | 80 |
| onion salt | 69 |
| envelope dry onion soup mix | 43 |
| dried onion flakes | 29 |
| can condensed french onion soup | 20 |
| sweet onion (such as vidalia®) | 17 |
| dried minced onion flakes | 15 |
| chopped yellow onions (2 onions) | 13 |
| packages dry onion soup mix | 13 |
| packet dry onion soup mix | 13 |
| chopped onion (optional) | 12 |
| onion powder, or to taste | 12 |
| small-diced red onion (1 small onion) | 12 |
| chopped green onion tops | 10 |
| chopped fresh chives or green onion tops | 9 |
| chopped onion (1 medium) | 9 |
| large sweet onion (such as vidalia®) | 9 |
| red onion slices | 9 |
| scallions (green onions) | 9 |

#### Random sample: Regex-not-family (up to 30)

| Recipe ID | Triggering raw ingredient line | Canonical value |
|---|---|---|
| `ar:3QuUfRGHW8KeVNDORxiB.ZJ1KB8jqxC` | 1/2 teaspoon onion powder ADVERTISEMENT | onion powder |
| `fn:eGFczWdTN81t96f19U657ORMi7gzITq` | 1/2 teaspoon onion powder | onion powder |
| `fn:5mwuNlC.y0jlxgpNU0VPjTgW1n/cAUW` | 1 tablespoon onion powder | onion powder |
| `ar:.3dsAN3Rf.yzm4VVU4aoQ3s3PYoQq.C` | 1/2 cup diced onion (optional) ADVERTISEMENT | diced onion (optional) |
| `fn:x0Ho8bauDmMMFXnXxMl66OSK5jvqe8m` | 1 sweet white onion (Maui or Vidalia) | sweet white onion (maui or vidalia) |
| `fn:MzwPOP3pSYYUuoDrRAmQWQKk/GxLBIu` | 1/2 cup finely diced white onions (about 1 small) | finely diced white onions (about 1 small) |
| `fn:u8kc4uat.3XOGq0iS24P1GkJzZaLPqe` | 1 teaspoon onion powder | onion powder |
| `epi:emVHdPd/8TYsa1XA/CXQPjvguMDLF8.` | 1 cup chopped green onion tops | chopped green onion tops |
| `fn:sQe43ctu70iYT1P0bwv6T9LrPZGNFUm` | 2 small red onions (11/2 thickly sliced, 1/2 thinly sliced) | small red onions (11/2 thickly sliced, 1/2 thinly sliced) |
| `ar:2knVkkbAR7vUn5Ery76CCUtf2R2hAS.` | 3/4 teaspoon onion powder ADVERTISEMENT | onion powder |
| `epi:USQcL6IoHWT9AExAHNIXEvdOX1MJwXG` | 3 cups sliced onions (about 2 onions) | sliced onions (about 2 onions) |
| `fn:llP.hTtF34kFGfzY.5wTGHlErKyWT7m` | 1 tablespoon onion powder | onion powder |
| `fn:tb9fa0iR.mpzAUpiK1K34/xmT.wihTm` | Garnish: celery sticks, trimmed green onions, and skewered cherry tomatoes | garnish: celery sticks, trimmed green onions, and skewered cherry tomato |
| `fn:921dxxqjBwtw.055VoKinOiH9XrmZtq` | 1 small onion chopped fine | small onion chopped fine |
| `ar:5EFsc/SQ.ijtY4tlLEmSlsVzyTr4BAu` | 1 (1 ounce) envelope dry onion soup mix ADVERTISEMENT | envelope dry onion soup mix |
| `fn:js0i1gXnwMozhRwK/FJf2NMKO7L10FG` | 1/2 cup each finely diced onions and Granny Smith apples | each finely diced onions and granny smith apples |
| `ar:j6Cy2edBzw4N4gElo5kj/ouHJla4RU2` | 1 (1 ounce) package dry onion soup mix (such as Lipton®) ADVERTISEMENT | package dry onion soup mix (such as lipton®) |
| `ar:qTnA9eDdxVPxXxrUGlV2sdFWjotvXGW` | 1 teaspoon onion powder ADVERTISEMENT | onion powder |
| `fn:R1MPOpVj276Mx56UJf2T7UNcmL8PERq` | 1 tablespoon onion powder | onion powder |
| `fn:7oAOtsOkCsF3bkWCxCKZlo2NaKMaovG` | 1 teaspoon onion powder | onion powder |
| `epi:dVwYWNoAy.n/TuUgBtBDiaus6wN.80y` | 2 large onions (1 1/2 lb total), halved lengthwise and cut lengthwise into 1/4-inch strips | large onions (1 1/2 lb total), halved lengthwise and cut lengthwise into 1/4-inch strips |
| `ar:I0mLAm/uQCec1DkoGRF5CgHk8uOV9we` | 1 tablespoon onion powder ADVERTISEMENT | onion powder |
| `ar:meaGGtxJUoHAzFJyJi7hTv5Vq33jU8G` | 2 teaspoons onion powder ADVERTISEMENT | onion powder |
| `fn:Gbz8v4nTYsc2OfcnFn9epp1ypn5XYC2` | 1 teaspoon dehydrated onion flakes | dehydrated onion flakes |
| `epi:5yQ5dN6sQOvg9fLIiFW0d2tdkGuW4km` | 4 spring onions or 6 scallions, whites only, thinly sliced | spring onions or 6 scallions, whites only, thinly sliced |
| `fn:CgPvjXdEZTGREq1lYyYtGawl9QE/d7q` | 1/2 cup onions (small diced) | onions (small diced) |
| `ar:Cl4gDLx55CEQhT1QmFJYMnYndVK7bPm` | 1 (1 ounce) package dry onion soup mix ADVERTISEMENT | package dry onion soup mix |
| `ar:bjW/OlWYfbWNlkLq0iobFlTaUJR0bOK` | 2 sweet onions (such as Vidalia®), quartered ADVERTISEMENT | sweet onions (such as vidalia®), quartered |
| `ar:QF0R5PMjo21bdWAF1QBDuuSJyv9UOLO` | 1 teaspoon onion powder ADVERTISEMENT | onion powder |
| `ar:dKmF93TzalpSQHJw8N6nAAJF.mKckCq` | 1 teaspoon onion seeds (kalonji) ADVERTISEMENT | onion seeds (kalonji) |

### Main sources of the gaps

- **Onion family-only matches:** configured scallion and spring-onion synonym merges produce canonical `green onion` values that a literal raw `onion` regex misses.
- **Regex-only matches:** raw ingredients that parse to a non-family canonical value, descriptions/noise retained in source lines, or preparation/product wording that the approved family excludes. Inspect the per-term top-20 tables to see the observed largest variants.
- **Product exclusions:** tomato paste/sauce and garlic/onion powders are intentionally excluded from their base families; these often account for regex-only variants.

