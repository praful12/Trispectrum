#By construction of grid, we only have kz>0, but we can extrapolate the rest because of conjugate symmetry
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rcParams
import os
os.environ['PATH'] = os.environ['PATH'] + ':/usr/texbin'
rcParams['ps.fonttype'] = 42
rcParams['ps.useafm']=True
rcParams['pdf.use14corefonts']=True
rcParams['text.usetex']=True

matplotlib.rcParams['legend.fontsize'] = 12.0

n = 16
n2 = int(n/2)

#Get data
fil_nam = 'grid'+str(n)+'.npy'
K_grid = np.load(fil_nam)


#Assign length values to grid points
kmin = 0.01
kmax = .2
k_val = np.array(np.linspace(kmin,kmax,n2))
k_val = np.concatenate((k_val,-k_val))

#Trispectrum Bin parameters
n_lenk = 5                                      #how many k bins do we want
kbin = (3**.5*kmax*1.2-3**.5*kmin)/n_lenk       #because kx,ky,kz!=0
mubin = 0.2
k_len = np.arange(3**.5*kmin,3**.5*kmax,kbin)
mu_len = np.arange(-1,1,mubin)

#Binning of k s and mu s such that we have a 2d array of vectors with the different observations

def bin_func(kx,ky,kz):
    len_k1 = (kx**2+ky**2+kz**2)**(.5)
    len_k1_bin = int((len_k1-kmin)/kbin)
    mu1_bin = int((kz/len_k1+1)/mubin)
    return len_k1_bin, mu1_bin

kmu_P_mat = np.zeros((len(k_len),len(mu_len)),dtype = object)       #matrix of observations of power of k,mu bin
for i in range(len(k_len)):
    for j in range(len(mu_len)):
        kmu_P_mat[i,j] = []


for i in range(n):
    for j in range(n):
        for k in range(n2):
            #kz>0
            kx1, ky1, kz1 = k_val[i], k_val[j], k_val[k]
            k_pos, mu_pos = bin_func(kx1, ky1, kz1)
            kmu_P_mat[k_pos,mu_pos].append(abs(K_grid[i,j,k])**2)
            
            #kz<0
            i1 = (i+n2)%n
            j1 = (j+n2)%n
            kx1, ky1, kz1 = k_val[i1], k_val[j1], -k_val[k]
            k_pos, mu_pos = bin_func(kx1, ky1, kz1)
            kmu_P_mat[k_pos,mu_pos].append(abs(K_grid[i1,j1,k])**2)

"""
#Check that every value is binned
sum = 0
for i in range(5):
    for j in range(10):
        print(k_len[i],mu_len[j],len(kmu_P_mat[i,j]))
        sum += len(kmu_P_mat[i,j])
print(sum,n**3)
"""
              
#Save this matrix
fil_name = 'kmubin'+str(n)+'.npy'
np.save(fil_name,kmu_P_mat)
fil_name = 'kmubin'+str(n)+'var.npz'
np.savez(fil_name,k = k_len, mu = mu_len)


