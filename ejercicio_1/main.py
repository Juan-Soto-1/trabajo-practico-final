import pandas

def limpiar_registro_sensor(registro_raw: dict)-> dict:
    
    datos_df = pandas.DataFrame(registro_raw)      
    
    datos_df["sensor_id"] = datos_df["sensor_id"].str.strip()
    datos_df["temperatura"] = datos_df["temperatura"].str.lower()
    datos_df["temperatura"] = datos_df["temperatura"].str.replace("c", "")
    datos_df["temperatura"] = datos_df["temperatura"].str.replace(",", ".")

    try:        
        float(datos_df.at[0, "temperatura"])
    except:
        raise ValueError("el dato ingresado en temperatura no es un valor aceptado") 
        
    datos_df["temperatura"] = pandas.to_numeric(datos_df["temperatura"]) 
    datos_df["ubicacion"] = datos_df["ubicacion"].str.strip()    
    datos_df["ubicacion"] = datos_df["ubicacion"].replace("", pandas.NA).fillna("ubicacion no asignada")

    return datos_df.to_dict(orient="records")[0]


def generar_resumen_sensores(lista_sensores_limpios: list[dict], umbral_temperatura: float)-> tuple:
    
    lista_sensores_alerta = []
    suma_temperaturas = 0
    
    for lectura in lista_sensores_limpios:
        suma_temperaturas += lectura.get("temperatura")
        if umbral_temperatura < lectura.get("temperatura"):
            lista_sensores_alerta.append(lectura.get("sensor_id"))

    promedio_temperatura = suma_temperaturas / len(lista_sensores_limpios)

    return (lista_sensores_alerta, promedio_temperatura)


lista_registros = [
    {
     "sensor_id": [" SENSOR-001 "],
     "temperatura": ["25.0C"], 
     "ubicacion": ["Planta Norte"]
    },
    {
     "sensor_id": [" SENSOR-002  "],
     "temperatura": ["20.0C"],
      "ubicacion": [None]
    },
    {
     "sensor_id": [" SENSOR-003"], 
     "temperatura": ["30.0C"], 
     "ubicacion": [""]
    },
]

lista_registros_limpios = []
for registro in lista_registros:
    lista_registros_limpios.append(limpiar_registro_sensor(registro))

print(lista_registros_limpios)

print(generar_resumen_sensores(lista_registros_limpios, 30))

