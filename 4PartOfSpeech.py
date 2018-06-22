import nltk
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import state_union
from nltk.tokenize import word_tokenize

train_text = state_union.raw("2005-GWBush.txt")
sample_text = " This country is America , And we are it's Citizens"

custom_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_tokenizer.tokenize(sample_text)

print(tokenized)

print("\n\n\n")

tokenize = word_tokenize(sample_text)

print(tokenize)

print("\n\n\n")
print(sample_text)
print("\n\n\n")



for i in tokenized:
    words = nltk.word_tokenize(i)
    tagged = nltk.pos_tag(words)
    print(tagged)
    

    
