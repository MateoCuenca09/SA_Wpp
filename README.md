# SA_Wpp

Todos sabemos que WhatsApp habilito el desarrollo de Bots para todos! Pero... A que costo? El flujo de conversaciones que puede manejar es bastante gigantesco y si ya tenemos un Bot no queremos contratar humanos para revisarlo... O si, pero, como sabemos si nuestros clientes estan satisfechos con nuestro producto? o nuestra atencion en post venta?
En esta libreria estamos desarrollando la herramienta definitiva!
Utilizando un red neuronal pre entrenada, analizamos SENTIMENTALMENTE todas las conversaciones, en varios formatos, para clasificarlas en las categorias que necesitamos!
En este caso utilizamos Chattigo para descargar las conversaciones, Pandas para manejar los datos en DataFrames, Robert-tuito en español para hacer el analisis y PowerBi para graficar los resultados y poder hacer filtros interactivos para encontrar casos puntuales.
Puntualmente en este proyecto se busca detectar los clientes insatisfechos o problematicos, entonces los puntajes de las conversaciones se van acumulando por numero de telefono, ademas en el tablero graficamos la conversacion en si para poder ver el problema puntual y adjuntamos el numero de telefono para poder resolverlo puntualmente!
Sin mas, los dejo con los detalles tecnicos!

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

- *Carga de Datos*: El programa solo espera recibir archivos .xlsx con formato de Chattigo.
  
- *Almacenacion de Datos*: El programa ira almacenando los distintos archivos que recibe en una carpeta oculta que se encuentra en '/Datos', y los ira separando por mes, dejando conectado al TableroWpp.pbi simplemente el ultimo mes analizado.
  
- *Analisis de los Datos*: Se analizaran simplemente los mensajes que envian los clientes, quitando de todo historial los mensajes enviados por el bot que atiende antes de derivar al cliente y almacenando pero no analizando los mensajes enviados por el agente.
  
- *Visualización de Datos POWER BI*: En el TableroWpp.pbi se visualizan varias metricas aplicadas a los puntajes negativos de los clientes, ya que lo que se desea en este caso es detectar clientes insatisfechos, y junto a las metricas se encuentra una tabla para visualizar la conversacion en si.
  
