from collections import Counter

filename = raw_input("What file do you want to count? ")
text = open(filename, 'r').read() # could remove filename variable - not sure if best practice?
words = text.split(None) #string split at space - double space counts as one
print "Word Count: ", len(words)
print "Unique words: ", len(set(words))
print "The 20 most common words are: ", Counter(words).most_common(20)

lower_text = text.lower() # am sure this stage can be simpler
lower_words = lower_text.split(None)
print "Unique words if case is not a consideration: ", len(set(lower_words))
print "The 20 most commons words if case is not a consideration are: ", Counter(lower_words).most_common(20)
