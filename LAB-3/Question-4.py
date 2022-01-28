# Write a Python program to read last n lines of a file.

from traceback import print_tb


with open("LAB-3/text.txt") as fname:
    for line in (fname.readlines()[-2:]):   
        print(line)