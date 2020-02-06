"""
Program ma za zadanie dopasować podwójnego gaussa do widm TOF
Zobaczymy, jak to wyjdzie w praniu ...

@author : Maciej Krakowiak @secauthor: entire internet and stackoverflow

"""

import numpy as np 
import matplotlib.pyplot as plt 
import os
import glob 
from scipy.optimize import curve_fit

