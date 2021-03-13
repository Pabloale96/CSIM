import h5py
import numpy as np
import matplotlib.pyplot as plt

from sp.multirate import multirate


class ExtractorDatos:

    def __init__(self,path):

        """  
        Esta clase extrae los datos de los archivos HDF5, la idea es que alla un metodo para cada uno de los diferentes archivos,
        ya que los archivos HDF5 depende de como se generan. Por ejemplo, el programa gprMax genera un HDF5, entonces hay una clase
        gprMax que  hereda de ExtractorDatos. Si luego alguien usa el programa "pepito", se agrega una clase de pepito y extrae toda la informacion ahi,
        para que luego si alguien tenga que usar pepito, no tengo que hacer devuelta el metodo.

        Parametros:

        path: es la direccion del archivo a extraer los datos


        """
        self.path = path
        self.filename = h5py.File(filename, 'r')
        self.datos = None

class gprMax(ExtractorDatos):
        """
        Esta clase extrae los datos de un archivo HDF5 generado por el programa gprMax. El archivo HDF5 tiene el 
        siguiente formato:

        /
            /rxs
                rx1/
                    Name [optional]
                    Position
                    Ex
                    Ey
                    Ez
                    Hx
                    Hy
                    Hz
                    Ix
                    Iy
                    Iz
                rx2/
                    Name [optional]
                    ...
            srcs/
                src1/
                    Type
                    Position
                src2/
                    ...
            tls/
                tl1/
                    Position
                    Resistence
                    dl
                    Vinc
                    Iinc
                    Vtotal
                    Itotal
                tl2/
                    ...
        """

        def __init__(self, path):
            super().__init__(path)

        


