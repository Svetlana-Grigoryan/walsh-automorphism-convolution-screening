"""Quantitative AES linear-layer recurrence benchmark."""
import csv
from pathlib import Path
from . import finite_field as gf
from .linear import mat_mul, mat_pow, eye, nullity_ff, projective_order

MC4 = [
    [2,3,1,1],
    [1,2,3,1],
    [1,1,2,3],
    [3,1,1,2],
]


def mixcolumns16():
    M=[[0]*16 for _ in range(16)]
    for col in range(4):
        idx=[4*col+r for r in range(4)]
        for i in range(4):
            for j in range(4):
                M[idx[i]][idx[j]]=MC4[i][j]
    return M


def shiftrows16():
    # State index = 4*column + row; ShiftRows moves (r,c) to (r,c-r mod 4).
    P=[[0]*16 for _ in range(16)]
    for c in range(4):
        for r in range(4):
            src=4*c+r
            dst=4*((c-r)%4)+r
            P[dst][src]=1
    return P


def fixed_dims_binary(A, powers):
    # Matrix entries in GF(2^8); rank over GF(2^8) times 8 is valid for kernels
    # of matrices defined over GF(2^8) viewed byte-linearly.
    out=[]
    for d in powers:
        B=mat_pow(A,d)
        for i in range(len(B)):
            B[i][i]^=1
        out.append(8*nullity_ff(B))
    return out


def run(out_csv: Path):
    MC16=mixcolumns16()
    SR=shiftrows16()
    AES=mat_mul(MC16,SR)
    rows=[]
    for name,A,divs,pows in [
        ('AES MixColumns',MC4,[1,2,4],[1,2,4]),
        ('AES ShiftRows-MixColumns',AES,[1,2,4,8],[1,2,4,8]),
    ]:
        order=next(d for d in divs if mat_pow(A,d)==eye(len(A)))
        po=projective_order(A,divs)
        dims=fixed_dims_binary(A,pows)
        rows.append((name,order,po,pows,dims))
    assert rows[0][1:3]==(4,4) and rows[0][4]==[8,16,32]
    assert rows[1][1:3]==(8,8) and rows[1][4]==[16,32,64,128]
    out_csv.parent.mkdir(parents=True,exist_ok=True)
    with out_csv.open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        w.writerow(['layer','ordinary_order','projective_order','fixed_space_dimensions_bits'])
        for name,o,po,pows,dims in rows:
            w.writerow([name,o,po,';'.join(f'F_{d}={v}' for d,v in zip(pows,dims))])
    return rows
