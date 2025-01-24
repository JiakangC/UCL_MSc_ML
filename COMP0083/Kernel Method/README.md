# COMP0083 Kernel Methods Coursework

This repository contains implementations and analyses for the Kernel Methods assignment in COMP0083. The coursework covers feature space representations, kernel dependence detection, and canonical correlation analysis using kernel-based techniques.

## Overview of Tasks

### Section 1: Feature Spaces (30%)
- Constructed feature spaces for error-free linear classification of datasets.
- Derived feature space representations using eigendecomposition of inner product matrices for finite input spaces.

### Section 2: Kernel Dependence Detection (40%)

#### Part 1: Incomplete Cholesky for Efficient COCO (20%)
- Derived a computationally efficient estimate for the COCO (Canonical Correlation Operator) using the incomplete Cholesky decomposition.
- Implemented the incomplete Cholesky-based COCO in Python with Gaussian kernels.
- Tested the implementation on sinusoidal datasets with Gaussian noise and visualized the projections \( f \) and \( g \), as well as the correlation of mapped variables.

#### Part 2: Kernel Canonical Correlation Analysis (Kernel CCA) (20%)
- Developed a kernelized solution for the canonical correlation problem using Gram matrices and formulated it as a generalized eigenvalue problem.
- Regularized the solution to address numerical instability with low-rank kernel matrices.
- Implemented and tested the solution with Gaussian kernels on given datasets.
- Compared the results of kernel CCA to the COCO implementation, analyzing the differences in the projection functions.

### Section 3: Dataset Design for Kernel CCA (Optional for COMP0083)
- Designed a dataset with nonlinear relationships for kernel CCA.
- Visualized the largest kernel canonical projections for self-generated and peer datasets.
- Analyzed and documented the results, providing insights into the impact of dataset characteristics on kernel CCA performance.
