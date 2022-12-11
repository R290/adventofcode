trees = []

with open('input', 'r') as f:

    for line in f:
        trees.append([int(t) for t in line.rstrip('\n')])

Nrows = len(trees[0])
Ncols = len(trees)

# 1
Nvisible = 2*Nrows + 2*Ncols - 4

for row in range(1, Nrows-1):
    for col in range(1, Ncols-1):

        h = trees[row][col]

        # row check
        if h > max(trees[row][:col]) or h > max(trees[row][(col+1):]):
            Nvisible += 1
            continue
        
        # column check
        column = [trees[r][col] for r in range(Nrows)]

        if h > max(column[:row]) or h > max(column[(row+1):]):
            Nvisible += 1

print(Nvisible)