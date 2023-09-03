import numpy as np
import math

#given data
N = 3
V = np.zeros((N,N))
w=np.zeros(N)
E=np.zeros(N)
# Expected returns values
E[0] = 0.026
E[1] = 0.08
E[2] = 0.074
#Covariance matrix values
V[0,0] = 0.017
V[0,1] = 0.003
V[0,2] = -0.001
V[1,0] = 0.003
V[1,1] = 0.005
V[1,2] = 0.004
V[2,0] = -0.001
V[2,1] = 0.004
V[2,2] = 0.063

#part B
Vinv = np.linalg.inv(V)
u = np.ones(N)
uT = np.matrix.transpose(u)
T2 = np.matmul(Vinv, uT)
T2 = np.matmul(u,T2)
T1 = np.matmul(u, Vinv)
w = T1 / T2 
print("Part a:""\n""w1 = ",w[0],"w2 = ",w[1],"w3 = ",w[2])


wT = np.matrix.transpose(w)
Ex = np.matmul(E, wT)
Var = np.matmul(V, wT)
Var = np.matmul(w, Var)
print("Expected return = ",Ex)
print("Variance = ",Var)

#part B
ET = np.matrix.transpose(E)
t1 = np.matmul(Vinv, uT)
t1 = np.matmul(u, t1)
t2 = np.matmul(Vinv, ET)
t2 = np.matmul(u, t2)
t3 = np.matmul(Vinv, uT)
t3 = np.matmul(E, t3)
t4 = np.matmul(Vinv, ET)
t4 = np.matmul(E, t4)
T2 = t1 * t4 - (t3 * t2)

t1 = 1
t3 = 0.09                       #Condition  for return of potfolio given in Qs

leftCoef = t1 * t4 - (t3 * t2)
t1 = np.matmul(Vinv, uT)
t1 = np.matmul(u, t1)
t3 = np.matmul(Vinv, uT)
t3 = np.matmul(E, t3)

t2 = 1
t4 = 0.09                       #Condition for return on portfolio given in Qs

rightCoef = t1 * t4 - (t3 * t2)

rightCoef = rightCoef / T2
leftCoef = leftCoef / T2

lmatrix = np.matmul(u, Vinv)
rmatrix = np.matmul(E, Vinv)

w2 = leftCoef * lmatrix + rightCoef * rmatrix
print("Part b:""\n""w1 = ",w2[0],"w2 = ",w2[1],"w3 = ",w2[2])

w2T = np.matrix.transpose(w2)
Var1 = np.matmul(V, w2T)
Var1 = np.matmul(w2, Var1)
print("Variance = ",Var1)
