# Write a Python program to combine each line from first file with the corresponding line in second file

with open('LAB-3/text.txt') as file1, open('LAB-3/test.txt') as file2:
    for line1, line2 in zip(file1, file2):
       print(line1+line2)