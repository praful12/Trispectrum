#change
import numpy as np

#Cube Parameters
n = 16                  #Grid size
n2 = int(n/2)

P = 2.                  #Power
K_grid = np.zeros((n,n,n2), dtype = np.complex)

realK = np.random.normal(0,P,(n,n,n2))        #Mean, standard deviation, size
imK = np.random.normal(0,P,(n,n,n2))        #Mean, standard deviation, size

K_grid = realK + (-1)**.5*imK

#Grid save
nam = 'grid'+str(n)+'.npy'
np.save(nam,K_grid)

print(K_grid[:,:,1])
"""
#Check Variance
var = [0,0,0]

for i in range(n2):
    var[0] += 2/n*kx[i]**2
    var[1] += 2/n*ky[i]**2
    var[2] += 2/n*kz[i]**2

varK = np.zeros(6,dtype = np.complex)
for i in range(6):
    for j in range(n2):
        varK[i]+=K[j,i]**2/n2

print(var)
print(varK)

"""
