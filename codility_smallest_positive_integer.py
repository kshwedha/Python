"""
return if any absence of smallest
positive no in the list else return
"""


def solution(A):
    if len(A) < 1 and len(A) > 10**10000:
        return
    if A[0] < -1000000 and A[len(A)-1] > 1000000:
        return
    max_val = max(A)
    if max_val < 2:
        return
    for i in range(1, max_val):
        if i not in A:
            return i
    return
