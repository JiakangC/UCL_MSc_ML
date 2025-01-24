
# COMP0083 Optimization Coursework

This repository contains solutions and implementations for the optimization-focused section of COMP0083: Advanced Topics in Machine Learning. The coursework combines theoretical and practical aspects of convex analysis and optimization algorithms.

## Overview of Tasks

### Section 1: Multiple Choice and Conceptual Questions (30%)
- **Convex Functions:** Identified convexity in given mathematical functions.
- **Subdifferentials:** Analyzed graphical representations of subdifferentials for piecewise-defined functions.
- **Gradient Calculations:** Derived gradients for functions involving matrix operations.
- **Fenchel Conjugates:** Computed Fenchel conjugates of transformed convex functions.

### Section 2: Theory of Convex Analysis and Optimization (40%)
- **Fenchel Conjugates:**
  - Derived conjugates for various convex functions, including logarithmic and indicator functions.
- **Jensen’s Inequality:**
  - Proved the inequality using induction and applied it to establish arithmetic-geometric inequalities.
- **Convex Hulls:**
  - Demonstrated that the maximum of a convex function over a polytope occurs at one of its vertices.
- **Joint Convexity:**
  - Proved joint convexity of functions involving norms.
- **Dual Optimization Problem:**
  - Derived the dual problem for an infinity-norm-constrained quadratic optimization problem.
  - Verified strong duality conditions and derived KKT conditions.
  - Analyzed FISTA’s convergence rate for solving the dual problem.

### Section 3: Solving the Lasso Problem (30%)
- **Stochastic Gradient Descent Algorithms:**
  - Implemented the Proximal Stochastic Gradient Algorithm (PSGA) for solving the Lasso problem.
  - Developed the Randomized Coordinate Proximal Gradient Algorithm (RCPGA) for efficiency.
- **Data Generation:**
  - Used Python to generate synthetic data based on a provided script.
- **Comparison of Algorithms:**
  - Evaluated convergence and objective function performance for PSGA and RCPGA.
  - Analyzed the behavior of objective values using ergodic means for PSGA.
  - Visualized objective values as a function of iterations to compare algorithm efficiency.

