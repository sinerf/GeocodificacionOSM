def geocodificar(pathArchivoOrigina,pathArchivoresultado):
    from geopy.geocoders import Nominatim
    import csv
    import pandas as pd

    # Creamos una lista vacía donde almacenaremos las direcciones.
    nombres=[]
    nombresCorregidos=[]
    direcciones = []
    direccionesCorregidas=[]
    telefonos= []
    telefonosCorregidos=[]
    paginasWeb=[]
    paginasWebCorregidas=[]
    tipos=[]
    tiposCorregido=[]

    archivo = open(pathArchivoOrigina,encoding="utf8")
    csv_archivo = csv.reader(archivo, delimiter=';', quotechar='|', lineterminator='\r\n', quoting=csv.QUOTE_NONE)
    for fila in csv_archivo:
        nombres.append(str(fila[0]))
    nombres.pop(0)
    for nombre in nombres:
        nombreC=nombre.strip("\"").strip(" \"").replace(";",",")
        nombresCorregidos.append(nombreC)
    # print(nombresCorregidos)
    # # Cerramos el archivo abierto
    archivo.close()


    archivo = open(pathArchivoOrigina,encoding="utf8")
    #
    # Utilizamos la función reader para leer el contenido del csv cuyas columnas están delimitadas por el caracter ;
    csv_archivo = csv.reader(archivo, delimiter='"', quotechar='|', lineterminator='\r\n', quoting=csv.QUOTE_NONE)
    # Vamos leyendo la primera columna de cada fila del csv y añadiendo la dirección a la lista.
    # print(csv_archivo)
    for fila in csv_archivo:
        direcciones.append(str(fila[3]))
    direcciones.pop(0)
    for direccion in direcciones:
        direccionC=direccion.strip("\"").strip(" \"").replace(";",",")[:-6]+"03710, España"
        direccionesCorregidas.append(direccionC)
    # print(direccionesCorregidas)
    # # Cerramos el archivo abierto
    archivo.close()


    archivo = open(pathArchivoOrigina,encoding="utf8")
    csv_archivo = csv.reader(archivo, delimiter='"', quotechar='|', lineterminator='\r\n', quoting=csv.QUOTE_NONE)
    for fila in csv_archivo:
        # print(fila)
        telefonos.append(str(fila[5]))
    telefonos.pop(0)
    for telefono in telefonos:
        telefonoC=telefono.strip("\"").strip(" \"").replace(";",",")
        telefonosCorregidos.append(telefonoC)
    # print(telefonosCorregidos)
    # # Cerramos el archivo abierto
    archivo.close()

    archivo = open(pathArchivoOrigina,encoding="utf8")
    csv_archivo = csv.reader(archivo, delimiter='"', quotechar='|', lineterminator='\r\n', quoting=csv.QUOTE_NONE)
    for fila in csv_archivo:
        paginasWeb.append(str(fila[7]))
    paginasWeb.pop(0)
    for pagina in paginasWeb:
        paginaC=pagina.strip("\"").strip(" \"").replace(";",",")
        paginasWebCorregidas.append(paginaC)
    # print(paginasWebCorregidas)
    # # Cerramos el archivo abierto
    archivo.close()


    archivo = open(pathArchivoOrigina,encoding="utf8")
    csv_archivo = csv.reader(archivo, delimiter='"', quotechar='|', lineterminator='\r\n', quoting=csv.QUOTE_NONE)
    for fila in csv_archivo:
        tipos.append(str(fila[9]))
    tipos.pop(0)
    for tipo in tipos:
        tipoC=tipo.strip("\"").strip(" \"").replace(";",",")
        tiposCorregido.append(tipoC)
    # print(tiposCorregido)
    # # Cerramos el archivo abierto
    archivo.close()

    # Creamos un nueva lista donde se guardarán las localizaciones.
    latitud=[]
    longitud=[]
    # # #
    # # # # Cada servicio de geolocalización como Google Maps, Bing Maps, Yahoo, MapQuest o Nominatim tiene su propia clase en geopy.geocoders para utilizar el servicio API.
    # # # Creamos un objeto llamado geolocalizador a partir de la clase Nominatim().
    geolocalizador = Nominatim(user_agent="Google Chrome")
    # # #
    # # # # Para cada dirección almacenada en la lista 'direcciones' pedimos al servicios de geocodificación de Nominatim que nos devuelva su coordenada y la guardamos en la variable 'coordenadas'. Añadimos la latitud y lo9ngitud a la lista 'localizaciones'.
    for val in direccionesCorregidas:
        direccionesGeo = geolocalizador.geocode([val], timeout=15)
        try:
            latitud.append(str(direccionesGeo.latitude))
            longitud.append(str(direccionesGeo.longitude))
        except:
            latitud.append(' ')
            longitud.append(' ')
    # print(longitud)
    # print(latitud)
    # Creamos un dataframe para luego exportarlo com un archivo .csv
    dataframe={'nombre':nombresCorregidos,'direcciones':direccionesCorregidas,'telefon':telefonosCorregidos,'paginasWeb':paginasWebCorregidas,'tipo':tiposCorregido,'longitud':longitud,'latitud':latitud}
    df = pd.DataFrame(data=dataframe)
    df.to_csv(pathArchivoresultado, sep=';', mode='a')

# Geocodificamos todos los archivos dentro de una carpetas
from os import walk
carpeta ="C:\PFM\ScrapCalpeGeocodifiado"
listaEntidades = []

for(path,carpetas, archivos) in walk(carpeta):
    for elemento in archivos:
            listaEntidades.append(path + "\\" + elemento)
print(listaEntidades)
for w in listaEntidades:
    try:
        geocodificar(w,w[:-4]+"final.csv")
    except:
        print("problemas con"+w)