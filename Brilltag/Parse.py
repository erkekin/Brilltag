class Parse:
    def __init__(self, text):
        self.text = text
        self.frequency = 1

    @staticmethod
    def convert_parse_to_tag(parse):

        if '^DB' in parse:
            afterDB = parse.split("^DB")[-1]

            afterDBSplitted = afterDB.split("+")
            afterDBSplitted.remove('')

            if len(afterDBSplitted) > 1:
                del afterDBSplitted[1]

                return "+".join(afterDBSplitted)
        else:
            # If the morphological parse does not contain a derivational boundary (^DB), except the root word assume that the rest of the morphological parse as a part of speech tag. See the following examples.
            return parse.partition("+")[-1]