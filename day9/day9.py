# the basis is copied from day7
class Amplifier:

    def __init__(self, program, phase=None):

        self.program = program.copy()
        self.i = 0
        self.output_value = None
        self.halted = False
        self.relative_base = 0

        if phase:
            self.run_until_next_input(phase)

    def run_until_next_input(self, input_value=None): 

        i = self.i
        program = self.program
        first_input = True
        self.output_value_list = []

        while program[i] != 99:

            opcode = program[i] % 100
            modes = str((program[i] - opcode))[:-2].zfill(3)

            parameter = [i+1]
            if modes[-1] == '0':
                parameter[0] = program[parameter[0]]
            elif modes[-1] == '2':
                parameter[0] = self.relative_base + program[parameter[0]]

            if opcode in [3,4,9]:
                if opcode == 3:
                    if not first_input:
                        self.i = i
                        self.program = program
                        break
                    program[parameter[0]] = input_value
                    first_input = False
                elif opcode == 4:
                    self.output_value = program[parameter[0]]
                    self.output_value_list.append(self.output_value)
                elif opcode == 9:
                    self.relative_base += program[parameter[0]]
                i += 2
                continue

            parameter.append(i+2)
            if modes[-2] == '0':
                parameter[1] = program[parameter[1]]
            elif modes[-2] == '2':
                parameter[1] = self.relative_base + program[parameter[1]]

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
            elif modes[-3] == '2':
                parameter[2] = self.relative_base + program[parameter[2]]

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

program += [0]*10000 # quick & dirty

# part 1
amp = Amplifier(program)
amp.run_until_next_input(1)
# print(amp.output_value_list)
print('Part 1: {}'.format(amp.output_value))

# part 2
amp = Amplifier(program)
amp.run_until_next_input(2)
print('Part 2: {}'.format(amp.output_value))