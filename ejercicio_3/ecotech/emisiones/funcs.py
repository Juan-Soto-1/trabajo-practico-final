import pandas

def calcular_emisiones_carbono(consumo_kwh: float, factor_emision: float = 0.4)-> float:
    if consumo_kwh < 0:
        raise ValueError("el consumo de kilovatio hora debe ser mayor a 0")
    return consumo_kwh * factor_emision

def obtener_metricas_consumo(registros: list[dict])-> dict:

   registros_df = pandas.DataFrame(registros)
   valor_total_emisiones = 0
   registros_totales = []

   for indice, registro in registros_df.iterrows():
       try:
          valor_total_registros = calcular_emisiones_carbono(registro["consumo_kwh"], registro["factor_emision"])
          registros_totales.append(valor_total_registros) 
          valor_total_emisiones += valor_total_registros
       except ValueError: continue

    registros_df["registros_totales"] = registros_totales

    indice_planta_mayor_consumo = registros_df["consumo_kwh"].idxmax()
    planta_mayor_consumo = registros_df.loc[indice_planta_mayor_consumo, "planta"]

    metricas = {
        "valor_total_emisiones": valor_total_emisiones,
        "planta_mayor_consumo": planta_mayor_consumo,
        "desglose": registros_df.to_dict()
    }

    return metricas
        
