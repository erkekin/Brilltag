from Parse import Parse


class Word:

    def getKey(self, parse):
        return parse.frequency

    def sortParses(self):
        self.parses = sorted(self.parses, key=self.getKey, reverse=True)

    def addParse(self, parseText):
        parseText = parseText.strip()
        for parse in self.parses:
            if parseText == parse.text:
                parse.frequency += 1
                return

        parse = Parse(parseText)
        self.parses.append(parse)
        self.sortParses()

    @staticmethod
    def find_word_by_text(text, words):

        for serialized_word in words:

            if serialized_word.text == text:
                return serialized_word

        return None

    def __init__(self, text):
        self.text = text
        self.parses = []
        self.correct_parse = None
        self.assigned_parse = None
        self.frequency = 1
