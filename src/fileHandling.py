import pandas as pd
import shutil
import os

# Carpeta Recibidora de Archivos
carpeta = 'O:/Gestion y Experiencia del Cliente/5. SERVICIO DE ATENCIÓN AL CLIENTE/11. TRANSFORMACIÓN DIGITAL/ReportesSentiment/Entrada Datos'
carpeta_analizados = 'O:/Gestion y Experiencia del Cliente/5. SERVICIO DE ATENCIÓN AL CLIENTE/11. TRANSFORMACIÓN DIGITAL/ReportesSentiment/Entrada Datos/Procesados' 

# Archivo Activo de PowerBi
activo_path = 'O:/Gestion y Experiencia del Cliente/5. SERVICIO DE ATENCIÓN AL CLIENTE/11. TRANSFORMACIÓN DIGITAL/ReportesSentiment/Datos/Activo.xlsx'
# Archivo Temp y Carpeta
temp_path = "O:/Gestion y Experiencia del Cliente/5. SERVICIO DE ATENCIÓN AL CLIENTE/11. TRANSFORMACIÓN DIGITAL/ReportesSentiment/Datos/Temp.xlsx"
folder_temp_path = 'O:/Gestion y Experiencia del Cliente/5. SERVICIO DE ATENCIÓN AL CLIENTE/11. TRANSFORMACIÓN DIGITAL/ReportesSentiment/Datos/'

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

def move_file(archivo_a_mover):
    try:
        shutil.move(archivo_a_mover, carpeta_analizados)
        print("Archivo movido con EXITO!")

    except FileExistsError:
        try:
            print("Se encontro una copia del archivo: ",archivo_a_mover)
            os.remove(archivo_a_mover)
            print("Archivo Eliminado")
        except Exception as e:
            print("Se encontro una copia del archivo: ",archivo_a_mover)
            print("Error al intentar eliminarlo: ",e)
    except Exception as e:
        print("1er Error move_file(): ", e)
        try:
            shutil.move("Copia" + archivo_a_mover, carpeta_analizados)
        except Exception as e2:
            print("2do Error move_file(): ", e2)
