class StockInvalidoError(Exception):
    """
    Excepcion personalizada pensada para ser lanzada al momento de intentar asignar una cantidad negativa o 
    no numerica
    """



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
        except ValueError:
            raise StockInvalidoError("el valor a agregar en cantidad tiene que ser un numero entero")
        except TypeError:
            raise StockInvalidoError("el valor a agregar en cantidad no puede ser nulo")
        
    
        if valor_entero < 0:
            raise StockInvalidoError("el valor a agregar en cantidad tiene que ser mayor o igual a 0")
            
        self.__cantidad = valor_entero

    def ficha_tecnica(self, imprimir: bool = False)-> str:
        ficha = f"* codigo: {self.codigo} ** nombre: {self.nombre} *** cantidad: {self.cantidad}"

        if imprimir: print(ficha)
        return ficha


class PanelSolar(DispositivoEcológico):
    potencia: float

    def __init__(self, codigo: str, nombre: str, cantidad: int, potencia: float):
        super().__init__(codigo, nombre, cantidad)
        self.potencia = potencia

    def ficha_tecnica(self, imprimir = False):
        ficha_dispositivo_ecologico = super().ficha_tecnica(imprimir)
        ficha_dispositivo_ecologico += f"**** potencia: {self.potencia}"

        if imprimir: print(ficha)
        return ficha


equipo = DispositivoEcológico("probando", "probando", 30)       
equipo.ficha_tecnica(True)
