"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as file:
      lineas = file.readlines()
    filas = []
    bloque = []

    
    for linea in lineas[4:]:
        linea = linea.strip()
        if linea:
            bloque.append(linea)
        else:
            if bloque:
                fila_completa = " ".join(bloque)
                filas.append(fila_completa)
                bloque = []

  
    if bloque:
        filas.append(" ".join(bloque))
    datos = []



    for fila in filas:
        partes = fila.split()
        cluster = int(partes[0])
        cantidad = int(partes[1])
        porcentaje = float(partes[2].replace(",", "."))
        palabras = " ".join(partes[3:]).replace(" ,", ",").rstrip(".").strip("%").strip()
        datos.append([cluster, cantidad, porcentaje, palabras])

    columnas = [
        "cluster",
        "cantidad_de_palabras_clave",
        "porcentaje_de_palabras_clave",
        "principales_palabras_clave"
    ]

    return pd.DataFrame(datos, columns=columnas)
    
print(pregunta_01())
