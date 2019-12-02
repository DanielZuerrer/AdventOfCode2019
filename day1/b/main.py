with open('input.txt') as input_file:
    inputs = input_file.readlines()

masses = [int(i) for i in inputs]

def calculate_fuel(mass):
    fuel = 0

    fuel_needed = int(mass / 3) - 2
    if fuel_needed > 0:
        fuel += fuel_needed + calculate_fuel(fuel_needed)

    return fuel

required_fuels = [calculate_fuel(mass) for mass in masses]

total_fuel = sum(required_fuels)

print(total_fuel)
