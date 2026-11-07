from django.shortcuts import render, redirect
from django.http import HttpRequest
import funcs 

def vista_panel_sustentabilidad(request: HttpRequest):
    lista_registros = [
        { "planta": "001", "consumo_kwh": 200, "factor_emision": 0.6  },
        { "planta": "002", "consumo_kwh": 300, "factor_emision": 0.7  },
        { "planta": "003", "consumo_kwh": 400, "factor_emision": 0.8  }         
    ]

    metricas = funcs.obtener_metricas_consumo(lista_registros)

    contexto = {"titulo": "sustentabilidad", "metricas": metricas}

    return render(request, "sustentabilidad/panel.html", contexto)