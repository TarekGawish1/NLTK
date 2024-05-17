import nltk
from nltk.corpus import brown as bwn

nltk.download('brown')
nltk.download('averaged_perceptron_tagger')
nltk.download('universal_tagset')
result = bwn.tagged_words()[0:40]

print(result)

from nltk.tokenize import word_tokenize as w_tok
from nltk import pos_tag as p_tag

utt1 = w_tok("Give me a call")
utt2 = w_tok("Call me later")

result2 = p_tag(utt1, tagset='universal')
result3 = p_tag(utt2, tagset='universal')

print(result2)
print(result3)