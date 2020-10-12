"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

def _get_value(input:str)->str:
    """a is 1, so input str should be converted to int"""
    return chr(int(input) + ord('a')-1)

def _decode_substr(input:str)->int:
    """This decodes a 2-char substring"""
    first = _get_value(input[:1])
    second = _get_value(input)
    print(f"Decoding substring {input} into {first} and {second}")
    return int(str.isalpha(first)) + int(str.isalpha(second))

def decode_string(input:str):
    """This decodes the whole string"""
    total_ways = 0
    for i in range(0, len(input) - 1):
        total_ways += _decode_substr(input[i:i+2])

    print("Total ways to decode: {}".format(total_ways))

decode_string("123214")
decode_string("111111111")