from datetime import datetime
current = datetime.now()
print('Current date and time', current.strftime("%d/%m/%Y %H:%M:%S"))
print('Current year:', current.strftime("%Y"))
print('Month of year', current.strftime("%B"))
print('Week number of the year', current.strftime("%W"))
print('Weekday of the week', current.strftime("%w"))
print('Day of year',current.strftime("%j"))
print('Day of the month', current.strftime("%d"))
print('Day of week', current.strftime("%A"))