"""Write a password generator in Python. 
Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password every time the user asks for a new password."""

import random
import string
print('***PASSWORD GENERATOR***')
length = int(input('Enter the required length:'))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower+upper+num+symbols
temp = random.sample(all,length)
password = "".join(temp)
print(password)
