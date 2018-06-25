from nltk.stem import WordNetLemmatizer

lemma = WordNetLemmatizer()

print(lemma.lemmatize("better",pos="a"))
# a means it is adjective!!!
print(lemma.lemmatize("cats"))


print(lemma.lemmatize("runs",'v'))
