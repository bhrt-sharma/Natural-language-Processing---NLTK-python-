from nltk.corpus import wordnet

lis = wordnet.synsets("programs")
# since the output is a list
# therefore to see the first element
print(lis[0])

#to get only the word !
print(lis[0].lemmas()[0].name())

#to get the defination
print(lis[0].definition())

#examples
print(lis[0].examples())

#to get the synonyms and antonyms





# to get the similarity between two words
w1 = wordnet.synset("bag.n.01")
w2 = wordnet.synset("pocket.n.01")

print(w1.wup_similarity(w2))

