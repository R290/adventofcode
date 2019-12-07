with open('input', 'r') as f:
    program = [int(i) for i in f.read().split(',')]

i=0 # instruction pointer

while program[i] != 99:

    if program[i] == 1: # add
        program[program[i+3]] = program[program[i+1]] + program[program[i+2]]
        i += 4

    elif program[i] == 2: # multiply
        program[program[i+3]] = program[program[i+1]] * program[program[i+2]]
        i += 4

    elif program[i] == 3: # input
        program[program[i+1]] = 1 # as stated in the description
        i += 2

    elif program[i] == 4: # output
        print(program[program[i+1]])
        i += 2
    
    elif program[i] >= 100: # immediate mode

        opcode = program[i] % 100
        parameter_modes = str((program[i] - opcode))[:-2]

        # pad the paramater modes if necesary
        if opcode != 4:
            parameter_modes = parameter_modes.zfill(3)[::-1]
        else:
            parameter_modes = parameter_modes[::-1]

        parameters = []

        for p in range(len(parameter_modes)):

            mode = parameter_modes[p]

            if mode == '0':
                parameters.append(program[program[i+p+1]])
            elif mode == '1':
                parameters.append(program[i+p+1])

        if opcode == 1: # add
            program[program[i+3]] = parameters[0]+parameters[1]
            i += 4
        elif opcode == 2: # multiply
            program[program[i+3]] = parameters[0]*parameters[1]
            i += 4
        elif opcode == 4:
            print(parameters[0])
            i += 2
    
    

        