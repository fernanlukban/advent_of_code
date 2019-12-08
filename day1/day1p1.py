def calculate_fuel(mass: int) -> int:
    return mass//3 - 2

total = 0

with open("input1.txt", 'r') as input_file:
    for line in input_file:
        mass = int(line.strip())
        total += calculate_fuel(mass)

print(total)