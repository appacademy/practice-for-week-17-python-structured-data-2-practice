#  Stacks

# Create a function named stack that keeps the scores of a game with specific
# rules. At the beginning of the game, you start with an empty record. You are
# given a list of strings, some strings have a special rule applied to the
# record.

# An integer n.
# Record a new score of n.

# The symbol '+'.
# Records a new score that is the sum of the previous two scores.

# 'T'.
# Record a new score that is the Triple of the previous score.

# 'P'.
# Removes the previous score from the record.

# Your code here

lst = ["10","5","P","T","+"]

print(stack(lst)) # 80