#!/usr/bin/env python3

###############################################################################
#
print("\nExercise 13.5\n")
#
# Question 1
# 1. Write a function named choose_from_hist that takes a histogram as defined
# in "Dictionary as a Collection of Counters" and returns a random value from 
# the histogram, "chosen with probability in proportion to frequency. For 
# example, for this histogram:
#
# >>> t = ['a', 'a', 'b']
# >>> hist = histogram(t)
# >>> hist
# {'a': 2, 'b': 1}
# 
# Your function should return 'a' with probability 2/3 and 'b' with probability 
# 1/3.
#