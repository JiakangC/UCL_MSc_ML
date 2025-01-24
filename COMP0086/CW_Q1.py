# Q1
# %%
import matplotlib.pyplot as plt
import numpy as np
# %%
def MLE(x):
    return np.mean(x, axis=0)
def MAP(x, alpha, beta):
    N,_ = x.shape
    return  (alpha - 1 + np.sum(x, axis=0)) / (N + alpha + beta - 2)
# %%
# load data
x = np.loadtxt('binarydigits.txt')
MLE_data = np.reshape(MLE(x), (8, 8))
MAP_data = np.reshape(MAP(x,3,3), (8, 8))
# %%
# plot and save pic
plt.figure()
plt.imshow(MLE_data, interpolation="None")
plt.axis('off')
#plt.savefig('MLE_Plot')
# %%
plt.figure()
plt.imshow(MAP_data, interpolation="None")
plt.axis('off')
#plt.savefig('MLE_Plot')
