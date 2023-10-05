import pandas as pd

def filtro_ascesor(df):
    """  
    Funcion que detecta en el Dataframe cuando un chat sale del menu del Bot
    """
    try:        
        Idchats = df['ID Chat'].unique()
        idchats_no = []
        for idchat in Idchats:
            df1 = df.loc[(df['ID Chat'] == idchat)]
            if not df1['Mensaje'].str.startswith('CHAT ASIGNADO A AGENTE').any():
                idchats_no.append(idchat)
        df = df[~df['ID Chat'].isin(idchats_no)]
        return df
    except Exception as e:
        print("Error filtro_asesor: ",e)


def link_multimedia(df):
    """  
    Funcion que detecta cuando hay un link que lleva a un archivo multimedia 
    y lo mueve a la columna Mensaje que no es eliminada al preprocesar.
    """
    try:
        # Verificar si hay valores en la columna "Attachment"
        df['Mensaje'] = df.apply(lambda row: row['Attachment'] if pd.notnull(row['Attachment']) else row['Mensaje'], axis=1)
        
        # Eliminar la columna "Attachment" si se desea
        # del df['Attachment']
    except Exception as e:
        print("Error en link_multimedia(): ",e)
    
    return df   

def cambiar_remitente(df):
    """  
    Funcion que detecta cuando los mensajes enviados por el Bot y cambia la columna Remitentes
    """
    try:
        remitentes_inbound = df[df['Tipo'] == 'INBOUND']['Remitente'].unique()
        for inbound in remitentes_inbound:
            df.loc[(df['Tipo'] == 'OUTBOUND') & (df['Remitente'] == inbound), 'Remitente'] = 'Bot'
        return df
    except Exception as e:
        print("Error cambiar_remitente(): ",str(e))

def obtener_rango_fechas(df):
    """  
    Funcion que obtiene el rango de fechas del archivo para el guardado del mismos
    """
    try:
        df['Fecha Hora'] = pd.to_datetime(df['Fecha Hora'])
        fecha_mas_antigua = df['Fecha Hora'].dt.date.min().strftime("%Y-%m-%d")
        fecha_mas_reciente = df['Fecha Hora'].dt.date.max().strftime("%Y-%m-%d")
        return fecha_mas_antigua, fecha_mas_reciente
    except Exception as e:
        print("Error al obtener fechas: ",e)

