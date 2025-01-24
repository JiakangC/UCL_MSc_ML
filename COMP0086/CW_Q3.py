#%%
import matplotlib.pyplot as plt
import numpy as np

#%% 
# Q3 (d)
def E_step(X,K,Pi,P):
    N, D = X.shape
    # create an empty matrix for responsibility
    Responsibility = np.empty((N,K))
    # sum over N
    for n in range(N):
        Numerator = np.empty(K)
        # sum over K
        for k in range(K):
            Numerator[k] = Pi[k]*np.prod((P[k,:]**X[n,:])*((1-P[k,:])**(1-X[n,:])))
        Denominator = np.sum(Numerator)
        # find responsibility
        Responsibility[n,:] = Numerator/Denominator
    return Responsibility

    
def M_step(X,K,Responsibility):
    N, D = X.shape
    # create hat_p_kd and hat_pi_k
    Hat_P = np.empty((K,D))
    Hat_Pi = np.empty(K)
    for k in range(K):
        # Follow the expressions in Q3(c)
        Hat_P[k,:] = np.sum(Responsibility[:,k]*X.T,1)/np.sum(Responsibility[:,k])
        Hat_Pi[k] = np.sum(Responsibility[:,k])/N 
    return Hat_P, Hat_Pi

def likelihood_K_Mixing_Bernoulli(X,K,Pi,P):
    N, D = X.shape
    likelihood = 0
    for n in range(N): # sum over N
        likelihood_N = []
        for k in range(K): # sum over K
            likelihood_NK = Pi[k]*np.prod((P[k,:]**X[n,:])*((1-P[k,:])**(1-X[n,:])))
            likelihood_N.append(likelihood_NK)
        likelihood += np.log(np.sum(likelihood_N))
    return likelihood

def EM_Start(X,K):
    N, D = X.shape
    max_iterations = 100 # set iterations as 100
    convergence = 0.0001 # less than convergence, the loop breaks
    # initials Pi and P
    Pi_initial = np.random.rand(K)
    Pi__initial_normal = Pi_initial/np.sum(Pi_initial)
    P_initial = np.random.rand(K,D)
    Pi = Pi__initial_normal
    P = P_initial
    log_likelihoods = []
    log_likelihoods.append(likelihood_K_Mixing_Bernoulli(X,K,Pi,P))
    # start our EM 
    for i in range(max_iterations):
        # E-step
        Responsibility = E_step(X,K,Pi,P)
        # M-step 
        P, Pi = M_step(X,K,Responsibility)
        log_likelihoods.append(likelihood_K_Mixing_Bernoulli(X,K,Pi,P))
        difference = np.abs(log_likelihoods[i]-log_likelihoods[i+1])
        if difference < convergence:
            break
    return Responsibility, P, Pi, log_likelihoods
#%% 
# Q3 (d)
seed = 10
np.random.seed(seed)
# load data
X = np.loadtxt('binarydigits.txt')
# K list:
K_list = [2,3,4,7,10]
# K_list = [2,3,4,5,6,7,8,9,10] 
# In Q3 (e), we check more different k values

# create the list for collection
Responsibility_list = []
P_list = []
Pi_list = []

plt.figure(figsize=(10,8))
# EM algorithm for different K
for K in K_list:
    Responsibility, P, Pi, log_likelihoods= EM_Start(X, K)
    # collect parameters
    Responsibility_list.append(Responsibility)
    P_list.append(P)
    Pi_list.append(Pi)

    # plot
    num_iterations = len(log_likelihoods)
    iterations = np.linspace(0, num_iterations, num_iterations)
    plt.plot(iterations, log_likelihoods, label = "K = " + str(K))

print(Responsibility_list, P_list, Pi_list)
plt.legend(loc='lower right')
plt.xlabel('Iterations', fontsize = 15)
plt.ylabel('Log-likelihood', fontsize = 15)
plt.grid()
plt.title("Log-likelihood VS Iterations",fontsize = 15)
plt.savefig('Q3(d).png')
#%%
# Q3(e)
rows = len(P_list)
cols = max(len(images) for images in P_list)
#K_list =[2,3,4,5,6,7,8,9,10]
K_list = [2,3,4,7,10]
fig, axes = plt.subplots(rows, cols, figsize=(2 * cols, 2 * rows)) 
plt.subplots_adjust(hspace=0.5)

for i, images in enumerate(P_list):
    for j, image in enumerate(images):
        ax = axes[i, j] if rows > 1 else axes[j]  # Handle case if there's only 1 row
        ax.imshow(np.reshape(image, (8, 8)), interpolation="none", cmap='gray')
        ax.axis('off')
    
    # Add caption at the lower boundary of each row
    fig.text(0.5, 1 - (i + 1) / rows + 0.05, f'K = {K_list[i]}', ha='center', va='center', fontsize=15)

    # Hide any extra subplots if rows or columns are uneven
    for j in range(len(images), cols):
        if rows > 1:
            axes[i, j].axis('off')
        else:
            axes[j].axis('off')

#plt.tight_layout()
#plt.savefig('Q3(e).png')
plt.show()
# %%
# Q3(e) check the responsibility list 
Responsibility_list
# %%
