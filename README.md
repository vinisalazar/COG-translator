# COG-translator
🧬 ↩️ Easy translation of COG names

Pure Python package for easy translation between COG names, codes and categories.

#### Installation
`pip install COG-translator`

or
```
git clone https://github.com/vinisalazar/COG-translator.git
cd COG-translator
python setup.py install  # or even `pip install .`
```

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

Have fun.
All contributions welcome.
If you have any problems, feel free to open an issue.

If you use this software, please cite this GitHub repository:
*Salazar, V. W. (2019). COG-translator: easy translation of COG names. Retrieved from https://github.com/vinisalazar/COG-translator/*

COG reference:
*Galperin, M. Y., Makarova, K. S., Wolf, Y. I., & Koonin, E. V. (2014). Expanded microbial genome coverage and improved protein family annotation in the COG database. Nucleic Acids Research, 43(D1), D261--D269.*
