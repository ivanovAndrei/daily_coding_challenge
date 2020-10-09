def comparer(a, b):
    if len(a) < len(b):
        return -1
    elif len(a) > len(b):
        return 1
    else:
        return -1 if a < b else 1
    
    
def analyze(input):
    tokens = input.split()
    lex = list()
    count = dict()
    
    low = 0
    buf_length = 10
    
    while low < len(input):
        buf = input[low:low+buf_length]        
        
    for s in tokens:
        if s in count.keys():
            count[s]= count[s]+1
        else:
            lex.append(s)
            count[s] = 1
            
    lex.sort(cmp=comparer)
    
    for entry in lex:
        print("{} {}".format(count[entry], entry))
   
analyze("Mary had a little lamb and his name was Christopher Robin and he was a Trex so not really a lamb")

'''
Unit tests to write:
1. null string
2. string with punctuation: do we have diff entries for 'blah' and 'blah,'?
3. string longer than some reasonable buffer? How big? 1GB?
4. Single word string large, esp if we're using a buffering implementation
5. If case-insensitive, test with same string with difFerENT CaseS
'''