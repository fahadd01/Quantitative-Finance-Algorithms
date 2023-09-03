import numpy as np

for j in range (2,6):
    N=10**j
    sum=0
    x=np.zeros(N)
    f=np.zeros(N)
    for i in range (N):
        x[i]=np.random.uniform(0,1)
        f[i]=np.exp((-x[i]**2))
        sum=sum+f[i]
    num_sol=sum/N
    print ("N = ",N)
    print("MonteCarlo Solution = ",num_sol)