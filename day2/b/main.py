instructions = {
    1: lambda x, y: x + y,
    2: lambda x, y: x * y,
    99: 'terminate'
}

with open('input.txt') as input_file:
    input = input_file.readline()

default_memory = [int(i) for i in input.split(",")]

def get_answer(default_memory, noun, verb):
    memory = default_memory.copy()

    memory[1] = noun
    memory[2] = verb

    instruction_pointer = 0
    while (True):
        instruction = instructions[memory[instruction_pointer]]

        if (instruction == 'terminate'): break

        param_1_address = memory[instruction_pointer + 1]
        param_2_address = memory[instruction_pointer + 2]
        result_address = memory[instruction_pointer + 3]

        memory[result_address] = instruction(memory[param_1_address], memory[param_2_address])
        instruction_pointer += 4

    return memory[0]

for noun in range(100):
    for verb in range(100):
        answer = get_answer(default_memory, noun, verb)
        if (answer == 19690720):
            print(f'Result: {100 * noun + verb}')
            exit()
