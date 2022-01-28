#Ask the user for a string and print out whether this string is a palindrome or not

userInput= str(input('Enter a string:'))
if userInput == userInput[::-1]:
    print('It is a palindrome')
else:
    print('Not a palindrome')