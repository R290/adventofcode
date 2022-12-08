with open('input', 'r') as f:
    line = f.readline().rstrip('\n')

# 1
for i in range(len(line)-3):
    charset = set(line[i:i+4])

    if len(charset) == 4:
        print(i+4)
        break

for i in range(len(line)-13):

    charset2 = set(line[i:i+14])

    if len(charset2) == 14:
        print(i+14)
        break
