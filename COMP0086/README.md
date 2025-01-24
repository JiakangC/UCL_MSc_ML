# COMP0086 Probabilistic and Unsupervised Learning Coursework

This repository contains solutions and implementations for the COMP0086 coursework. Below is an overview of the addressed tasks:

## Overview of Tasks

### Question 1: Binary Vector Models
- **Multivariate Gaussian Inappropriateness:** Explained why Gaussian models are unsuitable for binary data.
- **Maximum Likelihood (ML) Estimation:** Derived ML estimates for a multivariate Bernoulli model.
- **Maximum A Posteriori (MAP) Estimation:** Incorporated Beta priors into the estimation process.
- **Parameter Learning and Visualization:** Implemented code to estimate ML and MAP parameters for binary digit data and visualized them as 8×8 images.

### Question 2: Model Selection
- **Relative Model Probabilities:** Derived expressions to compute posterior probabilities for three different binary data models:
  1. Uniform probabilities for all components.
  2. Identical unknown probabilities for all components.
  3. Separate unknown probabilities for each component.
- **Posterior Calculations:** Computed posterior probabilities given uniform priors.

### Question 3: Expectation-Maximization (EM) for Binary Data
- **Likelihood and Responsibilities:** Formulated the likelihood for a mixture of multivariate Bernoullis and computed the responsibilities in the E-step.
- **Parameter Updates:** Derived the M-step equations for mixture weights and Bernoulli parameters.
- **EM Implementation:** 
  - Developed a general EM algorithm for mixtures of multivariate Bernoullis.
  - Analyzed results for varying numbers of mixture components \( K \) (e.g., \( K = 2, 3, 4, 7, 10 \)).
  - Visualized log-likelihood convergence and learned parameters for multiple runs.
- **Analysis:** Evaluated sensitivity to initialization and provided suggestions for model improvement.

### Question 5: Decrypting Messages with MCMC
- **Transition Probabilities:** Estimated transition statistics for letters and punctuation in English text.
- **MCMC Sampling:** 
  - Implemented a Metropolis-Hastings sampler for decrypting a substitution cipher.
  - Reported intermediate decryption progress and analyzed convergence properties.
- **Ergodicity Analysis:** Explored conditions under which the Markov chain remains ergodic and proposed fixes if violated.
- **Approach Evaluation:** Discussed the impact of symbol probabilities and extensions to higher-order Markov chains or complex languages.

### Question 7: Optimization
- **Constrained Optimization:** Found local extrema of a function subject to a nonlinear constraint using the Lagrange multiplier method.
- **Logarithmic Function via Newton’s Method:** 
  - Derived a Newton's update equation for computing \( \ln(a) \).
  - Implemented and tested convergence properties.

### Question 8: Eigenvalue Optimization (Bonus)
- **Largest Eigenvalue as Optimization:** 
  - Proved that the largest eigenvalue of a symmetric matrix can be derived from an optimization problem on the unit sphere.
  - Demonstrated that only eigenvectors corresponding to the largest eigenvalue maximize the quadratic form.
- **Optimization and Subspaces:** Showed that vectors outside the span of eigenvectors associated with the largest eigenvalue cannot achieve the maximum.
