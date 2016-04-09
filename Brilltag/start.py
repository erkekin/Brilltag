from Corpus import Corpus

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

print("analysis succesfully finished.")
