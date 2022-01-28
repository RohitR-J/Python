# returns a list that contains only the elements that are common between the lists

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# a_set = set(a)
# b_set = set(b)
# c_set = a_set.intersection(b_set)
# c_set = list(c_set)
# print(c_set)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c =[]
for i in a:
    if i in b and i not in c:
        c.append(i)
print(c)
