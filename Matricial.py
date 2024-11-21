class Matriz:
    def __init__(self, cadena: str):
        if not (cadena[0]=="[" and cadena[-1]=="]"):
            print("Cadena no valida")
            return(None)
        #print("Continuamos")
        cadena=cadena[1:-1]
        sfilas=cadena.split(";")
        #print(sfilas)
        self.nrows=len(sfilas)
        ncols=0
        Filas=[]
        for s in sfilas: ##Llena la lista vacia con los valores separados
            filastr=s.split(" ")     
            if ncols==0:
                ncols=len(filastr)
            elif ncols!=len(filastr):
                print("error por numero de filas")
                return(None)
            fila_float=[]
            for x in filastr:
                fila_float.append(float(x)) 
            Filas.append(fila_float)
            
            ncols=len(fila_float)
        self.ncols=ncols
        self.matriz=Filas.copy()


    def imprimir(self, decimales=2):
        for fila in self.matriz:
            for e in fila:
                print(f"{e:-8.2f}", end="")
            print(" ")

    def dimensiones(self):
        """Devuelve las dimensiones de la matriz."""
        pass

    def sumar(self, otra_matriz):
        """Suma dos matrices."""
        pass

    def multiplicar_escalar(self, escalar):
        if not self.matriz:
            #print("No se puede")
            return None
        res_matriz=[]
    
        for i in self.matriz:
            nrows = [elemento * escalar for elemento in i]
            res_matriz.append(nrows)
    
        return res_matriz
    
    


    def multiplicar_matriz(self, otra_matriz):
        """Multiplica dos matrices."""
        pass

    def son_iguales(self, otra_matriz):
        """Verifica si dos matrices son iguales."""
        pass

    def traza(self):
        """Calcula la traza de la matriz."""
        pass

    def traspuesta(self):
        """Devuelve la traspuesta de la matriz."""
        pass

    def determinante_2x2(self):
        """Calcula el determinante de una matriz 2x2."""
        pass

    def generar_identidad(self, tamano):
        """Genera una matriz identidad de tama~no n x n."""
        pass

    def determinante(self):
        """Calcula el determinante de una matriz 3x3."""
        pass


