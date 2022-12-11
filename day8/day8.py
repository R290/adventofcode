trees = []

with open('input', 'r') as f:

    for line in f:
        trees.append([int(t) for t in line.rstrip('\n')])

Nrows = len(trees[0])
Ncols = len(trees)

# 1
Nvisible = 2*Nrows + 2*Ncols - 4

# 2
scenic_score_max = 0

for row in range(1, Nrows-1):
    for col in range(1, Ncols-1):

        h = trees[row][col]
        column = [trees[r][col] for r in range(Nrows)]

        # 1
        if h > max(trees[row][:col]) or h > max(trees[row][(col+1):]):
            Nvisible += 1
        elif h > max(column[:row]) or h > max(column[(row+1):]):
            Nvisible += 1

        # 2

        # left
        for i, t in enumerate(trees[row][col-1::-1]):
            if t >= h:
                left = i+1
                break
        else:
            left = col

        # right
        for i, t in enumerate(trees[row][col+1:]):
            if t >= h:
                right = i+1
                break
        else:
            right = Ncols - col - 1

        # up
        for i, t in enumerate(column[row-1::-1]):
            if t >= h:
                up = i+1
                break
        else:
            up = row

        # down
        for i, t in enumerate(column[row+1:]):
            if t >= h:
                down = i+1
                break
        else:
            down = Nrows - row - 1

        scenic_score = left*right*up*down

        if scenic_score > scenic_score_max:
            scenic_score_max = scenic_score


print(Nvisible)
print(scenic_score_max)