# Write a Python program to count the frequency of words in a file.

from collections import Counter
with open('LAB-3/text.txt') as fname:
    freq = Counter(fname.read().split())
    print(freq)