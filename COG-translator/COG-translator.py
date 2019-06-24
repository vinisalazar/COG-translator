"""
Our main class for translating.a
"""


class COGTranslator(object):
    """
    Our main class which contains the COG data file, called the 'translation tab'
    attribute.
    """

    translation_tab = "data/cognames2003-2014.tab"

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
