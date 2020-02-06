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
      return y0+A0*np.exp(-(x-x0)^2/2/s0^2)+A1*np.exp(-(x-x1)^2/2/s1^2)
      

files = glob.glob("Na_U*\\UNFILTERED\\*TOFspec*" + "*.txt", recursive=True) #znajdź mi wszystkie pliki TOF

for file in files:
    xdata = []
    ydata = []
    fitx=[]
    fity=[]
    opened=open(file)  #otwórz mi plik z katalogu pobranego przez glob 
    for line in opened:
        a = int(line.rstrip())
        ydata.append(a) #wczytaj wszystko 
    if "U29" in file or "U30" in file :   #od 29 i 30 zmieniało się wyrównanie x
         for i in range(len(ydata)):
             xdata.append(-50+0.02*i)
    else:
        for i in range(len(ydata)):
            xdata.append(-50+0.05*i)

    for i,j in zip(xdata,ydata):  # przygotuj obie listy tak aby był pik do dofitowania 
       if i > -1.5 and i<1.5:
           fitx.append(i)
           fity.append(j)

    #testowe dopasowanie zwykłego gaussa
    popt,pcov = curve_fit(gauss_function, fitx, fity, p0 = [1, 1, 1])
    #popt, pcov = curve_fit(gaussa,fitx,fity,p0=[0,300,800,0.3,0.7,-0.2,0])  
    #print(popt)
    
    plt.plot(fitx,fity, label = "orginal curve")
    plt.plot(fitx, gauss_function(fitx, *popt), label='fit: a=%5.3f mean=%5.3f, sigma=%5.3f' % tuple(popt))
    plt.legend()
    plt.show()
    

