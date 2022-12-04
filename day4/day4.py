fully_contains = 0
overlap = 0

with open('input', 'r') as f:

    for line in f:

        ass1, ass2 = line.rstrip('\n').split(',')

        b1, e1 = ass1.split('-')
        b2, e2 = ass2.split('-')

        sec1 = set(range(int(b1),int(e1)+1))
        sec2 = set(range(int(b2),int(e2)+1))

        if sec1 >= sec2 or sec2 >= sec1:
            fully_contains += 1

        if len(sec1 & sec2) > 0:
            overlap += 1

print(fully_contains)
print(overlap)