import os
import time
from main import main
#O:\Gestion y Experiencia del Cliente\5. SERVICIO DE ATENCIÓN AL CLIENTE\11. TRANSFORMACIÓN DIGITAL\ReporteWpp


os.chdir(r'O:\\Gestion y Experiencia del Cliente\\5. SERVICIO DE ATENCIÓN AL CLIENTE\\11. TRANSFORMACIÓN DIGITAL\\ReporteWpp')
carpeta = os.path.join('EntradaDatos')  # Ruta de la carpeta a monitorear
extension = '.xlsx'  # Extensión del archivo a detectar

archivos_previos = set()  # Conjunto de archivos previamente encontrados

while True:
    archivos_actuales = set()
    # Obtener la lista de archivos en la carpeta
    for archivo in os.listdir(carpeta):
        if archivo.endswith(extension):
            archivos_actuales.add(archivo)

    # Obtener los nuevos archivos encontrados
    nuevos_archivos = archivos_actuales - archivos_previos

    # Ejecutar el programa para cada nuevo archivo
    for archivo in nuevos_archivos:
        try:
            print(archivo)
            main(carpeta,archivo)
            print("Archivo procesado: ",archivo)
        except Exception as e:
            print("Error al iniciar programa: ", e)

    # Actualizar los archivos previamente encontrados
    archivos_previos = archivos_actuales

    # Esperar un tiempo antes de la siguiente verificación
    time.sleep(1)

