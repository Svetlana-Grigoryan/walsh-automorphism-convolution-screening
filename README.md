# Automorphism–Convolution Operators over Elementary Abelian 2-Groups

Reproducibility repository for the manuscript

> **Recurrence and Primary Structure of Automorphism–Convolution Operators over Elementary Abelian 2-Groups**

**Authors:** Sergo A. Episkoposian and Svetlana A. Grigoryan

## Reproducibility

This repository contains the code and exact finite computational results supporting the finite-field examples in the manuscript.

The package reproduces:

* the complete 240-shift Cauchy–Walsh census over the AES field;
* the complete 16-coordinate binary census;
* the nine binary recurrence signatures;
* the nullity-growth profiles and projective orders reported in the manuscript;
* the branch numbers of the selected displayed binary representatives.

The repository also retains auxiliary AES linear-operator benchmark code for independent comparison and regression testing. These AES benchmark results are not required for the main mathematical results of the current manuscript.

## Run

Install the required packages with:

    python -m pip install -r requirements.txt

Run the complete verification with:

    python run_all.py

A successful run ends with:

    ALL_CHECKS_PASSED

Generated machine-readable results are stored in `results/`.

## Computational scope

The computational censuses complement the analytic results of the manuscript. They use exact finite-field arithmetic and exact Gaussian elimination; no statistical inference is involved.

The displayed hexadecimal binary kernels are selected representatives of their recurrence signatures.

## Archive

The synchronized reproducibility package is version **v1.0.1**.

**Zenodo DOI for v1.0.1:** 10.5281/zenodo.22180270

The previous version **v1.0.0** is available at DOI
`10.5281/zenodo.21770573`.

## License

The code is released under the MIT License.
