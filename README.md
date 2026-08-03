# Walsh-Indexed Automorphism–Convolution Linear Layers

Reproducibility package for the manuscript

> **Exact Recurrence and Cryptographic Screening of Walsh-Indexed Automorphism–Convolution Layers**

**Authors:** Sergo A. Episkoposian and Svetlana A. Grigoryan

## Reproducibility

This repository contains the code and computational results used in the manuscript.

The package reproduces:

* the 240-shift Cauchy–Walsh census over the AES field;
* the 16-coordinate binary census;
* the nine binary recurrence classes;
* branch numbers of the canonical representatives;
* AES MixColumns and full AES byte-linear recurrence benchmarks.

## Run

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

Run the complete verification:

```bash
python run_all.py
```

A successful run ends with:

```text
ALL_CHECKS_PASSED
```

Generated results are stored in `results/`.

## Archive

The reproducibility package corresponding to version **1.0.0** is archived on Zenodo:

**DOI:** https://doi.org/10.5281/zenodo.21770573

GitHub repository:

https://github.com/Svetlana-Grigoryan/walsh-automorphism-convolution-screening

## License

The code is released under the MIT License.