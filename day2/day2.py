# 1
# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# The score for a single round is the score for the shape you selected 
# (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round
# (0 if you lost, 3 if the round was a draw, and 6 if you won).

# 2
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.

score_sum1 = 0
score_sum2 = 0

scores1 = {'X': 1, 'Y': 2, 'Z': 3}
draw1 = {'X': 'A', 'Y': 'B', 'Z': 'C'}
win1 = {'X': 'C', 'Y': 'A', 'Z': 'B'}

scores2 = {'X': 0, 'Y': 3, 'Z': 6}
draw2 = {'A': 1, 'B': 2, 'C': 3}
win2 = {'A': 2, 'B': 3, 'C': 1}
lose2 = {'A': 3, 'B': 1, 'C': 2}

with open('input', 'r') as f:
    for line in f:
        op, me = line.rstrip('\n').split(' ')

        # 1
        score_sum1 += scores1[me]

        if draw1[me] == op:
            # draw
            score_sum1 += 3
        elif win1[me] == op:
            # win
            score_sum1 += 6 
        # no action on loss

        # 2
        end = me
        score_sum2 += scores2[end]

        # draw
        if end == 'Y':
            score_sum2 += draw2[op]
        elif end == 'Z':
            # win
            score_sum2 += win2[op]
        elif end == 'X':
            # lose
            score_sum2 += lose2[op]


print(score_sum1)
print(score_sum2)