import json
import os
from pathlib import Path

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

    def to_dict(self)-> dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "cantidad": self.cantidad
        }


class PanelSolar(DispositivoEcológico):
    potencia: float

    def __init__(self, codigo: str, nombre: str, cantidad: int, potencia: float):
        super().__init__(codigo, nombre, cantidad)
        self.potencia = potencia

    def ficha_tecnica(self, imprimir = False):
        ficha = super().ficha_tecnica()
        ficha += f" **** potencia: {self.potencia}"

        if imprimir: print(ficha)
        return ficha

    def to_dict(self):
        dict = super().to_dict()
        dict["potencia"] = self.potencia

        return dict

class GestorInventario:
    @staticmethod
    def guardar_catalogo_json(lista_dispositivos: list[DispositivoEcológico | PanelSolar], ruta_archivo: str)-> bool:

        Path(ruta_archivo).mkdir(exist_ok=True)

        with open(ruta_archivo + "/catalogo_ecotech.json", "w") as archivo:
            lista_dispositivos_serializados = []
            for elemento in lista_dispositivos:
                lista_dispositivos_serializados.append(elemento.to_dict())
            json.dump(lista_dispositivos_serializados, archivo, indent=4)


equipo_1 = DispositivoEcológico("probando-1", "probando-1", 10) 
equipo_2 = DispositivoEcológico("probando-2", "probando-2", 20)       


panel_1 = PanelSolar("panel-probando-1", "panel-probando-1", 10, 20.5)
panel_2 = PanelSolar("panel-probando-2", "panel-probando-2", 20, 30.6)
panel_3 = PanelSolar("panel-probando-3", "panel-probando-3", 30, 40.8)

try: 
    equipo_erroneo_1 = DispositivoEcológico("Test-error-1", "Test-error-1", -20 )
except StockInvalidoError as e:
    print(f"Excepcion capturada al instanciar un dispositivo ecologico con precio negativo: {e}")

try: 
    panel_1.cantidad = None
except StockInvalidoError as e:
    print(f"Excepcion capturada al modificar un dispositivo ecologico con un valor nulo: {e}")

lista_equipos: list[DispositivoEcológico | PanelSolar] = [
    equipo_1,  
    equipo_2,    
    panel_1,
    panel_2, 
    panel_3 
]

for equipo in lista_equipos:
    equipo.ficha_tecnica(True)

GestorInventario.guardar_catalogo_json(lista_equipos, "pruebas" )