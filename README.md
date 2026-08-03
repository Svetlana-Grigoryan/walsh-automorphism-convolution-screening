# Walsh-Indexed Automorphism–Convolution Linear Layers

Reproducibility package for the manuscript:

> **Exact Recurrence and Cryptographic Screening of Walsh-Indexed Automorphism–Convolution Layers**

**Authors:** Sergo A. Episkoposian and Svetlana A. Grigoryan

## Overview

This repository contains the reference implementation, exact computational outputs, and reproducibility documentation supporting the finite computational claims reported in the manuscript.

All computations are exact. Finite-field and binary linear-algebra operations are performed without floating-point arithmetic.

## What this repository verifies

The package reproduces the following computational results:

1. the complete Cauchy–Walsh census for all 240 admissible shifts in the AES field;
2. the scalar-order distribution
   `5, 17, 51, 85, 255`
   with exact counts
   `16, 16, 32, 64, 112`;
3. the normalized projective order and kernel-growth profile
   `(4, 8, 12, 16)`;
4. the exhaustive census of all 32,768 odd-augmentation binary kernels on 16 coordinates;
5. the nine binary recurrence classes and their exact multiplicities;
6. the branch numbers of the canonical representatives;
7. the ordinary and projective orders and the fixed-space dimensions of AES MixColumns and the full AES byte-linear layer;
8. the Cauchy coefficient certificate used to establish maximal Jordan depth for all 240 admissible shifts.

## Quick start

Check the Python version:

```bash
python --version
```

Install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the complete verification suite:

```bash
python run_all.py
```

A successful run terminates with:

```text
ALL_CHECKS_PASSED
```

The program regenerates the finite computational certificates, writes the corresponding CSV files to `results/`, and refreshes the `SHA256SUMS` manifest.

## Repository layout

* `run_all.py` — runs the complete reproducibility suite.
* `requirements.txt` — Python dependencies.
* `src/finite_field.py` — exact AES-field arithmetic.
* `src/linear.py` — exact binary and finite-field linear algebra.
* `src/cauchy_census.py` — complete 240-shift Cauchy–Walsh census.
* `src/binary_census.py` — exhaustive 16-coordinate binary census.
* `src/aes_benchmark.py` — quantitative AES recurrence benchmark.
* `results/` — generated machine-readable CSV certificates.
* `supplementary/COMPUTATIONAL_PROTOCOL.md` — computational definitions, conventions, and verification protocol.
* `docs/ZENODO_RELEASE.md` — archival-release documentation.
* `CITATION.cff` — citation metadata.
* `SHA256SUMS` — SHA-256 manifest for the reproducibility package.

## Reproducibility conventions

The computations use the following fixed conventions:

* AES field polynomial:
  `0x11B`, corresponding to
  (z^8+z^4+z^3+z+1);
* byte values are represented using polynomial-basis integer encoding;
* coordinates are ordered by increasing integer labels;
* XOR convolution is defined by
  `(C_h)_{u,v} = h[u xor v]`;
* ranks and nullities are computed by exact Gaussian elimination;
* no floating-point arithmetic or statistical approximation is used.

These conventions are fixed so that all reported matrices, orders, nullities, branch numbers, and census tables can be reproduced exactly.

## Archival version

An immutable reproducibility package corresponding to version **1.0.0** has been archived on Zenodo:

**DOI:** https://doi.org/10.5281/zenodo.21770573

The Zenodo archive contains the code, exact computational outputs, checksums, and reproducibility documentation associated with the manuscript.

The GitHub repository contains the development version of the project and may receive future maintenance updates. For citation of the exact archived version associated with the manuscript, please use the Zenodo record.

## Citation

For an immutable citation of the reproducibility package, please cite the Zenodo archive:

**DOI:** https://doi.org/10.5281/zenodo.21770573

Citation metadata are also provided in `CITATION.cff` and can be accessed through GitHub's **Cite this repository** button.

## License

The code in this repository is released under the MIT License.

The manuscript and its published version remain subject to the applicable publisher's copyright and publication agreement.
