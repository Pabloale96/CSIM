import numpy as np
import sympy as sym
from  scipy.optimize import minimize_scalar
import sys
import matplotlib.pyplot as plt
import pylab
import math as mt

#  Clases usadas:
from metodo_grad import MetodoGradiente
from csmi import CSMI

# Funciones y gradiente para minimizar:
def f(x):
    return -np.exp(-x[0]**2-x[1]**2)*np.cos(2*np.pi*x[0] )*np.cos(2*np.pi*x[1])

def df(x):
    return np.array([2*x[0]*np.exp(-x[0]**2-x[1]**2)*np.cos(2*np.pi*x[0])*np.cos(2*np.pi*x[1])+2*np.pi*np.exp(-x[0]**2-x[1]**2)*np.sin(2*np.pi*x[0] )*np.cos(2*np.pi*x[1]), 2*x[1]*np.exp(-x[0]**2-x[1]**2)*np.cos(2*np.pi*x[0])*np.cos(2*np.pi*x[1])+2*np.pi*np.exp(-x[0]**2-x[1]**2)*np.sin(2*np.pi*x[1] )*np.cos(2*np.pi*x[0])])
