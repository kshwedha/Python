"""
Given a string check if it has only a&b chars
and return False if a is followed by b, else True
"""

import re


def solution(S):
    # Implement your solution here
    if len(S) == 1:
        return True
    if len(S) < 1 and len(S) > 3**100000:
        return
    if re.search("[^ab]", S):
        return
    return False if "ba" in S else True
