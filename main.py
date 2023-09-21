import pandas as pd
import os
from process import preproces, analisis, guardar_historico


def main(carpeta,archivo):
    # Leo Archivo!
    archivo_completo = os.path.join(carpeta,archivo)
    df_crudo = pd.read_excel(archivo_completo)

    # Filtro DF y separo en Clientes y Agentes
    df = preproces(df_crudo)

    # Analizo DF Clientes y puntuo mensajes
    df_analizado = analisis(df['Clientes'])


    # Generamos DF con todos los datos
    df_completo = pd.merge(df_analizado, df['Agentes'],how='outer')

    #guardar(df_completo)

    guardar_historico(df_completo)

    carpeta = carpeta + "\\Procesados"
    archivo_completo = os.path.join(carpeta,archivo)
    try:
        df_crudo.to_excel(archivo_completo, index=False)
    except Exception:
        archivo = "COPIA" + archivo
        df_crudo.to_excel(archivo_completo, index=False)