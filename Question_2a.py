import numpy as np
import math

for j in range (2,5):
    M =365*4        # no. of time steps
    N=10**j         # no. of MC
    St=90
    r=0.1
    sig=0.3
    T = 1
    dt = T/M
    E=100
    S= np.zeros((N,M),np.float)
    V= np.zeros((N),np.float)
    for s in range (N):
        S[s][0]=90
        for t in range (1,M):
            dS=r*dt*S[s][t-1]+S[s][t-1]*sig*(math.sqrt(dt)*np.random.randn())
            S[s][t]=S[s][t-1]+dS
        V[s]=np.maximum(E-S[s][M-1],0)      #Payoff at expiry of put
    vmean=np.mean(V)
    OV=vmean*math.exp(-r*T)
    print("N =",N,"Option Value = ",OV)
