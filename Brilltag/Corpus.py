from Word import Word
import re
from collections import Counter


class Corpus:

    def getKey(self, word):
        word.sortParses()
        return len(word.parses)

    def sortWords(self):
        self.words = sorted(self.words, key=self.getKey, reverse=True)

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

            goodWord.addParse(correctMorphParseFull)
            wordAttachedToCorrectParse = wordText, correctMorphParseFull

            self.allWordsInCorpus.append(wordAttachedToCorrectParse)

    def find_all_POS_tags(self, text):

        fullTags = re.findall(re.escape("     ") + "(.*)" + re.escape("\n"), text)
        POSes = []

        for tag in fullTags:
            if '^DB' in tag:

                afterDB = tag.split("^DB")[-1]

                afterDBSplitted = afterDB.split("+")
                afterDBSplitted.remove('')

                if len(afterDBSplitted) > 1:
                    del afterDBSplitted[1]

                POSes.append("+".join(afterDBSplitted))
            else:
                # If the morphological parse does not contain a derivational boundary (^DB), except the root word assume that the rest of the morphological parse as a part of speech tag. See the following examples.
                POSes.append(tag.partition("+")[-1])

        self.POStags += POSes

    def calculate_precision(self, tagged_order):
        # Precision = Number of Correctly Tagged Words / Number of Total Words
        tagged_order += 1
        number_of_total_words = len(self.allWordsInCorpus)
        number_of_correctly_tagged_words = 0

        for word in self.allWordsInCorpus:
            correct_morph_parse = word[1]
            tagged_morph_parse = word[tagged_order]
            if correct_morph_parse == tagged_morph_parse:
                number_of_correctly_tagged_words += 1

        precision = number_of_correctly_tagged_words / number_of_total_words
        return precision

    def tag_words_with_most_likely_morph_parse(self):
        new_words = []
        for word in self.allWordsInCorpus:  # a word is a tuple here
            most_likely_morph_parse = self.get_most_likely_morph_parse(word[0])

            if most_likely_morph_parse is not None:
                word += (most_likely_morph_parse,)
                new_words.append(word)

        self.allWordsInCorpus = new_words

    def find_word_by_text(self, text):

        for serialized_word in self.words:

            if serialized_word.text == text:
                return serialized_word

    def get_most_likely_morph_parse(self, word_text):
        serialized_word = self.find_word_by_text(word_text)

        if len(serialized_word.parses) > 0:

            return serialized_word.parses[0].text
        else:

            return None

    def outputPOStags(self, fileName):

        outputFile = open(fileName, "w+")

        POSTuples = Counter(self.POStags).items()

        sorted_by_second = sorted(POSTuples, key=lambda tup: tup[1], reverse=True)
        for POS in sorted_by_second:
            line = POS[0] + "\t" + str(POS[1]) + "\r"
            outputFile.writelines(line)

        outputFile.close()

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

    def __init__(self, files):
        self.words = []
        self.allWordsInCorpus = []
        self.POStags = []

        for file_path in files:
            f = open(file_path, 'r')
            fullText = f.read()

            self.find_all_POS_tags(fullText)

            fullText = fullText.replace("\r\n", "\n")
            fullText = fullText.replace("<S>\n", "")  # exclude Sentences information <S>
            fullText = fullText.replace("P:     ", "")  # remove noise
            fullText = fullText.replace("D:     ", "")  # remove noise
            words = fullText.split("\n\n")
            self.getWordsAndTheirParses(words)

