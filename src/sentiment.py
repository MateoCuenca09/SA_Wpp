import pandas as pd
import os
from process import preproces, analisis, guardar_historico
from MIfileHandling import guardar, move_file


def mainSent(carpeta,archivo):
    """
    Funcion principal que maneja el flujo del programa. Se encarga tambien de mover el archivo analizado a otra carpeta.
    Parametros: --void--
    Return: --void--
            - Guarda un archivo .xlsx en la carpeta Datos
    """
    # Leo Archivo!
    archivo_completo = os.path.join(carpeta,archivo)
    df_crudo = pd.read_excel(archivo_completo)

    # Filtro DF y separo en Clientes y Agentes
    df = preproces(df_crudo)

    # Analizo DF Clientes y puntuo mensajes
    df_analizado = analisis(df['Clientes'])


    # Generamos DF con todos los datos
    df_completo = pd.merge(df_analizado, df['Agentes'],how='outer')

    # Guardamos el Archivo
    guardar(df_completo)

    # Movemos de Carpeta el ya analizado
    move_file(archivo_completo)
    