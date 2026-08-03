"""Exact matrix utilities over GF(2) and GF(2^8)."""
from . import finite_field as gf


def mat_mul(A, B, mul=gf.mul, add=lambda x, y: x ^ y):
    n, k, m = len(A), len(B), len(B[0])
    C = [[0] * m for _ in range(n)]
    for i in range(n):
        for t in range(k):
            a = A[i][t]
            if a:
                for j in range(m):
                    if B[t][j]:
                        C[i][j] = add(C[i][j], mul(a, B[t][j]))
    return C


def eye(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def mat_pow(A, e):
    R = eye(len(A))
    while e:
        if e & 1:
            R = mat_mul(R, A)
        A = mat_mul(A, A)
        e >>= 1
    return R


def rank_ff(A):
    M = [row[:] for row in A]
    n, m = len(M), len(M[0]) if M else 0
    r = 0
    for c in range(m):
        p = next((i for i in range(r, n) if M[i][c]), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        ip = gf.inv(M[r][c])
        M[r] = [gf.mul(x, ip) for x in M[r]]
        for i in range(n):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [x ^ gf.mul(f, y) for x, y in zip(M[i], M[r])]
        r += 1
        if r == n:
            break
    return r


def nullity_ff(A):
    return len(A[0]) - rank_ff(A)


def sub_identity(A):
    B = [row[:] for row in A]
    for i in range(len(B)):
        B[i][i] ^= 1
    return B


def scalar_mul_matrix(c, A):
    return [[gf.mul(c, x) for x in row] for row in A]


def is_scalar(A):
    n = len(A)
    c = A[0][0]
    for i in range(n):
        for j in range(n):
            if A[i][j] != (c if i == j else 0):
                return False, None
    return True, c


def matrix_order(A, divisors):
    for d in sorted(divisors):
        if mat_pow(A, d) == eye(len(A)):
            return d
    raise AssertionError("order not found")


def projective_order(A, divisors):
    for d in sorted(divisors):
        ok, _ = is_scalar(mat_pow(A, d))
        if ok:
            return d
    raise AssertionError("projective order not found")

# Binary matrices as row bitmasks.
def gf2_rank(rows, n):
    rows = rows[:]
    r = 0
    for c in range(n):
        p = next((i for i in range(r, len(rows)) if (rows[i] >> c) & 1), None)
        if p is None:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        for i in range(len(rows)):
            if i != r and ((rows[i] >> c) & 1):
                rows[i] ^= rows[r]
        r += 1
    return r


def gf2_matmul(A, B, n):
    cols = []
    for j in range(n):
        col = 0
        for i, row in enumerate(B):
            if (row >> j) & 1:
                col |= 1 << i
        cols.append(col)
    out = []
    for row in A:
        val = 0
        for j, col in enumerate(cols):
            if (row & col).bit_count() & 1:
                val |= 1 << j
        out.append(val)
    return out


def gf2_eye(n):
    return [1 << i for i in range(n)]


def gf2_add_identity(A, n):
    return [row ^ (1 << i) for i, row in enumerate(A)]


def gf2_nullity(A, n):
    return n - gf2_rank(A, n)
