"""Exhaustive census of odd-augmentation binary kernels on 16 coordinates."""
import csv
from collections import Counter
from pathlib import Path
from .linear import gf2_matmul, gf2_add_identity, gf2_nullity

N = 16


def swap_low_bits(x):
    return (x & ~3) | ((x & 1) << 1) | ((x >> 1) & 1)


def operator_rows(kernel):
    # L=P_A C_h: output row u equals C_h row A^{-1}u; A is involutive.
    rows = []
    for u in range(N):
        a = swap_low_bits(u)
        row = 0
        for v in range(N):
            if (kernel >> (a ^ v)) & 1:
                row |= 1 << v
        rows.append(row)
    return rows


def profile_and_order(L):
    D = gf2_add_identity(L, N)
    cur = D
    prof = []
    for _ in range(4):
        prof.append(gf2_nullity(cur, N))
        cur = gf2_matmul(cur, D, N)
    order = 2 if prof[1] == N else 4
    return order, tuple(prof)


def apply(L, x):
    y = 0
    for i,row in enumerate(L):
        if (row & x).bit_count() & 1:
            y |= 1 << i
    return y


def branch_number(L):
    best = 2*N
    for x in range(1, 1 << N):
        score = x.bit_count() + apply(L, x).bit_count()
        if score < best:
            best = score
            if best == 2:
                break
    return best


def run(out_csv: Path):
    counter = Counter()
    first = {}
    for h in range(1 << N):
        if h.bit_count() % 2 == 0:
            continue
        L = operator_rows(h)
        key = profile_and_order(L)
        counter[key] += 1
        first.setdefault(key, h)
    expected = {
        (2,(8,16,16,16)):1792,
        (2,(10,16,16,16)):224,
        (2,(11,16,16,16)):16,
        (2,(12,16,16,16)):16,
        (4,(4,8,12,16)):16384,
        (4,(6,12,14,16)):6144,
        (4,(8,12,16,16)):6144,
        (4,(8,14,16,16)):1792,
        (4,(10,14,16,16)):256,
    }
    assert dict(counter) == expected
    representatives = {
        (2,(8,16,16,16)):0x0007,
        (2,(10,16,16,16)):0x0091,
        (2,(11,16,16,16)):0x9991,
        (2,(12,16,16,16)):0x0001,
        (4,(4,8,12,16)):0x0002,
        (4,(6,12,14,16)):0x0122,
        (4,(8,12,16,16)):0x0023,
        (4,(8,14,16,16)):0x2225,
        (4,(10,14,16,16)):0x2223,
    }
    expected_branch = {0x0007:4,0x0091:4,0x9991:4,0x0001:2,0x0002:2,0x0122:4,0x0023:4,0x2225:6,0x2223:4}
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    with out_csv.open('w', newline='', encoding='utf-8') as f:
        w=csv.writer(f)
        w.writerow(['order','profile','representative_hex','count','branch_number'])
        for key,count in sorted(counter.items()):
            rep=representatives[key]
            b=branch_number(operator_rows(rep))
            assert b==expected_branch[rep]
            w.writerow([key[0],'-'.join(map(str,key[1])),f'{rep:04X}',count,b])
    return counter
