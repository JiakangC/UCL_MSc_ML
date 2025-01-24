# COMP0085 Approximate Inference Coursework

This repository contains solutions and implementations for the COMP0085 Approximate Inference coursework. Below is an overview of the questions addressed:

## Overview of Tasks

### Question 1: Graphical Models and Factor Analysis
- **Directed Acyclic Graphs (DAGs):** Constructed and analyzed dependency graphs for biochemical cascades.
- **Moralization and Triangulation:** Converted DAGs into moralized and triangulated graphs, deriving junction trees for inference.
- **Factor Graphs:** Represented junction trees as factor graphs and identified conditional independencies.
- **Factor Analysis:** Performed factor analysis on observed variables, recovering latent factors based on a given model.

### Question 2: Gaussian Processes and Kernel Methods
- **Posterior Inference:** Derived the posterior distribution of parameters in Gaussian models.
- **Residual Analysis:** Analyzed residuals for time dependence and validated model assumptions.
- **Kernel Selection:** Implemented and tested Gaussian processes using squared-exponential and custom kernels with parameter tuning.
- **Extrapolation:** Used Gaussian processes to extrapolate CO2 concentration trends, analyzing sensitivity to kernel hyperparameters.

### Question 3: Variational Inference and Free Energy Optimization
- **Mean-Field Variational Inference:** Implemented mean-field updates for variational parameters to maximize free energy.
- **Connection to Linear Regression:** Demonstrated the relationship between free energy maximization and linear regression updates.
- **Complexity Analysis:** Analyzed the computational complexity of the M-step in variational inference.
- **Binary Factor Analysis:** Developed and tested a binary factor analysis model for synthetic data, optimizing parameters to learn latent features.

### Question 4: Variational Bayesian Inference (Bonus)
- **Automatic Relevance Determination (ARD):** Enhanced the binary factor analysis model with ARD to infer the number of active factors automatically.
- **Parameter Updates:** Derived and implemented updates for additional parameters, including precision terms for ARD priors.

### Question 6: Loopy Belief Propagation (Bonus)
- **Loopy BP Implementation:** Applied loopy belief propagation as an alternative E-step in binary factor analysis.
- **Comparison with Mean-Field:** Evaluated and compared convergence and feature learning between loopy BP and mean-field methods over multiple runs.
