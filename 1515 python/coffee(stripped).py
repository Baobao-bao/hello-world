# ACIT 1515: Exercise 2 -  Coffee Refactor
# Author: Jinbiao Liao, A01057463, Set 1C
# Date: Sept 14, 2019

PRICE = 14.99
SHIPPING_COST = 0.89
ONLINE_CHARGE = 1.50
TAX_RATE = 0.13

def getInput():
    a = int(input("Enter pounds of coffee: \n"))
    return a
def roundTo2(num):
    return round(num,2)
def separateLine():
    print('-' * 48)

if __name__ == "__main__":
    number_of_pounds = getInput()
    subtotal = roundTo2(number_of_pounds * PRICE)
    shipping_charges = roundTo2(number_of_pounds * SHIPPING_COST + ONLINE_CHARGE)
    tax = roundTo2((subtotal + shipping_charges) * TAX_RATE)
    total = roundTo2(subtotal + shipping_charges + tax)
    separateLine()
    print(number_of_pounds, 'lbs @', PRICE, '/ lb\t\t\t$', subtotal)
    print('Shipping:\t\t\t\t$', shipping_charges)
    print('Tax:\t\t\t\t\t$', tax)
    separateLine()
    print('Total:\t\t\t\t\t$', total)
    separateLine()