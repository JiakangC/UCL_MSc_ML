# Q2
# %%
import numpy as np
from scipy.special import betaln
#Load Data
X = np.loadtxt('binarydigits.txt')
N, D = X.shape
# Model 1
log_P_M1 = - N*D*np.log(2) - np.log(3)
# Model 2
log_P_M2 = betaln(np.sum(X)+1,np.sum(1-X)+1) - np.log(3)
# Model 3
log_P_M3 = 0
for d in range(D):
    X_d = X[d,:]
    log_P_M3 += betaln(np.sum(X_d)+1,N-np.sum(X_d)+1)
log_P_M3 -= np.log(3)
print(log_P_M1,log_P_M2,log_P_M3)
# %%
