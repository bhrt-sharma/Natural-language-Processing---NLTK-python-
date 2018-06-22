from nltk import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = [ "python" , "pythoner", "pythoning" , "pythoned" , "pythonly" ]


#for w in example_words:
 #   print(ps.stem(w))

new = " is is very important to be pythonly while you are pythoning with python."

words = word_tokenize(new)

for w in words:
    print(ps.stem(w))
