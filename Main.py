import sys

########################################### Descripción del proyecto: ###########################################
#   Programa en Python que realiza diversas operaciones al recibir un texto.
#   Operaciones a realizar:
#       - Mostrar una estadistica del texto, como por ejemplo cantidad de palabras, espacios, entre otras.
#       - Buscar una palabra.
#       - Reemplazar una palabra existente, por otra a ingresar.
#
#   Autores:
#       - Victor Gatica (https://github.com/victorex)
#       - Nicolas Aburto (https://github.com/NicolasAburto)
#       - Felipe Valentin (https://github.com/fvalentin1)
#
#   Licencia:
#       - Abril 2022. Apache 2.0.
#
#################################################################################################################


#Capturar párametro de entrada
entrada = sys.argv[1]
Libro = "Libros_txt_utf-8/"+ entrada + ".txt"

# INICIO PROGRAMA
f=open(Libro ,"rt",encoding="UTF-8")
linea  = f.readline()
texto = f.read()
f.seek(0,0)


######################################################## FUNCION 1 ########################################################
def EspaciosBlancos(linea, CountPalabrasEspBlanco):
    # Cuenta el número de caracteres con espacios
   
    for i in linea:
       
        if i != "\n":
            CountPalabrasEspBlanco += 1

    return CountPalabrasEspBlanco

def SinEspaciosBlancos(linea, CountPalabrasSinEspBlanco):
    # Cuenta el número de caracteres sin espacios
   
    for i in linea:
       
        if i != " " and i != "\n":
            CountPalabrasSinEspBlanco += 1
           
    return CountPalabrasSinEspBlanco

#Definir diccionario como una variable "Diccionario"
diccionario = dict()

Count = 0
CountPalabras = 0
CountPalabrasEspBlanco = 0
CountPalabrasSinEspBlanco = 0

# Leer cada linea de texto hasta el final, y contar las lineas y palabras que tenga
while linea:
    Count += 1
    CountPalabras += len(linea.split())
    CountPalabrasEspBlanco = EspaciosBlancos(linea, CountPalabrasEspBlanco)
    CountPalabrasSinEspBlanco = SinEspaciosBlancos(linea, CountPalabrasSinEspBlanco)
   
    #Guarda la lista de palabras en un diccionario
    palabras = list(linea.split())
    for p in palabras:
        diccionario[p] = diccionario.get(p,0) + 1

    linea = f.readline()

# Palabras no repetidas
PalabrasNoRepeat = list(diccionario.values())

f.close()

######################################################## FUNCION 2 ########################################################

def funBuscarPalabra(d,p):
   #Buscar una palabra en un diccionario y las veces que esta repetida.
   try:
      Found = p in d
      Cantidad = d[p]  
   except LookupError:  
      #Error de key no encontrada
      Found = False
      Cantidad = 0  

   return Found, Cantidad

#Separar texto en palabras y guardarlo en una lista
palabras = list(texto.split())

#Guarda la lista de palabras en un diccionario
diccionario2 = dict()
for p in palabras:
   diccionario2[p] = diccionario2.get(p,0) + 1


######################################################## FUNCION 3 ########################################################

def funReemplazarPalabra(t):
   #Buscar una palabra en un diccionario y las veces que esta repetida.
   p1 = input('Palabra a reemplazar: ')
   while texto.find(p1) == -1:
      print('Palabra no encontrada en el texto, vuelva a intentar')
      p1 = input('Palabra a reemplazar: ')
   p2 = input('Palabra por la cual reemplazar: ')

   try:
      t = t.replace(p1, p2)
   except LookupError:  
      #Error palabra no encontrada
      0

   return t 

###################################################### Fin funciones ######################################################


#Menú

var = True
while var:
    print("Elija una operacion a realizar con el documento")
    print()
    print("1. Mostrar estadistica")
    print("2. Buscar una palabra")
    print("3. Reemplazar una palabra")
    print("4. Cerrar el programa")
    opcion = input("Opción: ")
    
    try:
        opcion = int(opcion)
        if opcion > 4 or opcion < 1:
            print("Opcion Inválida")
            print()
            print("-----------------")
        else:
            if opcion == 1:
                print()
                print("Estadisticas del documento:")
                print()
                
                print("Número de lineas: " + str(Count))
                print("Número de palabras: " + str(CountPalabras))
                print("Número de palabras no repetidas: " + str(PalabrasNoRepeat.count(1)))
                print("Número de caracteres con espacio: " + str(CountPalabrasEspBlanco))
                print("Número de caracteres sin espacio: " + str(CountPalabrasSinEspBlanco))
                
                print()
                print("-----------------")

            elif opcion == 2:
                print()
                print("Busqueda de una palabra")
                print()

                palabraB = input('Palabra a buscar: ')
                busquedaP = funBuscarPalabra(diccionario2, palabraB)
                if busquedaP[0]== True:
                    print (f'Se ha encontrado la palabra "{palabraB}" {busquedaP[1]} veces en el texto.')
                else:
                    print (f'No se ha encontrado la palabra "{palabraB}" en el texto.')

                print()
                print("-----------------")

            elif opcion == 3:
                print()
                print("Reemplazar una palabra")
                print()

                textoR = funReemplazarPalabra(texto)
                f.close()
                LibroReemplazo = "Libros_txt_utf-8/"+ entrada + " reemplazado.txt"
                f2 = open(LibroReemplazo, 'wt', encoding='utf-8')
                f2.write(textoR)

                f2.close()

                print()
                print(f"Palabra reemplazada y texto guardado en el archivo: '{entrada} reemplazado.txt'")

                print()
                print("-----------------")

            elif opcion == 4:
                print("Programa finalizado")
                var = False
    except:
        print()
        print("Ingrese un número entero, porfavor")
        print()
        print("-----------------")
