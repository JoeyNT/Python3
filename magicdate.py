# Project 1 Chapter 3

month = int(input('Enter month (numeric) :'))
day = int(input('Enter day:'))
year = int(input('Enter two digit year:'))
month_by_date= month*day

if month_by_date == year: 
  print('This date is magic!')
else:
  print('This date is not magic')
