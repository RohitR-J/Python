# Write a Python program to append text to a file and display the text.

f = open('LAB-3/text.txt', 'a')
f.write('Adding more content to the existing file')
f.close()
f =open('LAB-3/text.txt', 'r')
print(f.read())
