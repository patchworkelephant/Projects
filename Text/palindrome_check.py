# Ask user to input word & check

string = raw_input("What is your word, punk? ").lower()

# if raw input and reverse are the same, print success message. 
if string == string[::-1]:
    print "%s is a palindromemordnilap" % string 

else:
    print "%s is not a palindrome. That is sad" % string