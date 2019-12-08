from itertools import permutations

def run(program, input_values): # copied from day5 and modified for multiple inputs and output buffer
    i = 0
    input_counter = 0
    output_buffer = []

    while program[i] != 99:

        opcode = program[i] % 100
        modes = str((program[i] - opcode))[:-2].zfill(3)

        parameter = [i+1]
        if modes[-1] == '0':
            parameter[0] = program[parameter[0]]

        if opcode in [3,4]:
            if opcode == 3:
                program[parameter[0]] = input_values[input_counter]
                input_counter += 1
            elif opcode == 4:
                # print(program[parameter[0]])
                output_buffer.append(program[parameter[0]])
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
    
    return output_buffer

with open('input', 'r') as f:
    program = [int(i) for i in f.read().split(',')]

# first input is phase setting
# second input is input signal

# part 1

phases = [0,1,2,3,4]
max_thruster_signal = 0

for phase_setting_sequence in permutations(phases):

    thruster_signal = 0

    for phase_setting in phase_setting_sequence:

        output_buffer = run(program, [phase_setting, thruster_signal])
        thruster_signal = output_buffer[0]

    if thruster_signal > max_thruster_signal:
        max_thruster_signal = thruster_signal

print('Part 1: {}'.format(max_thruster_signal))