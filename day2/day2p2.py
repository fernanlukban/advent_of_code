from collections import defaultdict

ADD_OPCODE = 1
MULTIPLY_OPCODE = 2
END_OPCODE = 99

def run_program(input_file, noun = 12, verb = 2):
    input_file = list(map(lambda num_as_string: int(num_as_string), input_file))
    input_file[1] = noun
    input_file[2] = verb
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
            return input_file
        index += 4
    return input_file

TARGET = 19690720
noun = 50
verb = 50

for noun in range(100):
        for verb in range(100):
            # print(noun, verb)
            with open("input2.txt", "r") as input_file:
                input_file = input_file.read().strip().split(",")
                input_file = run_program(input_file, noun, verb)
                if input_file[0] == TARGET:
                    print(noun, verb)
                    print(100 * noun + verb)