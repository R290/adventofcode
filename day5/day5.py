def run(program, input_value):
    i = 0

    while program[i] != 99:

        opcode = program[i] % 100
        modes = str((program[i] - opcode))[:-2].zfill(3)

        parameter = [i+1]
        if modes[-1] == '0':
            parameter[0] = program[parameter[0]]

        if opcode in [3,4]:
            if opcode == 3:
                program[parameter[0]] = input_value   
            elif opcode == 4:
                print(program[parameter[0]])
            i += 2
            continue

        parameter.append(i+2)
        if modes[-2] == '0':
            parameter[1] = program[parameter[1]]

        if opcode in [5,6]:
            if opcode == 5 and (program[parameter[0]] != 0):
                i = program[parameter[1]]
                continue
            elif opcode == 6 and (program[parameter[0]] == 0):
                i = program[parameter[1]]
                continue
            i += 3
            continue

        parameter.append(i+3)
        if modes[-3] == '0':
            parameter[2] = program[parameter[2]]

        if opcode in [1,2,7,8]:
            if opcode == 1:
                program[parameter[2]] = program[parameter[0]] + program[parameter[1]]
            elif opcode == 2:
                program[parameter[2]] = program[parameter[0]] * program[parameter[1]]
            elif opcode == 7:
                program[parameter[2]] = int(program[parameter[0]] < program[parameter[1]])
            elif opcode == 8:
                program[parameter[2]] = int(program[parameter[0]] == program[parameter[1]])
            i += 4

with open('input', 'r') as f:
    program = [int(i) for i in f.read().split(',')]

print('part1:')
run(program.copy(), 1)

print('\npart2:')
run(program.copy(), 5)