# COMP0078 Coursework

This repository contains the coursework submissions for the COMP0078 module, focused on supervised learning techniques and their theoretical foundations. Below is an overview of the completed tasks:

## Coursework 1

### Part II: k-Nearest Neighbors (k-NN)
- Implemented the k-NN algorithm and analyzed its performance for varying numbers of neighbors \( k \).
- Studied the effect of training set size on the optimal \( k \) using rigorous experimentation.
- Evaluated the generalization error and provided insights into overfitting and model selection.

### Part III: Theoretical Questions
- Explored kernel properties, including positive semi-definiteness and their influence on regression solutions.
- Investigated kernel parameterization and its role in approximating 1-NN classifiers.
- Proved the No-Free-Lunch theorem and discussed its implications for machine learning algorithm design and function space learnability.

## Coursework 2

### Part I: Rademacher Complexity
- Derived bounds for the Rademacher complexity of finite hypothesis spaces.
- Provided mathematical proofs to connect hypothesis space cardinality with generalization error bounds.

### Part II: Bayes Decision Rule and Surrogate Approaches
- Investigated surrogate frameworks for classification problems, including squared loss, exponential loss, logistic loss, and hinge loss.
- Proved Fisher consistency for surrogate methods and derived comparison inequalities.
- Developed theoretical connections between surrogate risk minimization and misclassification error.

### Part III: Kernel Perceptron for Handwritten Digit Classification
- Implemented and extended a kernel perceptron to classify handwritten digits.
- Compared two generalization methods for multi-class classification: **One-versus-Rest** and **One-versus-One**.
- Conducted extensive experiments with polynomial and Gaussian kernels, including:
  - Cross-validation for hyperparameter selection.
  - Evaluation of training and test errors over multiple runs.
  - Analysis of confusion matrices to identify challenging cases and misclassifications.
- Visualized and interpreted the hardest-to-predict samples in the dataset.