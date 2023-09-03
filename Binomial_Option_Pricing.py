import numpy as np

N_s=252 # number of steps in binomial according to required discretization
T=1
K=100
sigma=0.3
r=0.1
initialstock=90
delta_t=T/N_s

V=np.zeros((N_s+1,N_s+1),np.float)
S=np.zeros((N_s+1,N_s+1),np.float)

u=np.exp(sigma*np.sqrt(delta_t))
v=1/u
p=(np.exp(r*delta_t)-v)/(u-v)


Option=np.zeros((N_s+1))


S[0][0]=initialstock
for i in range(N_s+1):
    for j in range(i):
        S[j][i]=u*S[j][i-1]
        S[j+1][i]=v*S[j][i-1]
        

for i in range(N_s+1):
    V[i][N_s]=np.maximum(K-S[i][N_s],0)         #payoff at expiry of put
    
    
for i in range(N_s-1,-1,-1):
    for j in range(i+1):
        V[j][i]=(1/(np.exp(r*delta_t)))*(p*V[j][i+1]+(1-p)*V[j+1][i+1])

    OV=(V[0][0])
print ("Option value = ",OV)
