"""Given a list of integers and number k, return whether list contains any 2 numbers which add up to k"""
def google_two_numbers(input_list:list, k:int)->bool:
    hash = dict()
    for i in input_list:
        if i in hash.keys():
            # Since this is a dup number just move on
            continue
        else:
            hash[i] = 1

            if k - i in hash.keys():
                # we found our match of K with i and another number.
                return True


    return False

    
google_two_numbers([10, 15, 10, 3, 7, 1], 13)