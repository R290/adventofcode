## part 1

with open('input', 'r') as f:
    program = [int(i) for i in f.read().split(',')]

# modifications
program[1] = 12
program[2] = 2

i = 0

while program[i] != 99:

    if program[i] == 1: # add
        program[program[i+3]] = program[program[i+1]] + program[program[i+2]]
    elif program[i] == 2: # multiply
        program[program[i+3]] = program[program[i+1]] * program[program[i+2]]

    i += 4

print('part 1: {}'.format(program[0]))

## part 2

with open('input', 'r') as f:
    program_init = [int(i) for i in f.read().split(',')]

# brute force approach
for noun in range(100):
    for verb in range(100):
        program = program_init.copy()

        program[1] = noun
        program[2] = verb

        i = 0

        while program[i] != 99:

            if program[i] == 1: # add
                program[program[i+3]] = program[program[i+1]] + program[program[i+2]]
            elif program[i] == 2: # multiply
                program[program[i+3]] = program[program[i+1]] * program[program[i+2]]

            i += 4

        if program[0] == 19690720:
            break

    else: # required to break outer loop as well
        continue
    break

print('part 2: {}'.format(100*noun+verb))