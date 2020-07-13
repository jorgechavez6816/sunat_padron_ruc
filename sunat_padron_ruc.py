### Procedimiento automatizado de descarga de Padrón Reducido Ruc de SUNAT - Perú

# 01. Librerías a utilizar
from urllib.request import urlopen
from zipfile import ZipFile

# 02. Definición de ruta web
zip_url = 'http://www2.sunat.gob.pe/padron_reducido_ruc.zip'

# 03. Abrir URL
archivo_zip = urlopen(zip_url)

# 04. Crea un archivo temporal de tránsito en disco duro
tempo_zip = open("C:\\Users\\Intel\\temporal.zip", "wb")

# 05. Traslada info de archivo descargado a nuevo archvo
tempo_zip.write(archivo_zip.read())

# 06. Cierra el archivo temporal creado
tempo_zip.close()

# 07. Re-open the newly-created file with ZipFile()
z_final = ZipFile("C:\\Users\\Intel\\temporal.zip")

# 08. Deposita el archivo extraido en ruta señalada
z_final.extractall(path = 'C:\\Users\\Intel\\Documents\\Mis documentos IDEA\\Samples\\Archivos fuente.ILB')

# 09. Cierra el archivo zip
z_final.close()