"""
Program ma za zadanie dopasować podwójnego gaussa do widm TOF
Zobaczymy, jak to wyjdzie w praniu ...


"""

import numpy as np 
import matplotlib.pyplot as plt 
import os
import glob 
from scipy.optimize import curve_fit

#test zwykły gauss
def gauss_function(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))


#będziemy to fitować
def gaussa(x,y0, A0, A1, s0, s1 , x0, x1):
  
    return y0+A0*np.exp(-(x-x0)**2/2/s0**2)+A1*np.exp(-(x-x1)**2/2/s1**2)

def save_to_file(file):
    fdir,filename = os.path.split(file)
    f.write("\n{} \n".format(filename))
    f.write("\ny0 = {} \nA0 = {} \nA1 = {} \ns0 = {} \ns1 = {} \nx0 = {} \nx1 = {} \n".format(y0, A0, A1, s0, s1 , x0, x1))


def search_and_append(file):
    xdata = []
    ydata = [] 
    fitx=[]
    fity=[]
    opened=open(file)  
    for line in opened:
        a = int(line.rstrip())
        ydata.append(a) 
    if "U29" in file or "U30" in file :   
         for i in range(len(ydata)):
             xdata.append(-50+0.02*i)
    else:
        for i in range(len(ydata)):
            xdata.append(-50+0.05*i)

    for i,j in zip(xdata,ydata): 
       if i > -1.5 and i<1.5:
           fitx.append(i)
           fity.append(j)

    return fitx,fity

def fit():
    fitx,fity = search_and_append(file)
    init_params=[1,300,800,0.02,0.05,-0.3,-0.1]
    popt, pcov = curve_fit(gaussa,fitx,fity,p0=init_params)
    y0, A0, A1, s0, s1 , x0, x1 = popt

    plt.plot(fitx,fity, label = "orginal curve")
    plt.plot(fitx, gaussa(fitx, *popt) ,label = "fitted" )
    plt.legend()
    plt.show()
    return y0, A0, A1, s0, s1 , x0, x1


      

files = glob.glob("Na_U*\\UNFILTERED\\*TOFspec*" + "*.txt", recursive=True) 

f=open("results.txt",'w')
for file in files:
    y0, A0, A1, s0, s1 , x0, x1 = fit()
    save_to_file(file)
f.close()

