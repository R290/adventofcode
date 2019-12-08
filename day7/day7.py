from itertools import permutations

class Amplifier:

    def __init__(self, program, phase):

        self.program = program.copy()
        self.i = 0
        self.output_value = None
        self.halted = False

        self.run_until_next_input(phase)

    def run_until_next_input(self, input_value): 

        i = self.i
        program = self.program
        first_input = True

        while program[i] != 99:

            opcode = program[i] % 100
            modes = str((program[i] - opcode))[:-2].zfill(3)

            parameter = [i+1]
            if modes[-1] == '0':
                parameter[0] = program[parameter[0]]

            if opcode in [3,4]:
                if opcode == 3:
                    if not first_input:
                        self.i = i
                        self.program = program
                        break
                    program[parameter[0]] = input_value
                    first_input = False
                elif opcode == 4:
                    self.output_value = program[parameter[0]]
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

        else:
            self.halted = True


with open('input', 'r') as f:
    program = [int(i) for i in f.read().split(',')]

# part 1

phases = [0,1,2,3,4]
max_thruster_signal = 0

for phase_setting_sequence in permutations(phases):

    amp_series = [Amplifier(program,p) for p in phase_setting_sequence]
    thruster_signal = 0

    for amp in amp_series:
        amp.run_until_next_input(thruster_signal)
        thruster_signal = amp.output_value

    if thruster_signal > max_thruster_signal:
        max_thruster_signal = thruster_signal

print('Part 1: {}'.format(max_thruster_signal))

# part 2

phases = [9,7,8,5,6]
max_thruster_signal = 0

for phase_setting_sequence in permutations(phases):

    amp_series = [Amplifier(program,p) for p in phase_setting_sequence]
    thruster_signal = 0

    while not amp_series[-1].halted:
        for amp in amp_series:
            amp.run_until_next_input(thruster_signal)
            thruster_signal = amp.output_value

    if thruster_signal > max_thruster_signal:
        max_thruster_signal = thruster_signal

print('Part 2: {}'.format(max_thruster_signal))