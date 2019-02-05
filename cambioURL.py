import re
import csv

def main(archivoDB,archivoCSV):
	doc = open(archivoDB,"r")
	contenido = doc.read()
	doc.close()
	contador1 = 0
	listaURL = extraerURL(contenido)
	print(len(listaURL) + "URL extraidas")
	for url in listaURL:
		doc1 = open(archivoCSV, "r")
		csv1 = csv.reader(doc1)
		codigoAntiguo = extraerCodigos(url)
		codigoNuevo = sustitutirCodigoCSV(csv1, codigoAntiguo[0])
		urlNueva = "" #NUEVA URL CON EL NUEVO CÓDIGO
		doc1.close()
		contenido = contenido.replace(url,urlNueva)
		if contador1%100 == 0:
			print(str(contador1) +"URL nuevas")
		contador1 += 1
	nuevoDocumento = open("nuevoFichero.SQL", "w")
	nuevoDocumento.write(contenido)
	nuevoDocumento.close()

def extraerURL(archivoDB):
	pattern = r"" #PATRÓN DE LA URL ANTIGUA
	url = re.findall(pattern,archivoDB)
	url = set(url)
	return url

def extraerCodigos(archivoDB):
	codigo = r"[0-9]{7}"
	codigoAntiguo = re.findall(codigo,archivoDB)
	return codigoAntiguo

def sustitutirCodigoCSV(archivoCSV, codigoAntiguo):
	codigoNuevo = ""
	for line in archivoCSV:
		codigo = line[1][1:-11]
		if codigoAntiguo in codigo:
			codigoNuevo = line[0]
			break
	return codigoNuevo

