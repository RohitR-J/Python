#Write a Python program to subtract five days from current date

from datetime import date, datetime, timedelta
current = date.today()
fiveBefore = date.today()- timedelta(5)
print(f"5 days before {current} is ---- {fiveBefore}")
