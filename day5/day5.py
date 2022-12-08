from copy import deepcopy

stacks = []

with open('input','r') as f:

    for line in f:

        # end of initial stack definition
        if line[1] == '1':
            break
        
        if len(stacks) == 0:
            stacks = [[] for _ in range(int((len(line)+1)/4))]
        
        for i in range(1, len(line), 4):
            if line[i] != ' ':
                stacks[i//4].append(line[i])

# reverse stacks
for i in range(len(stacks)):
    stacks[i] = stacks[i][::-1]

# stacks = [['Z', 'N'],
#           ['M', 'C', 'D'],
#           ['P']]

# copy for part 2
stacks2 = deepcopy(stacks)

with open('input','r') as f:
    for line in f:
        if line[:4] != 'move':
            continue

        (_, N, _, org, _, dst) = line.rstrip('\n').split(' ')

        org = int(org)-1
        dst = int(dst)-1
        N = int(N)

    	# 1
        for _ in range(N):
            stacks[dst].append(stacks[org].pop())

        # 2
        stacks2[dst] += stacks2[org][-N:]
        del stacks2[org][-N:]

print(''.join([stack[-1] for stack in stacks]))
print(''.join([stack[-1] for stack in stacks2]))