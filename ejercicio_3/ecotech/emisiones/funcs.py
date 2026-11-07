def calcular_emisiones_carbono(consumo_kwh: float, factor_emision: float = 0.4)-> float:
    if consumo_kwh < 0:
        raise ValueError("el consumo de kilovatio hora debe ser mayor a 0")
    return consumo_kwh * factor_emision

