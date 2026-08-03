# Computational protocol

## 1. Finite field

All byte-level calculations use

`GF(2^8) = GF(2)[z]/(z^8+z^4+z^3+z+1)`.

Elements are encoded as integers `0..255` in the standard polynomial basis.

## 2. XOR convolution

For a kernel `h` indexed by `G=F_2^r`,

`C_h[u,v] = h[u xor v]`.

## 3. Automorphism permutation

The involution used in the 16-coordinate censuses swaps the two low index bits.
The operator is `L=P_A C_h`.

## 4. Normalization

For nonzero augmentation `c=sum h`, define `U=c^{-1}L`.
Projective order is the ordinary order of `U` when `U` is unipotent under the
chosen normalization.

## 5. Nullity profile

For involutions, the reported profile is

`(null(U-I), null((U-I)^2), null((U-I)^3), null((U-I)^4))`.

## 6. Binary branch number

For a binary matrix `L`,

`B(L)=min_{x != 0} (wt(x)+wt(Lx))`.

## 7. Independent verification

Every generated CSV is deterministic. `SHA256SUMS` records hashes of all
machine-readable outputs and source files used for the release.
