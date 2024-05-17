import nltk

from nltk import ngrams

sentence =("The sun is shining brightly.")
n = int(input("Enter the value of n: " ))

n_grams = ngrams(sentence.split(),n)
for grams in n_grams:
    print(grams)