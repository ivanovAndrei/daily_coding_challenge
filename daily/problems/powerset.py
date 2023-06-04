'''
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.
For example, given the set {1, 2, 3, 4}, it should return {{}, {1}, {2}, {3}, {4},
{1, 2}, {1, 3}, {3, 4}, {1, 2, 4}, {1, 3, 4}, {2, 3, 4}, {1, 2, 3, 4}}.
You may also use a list or array to represent a set.
'''

import math


def printPowerSet(original_set):
    set_size = len(original_set)
    # set_size of power set of a set
    # with set_size n is (2**n -1)
    pow_set_size = (int)(math.pow(2, set_size))

    # Run from counter 000..0 to 111..1
    for counter in range(0, pow_set_size):
        subset = set()
        for j in range(0, set_size):

            # Check if jth bit in the
            # counter is set If set then
            # print jth element from set
            if (counter & (1 << j)) > 0:
                subset.add(original_set[j])
        print(subset)


# Driver program to test printPowerSet
input_set = ['1', '2', '3', '4']
printPowerSet(input_set)
