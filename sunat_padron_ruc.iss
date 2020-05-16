Sub Main
	IgnoreWarning(True)
	Call TextImport()	'C:\Users\Intel\Documents\Mis documentos IDEA\Samples\Archivos fuente.ILB\padron_reducido_ruc.txt
	Client.RefreshFileExplorer
End Sub


' Archivo - Asistente de importación: Texto delimitado
Function TextImport
	dbName = "padron_reducido_ruc.IMD"
	Client.ImportDelimFile "C:\Users\Intel\Documents\Mis documentos IDEA\Samples\Archivos fuente.ILB\padron_reducido_ruc.txt", dbName, FALSE, "", "C:\Users\Intel\Documents\Mis documentos IDEA\Samples\Definiciones de importación.ILB\padron_reducido_ruc.RDF", TRUE
	Client.OpenDatabase (dbName)
End Function

