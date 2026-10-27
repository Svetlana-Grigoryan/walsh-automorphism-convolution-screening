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

The operator is

`L = P_A C_h`.

## 4. Normalization

For nonzero augmentation

`c = sum h`,

define

`U = c^{-1} L`.

For the Cauchy-Walsh census, the normalized kernel is

`g = c^{-1} h`.

## 5. First augmentation-layer certificate

For the order-two automorphism, define

`omega_2 = (g o A^{-1}) * g`

and

`eta_2 = omega_2 - delta_0`.

Since the characteristic is two, subtraction equals addition.

The code computes the image of `eta_2` in the first augmentation layer

`J/J^2`.

With coordinates indexed by `F_2^4`, the coordinate corresponding to bit `i`
is

`sum_{v: v_i = 1} eta_2[v]`.

The implementation explicitly verifies that this class is nonzero for every
one of the 240 admissible Cauchy-Walsh shifts.

## 6. Nullity profile

For involutions, the reported profile is

`(null(U-I), null((U-I)^2), null((U-I)^3), null((U-I)^4))`.

For the 240-shift Cauchy-Walsh census, every normalized operator has profile

`(4, 8, 12, 16)`

and projective order `4`.

## 7. Binary recurrence signatures

The complete 16-coordinate binary census groups kernels by recurrence data,
including projective order and nullity-growth profile.

The hexadecimal kernels displayed in the manuscript and result tables are
selected representatives of these recurrence signatures. They are not claimed
to be canonical representatives under an additional equivalence relation.

## 8. Binary branch number

For a binary matrix `L`,

`B(L) = min_{x != 0} (wt(x) + wt(Lx))`.

## 9. Independent verification

Every generated CSV is deterministic.

`SHA256SUMS` records hashes of the machine-readable outputs and source files
used for the release.

Running

`python run_all.py`

regenerates the computational outputs and checks all expected results.

A successful verification ends with

`ALL_CHECKS_PASSED`.
