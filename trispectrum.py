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

#Get data and bin parameters
fil_nam = 'kmubin'+str(n)+'.npy'
kmu_bin = np.load(fil_nam)
fil_nam = 'kmubin'+str(n)+'var.npz'
kmu_bin_var = np.load(fil_nam)
k = kmu_bin_var['k']
mu = kmu_bin_var['mu']
kbin = k[1]-k[0]
mubin = mu[1]-mu[0]



#Trispectrum function for a given pair
def trispectrum(k1,mu1,k2,mu2):
    i_k1 = int((k1 - k[0])/kbin)
    i_k2 = int((k2 - k[0])/kbin)
    i_mu1 = int((mu1 - mu[0])/mubin)
    i_mu2 = int((mu2 - mu[0])/mubin)

    Pk1 = kmu_bin[i_k1,i_mu1]
    Pk2 = kmu_bin[i_k2,i_mu2]
    #print(Pk1,Pk2)

    flag = len(Pk1)*len(Pk2)
    tri = 0.

    for i in range(len(Pk1)):
        for j in range(len(Pk2)):
                tri += Pk1[i]*Pk2[j]
    if flag != 0:
        return tri/(flag)
    else:
        return 0.

#returns something!
print(trispectrum(.1,.15,.25,-.4))
print(trispectrum(.1,-.15,.25,-.4))
print(trispectrum(.1,.15,.25,.4))
print(trispectrum(.1,-.15,.25,.4))