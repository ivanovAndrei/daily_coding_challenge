#!/usr/local/bin/python3

"""
    ** Prompt **
    Given a long string of text, count occurrence of unique words in it.
    When the count is complete, print them in a sorted by the frequency (most frequent first).
    The count should be case insensitive, and ignore extra whitespace and all punctuation.
    Hyphenated words (e.g. "brother-in-law") should count as a single word.
    The input string is declared in the class.
    There is a test method defined in the class. This method should print "Success!" when your input is sorted correctly.
    Proper error checking/exception handling is not required.

    For Example:
    excerpt = "Well The. quick, brown?    fox!! jumped over         the lazy dog The lazy brown dog jumped over the quick fox. ";
    
    Expected Test Output:
    the 4
    quick 2
    brown 2
    fox 2
    jumped 2
    over 2
    lazy 2
    dog 2
    well 1
    Success!
"""


_EXCERPT = """
A SQUAT grey building of only thirty-four stories. Over the main entrance the
 words, CENTRAL LONDON HATCHERY AND CONDITIONING CENTRE, and, in a shield, the
 World State's motto, COMMUNITY, IDENTITY, STABILITY. The enormous room on the
 ground floor faced towards the north. Cold for all the summer beyond the
 panes, for all the tropical heat of the room itself, a harsh thin light
 glared through the windows, hungrily seeking some draped lay figure, some
 pallid shape of academic goose-flesh, but finding only the glass and nickel
 and bleakly shining porcelain of a laboratory. Wintriness responded to
 wintriness. The overalls of the workers were white, their hands gloved with a
 pale corpse-coloured rubber. The light was frozen, dead, a ghost. Only from
 the yellow barrels of the microscopes did it borrow a certain rich and living
 substance, lying along the polished tubes like butter, streak after luscious
 streak in long recession down the work tables. """

import string

def _count_and_print_words(excerpt):
    word_counts_by_word = {}

    # Write your code here
    import re
    excerpt=re.sub('[^a-zA-Z0-9 -]', ' ', excerpt)
    
    tokens = excerpt.split()
    for t in tokens:
        t = t.lower()
        if t in word_counts_by_word.keys():
            word_counts_by_word[t] = word_counts_by_word[t]+1
        else:
            word_counts_by_word[t] = 1

    word_counts_by_word = {k: v for k, v in sorted(word_counts_by_word.items(), key=lambda item: item[1], reverse=True)}

    for k,v in word_counts_by_word.items():
        print(f"{v}:{k}")

    return word_counts_by_word


def main():
    word_counts_by_word = _count_and_print_words(_EXCERPT)
    _test_that_solution_is_sorted_descending(word_counts_by_word)


def _test_that_solution_is_sorted_descending(word_counts_by_word):
    previous_count = len(word_counts_by_word) + 1
    print(previous_count)
    
    if len(word_counts_by_word) == 0:
        print("Failure: List Empty!")
        return
    for word, word_count in word_counts_by_word.items():
        if word is None or word == "":
            print("Failure: Not a word: null or empty!");
            return
        if word == "thirtyfour":
            print("Failure: Not a word: \"thirtyfour\"!");
            return
        if "." in word or "," in word or "\"" in word:
            print(f"Failure: Word contains punctuation: \"{word}\"!");
            return
        if word_count > previous_count:
            print(f"{word} and {word_count} against {previous_count}")
            print("Failure: Not sorted correctly!")
            return
        previous_count = word_count
    print("Success!")


main()