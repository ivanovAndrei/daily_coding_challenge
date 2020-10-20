"""
Given an array of integers and a number k, where 1 <= k <= length of the array, 
compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

    10 = max(10, 5, 2)
    7 = max(5, 2, 7)
    8 = max(2, 7, 8)
    8 = max(7, 8, 7)

Do this in O(n) time and O(k) space. You can modify the input array in-place and 
you do not need to store the results. You can simply print them out as you compute them.
"""
def compute_max_subarray(input:list, k:int):
    """What we want to do is take a subarray of length k, find its max, and write max into the 1st 
    element of the array"""
    i = 0
    saved_max = False
    for i in range(len(input)):
        if i + k > len(input):
            break

        subarray=input[i:i+k]
    
        print(f"checking sublist {subarray}, max value saved? {saved_max}")

        if saved_max:
            sub_max = max(subarray[0], subarray[k-1])
        else:
            sub_max = max(subarray)

        if subarray[0] == sub_max:
            # Our first element of subarray is the max one, it's goiing to disappear next iteration
            # Don't care. Just print
            print(sub_max)
            saved_max = False
        else:
            # Turns out our max value isn't going to go away next iteration. So, write it into i+1'th
            # index of the array, and next iteration we'll compare it to the new last element
            input[i+1] = sub_max
            saved_max = True
            print(sub_max)

compute_max_subarray( [10, 5, 2, 7, 8, 7] , 3)