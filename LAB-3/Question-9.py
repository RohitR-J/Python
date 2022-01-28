# Write a Python program to count the number of lines in a text file.

with open('LAB-3/text.txt') as fname:
    lineCount = 0
    for line in fname:
        if lineCount != '/n':
            lineCount +=1
fname.close()
print(lineCount)