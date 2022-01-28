#prints out a list of all the divisors of that number.

num = int(input('Enter a number:'))
listOutput = []
for i in range(1, num + 1):
    if num % i == 0:
        listOutput.append(i)
print('Divisors list', listOutput)
