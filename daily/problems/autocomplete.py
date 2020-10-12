"""
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
"""

def autocomplete(query:str, dictionary:list)->list:
    dictionary.sort()
    start=None
    end=None
    for i, entry in enumerate(dictionary):
        found_match = entry.startswith(query)
        if found_match and not start:
            start = i
        elif start and not found_match:
            end = i
            return dictionary[start:end]

acs = autocomplete("de", ["abc", "deer", "dog", "gazelle", "dumbo", "dumb", "destiny", "croc"])
print(acs)