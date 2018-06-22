import nltk

from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import state_union

train_text = state_union.raw("2005-GWBush.txt")
sample_text = " this country is america and we are its citizens and lets eat apple to saty healthy"

custom = PunktSentenceTokenizer(train_text)
tokenized = custom.tokenize(sample_text)

for i in tokenized:
    words = nltk.word_tokenize(i)
    tagged = nltk.pos_tag(words)

    chunkGram = r"""bhrt_Chunk: {<.*>+}
}<NN.?>+{"""

#now every thing will be chunked except the Nouns !!
                                    
    
    chunkParser = nltk.RegexpParser(chunkGram)
    chunked = chunkParser.parse(tagged)

    chunked.draw()
