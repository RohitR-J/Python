# Write a Python program to read a file line by line store it into a variable

with open('LAB-3/text.txt') as fname:
    data = fname.readlines()
    print(data)
