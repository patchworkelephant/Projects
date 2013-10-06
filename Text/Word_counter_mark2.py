# user input of file, read and input into variables
# seems messy, must be better way of doing this
text = raw_input("What file do you want to count? ")

# open file
# read file
# linesplit - not changing it, want it to do it at space. 
words = text.split()
print wordCount, words.count()
# print word count