from math import floor

## part 1

def calc_fuel(mass):

    fuel = floor(int(mass)/3) - 2
    return fuel

fuel_total = 0

with open('input', 'r') as f:
    for mass in f:
        fuel_total += calc_fuel(mass)

print('part 1: {}'.format(fuel_total))

## part 2

def calc_fuel_rec(mass):

    fuel = 0
    dfuel = calc_fuel(mass)
    
    while dfuel > 0:
        fuel += dfuel
        dfuel = calc_fuel(dfuel)

    return fuel

fuel_total2 = 0

with open('input', 'r') as f:
    for mass in f:
        fuel_total2 += calc_fuel_rec(mass)

print('part 2: {}'.format(fuel_total2))