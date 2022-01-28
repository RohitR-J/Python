# Write a Python program to write a list to a file.

ls = ['Apple', 'Orange', 'Grapes']
textFile = open('LAB-3/text.txt','w')
for element in ls:
    textFile.write(element+'\n')
textFile.close()