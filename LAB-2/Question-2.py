# Write a Python program to count the number of characters (character frequency) in a string.

characters = "sample character"
dic = {}
for n in characters:
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1
        
print(dic)
