class StockInvalidoError(Exception):
     pass



class DispositivoEcológico:
    codigo: str
    nombre: str
    __cantidad: int

    def __init__(self, codigo: str, nombre: str, cantidad: int):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad

    @property
    def cantidad(self): return self.__cantidad

    @cantidad.setter
    def cantidad(self, valor):
    
        try:
            valor_entero = int(valor)
        except (ValueError, TypeError):
            raise StockInvalidoError("el valor a agregar en cantidad tiene que ser un numero entero")
        
    
        if valor_entero < 0:
            raise StockInvalidoError("el valor a agregar en cantidad tiene que ser mayor a 0")
            
        self.__cantidad = valor_entero


DispositivoEcológico("probando", "probando2", 0)



        

