# Write a Python program to remove an item from a set if it is present in the set.

s = {1,2,3,4,5,6,7,8,9,10}
print(s)
inp = int(input("Enter a number you wish to remove:"))
s.remove(inp)
print('Making changes....','\n','Output:',s)