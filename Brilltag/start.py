from Corpus import Corpus

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

corpus.sortWords()
# 1
corpus.outputWords("./Output/MostLikelyMorphParseForWord.txt")
print("Most likely morphological parses for words are written to ./Output/MostLikelyMorphParseForWord.txt")
# 2
corpus.outputPOStags("./Output/MostLikelyTag.txt")
print("Most likely tags are written to ./Output/MostLikelyTag.txt")
# 3
tagged_words = corpus.tag_words_with_most_likely_morph_parse()
print(tagged_words)
# 4

print("Analysis succesfully finished...")

