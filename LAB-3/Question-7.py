# Write a Python program to read a file line by line store it into an array.

contentArray = []
with open('LAB-3/text.txt') as fname:
    for arr in fname:
        contentArray.append(arr)
print(contentArray)
