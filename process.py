import pandas as pd
import os
from pysentimiento import create_analyzer
from funciones import filtro_ascesor,link_multimedia,cambiar_remitente



def preproces(df):
    """ 
    Funcion que preprocesa el archivo para analizarlo. Asi como quitar palabras que confunden al analyzer, 
    y analizar simplemente los mensajes de los clientes.
    Parametros: - df : DataFrame con los datos a analizar
    Return: - df : DataFrame con los datos preprocesados
    """
    try:
        df = filtro_ascesor(df)
        df = link_multimedia(df)
        df = cambiar_remitente(df)
        # Filtra las filas del ChatBot
        df_filtro1 = df.loc[df['Remitente'] != 'ChatBot']

        #Escribir nuevo excel con cliente fecha mensaje
        columnas = ['Fecha Hora','ID Contacto','Remitente','Tipo','Mensaje']
        df = df_filtro1[columnas]
        df_clientes = df.loc[df['Tipo'] == 'INBOUND']
        df_agentes = df.loc[df['Tipo'] != 'INBOUND']

        # Filtro mensajes inutiles
        df_clientes = df_clientes[df_clientes['Mensaje'].str.len() > 2]

        palabras_filtro = ['Soy Propietaria/o ',
                            'Otro',
                            'Otras consultas',
                            'Inic. obra/Amojonado',
                            'Cesión del Inmueble',
                            'Loteo',
                            'Expensas',
                            'Volver menú anterior',
                            'Muy Satisfecha/o',
                            'Satisfecha/o',
                            'Muy Insatisfecha/o',
                            'Indiferente',
                            'Por este medio',
                            'Llamada',
                            'Por teléfono',
                            'Quebradas',
                            'Medios de pago',
                            'Expensa corriente',
                            'CuestasCamposPampas'  
                        ]

        df_clientes = df_clientes[~df_clientes['Mensaje'].isin(palabras_filtro)]

        df = {"Clientes":df_clientes,"Agentes":df_agentes}

        return df 

    except Exception as e:
        print("Error al Preprocesar los datos: ", e)


def analisis(df):
    """ 
    Funcion que analiza el DataFrame con el Analyzer.
    Parametros: - df : Dataframe con los datos preprocesados.
    Return: - df : Dataframe con cuatro columnas nuevas representando el analisis de los mensajes
    """
    try:
        print("Arranca Sentiment Analisis!")

        # Inicializar el analizador de sentimientos de Pysentimiento
        analyzer = create_analyzer(task="sentiment", lang="es")

        # Carga todos los archivos a analizar por Robertuito
        columna = df['Mensaje'].astype(str)
        output = []
        neg = []
        neu = []
        pos = [] 

        for valor in columna:

            result = analyzer.predict(valor)
            output_process = result.output
            neg_process = result.probas['NEG']
            neu_process = result.probas['NEU']
            pos_process = result.probas['POS']
            output.append(output_process)
            neg.append(neg_process)
            neu.append(neu_process)
            pos.append(pos_process)



        df['Output'] = output
        df['NEG'] = neg
        df['NEU'] = neu
        df['POS'] = pos
        print("Termina Sentiment Analis")
        return df

    except Exception as e:
        print("Error al analizar: ",e)


def guardar_historico(df):
    """  
    Funcion que intenta guardar el DataFrame ya analizado.
    Parametros: - df : Dataframe con los mensajes analizados.
    Return: --void--
    """
    try:
        df_historico = pd.read_excel("O:\\Gestion y Experiencia del Cliente\\5. SERVICIO DE ATENCIÓN AL CLIENTE\\11. TRANSFORMACIÓN DIGITAL\\ReporteWpp\\Datos\\Historico.xlsx")
        historico = True
    except FileNotFoundError as e:
        historico = False
        print("No se encuentra Excel Historico")
        print("Procede a crear uno nuevo vacio")
        df_historico = pd.DataFrame()

    try:
        df_historico_nuevo = pd.concat( [df_historico,df], ignore_index=True, verify_integrity = True)
        if historico:
            df_historico_nuevo = df_historico_nuevo.drop_duplicates()
        df_historico_nuevo.to_excel("O:\\Gestion y Experiencia del Cliente\\5. SERVICIO DE ATENCIÓN AL CLIENTE\\11. TRANSFORMACIÓN DIGITAL\\ReporteWpp\\Datos\\Historico.xlsx", index= False)
    except Exception as e:
        print("Error al indexar DF o guardar: ",e)


        


