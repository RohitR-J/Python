# Write a Python program to remove newline characters from a file.

def remove_newlines(fname):
    ls = open(fname).readlines()
    return [s.rstrip('\n') for s in ls]

print(remove_newlines("LAB-3/test.txt"))