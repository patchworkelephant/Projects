# user input of file, read and input into variables
# seems messy, must be better way of doing this
filename = raw_input("What file do you want to count? ")
file = open(filename, 'r')
text = file.read()
sub = " " # Presume white space is sufficient marker for words - may not be. eg. double spacing
# output the number of words - with +1 for first word
print "Number of words: ", text.count(sub)+1
