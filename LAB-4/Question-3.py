# Write a Python program to convert unix timestamp string to readable date

from datetime import datetime
t = int("1217463487")
unixTime = datetime.fromtimestamp(t)
print(unixTime.strftime('%Y/%m/%d \n %H:%M:%S'))