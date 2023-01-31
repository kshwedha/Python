def get_sparse_list(n, N, pure):
    if 2*n <= (N+1)//2:
        if "11" not in format(N-(2*n), 'b'):
            return N-2*n
        val = get_sparse_list(
            n=2*n, N=N, pure=True)
        if val != -1:
            return val
        if pure:
            if 2*n+1 <= N:
                if "11" not in format(N-(2*n+1), 'b'):
                    return N-(2*n+1)
                val = get_sparse_list(
                    n=2*n+1, N=N, pure=False)
                if val != -1:
                    return val
    return -1


def solution(N):
    if N < 0 and N > 10**8:
        return -1
    if N <= 2:
        return N
    if "11" not in format(N, 'b'):
        return N
    if "11" not in format(N-1, 'b'):
        return N-1
    if "11" not in format(N-2, 'b'):
        return N-2
    return get_sparse_list(
        n=2, N=N, pure=True)
