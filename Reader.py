import os

# ESTA FUNCION SACA EL NOMBRE DE LA CATEGORIA
def nombreDeCategoria(linea):
	a = linea.split() #Separa la linea de acuerdo a la ocurrencia de espacios	
	b = a[4:] #Copia los ultimos caracteres
	text = ""
	for item in b:
		text = text+" "+item
	text = text[1:]
	return text


# ESTA FUNCION CHEQUEA SI EL ARCHIVO CON NOMBRE DE CATEGORIA EXISTE
def fileExist(name):

	exist=os.path.exists(name+".txt")

	return exist


# ESTA FUNCION ESCRIBE UNA NUEVA LINEA EN UN DOCUMENTO O LO CREA

def escribeLinea(fileName,linea):
	oldFile = open(fileName+".txt","a")	
	oldFile.write(linea)
	print("Done")

#ESTA FUNCION QUITA CARACTERES PROHIBIDOS
def aceptable(texto):

	nuevoTexto = texto.replace("/","%")

	return nuevoTexto



# CAMPO DE EJECUCION DE CODIGO
file = open("puntosPasantias.txt",mode="r")

#Lee una linea completa
for line in file :

	#Copia los caracteres de la ultima columna y almacena el resultado de categoria
	nombre = aceptable(nombreDeCategoria(line))

	#Revisar si archivo con nombre de variable existe o no
	print(fileExist(nombre))
		
	escribeLinea(nombre,line)
	


#lines = file.readlines()
#print(lines[])

os.system("PAUSE")
