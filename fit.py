"""
Program ma za zadanie dopasować podwójnego gaussa do widm TOF
Zobaczymy, jak to wyjdzie w praniu ...


"""

import numpy as np 
import matplotlib.pyplot as plt 
import os
import glob 
from scipy.optimize import curve_fit

#będziemy to fitować
def gaussa(x,y0, A0, A1, s0, s1 , x0, x1):
      y = y0+A0*np.exp(-(x-x0)^2/2/s0^2)+A1*np.exp(-(x-x1)^2/2/s1^2)
      return y

files = glob.glob("Na_U*\\UNFILTERED\\*TOFspec*" + "*.txt", recursive=True) #znajdź mi wszystkie pliki TOF

for file in files:
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

    #parameters = [1,1,1,0.8,0.4,500,1000]
    #param, cobver = curve_fit(gaussa,fitx,fity,p0=parameters)   
    #print(param)
    
    plt.plot(fitx,fity, label = "orginal curve")
    plt.legend()
    plt.show()
    

