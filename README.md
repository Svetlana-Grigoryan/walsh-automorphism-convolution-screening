# Walsh-Indexed Automorphism-Convolution Linear Layers

Reproducibility package for the manuscript

> **Exact Recurrence and Cryptographic Screening of Walsh-Indexed Automorphism–Convolution Layers**

Authors: Sergo A. Episkoposian and Svetlana A. Grigoryan.

## What this repository verifies

The package regenerates the finite computational claims used in the article:

1. the complete Cauchy-Walsh census for the 240 admissible shifts in the AES field;
2. the scalar-order distribution `5, 17, 51, 85, 255` with counts `16, 16, 32, 64, 112`;
3. the normalized projective order and kernel-growth profile `(4, 8, 12, 16)`;
4. the complete census of all 32,768 odd-augmentation binary kernels on 16 coordinates;
5. the nine binary recurrence classes and their exact multiplicities;
6. branch numbers of the canonical representatives;
7. ordinary/projective orders and fixed-space dimensions of AES MixColumns and the full AES byte-linear layer.

## Quick start

```bash
python --version
python run_all.py
```

Expected final line:

```text
ALL_CHECKS_PASSED
```

The program writes reproducible CSV files into `results/` and refreshes `SHA256SUMS`.

## Repository layout

- `src/finite_field.py`: AES-field arithmetic.
- `src/linear.py`: exact binary/finite-field linear algebra.
- `src/cauchy_census.py`: 240-shift Cauchy-Walsh census.
- `src/binary_census.py`: exhaustive 16-coordinate binary census.
- `src/aes_benchmark.py`: quantitative AES recurrence benchmark.
- `results/`: generated CSV certificates.
- `supplementary/COMPUTATIONAL_PROTOCOL.md`: definitions and conventions.
- `docs/ZENODO_RELEASE.md`: release and DOI workflow.

## Reproducibility conventions

- AES field polynomial: `0x11B`, corresponding to
  `z^8 + z^4 + z^3 + z + 1`.
- Byte values use polynomial-basis integer encoding.
- Coordinates are ordered by increasing integer labels.
- XOR convolution uses `(C_h)_{u,v}=h[u xor v]`.
- Exact ranks and nullities are computed by Gaussian elimination, never floating point.

## Citation

Use `CITATION.cff` through GitHub's **Cite this repository** button. After creating a Zenodo release, replace the placeholder repository URL and add the Zenodo DOI.

## License

Code is released under the MIT License. The manuscript remains subject to the publisher's publication agreement.
