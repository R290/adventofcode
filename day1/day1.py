with open('input', 'r') as f:

    calories = [0]

    for line in f:

        if line != '\n':
            calories[-1] += int(line.rstrip('\n'))
        else:
            calories.append(0)
        
calories.sort(reverse=True)

print(calories[0])
print(sum(calories[:3]))