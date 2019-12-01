# Advent of code Year 2019 Day 1 solution
# Author = rygel
# Date = December 2019
import io

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

total_fuel = 0

for mass in io.StringIO(input):
    fuel = int(int(mass) / 3) - 2
    total_fuel = fuel + total_fuel


print("Part One : "+ str(total_fuel))

total_fuel = 0

for mass in io.StringIO(input):
    fuel_for_mass = int(int(mass) / 3) - 2

    fuel_for_fuel = fuel_for_mass
    total_fuel_for_fuel = 0

    while fuel_for_fuel > 0:
        fuel_for_fuel = int(int(fuel_for_fuel) / 3) - 2
        if fuel_for_fuel > 0 :
            total_fuel_for_fuel = total_fuel_for_fuel + fuel_for_fuel 

    
    total_fuel = total_fuel + total_fuel_for_fuel + fuel_for_mass

print("Part Two : "+ str(total_fuel))