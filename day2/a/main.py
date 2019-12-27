instructions = {
    1: lambda x, y: x + y,
    2: lambda x, y: x * y,
    99: 'terminate'
}

with open('input.txt') as input_file:
    input = input_file.readline()

memory = [int(i) for i in input.split(",")]

# before running the program, replace position 1 with the value 12 and replace position 2 with the value 2
memory[1] = 12
memory[2] = 2

instruction_pointer = 0
while (True):
    instruction = instructions[memory[instruction_pointer]]

    if (instruction == 'terminate'): break

    param_1_address = memory[instruction_pointer + 1]
    param_2_address = memory[instruction_pointer + 2]
    result_address = memory[instruction_pointer + 3]

    memory[result_address] = instruction(memory[param_1_address], memory[param_2_address])
    instruction_pointer += 4

print(f'Result: {memory[0]}')
