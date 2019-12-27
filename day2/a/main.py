operations = {
    1: lambda x, y: x + y,
    2: lambda x, y: x * y,
    99: 'terminate'
}

with open('input.txt') as input_file:
    input = input_file.readline()

intcode = [int(i) for i in input.split(",")]

# before running the program, replace position 1 with the value 12 and replace position 2 with the value 2
intcode[1] = 12
intcode[2] = 2

program_pointer = 0
while (True):
    operation = operations[intcode[program_pointer]]

    if (operation == 'terminate'):
        print(f'Result: {intcode[0]}')
        exit()

    arg_1_pos = intcode[program_pointer + 1]
    arg_2_pos = intcode[program_pointer + 2]
    result_pos = intcode[program_pointer + 3]

    intcode[result_pos] = operation(intcode[arg_1_pos], intcode[arg_2_pos])
    program_pointer += 4
