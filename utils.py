def _ppcm(a, b):
    p = a * b
    while a != b:
        if a < b:
            b -= a
        else:
            a -= b
    return p // a


def ppcm(L):
    if len(L) == 2:
        return _ppcm(L[0], L[1])
    else:
        n = len(L)
        i = 0
        A = []
        while i <= n - 2:
            A.append(_ppcm(L[i], L[i + 1]))
            i += 2

        if n % 2 != 0:
            A.append(L[n - 1])

        return ppcm(A)