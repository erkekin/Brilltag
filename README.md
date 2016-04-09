# Brilltag
Morphological Disambiguation using Brill Tagging Method

For each word in the training set, MostLikelyMorphParseForWord table should hold how many times that word occurred in the training set, and which morphological parse of that word is most likely. Your program should also collect how many times each morphological parse of each word is selected as a correct parse.
Write the contents of this table into a text file ( MostLikelyMorphParseForWord.txt ) in the descending order (the first word in this file is the word with the highest frequency in the training set). On the first line of this file, put the total number of the words and the number of the unique words in the training set. For each word, put the following lines into this file.
 
word    its frequency
mostlikelymorphparse    its frequency
2ndmostlikelymorphparse its frequency
...
leastlikelymorpparse    its frequency

leave a blank line after each word in the file