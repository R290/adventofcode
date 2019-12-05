lower = 145852
upper = 616942

password_count = 0

for password in range(lower,upper):

    digits = [int(d) for d in str(password)]

    increasing = True
    i = 0

    while increasing and i < 5:
        if digits[i+1] < digits[i]:
            increasing = False
        i += 1

    if increasing:

        double_digit = False
        i = 0

        while not double_digit and i < 5:
            if digits[i+1] == digits[i]:
                double_digit = True
            else:
                i += 1

        if double_digit:
            password_count += 1

print(password_count)