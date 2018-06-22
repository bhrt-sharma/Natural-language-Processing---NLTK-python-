import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer



train_text = state_union.raw("2005-GWBush.txt")
sample_text = " Hey there there is a famous saying , An Apple a day keeps the doctor away !! and we live in America"

custom_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_tokenizer.tokenize(sample_text)





for i in tokenized:
    words = nltk.word_tokenize(i)
    tagged = nltk.pos_tag(words)
    print(tagged)

    
    chunkGram = r""" bhrt_chunk: { <NN.?>* }    """

#identifier    # here .  means ----> . = any character, except for a new line
#modifier      # here ?  means ----> ? = match 0 or 1 repetitions.
    # i.e it will categorise all pos starting with NN...
#modifier      # here *  means ----> * = match 0 or MORE repetitions

#"0 or more of any tense of Noun," followed by:
    
     
    '''
    #here we are choosing all the Nouns, i.e
    NN	 noun, singular 'desk'
    NNS	 noun, plural	'desks'
    NNP	 proper noun, singular	'Harrison'
    NNPS proper noun, plural	'Americans'
    '''

    
    chunkParser = nltk.RegexpParser(chunkGram)
    chunked = chunkParser.parse(tagged)
    chunked.draw()
   # print(chunked)


