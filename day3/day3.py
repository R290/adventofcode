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
wire1 = 'R8,U5,L5,D3'.split(',')
wire2 = 'U7,R6,D4,L4'.split(',')

x1a = 0
y1a = 0

manhattan_distances = [] 

for w1 in wire1:

    x1b, y1b = follow_wire(x1a, y1a, w1)

    x2a = 0
    y2a = 0

    for w2 in wire2:

        x2b, y2b = follow_wire(x2a, y2a, w2)

        # check if wire2 crosses wire1 horizontally at an y of wire1
        if (max(x2a, x2b) > x1a) and (min(x2a, x2b) < x1a) and (min(y1a, y1b) < y2a < max(y1a, y1b)):
            print('crossing at {},{}'.format(x1a, y2a))
            manhattan_distances.append(abs(x1a) + abs(y2a))

        # check if wire2 crosses wire1 vertically at an x of wire1
        if (max(y2a, y2b) > y1a) and (min(y2a, y2b) < y1a) and (min(x1a, x1b) < x2a < max(x1a, x1b)):
            print('crossing at {},{}'.format(x2a, y1a))
            manhattan_distances.append(abs(x2a) + abs(y1a))

        # endpoint is the beginpoint for the next step
        x2a = x2b
        y2a = y2b

    # endpoint is the beginpoint for the next step
    x1a = x1b
    y1a = y1b

print(min(manhattan_distances))