from Word import Word
from Parse import Parse

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

            unique_serialized_word = self.upsertWord(wordText)

            correctMorphParseNumber = splittedFirstLine[1]  # get correct
            correctMorphParseFull = lines[int(correctMorphParseNumber)]

            unique_serialized_word.addParse(correctMorphParseFull)

            if "Punc" not in correctMorphParseFull:
                w = Word(wordText)  # add all words to all_words_in_corpus
                w.correct_parse = correctMorphParseFull
                self.all_words_in_corpus.append(w)

    def find_all_POS_tags(self, text):

        parses = re.findall(re.escape("     ") + "(.*)" + re.escape("\n"), text)
        tags = []

        for parse in parses:
            tags.append(Parse.convert_parse_to_tag(parse))

        self.tags += tags

    def calculate_precision(self):
        # Precision = Number of Correctly Tagged Words / Number of Total Words
        number_of_total_words = len(self.all_words_in_corpus)
        number_of_correctly_tagged_words = 0

        for word in self.all_words_in_corpus:

            if word.correct_parse == word.assigned_parse.text:
                number_of_correctly_tagged_words += 1

        precision = number_of_correctly_tagged_words / number_of_total_words
        return precision

    def tag_words_with_most_likely_parses(self):
        for word in self.all_words_in_corpus:
            parse = self.get_most_likely_morph_parse(word.text)
            word.assigned_parse = parse
            #print(word.text + " " + parse.text)

    def get_most_likely_morph_parse(self, word_text):
        serialized_word = Word.find_word_by_text(word_text, self.words)
        if serialized_word is None or len(serialized_word.parses) == 0:
            return None

        return serialized_word.parses[0]  # to get the most likely

    def outputPOStags(self, fileName):

        outputFile = open(fileName, "w+")

        POSTuples = Counter(self.tags).items()

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
        self.all_words_in_corpus = []
        self.tags = []

        for file_path in files:
            f = open(file_path, 'r')
            fullText = f.read()

            self.find_all_POS_tags(fullText)

            # preprocessing
            fullText = fullText.replace("\r\n", "\n")
            fullText = fullText.replace("<S>\n", "")  # exclude Sentences information <S>
            fullText = fullText.replace("P:     ", "")  # remove noise
            fullText = fullText.replace("D:     ", "")  # remove noise
            words = fullText.split("\n\n")
            self.getWordsAndTheirParses(words)


