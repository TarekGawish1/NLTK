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
