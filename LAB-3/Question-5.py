# Write a Python program to read a file line by line and store it into a list.

with open('LAB-3/text.txt') as fname:
    list=fname.readlines()
    print(list)