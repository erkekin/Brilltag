from Corpus import Corpus
from Rule import PossibleRules

print("Analysis starting...")
corpus = Corpus(["./dataset/train/file1.txt"
                 , "./dataset/train/file2.txt"
                 , "./dataset/train/file3.txt"
                 , "./dataset/train/file4.txt"
                 , "./dataset/train/file5.txt"
                 , "./dataset/train/file6.txt"
                 , "./dataset/train/file7.txt"
                 , "./dataset/train/file8.txt"

                 ])

# corpus.sortWords()
# 1
corpus.outputWords("./Output/MostLikelyMorphParseForWord.txt")
print("Most likely morphological parses for words are written to ./Output/MostLikelyMorphParseForWord.txt")
# 2
corpus.outputPOStags("./Output/MostLikelyTag.txt")
print("Most likely tags are written to ./Output/MostLikelyTag.txt")
# 3
corpus.tag_words_with_most_likely_parses()
tag_order = 1
print("Precision for DS" + str(tag_order) + " " + str(corpus.calculate_precision()))
# 4

print("Analysis succesfully finished...")

print("Possible rules are generating...")
rules = PossibleRules(corpus.tags[:10]).rules
print(str(len(corpus.all_words_in_corpus)) + "kelime var ")
for rule in rules:
    for i in range(1, 1000):

        original_word = corpus.all_words_in_corpus[i]
        word_after = corpus.all_words_in_corpus[i+1]

        rule_changed_any_tag = rule.apply(original_word, word_after, corpus.words)
        #if rule_changed_any_tag is True:
            # print("Precision for " + rule.name + " is " + str(corpus.calculate_precision()))


