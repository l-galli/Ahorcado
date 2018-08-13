import random
import os
import webbrowser
from files import imagen

def imprimir(solucion, letras_adivinadas):
	l = len(solucion)
	for i in solucion:
		if i in letras_adivinadas:
			print(i, end='')
		else:
			print("-", end='')
	print("")
	print("")



def limpiar_sol(solucion):
	solucion = solucion[: -1]

	solucion = solucion.replace("á", "a")
	solucion = solucion.replace("é", "e")
	solucion = solucion.replace("í", "i")
	solucion = solucion.replace("ó", "o")
	solucion = solucion.replace("ú", "u")

	return solucion

def estado_actual(solucion, letras_adivinadas, letras_usadas, restantes_intentos):
	print("Estado actual: ")
	print("")
	imprimir(solucion, letras_adivinadas)
	print("Letras usadas: ")
	print(letras_usadas)
	if restantes_intentos > 0:
		print("Intentos restantes: %s" % restantes_intentos)
		print("")

def ahorcado():
	#Abre base de datos y crea una lista a partir de eso
	rae = open("files/rae", encoding="utf8")
	rae = rae.readlines()
	indice = random.randint(0, len(rae))
	solucion = ""
	
	#Busca una palabra de por lo menos 3 letras
	while len(solucion) < 3:
		solucion = rae[indice]
	
	#Quita acentos
	sol_acentuada = solucion
	sol_acentuada = sol_acentuada[: -1]
	solucion = limpiar_sol(solucion)
	
	#Cantidad de intentos es el doble de la palabra, y como máximo 7
	total_intentos = len(solucion) * 2
	if total_intentos > 7:
		total_intentos = 7

	#Inicializo las variables
	actual_intentos = 0
	restantes_intentos = total_intentos
	letras_adivinadas = []
	letras_usadas = []
	gano = False
	
	#Ciclo principal
	while actual_intentos < total_intentos:
		os.system('cls' if os.name == 'nt' else 'clear')
		estado_actual(solucion, letras_adivinadas, letras_usadas, restantes_intentos)
		respuesta = input("Que elegís ahora? ")
		print("")
		
		#Entrada mala 1
		if len(respuesta) != 1 or respuesta == " ":
			os.system('cls' if os.name == 'nt' else 'clear')
			print("Tiene que ser UNA letra")
			print("\n")
			nada = input("Enter para continuar")
			
			continue

		#Entrada mala 2
		if respuesta in letras_usadas:
			os.system('cls' if os.name == 'nt' else 'clear')
			print("Esa ya la usaste")
			print("\n")
			nada = input("Enter para continuar")
			
			continue


		letras_usadas.append(respuesta)
		
		#La letra pertenece a la palabra y no se usó
		if respuesta in solucion:
			letras_adivinadas.append(respuesta)
			i = 0
			letras_correctas = 0
			gano = True
			while i < len(solucion):
				j = 0
				esta = False
				while j < len(letras_adivinadas):
					esta = esta or solucion[i] == letras_adivinadas[j]
					j += 1
				gano = gano and esta
				i += 1
			if gano:
				break
			continue

		actual_intentos += 1
		restantes_intentos = total_intentos - actual_intentos

	#fuera ciclo

	os.system('cls' if os.name == 'nt' else 'clear')

	if gano:
		
		print("Ganaste, felicitaciones!")
		print("")
		imagen.dibujar()
	else:

		estado_actual(solucion, letras_adivinadas, letras_usadas, 0)
		print("")
		print("No te quedan más intentos")
		print("")
		
		arriesgue = input("Arriesgá una palabra, o presioná Enter para terminar ")
		gano = (solucion == arriesgue) 

		if gano:
			os.system('cls' if os.name == 'nt' else 'clear')
			print("Ganaste, felicitaciones!")
			print("")
			imagen.dibujar()
		else:
			os.system('cls' if os.name == 'nt' else 'clear')
			print("Perdiste")
			imagen.dibujar_perder()

	print("")
	print("La palabra era %s" % sol_acentuada)

	print("")
	res1 = input("Buscar definición de la palabra? [s/n] ")
	if res1 == "s":
		webbrowser.open('http://dle.rae.es/%s' % sol_acentuada)

	os.system('cls' if os.name == 'nt' else 'clear')
	
	res2 = input("Jugar de vuelta? [s/n] ")
	return res2


if __name__ == "__main__":

	os.system('cls' if os.name == 'nt' else 'clear')
	res2 = 's'
	while(res2 != 'n'):
		res2 = ahorcado()

	os.system('cls' if os.name == 'nt' else 'clear')


