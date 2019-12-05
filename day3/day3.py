def follow_wire(x, y, step):

    dir = step[0]
    dst = int(step[1:])

    if dir == 'U':
        y += dst

    elif dir == 'D':
        y -= dst
    
    elif dir == 'L':
        x -= dst

    elif dir == 'R':
        x += dst
    
    return x, y

# read input
with open('input', 'r') as f:
    wire1 = f.readline().rstrip().split(',')
    wire2 = f.readline().rstrip().split(',')

# test problems
# wire1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(',')
# wire2 = 'U62,R66,U55,R34,D71,R55,D58,R83'.split(',')
# wire1 = 'R8,U5,L5,D3'.split(',')
# wire2 = 'U7,R6,D4,L4'.split(',')

x1a = 0
y1a = 0

manhattan_distances = []

step_sum1 = 0
step_sum_dict1 = {}

step_sum2 = 0
step_sum_dict2 = {}

step_sum_output = []

for w1 in wire1:

    x1b, y1b = follow_wire(x1a, y1a, w1)

    if (x1b, y1b) in step_sum_dict1:
        step_sum1 = step_sum_dict1[(x1b, y1b)]
    else:
        step_sum1 += abs(x1a - x1b) + abs(y1a - y1b)
        step_sum_dict1[(x1b, y1b)] = step_sum1
    
    x2a = 0
    y2a = 0

    for w2 in wire2:

        x2b, y2b = follow_wire(x2a, y2a, w2)

        if (x2b, y2b) in step_sum_dict2:
            step_sum2 = step_sum_dict2[(x2b, y2b)]
        else:
            step_sum2 += abs(x2a - x2b) + abs(y2a - y2b)
            step_sum_dict2[(x2b, y2b)] = step_sum2

        # check if wire2 crosses wire1 horizontally at an y of wire1
        if (min(x2a, x2b) < x1a < max(x2a, x2b)) and (min(y1a, y1b) < y2a < max(y1a, y1b)):
            print('crossing at {},{}'.format(x1a, y2a))

            # part 1
            manhattan_distances.append(abs(x1a) + abs(y2a)) 

            # part 2
            step_sum_output.append(step_sum_dict1[(x1a,y1a)] + step_sum_dict2[(x2a, y2a)] + abs(x1a - x2a) + abs(y1a - y2a))

        # check if wire2 crosses wire1 vertically at an x of wire1
        if (min(y2a, y2b) < y1a < max(y2a, y2b)) and (min(x1a, x1b) < x2a < max(x1a, x1b)):
            print('crossing at {},{}'.format(x2a, y1a))

            # part 1 
            manhattan_distances.append(abs(x2a) + abs(y1a)) # part 1

            # part 2
            step_sum_output.append(step_sum_dict1[(x1a,y1a)] + step_sum_dict2[(x2a, y2a)] + abs(x1a - x2a) + abs(y1a - y2a))

        # endpoint is the beginpoint for the next step
        x2a = x2b
        y2a = y2b

    # endpoint is the beginpoint for the next step
    x1a = x1b
    y1a = y1b

print('part 1: {}'.format(min(manhattan_distances)))
print('part 2: {}'.format(min(step_sum_output)))