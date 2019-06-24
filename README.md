# COG-translator
🧬 ↩️ Easy translation of COG names


Easily translate COG names and categories.

#### Usage
```
import COG

# Simple module functions
COG.name_from_code("COG0001")  # returns 'Glutamate-1-semialdehyde aminotransferase'
COG.cat_from_letter("WH")  # returns {'W': ('Cellular processes and signaling', 'Extracellular structures'),
                           #          'H': ('Metabolism', 'Coenzyme transport and metabolism')}
COG.letter_from_code("COG0001")  # returns {'H': ('Metabolism', 'Coenzyme transport and metabolism')}

# Also has the COGTranslator and COGFunction classes which hold the translation data
from COG import COGTranslator
cogt = COGTranslator()  # By default loads data file into memory
cogt.name_from_code("COG0001")  # Faster than module function because data already loaded.
```

Have fun. All contributions welcome.
