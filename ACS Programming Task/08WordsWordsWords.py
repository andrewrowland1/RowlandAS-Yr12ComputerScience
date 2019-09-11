#program that takes a sentence and outputs how many words are in the sentence
sentence = input(str("Please input a sentence"))
words = sentence.split()
wordCount = len(words)
print(wordCount)
