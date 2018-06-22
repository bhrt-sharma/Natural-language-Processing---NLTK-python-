import nltk

#nltk.download()

from nltk.tokenize import sent_tokenize , word_tokenize

example_text = " Hey there this is bharat! , now lets see how good is the nltk library. This is our Start and we belive that ,  we will go a long way !!! ."

print(sent_tokenize(example_text))

print(word_tokenize(example_text))

for i in word_tokenize(example_text):
    print (i)
