# SA_Wpp

Este proyecto es una herramienta que permite analizar sentimentalmente conversaciones almacenadas en un archivo de texto y luego guardar los resultados en un archivo Excel (.xlsx). Puede ser útil para comprender cómo se sienten las personas en una conversación o para realizar análisis de datos sentimentales en conjunto.

## Tabla de Contenidos

- [SA\_Wpp](#sa_wpp)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [Acerca del Proyecto](#acerca-del-proyecto)
  - [Instalación](#instalación)
  - [Manual de Usuario](#manual-de-usuario)
    - [Especificaciones](#especificaciones)

## Acerca del Proyecto

Este proyecto esta programado en Python 3 y utiliza esencialmente la libreria Pandas (v.1.5.3), corre en Windows 10 y la version instalada en el server debe contar con acceso a las carpetas donde se quiera guardar el archivo Historico.xlsx y el TableroWpp.pbix

## Instalación

Para instalar este proyecto, primero conseguimos el proyecto descargandolo de la web de GitHub, luego instalamos las dependencias/librerias necesarias o bien,

```bash
# Descargar el proyecto
git clone https://github.com/MateoCuenca09/SA_Wpp.git
cd MateoCuenca09
npm install
# Instalar las dependencias
pip install pandas, datatime, unidecode, schedule, time, requests
```

Por las dudas que falle, aqui dejo las versiones de las librerias que yo utilice:

- requests 2.28.2
- unidecode 1.3.6
- pandas 1.5.3
- schedule 1.2.0

## Manual de Usuario

- *Carga de Datos*: En la carpeta 'EntradaDatos' se debe dejar unicamente el archivo excel (.xlsx) con formato de Chattigo que se quiere analizar.Cuando en la carpeta 'EntradaDatos/Procesados' aparezca el archivo que se quizo analizar significa que el programa finalizo.

- *Visualización de Datos POWER BI*: Una vez finalizado la carga de datos, se debe ir al TableroWpp.pbi y en el mismo se debe clickear el boton que se encuentra en la parte de la derecha de la barra de herramientas que dice ACTUALIZAR.

### Especificaciones

- *Carga de Datos*: El programa solo espera recibir un solo archivo .xlsx con formato de Chattigo.
  
- *Almacenacion de Datos*: El programa ira almacenando los distintos archivos que recibe en una carpeta oculta que se encuentra en '/Datos', y los ira separando por mes, dejando conectado al TableroWpp.pbi simplemente el ultimo mes analizado.
  
- *Analisis de los Datos*: Se analizaran simplemente los mensajes que envian los clientes, quitando de todo historial los mensajes enviados por el bot que atiende antes de derivar al cliente y almacenando pero no analizando los mensajes enviados por el agente.
  
- *Visualización de Datos POWER BI*: En el TableroWpp.pbi se visualizan varias metricas aplicadas a los puntajes negativos de los clientes, ya que lo que se desea en este caso es detectar clientes insatisfechos, y junto a las metricas se encuentra una tabla para visualizar la conversacion en si.
  