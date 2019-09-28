# ACIT 1515: Exercise 2 - Time
# Author: Jinbiao Liao, A00123456, Set C
# Date: Sept 6, 2019

days = int(input('Enter number of days: '))
hours = int(input('Enter number of hours: '))
mins = int(input('Enter number of minutes: '))
total_sec = (days*24*3600 + hours*3600 + mins)*60
print(days,'days',hours,"hours",mins,'mins','=',total_sec,'seconds')