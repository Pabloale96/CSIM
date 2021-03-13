import numpy as np
import sympy as sym
from  scipy.optimize import minimize_scalar
import sys
import matplotlib.pyplot as plot
import pylab
import math as mt


class MetodoGradiente:

    """ 
    Genere una clase que calcula el metodo del gradiente. Es necesario parasarle
    una funcion, el gradiente de dicha funcion y el punto inicial p0 en forma de lista.
    """

    def __init__(self,p0=None,funcion=None,gradiente=None) -> None:
        """
        p0: lista con los diferentes puntos a aplicar el metodo del Gradiente. Los puntos p0 tiene
        que ser una lista del estilo:

        p0 = [p1 p2 p3 p4 ... pN]
                
        funcion: es la funcion a minimizar, se pasa en forma de una funcion usando el modulo numpy array. Por ejemplo,
        un paraboloide seria 
        
        def funcion(x):
            return x[0]**2+x[1]**2
        
        gradiente: es el gradiente de la funcion, se pasa igual que la funcion. Por ejemplo,

        def gradiente(x):
            return np.array([2*x[0],2*x[1]])
        """
        if type(p0) != type([]):
            print("Pasar los puntos como tipo de lista. Si es tipo numpy.array, hacer \"[ punto ]\" ")
        self.p0=p0
        self.p=p0[0] # este punto lo cambiamos para ir calculando el metodo del gradiente
        self.cant_puntos = len(p0)
        self.funcion = funcion
        self.gradiente = gradiente

    def metodo_gradiente_multiples_puntos(self):
        """
        Calcula el metodo de gradientes para la ubicacion de los puntos p0.

        Devuelve: 
            list_aux: una lista de listas que muestra los resultados en cada iteracción con cada punto.
            min1: la posicion p donde la funcion tiene el minimo.
        """

        if type(self.p0) != type([]):
                print("hay que pasar el o los puntos dentro de una lista.")
                sys.exit()

        list_aux = []
        if self.cant_puntos == 1:
            list_aux.append(self.metodo_gradiente())
            return list_aux,list_aux[0][-1]
        else:
            for i in range(0,self.cant_puntos):
                self.p = self.p0[i]
                list_aux.append(self.metodo_gradiente())
            min1 = self.evaluar_punto_minimo(list_aux)
        return list_aux,min1

    def metodo_gradiente(self):
        """ 
        Calcula el método del gradiente para un unico punto p.

        Devuelde, el valor p donde se encuentra el minimo de la funcion.
        """
        l=0
        df0 = self.evaluar_gradiente()
        direccion = df0 #la direccion para aplicar el metodo de busqueda de linea
        pReturn = np.array([self.p])
        ddf0 = np.linalg.norm(df0)
        while ( ddf0 > 1e-6 and l<200):
            self.p = self.minizar_en_direccion(direccion)
            pReturn = np.append(pReturn,[self.p],axis=0)
            df1 = self.evaluar_gradiente()
            gamma = self.calcular_gamma(df1,df0)
            direccion = df1 + gamma *direccion
            df0 = df1
            ddf0 = np.linalg.norm(df0)
            l = l+1
        return pReturn

    def evaluar_gradiente(self):

        """ 
        Evalua el gradiente en el punto p.
        """
        return -self.gradiente(self.p)

    def minizar_en_direccion(self,direccion):

        """ 
        Busca el minimo de la funcion en una direccion
        """
        funcion_direccion = lambda a: self.funcion(self.p+a*direccion)
        p_min = minimize_scalar(funcion_direccion).x

        return p_min*direccion + self.p
    
    def calcular_gamma(self,gradiente_1,gradiente_0):

        """ 
        Calcula la constante gamma del metodo del gradiente segun el criterio de Polak-Rieve
        """
        return np.sum((gradiente_1-gradiente_0)*gradiente_1)/np.sum(gradiente_0*gradiente_0)


    def evaluar_punto_minimo(self,list_aux):
        """
        Busca el minimo entre una sucecion de puntos en la funcion f
        """
        min=list_aux[0][0]
        for i in range(1,self.cant_puntos):
            punto = list_aux[i][-1]
            if self.funcion(min) > self.funcion(punto):
                min=punto
        return min