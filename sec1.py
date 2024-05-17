import nltk
from nltk.tokenize import sent_tokenize

wToknize = "hello my name is tarek and i'm 22 years old and i love programming."

wSentens = "Programming is the mental process of thinking up instructions to give to a machine (like a computer). It involves designing and implementing algorithms, step-by-step specifications of procedures, by writing code in one or more programming languages. Coding, on the other hand, is the process of transforming those ideas into a written language that a computer can understand. Think of it like following a recipe: the recipe author provides you with a set of instructions that you read and then follow. The more complex the instructions, the more complex the result! While sometimes used interchangeably, programming and coding have distinct definitions, but both are essential for creating software and enabling computers to perform tasks"

print(nltk.word_tokenize(wToknize))
print(nltk.sent_tokenize(wSentens))
