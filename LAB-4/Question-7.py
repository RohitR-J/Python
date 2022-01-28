# Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).

def sum(num):
    if num < 1:
        return 0
    else:
        return num + sum(num - 2)

print(sum(5))
