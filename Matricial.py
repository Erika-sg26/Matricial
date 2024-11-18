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
    
A= Matriz("[5 3 4;4 5 9;8 9 7]")
A.imprimir() ##Se llama asi en esta formato ya que es un metodo


