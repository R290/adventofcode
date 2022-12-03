def get_priority(c):
    if c.islower():
        return ord(c)-96 
    else:
        return ord(c)-38

#1
item_sum1 = 0

with open('input', 'r') as f:

    for line in f:

        items = line.rstrip('\n')
        N = int(len(items)/2)
        
        comp1 = items[:N]
        comp2 = items[N:]

        # can be replaced with sets
        for i in comp1:
            if i in comp2:
                item_sum1 += get_priority(i)
                break

print(item_sum1)

#2
item_sum2 = 0

with open('input', 'r') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

for li in range(0, len(lines), 3):
    r1 = set(lines[li])             
    r2 = set(lines[li+1])
    r3 = set(lines[li+2])

    badge = ''.join(r1 & r2 & r3)
    item_sum2 += get_priority(badge)

print(item_sum2)