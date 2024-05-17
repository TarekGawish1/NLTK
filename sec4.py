import spacy
nlp = spacy.load("en_core_web_sm")

text = "Programming is the mental process of thinking up instructions to give to a machine (like a computer). It involves designing and implementing algorithms, step-by-step specifications of procedures, by writing code in one or more programming languages. Coding, on the other hand, is the process of transforming those ideas into a written language that a computer can understand."

text = text.replace("\n", " ")

nlp = spacy.load("en_core_web_sm")

len(text)
text_doc = nlp(text) 
text_sent = [sentence.text for sentence in text_doc.sents]
text_words =[token.text for token in text_doc]


print(text_doc,"\n")
print(text_sent,"\n")
print(text_words)




# Step 1: Install NLTK and download stop words
# You can install NLTK using pip if you haven't already
# pip install nltk

# Importing necessary modules
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download the stopwords corpus if you haven't already
nltk.download('stopwords')
nltk.download('punkt')

# Define the input text
input_text = "This is a sample sentence, showing off the stop words filtration."

# Step 3: Tokenize the input text
words = word_tokenize(input_text)

# Step 4: Filter out the stop words
stop_words = set(stopwords.words('english'))
filtered_sentence = [word for word in words if word.lower() not in stop_words]

# Print the result
print("Original sentence:", input_text)
print("Filtered sentence:", ' '.join(filtered_sentence))
