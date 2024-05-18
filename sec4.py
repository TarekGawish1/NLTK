import spacy
nlp = spacy.load("en_core_web_sm")

text = "Programming is the mental process of thinking up instructions to give to a machine (like a computer). It involves designing and implementing algorithms, step-by-step specifications of procedures, by writing code in one or more programming languages."


text_doc = nlp(text) 

text_sent = [sentence.text for sentence in text_doc.sents]

text_words =[token.text for token in text_doc]


print(text_doc,"\n")
print(text_sent,"\n")
print(text_words)


