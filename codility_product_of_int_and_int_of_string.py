"""
Given a int value and string containing number phrase (limited to 5),
return the product of int*int_of_string
"""


def solution(D, S):
    """
    method restricted to string val of 5
    """
    num_words = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5
    }
    return D*num_words.get(S, -1)


def solution(D, S):
    """
    method 2: unrestricted
    """
    # S = "seven hundred ninety one"
    # S = "one hundred seventeen"
    # S = "seventy three"
    num_words = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
        "thirty": 30,
        "fourty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
        "hundred": 100,
        "thousand": 1000
    }
    val = 0
    for i in S.split(' '):
        val = (val if val != 0 else 1) * \
            num_words.get(i, 1) if num_words.get(
                i, 1) == 100 else val+num_words.get(i, 1)
    return D*val
