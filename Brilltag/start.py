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

corpus.outputWords("./Output/MostLikelyMorphParseForWord.txt")
print("Most likely morphological parses for words are written to ./Output/MostLikelyMorphParseForWord.txt")

corpus.outputPOStags("./Output/MostLikelyTag.txt")
print("Most likely tags are written to ./Output/MostLikelyTag.txt")


print("Analysis succesfully finished...")

