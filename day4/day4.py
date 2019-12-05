lower = 145852
upper = 616942
len = 6

password_count_part1 = 0
password_count_part2 = 0

for password in range(lower,upper):

    digits = [int(d) for d in str(password)]

    increasing = True
    i = 0

    while increasing and i < len-1:
        if digits[i+1] < digits[i]:
            increasing = False
        i += 1

    if increasing:
        # part 1
        double_digit = False
        i = 0

        while not double_digit and i < len-1:
            if digits[i+1] == digits[i]: 
                double_digit = True
            else:
                i += 1
        

        if double_digit:
            password_count_part1 += 1

        # part 2
        isolated_double_digit = False
        i = 0

        while not isolated_double_digit and i < len-1:
            if digits[i+1] == digits[i]:
                if (i == 0) and (digits[1] != digits[2]): # left edge case
                    isolated_double_digit = True
                elif (i == len-2) and (digits[i] != digits[i-1]): # right edge case
                    isolated_double_digit = True
                elif (digits[i-1] != digits[i]) and (digits[i+2] != digits[i]): # center case
                    isolated_double_digit = True
                else:
                    i += 1
            else:
                i += 1

        if isolated_double_digit:
            password_count_part2 += 1

print('part1: {}'.format(password_count_part1))
print('part2: {}'.format(password_count_part2))
