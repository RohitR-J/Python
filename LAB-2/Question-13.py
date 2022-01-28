# Write a Python program to generate all sublists of a list.

ls = [1, 2, 3]
lists =[[]]
for i in range(len(ls)+1):
    for n in range(i):
        lists.append(ls[n:i])
print(lists)
