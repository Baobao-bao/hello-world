# ACIT 1515: Exercise 1 - Fuel Errors
# Author: Jinbiao Liao, A01057463, Set 1C
# Date: Sept 14, 2019

KM_PER_MILE = 1.6
LT_PER_GAL = 4.54

def get_kms_driven():
    odo_start = int(input('Enter starting odometer reading (kms): '))
    odo_end = int(input('Enter ending odometer reading (kms): '))
    kms_driven = odo_end - odo_start
    return kms_driven

def get_fuel_used():
    lt_used = float(input('Amount of fuel used (litres): '))
    return lt_used

def calc_lp100(kms, lts):
    lts_per_100km = round((100 * (lts / kms)), 1)
    return lts_per_100km

def calc_mpg(kilometers, litres):
    miles = kms2miles(kilometers)
    gallons = lts2gals(litres)
    mpg = round(miles / gallons, 1)
    return mpg

def kms2miles(kms):
    mls = kms / KM_PER_MILE
    return mls

def lts2gals(lts):
    gals = lts / LT_PER_GAL
    return gals

def display_mileage(lp100, mpg):
    print("Your fuel efficiency is:")
    print( lp100, 'liters per 100 kilometers')
    print( mpg, 'miles per gallon')
    return

if __name__ == "__main__":
    kilometers = get_kms_driven()
    litres = get_fuel_used()
    lp100 = calc_lp100(kilometers,litres)
    mpg = calc_mpg(kilometers, litres)
    display_mileage(lp100,mpg)
