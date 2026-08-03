"""Exact GF(2^8) arithmetic for the AES polynomial 0x11B."""
MOD = 0x11B


def add(a: int, b: int) -> int:
    return a ^ b


def mul(a: int, b: int) -> int:
    a &= 0xFF
    b &= 0xFF
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & 0x100:
            a ^= MOD
    return out & 0xFF


def pow_(a: int, n: int) -> int:
    out = 1
    while n:
        if n & 1:
            out = mul(out, a)
        a = mul(a, a)
        n >>= 1
    return out


def inv(a: int) -> int:
    if a == 0:
        raise ZeroDivisionError("zero has no inverse")
    return pow_(a, 254)


def order(a: int) -> int:
    if a == 0:
        return 0
    for d in (1, 3, 5, 15, 17, 51, 85, 255):
        if 255 % d == 0 and pow_(a, d) == 1:
            return d
    raise AssertionError("order not found")
