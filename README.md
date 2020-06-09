# sunat_padron_ruc
Descarga automáticamente el padrón reducido del RUC de SUNAT - Perú.
(La base de datos más voluminosa puesta a disposición, más de 11 millones de registros)

Utilizando el software IDEA y scripts en IDEAScript y Python se descarga el padrón reducido de contribuyentes registrados en la página web de SUNAT.

Procedimiento:
1. Se cambia en la ruta de los scripts ISS y py, la parte de la ruta del dispositivo, es decir donde indica "intel" reemplazar por el usuario específico.
2. Se ejecuta el script "sunat_padron_ruc.ISS" desde IDEA y cosiderando que el archivo "padron_reducido_ruc.RDF" se encuentra en la carpeta /Samples/Definiciones de importación.ILB
3. Se tendrá como resultado el archivo bajado en formato IMD de aproximadamente 13.7 millones de registros.
