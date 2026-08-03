"""Complete 240-shift Cauchy-Walsh census over the AES field."""
import csv
from pathlib import Path
from . import finite_field as gf
from .linear import mat_mul, scalar_mul_matrix, sub_identity, nullity_ff, mat_pow, projective_order

V = list(range(16))


def swap_low_bits(x: int) -> int:
    b0, b1 = x & 1, (x >> 1) & 1
    return (x & ~3) | (b0 << 1) | b1


def convolution_matrix(h):
    return [[h[u ^ v] for v in V] for u in V]


def permutation_matrix():
    P = [[0] * 16 for _ in range(16)]
    for u in V:
        P[swap_low_bits(u)][u] = 1
    return P


def profile(U):
    N = sub_identity(U)
    cur = N
    out = []
    for _ in range(4):
        out.append(nullity_ff(cur))
        cur = mat_mul(cur, N)
    return tuple(out)


def run(out_csv: Path):
    P = permutation_matrix()
    rows = []
    counts = {}
    for gamma in range(16, 256):
        h = [gf.inv(gamma ^ v) for v in V]
        c = 0
        for x in h:
            c ^= x
        C = convolution_matrix(h)
        L = mat_mul(P, C)
        U = scalar_mul_matrix(gf.inv(c), L)
        prof = profile(U)
        po = projective_order(U, [1, 2, 4])
        so = gf.order(c)
        counts[so] = counts.get(so, 0) + 1
        rows.append((gamma, c, so, po, *prof))
    expected = {5: 16, 17: 16, 51: 32, 85: 64, 255: 112}
    assert counts == expected, (counts, expected)
    assert all(r[3] == 4 and tuple(r[4:]) == (4, 8, 12, 16) for r in rows)
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    with out_csv.open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['gamma_hex','augmentation_hex','scalar_order','projective_order','d1','d2','d3','d4'])
        for gamma,c,so,po,*prof in rows:
            w.writerow([f'{gamma:02X}',f'{c:02X}',so,po,*prof])
    return counts
