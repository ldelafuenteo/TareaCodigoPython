'''
Programa que crea un archivo y añade números dependiendo de la cuenta máxima.
Lolyna de la Fuente A01194774 
Creado el 18 de marzo del 2021
'''

#Importamos librería
import time

#Declaramos e imprimos variables
nombre_archivo = input("Teclea el nombre del archivo:")

print("Nombre del Archivo:",nombre_archivo)

cuenta_max = int(input("Cuenta máxima:")) #La variable cuenta_max determina el número de veces que el ciclo correrá

print("Cuenta máxima:",cuenta_max)

#Agregamos nuestra variable iterable i y la comenzamos en 0
i = 0

#Declaramos el ciclo
while i <= cuenta_max: #Establece que mientras nuestra variable iterable sea menor a la cuenta máxima puede seguir el ciclo

    modifica_archivo = open(nombre_archivo, "a") #Se abre el archivo

    time.sleep(1)

    modifica_archivo.write(str(i)) #Se agrega el número actual de la variable i

    modifica_archivo.write("\n")

    modifica_archivo.close() #Se cierra el archivo

    i += 1 #Se suma uno a nuestra variable iterable cada ciclo


#Se abre el archivo cuando se acaba el ciclo y se lee

archivo_final = open(nombre_archivo, "r")

print(archivo_final.read())

archivo_final.close() #Se cierra el archivo final
