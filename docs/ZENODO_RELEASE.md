# Zenodo release workflow

1. Finalize and push the GitHub repository.
2. In GitHub, create a release tagged `v1.0.0`.
3. Sign in to Zenodo and connect the GitHub account.
4. Enable this repository in Zenodo's GitHub settings.
5. Publish the GitHub release; Zenodo will archive it and mint a version DOI.
6. Copy the DOI into:
   - `README.md`;
   - `CITATION.cff` (`doi:` field);
   - the manuscript Data availability and Code availability statements.
7. Commit the DOI update and, if desired, create a metadata-only patch release.

Use the concept DOI for the repository as a whole and the version DOI when
citing the exact computational package used for the submitted manuscript.
