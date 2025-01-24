# Q4
#%%
from ssm_kalman import * 
import numpy as np
from matplotlib import pyplot as plt 
#%%
def logdet(A):
    return 2 * np.sum(np.log(np.diag(np.linalg.cholesky(A))))
# %%
# load data
train =  np.loadtxt('ssm_spins.txt')
# %%
# def parameter
theta1 = 2 * np.pi / 180
theta2 = 2 * np.pi / 90
A = 0.99 * np.array([
    [np.cos(theta1), -np.sin(theta1), 0, 0],
    [np.sin(theta1), np.cos(theta1), 0, 0],
    [0, 0, np.cos(theta2), -np.sin(theta2)],
    [0, 0, np.sin(theta2), np.cos(theta2)]
])
C = np.array([
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 1],
    [0.5, 0.5, 0.5, 0.5]
])
R = np.eye(5)
Q = np.eye(4) - A @ A.T
# %%
x = train.T
Y0 = np.random.multivariate_normal(np.zeros(4), np.eye(4))
Q0 = np.eye(4)
Y, V, _, L = run_ssm_kalman(x,Y0,Q0,A,Q,C,R, "filt")
Ys, Vs, Vj, Ls = run_ssm_kalman(x,Y0,Q0,A,Q,C,R, mode='smooth')

# %%
V_plot = []
Vs_plot = []
for i in V:
    V_plot.append(logdet(i))
for i in Vs:
    Vs_plot.append(logdet(i))
# %%
plt.figure(figsize=(13,5))
plt.plot(Y.T)
plt.savefig('q4_filt.png')
# %%
plt.figure(figsize=(13,5))
plt.plot(Ys.T)
plt.savefig('q4_smooth.png')
# %%
plt.plot(V_plot, linewidth=0.8)
plt.savefig('q4_cov_filter.png')
# %%
plt.plot(Vs_plot, linewidth=0.8)
plt.savefig('q4_cov_smooth.png')
plt.show()
# %%
