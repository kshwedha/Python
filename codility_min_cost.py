"""
Given string S and it's corresponding array of
len S with values(cost), find the minimum cost
output to make sure no adj char is repeatitive
"""
import re


def get_optimised_string(i=0, S=None, C=None, min_cost=0):
    if i == len(S)-1:
        return min_cost
    if C is None or S is None:
        return min_cost
    if S[i] == S[i+1]:
        if C[i] > C[i+1]:
            min_cost += C[i+1]
            C.pop(i+1)
        else:
            min_cost += C[i]
            C.pop(i)
        return get_optimised_string(i, S[:i]+S[i+1:], C, min_cost)
    else:
        return get_optimised_string(i+1, S, C, min_cost)


def solution(S, C):
    if not len(S) == len(C):
        return
    if len(S) < 1 and len(S) > 10*10000:
        return
    if len(S) == 1:
        return
    if re.search("[^a-z]", S):
        return
    return get_optimised_string(i=0, S=S, C=C)
