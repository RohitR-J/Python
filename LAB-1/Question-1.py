'''Write a program that asks the user to enter their name and their age. 
Print out a message that greets them and that tells them the year that they will turn 100 years old'''

from datetime import datetime
name = input('Please enter your name:')
age = int(input('Enter your age:'))
willTurnHundred = 100-age + datetime.now().year
print(f"Hi,{name},you are {age} years old.You will turn 100 years old in {willTurnHundred}")
