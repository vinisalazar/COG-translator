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
    def load_translation_tab(cls):
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

        print(f"Loaded {len(cls.codes)} COG names into memory.")

    @classmethod
    def get_name(cls, cog_code):
        """
        Gets COG name from COG code.
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


class COGFunctions(object):

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
    def cog_letter(cls, cog_letter):
        functions = dict()
        for k, v in cls.COG_letters.items():
            for k_, v_ in v.items():
                for char in cog_letter:
                    if char == k_:
                        functions[char] = (k, v_)

        return functions
