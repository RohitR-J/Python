'''Ask the user for a number. 
Depending on whether the number is even or odd,
print out an appropriate message to the user.'''

userInput = int(input('Please enter a number:'))
if (userInput % 2) == 0:
    print(f'{userInput} is even')
else:
    print(f'{userInput} is odd')
