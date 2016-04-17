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

    def __init__(self, text):
        self.text = text
        self.parses = []
        self.frequency = 1
