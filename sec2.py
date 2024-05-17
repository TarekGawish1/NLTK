# stem porter
from nltk.stem.porter import PorterStemmer as p_stem

s_stem_ENG = s_stem(language="english")
print(p_stem().stem("dogs"))


# snowball
from nltk.stem.snowball import SnowballStemmer as s_stem

w_plu = ['doors', 'dogs', 'photos', 'coputer', 'communications']
sgls = [s_stem_ENG.stem(wplu) for wplu in w_plu]
print(" ".join(sgls))