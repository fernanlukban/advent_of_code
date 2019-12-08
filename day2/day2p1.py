from collections import defaultdict

ADD_OPCODE = 1
MULTIPLY_OPCODE = 2
END_OPCODE = 99

with open("input2.txt", "r") as input_file:
    input_file = list(map(lambda num_as_string: int(num_as_string), input_file.read().strip().split(",")))
    input_file[1] = 12
    input_file[2] = 2
    index = 0
    while index < len(input_file):
        first_operand = input_file[index + 1]
        second_operand = input_file[index + 2]
        memory_location = input_file[index + 3]
        if input_file[index] == ADD_OPCODE:
            input_file[memory_location] = input_file[first_operand] + input_file[second_operand]
        elif input_file[index] == MULTIPLY_OPCODE:
            input_file[memory_location] = input_file[first_operand] * input_file[second_operand]
        elif input_file[index] == END_OPCODE:
            break
        else:
            print("ERROR", input_file, input_file[index])
        index += 4

print(input_file[0])
