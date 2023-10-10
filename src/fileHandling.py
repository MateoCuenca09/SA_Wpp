import pandas as pd

# Carpeta Recibidora de Archivos
carpeta = 'O:\Gestion y Experiencia del Cliente\5. SERVICIO DE ATENCIÓN AL CLIENTE\11. TRANSFORMACIÓN DIGITAL\ReportesSentiment/Entrada Datos'

# Archivo Activo de PowerBi
activo_path = 'C:/Users/cuenc/OneDrive - EDISUR SA/Mateo Cuenca/SA_Wpp/.ignore/Datos Procesados/Activo.xlsx'
# Archivo Temp y Carpeta
temp_path = "C:/Users/cuenc/OneDrive - EDISUR SA/Mateo Cuenca/SA_Wpp/.ignore/Datos Procesados/Temp.xlsx"
folder_temp_path = 'C:/Users/cuenc/OneDrive - EDISUR SA/Mateo Cuenca/SA_Wpp/.ignore/Datos Procesados/'

def guardar(df):
    try:
        guardar_archivo(df,activo_path)
        separar_dos_meses()
        separar_por_mes()
    except Exception as e:
        print("Error guardar(): ",e)

def separar_dos_meses():
    try:        
        df = pd.read_excel(activo_path)
        df['Fecha_Hora_temp'] = pd.to_datetime(df['Fecha Hora'])
        fecha_reciente = pd.to_datetime(df['Fecha Hora'].max())
        delta_tiempo = 60 # Tiempo en dias que se quiere acumular en el Excel historico
        fecha_antigua = fecha_reciente - pd.to_timedelta(delta_tiempo, unit='D')

        df_activo = df.loc[df['Fecha_Hora_temp']>= fecha_antigua]
        df_dump = df.loc[df['Fecha_Hora_temp']<= fecha_antigua]
        guardar_archivo(df_dump,temp_path)
        df_activo.to_excel(activo_path, index = False)


    except Exception as e:
        print("Error separar_dos_meses(): ",e)


def guardar_archivo(df,path):
    try:
        df_existente = pd.read_excel(path)
        df_nuevo = pd.concat([df, df_existente], ignore_index=True)
        df_nuevo = df_nuevo.drop_duplicates(ignore_index=True, keep='last', subset='ID Mensaje')
        df_nuevo.to_excel(path, index = False)
    except FileNotFoundError:
        print("Creando nuevo archivo, ",path)
        df.to_excel(path, index = False)
    except Exception as e:
        print("Error al guardar_archivo()")
        print("Archivo: ",path)
        print("Error: ",e)



def separar_por_mes():
    try:
        df_dump = pd.read_excel(temp_path)
        df_dump['Fecha_Hora_temp'] = df_dump['Fecha Hora']
        df_dump['Fecha_Hora_temp'] = pd.to_datetime(df_dump['Fecha_Hora_temp'])
        df_dump['Fecha_Hora_temp'] = df_dump['Fecha_Hora_temp'].dt.strftime('%Y-%m')
        meses = df_dump['Fecha_Hora_temp'].unique()
        for mes in meses:
            df_mes = df_dump.loc[df_dump['Fecha_Hora_temp'] == mes]
            df_mes = df_mes.drop('Fecha_Hora_temp', axis=1)
            archivo_path = folder_temp_path + mes + ".xlsx"
            guardar_archivo(df_mes, archivo_path)

    except Exception as e:
        print("Error separar_por_mes(): ", e) 