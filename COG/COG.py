"""
Our main class for translating COG codes and letters.
"""
from os import path


class COGTranslator(object):
    """
    Our main class which contains the COG data file, called the 'translation tab'
    attribute.
    """

    translation_tab = path.join(path.dirname(__file__), "cognames2003-2014.tab")

    def __init__(self, load=True):
        super(COGTranslator, self).__init__()
        if load:
            self.load_translation_tab()

    @classmethod
    def load_translation_tab(cls, print_=True):
        """
        Loads the COG translation tab into memory as a dictionary.
        """
        cls.codes = dict()
        with open(cls.translation_tab, "rb") as f:
            # This is to prevent Unicode Decode errors
            lines = (l.decode("utf-8", "ignore") for l in f.readlines())
            next(lines)  # This skips the first line
            for row in lines:
                row = row.split("\t")
                cls.codes[row[0]] = {"func": row[1], "name": row[2].strip()}

        if print_:
            print(f"Loaded {len(cls.codes)} COG names into memory.")

    @classmethod
    def name_from_code(cls, cog_code):
        """
        Gets COG name from COG code (e.g. COG0001)
        """
        if not cls.codes:
            try:
                cls.load_translation_tab()
            except:
                raise Exception("Couldn't load translation tab.")
        try:
            while cls.codes[cog_code]:
                return cls.codes[cog_code]["name"]
        except KeyError:
            raise Exception("COG code not found. Please check your COG code.")

    @classmethod
    def letter_from_code(cls, cog_code, translate=True):
        """
        Gets COG letter from COG code (e.g. COG0001)
        """
        if not cls.codes:
            try:
                cls.load_translation_tab()
            except:
                raise Exception("Couldn't load translation tab.")
        try:
            while cls.codes[cog_code]:
                if translate:
                    return COGFunctions.cat_from_letter((cls.codes[cog_code]["func"]))
                else:
                    return cls.codes[cog_code]["func"]
        except KeyError:
            raise Exception("COG code not found. Please check your COG code.")


class COGFunctions(object):

    """
    COG categories. Taken from the CLoVR website at:
    http://clovr.org/docs/clusters-of-orthologous-groups-cogs/
    """

    COG_letters = {
        "Cellular processes and signaling": {
            "D": "Cell cycle control, cell division, chromosome partitioning",
            "M": "Cell wall/membrane/envelope biogenesis",
            "N": "Cell motility",
            "O": "Post-translational modification, protein turnover, and chaperones",
            "T": "Signal transduction mechanisms",
            "U": "Intracellular trafficking, secretion, and vesicular transport",
            "V": "Defense mechanisms",
            "W": "Extracellular structures",
            "Y": "Nuclear structure",
            "Z": "Cytoskeleton",
        },
        "Information storage and processing": {
            "A": "RNA processing and modification",
            "B": "Chromatin structure and dynamics",
            "J": "Translation, ribosomal structure and biogenesis",
            "K": "Transcription",
            "L": "Replication, recombination and repair",
        },
        "Metabolism": {
            "C": "Energy production and conversion",
            "E": "Amino acid transport and metabolism",
            "F": "Nucleotide transport and metabolism",
            "G": "Carbohydrate transport and metabolism",
            "H": "Coenzyme transport and metabolism",
            "I": "Lipid transport and metabolism",
            "P": "Inorganic ion transport and metabolism",
            "Q": "Secondary metabolites biosynthesis, transport, and catabolism",
        },
        "Poorly characterized": {
            "R": "General function prediction only",
            "S": "Function unknown",
        },
    }

    @classmethod
    def cat_from_letter(cls, cog_letter, dict_output=True):
        """
        Gets COG higher and lower group from COG letter.
        Returns dict with input letter as key and groups as value (inside tuple).
        """
        functions = dict()
        for char in cog_letter:
            for k, v in cls.COG_letters.items():
                for k_, v_ in v.items():
                    if char == k_:
                        functions[char] = (k, v_)
            try:
                functions[char]
            except KeyError:
                print(f"{char} wasn't found! Check if it is a valid COG letter.")

        if functions:
            if dict_output:
                return functions
            else:
                for k, v in functions.items():
                    print(k, v)


"""
These are functions to be called out of the class scope.
"""


def name_from_code(cog_code, *args, **kwargs):
    """
    Takes COG code (e.g.: COG0001) and returns COG name (Glutamate-1-semialdehyde aminotransferase)
    """
    cogt = COGTranslator(load=False)
    cogt.load_translation_tab(print_=False)
    return cogt.name_from_code(cog_code, *args, **kwargs)


def cat_from_letter(cog_letter, *args, **kwargs):
    """
    Takes COG letter and returns a dictionary with letters as keys and
    COG categories as values (first value is higher category and second
    value is lower category).
    """
    cogf = COGFunctions()
    return cogf.cat_from_letter(cog_letter, *args, **kwargs)


def letter_from_code(cog_code, *args, **kwargs):
    """
    Takes COG code (e.g.: COG0001) and returns a dict with COG letter as keys
    and categories as values.

    Can specify dict_output=False to return a string.
    """
    cogt = COGTranslator(load=False)
    cogt.load_translation_tab(print_=False)
    return cogt.letter_from_code(cog_code, *args, **kwargs)
