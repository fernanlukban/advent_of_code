def calculate_fuel(mass: int) -> int:
    return mass//3 - 2

def calculate_magic_fuel(mass: int, total: int = 0) -> int:
    fuel = calculate_fuel(mass)
    if fuel <= 0:
        return total
    return calculate_magic_fuel(fuel, total + fuel)

total = 0

with open("input1.txt", 'r') as input_file:
    for line in input_file:
        mass = int(line.strip())
        total += calculate_magic_fuel(mass)

print(total)
