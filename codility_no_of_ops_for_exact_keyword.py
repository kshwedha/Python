"""
Given a string S, an operation can remove seven chars at once,
find the no of operation needed to make sure S contains only
the letters in forming_string(here BALLOON) only.
"""


def solution(S):
    # Implement your solution here
    forming_string = "BALLOON"
    for i in forming_string:
        if i in S:
            S = S[:S.index(i)] + S[S.index(i)+1:]
        else:
            return 0
    if S == "":
        return 0
    return len(S)//8+1
