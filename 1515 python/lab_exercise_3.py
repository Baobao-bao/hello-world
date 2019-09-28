# ACIT 1515: Exercise 3 - Time
# Author: Jinbiao Liao, A00123456, Set C
# Date: Sept 6, 2019

bill = float(input('Enter bill total (before tax): '))
tip_per = float(input('Enter percent you want to tip: '))
print('--------------------------')
tax = bill*0.05
print('changes = $',round(bill,2))
print('Tax = $',round(tax,2))
print('--------------------------')
subto = bill + tax
print('Subtotal = $',round(subto,2))
print('--------------------------')
tip = subto * tip_per * 0.01
print('Tip = $',round(tip,2))
print('--------------------------')
total = subto + tip
print('Total = $',round(total,2))
print('--------------------------')
