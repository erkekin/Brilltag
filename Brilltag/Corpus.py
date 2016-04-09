from Word import Word


class Corpus:

    def getKey(self, word):
        word.sortParses()
        return len(word.parses)

    def sortWords(self):
        self.words = sorted(self.words, key=self.getKey, reverse=True)

    def outputWords(self, fileName):

        # Open a file in write mode
        # w+ Opens a file for both writing and reading.
        # Overwrites the existing file if the file exists.
        # If the file does not exist, creates a new file for reading and writing.

        outputFile = open(fileName, "w+")

        for word in self.words:
            outputFile.write(word.text + "\t" + str(word.frequency))
            outputFile.write("\r")

            for parse in word.parses:
                outputFile.write(parse.text + "\t" + str(parse.frequency))
                outputFile.write("\r")

            outputFile.write("\r")

        outputFile.close()

    def printWords(self):

        for word in self.words:
            print(word.text + "\t" + str(word.frequency))

            for parse in word.parses:
                print(parse.text + "\t" + str(parse.frequency))

            print("\n")

    def upsertWord(self, wordText):

        for word in self.words:

            if wordText == word.text:

                word.frequency += 1
                return word

        word = Word(wordText)
        self.words.append(word)
        return word

    def getWordsAndTheirParses(self, words):

        for word in words:
            lines = word.split("\n")
            firstLine = lines[0]
            splittedFirstLine = firstLine.split(":")
            if len(splittedFirstLine) < 2:
                continue
            wordText = splittedFirstLine[0]

            goodWord = self.upsertWord(wordText)

            correctMorphParseNumber = splittedFirstLine[1]  # get correct
            correctMorphParseFull = lines[int(correctMorphParseNumber)]
            correctMorphParseFull = correctMorphParseFull.replace("P:     ", "")  # remove noise
            correctMorphParseFull = correctMorphParseFull.replace("D:     ", "")  # remove noise

            goodWord.addParse(correctMorphParseFull)

    def __init__(self, files):
        self.words = []

        for file_path in files:
            f = open(file_path, 'r')
            fullText = f.read()
            fullText = fullText.replace("\r\n", "\n")
            fullText = fullText.replace("<S>\n", "")  # exclude Sentences information <S>
            words = fullText.split("\n\n")
            self.getWordsAndTheirParses(words)
