from Corpus import Corpus
from Rule import PossibleRules

print("Analysis starting...")
train_corpus = Corpus(["./dataset/TrainingSet/file1.txt"
                 , "./dataset/TrainingSet/file2.txt"
                 , "./dataset/TrainingSet/file3.txt"
                 , "./dataset/TrainingSet/file4.txt"
                 , "./dataset/TrainingSet/file5.txt"
                 , "./dataset/TrainingSet/file6.txt"
                 , "./dataset/TrainingSet/file7.txt"
                 , "./dataset/TrainingSet/file8.txt"

                       ])

train_corpus.outputWords("./Output/MostLikelyMorphParseForWord.txt")
print("Most likely morphological parses for words are written to ./Output/MostLikelyMorphParseForWord.txt")

train_corpus.outputPOStags("./Output/MostLikelyTag.txt")
print("Most likely tags are written to ./Output/MostLikelyTag.txt")

train_corpus.tag_words_with_most_likely_parses()
tag_order = 1
print("TRAIN: Precision for DS" + str(tag_order) + " " + str(train_corpus.calculate_precision()))

print("Possible rules are generating...")
rules = PossibleRules(train_corpus.tags[:20]).rules
print(str(len(train_corpus.all_words_in_corpus)) + " words in training set.")

learned_rules_with_precision = []
for rule in rules:
    for i in range(100, 400):

        original_word = train_corpus.all_words_in_corpus[i]
        word_after = train_corpus.all_words_in_corpus[i + 1]

        rule_changed_any_tag = rule.apply(original_word, word_after, train_corpus.words)
        if rule_changed_any_tag is True:
            precision = train_corpus.calculate_precision()
            learned_rules_with_precision.append((rule, precision))
            print("Precision for " + rule.name + " is " + str(precision))

train_corpus.output_rules("./Output/rules.txt", learned_rules_with_precision)

print("Rules are trained succesfully...")

test_corpus = Corpus(["./dataset/TestSet/file9.txt", "./dataset/TestSet/file10.txt"])

test_corpus.tag_words_with_most_likely_parses()
tag_order = 1
print("TEST: Precision for DS" + str(tag_order) + " " + str(test_corpus.calculate_precision()))

