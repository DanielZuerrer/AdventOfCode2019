with open('input.txt') as input_file:
    inputs = input_file.readlines()

masses = [int(i) for i in inputs]

def calculate_fuel(mass):
    return int(mass / 3) - 2

required_fuels = [calculate_fuel(mass) for mass in masses]

total_fuel = sum(required_fuels)

print(total_fuel)
