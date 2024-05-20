import spacy

nlp = spacy.load("en_core_web_md")

utt1 = nlp("i ate a banana.")

import en_core_web_md
nlp = en_core_web_md.load()
print(utt1[3].vector)