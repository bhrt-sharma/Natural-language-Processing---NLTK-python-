from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_text = " this is an example showing off stop word filtration. "
stop_words = set(stopwords.words("english"))

words = word_tokenize(example_text)

filtered = []

for w in word_tokenize(example_text):
    if w not in stop_words:
        filtered.append(w)


print(filtered)
