# Tendencias e innovación en Tecnología Agrícola (TEA)
# Autor : Victoria Alejandra Zavala
# Fecha : 2022.09.29
# Editado : 2022.08.29 

try:
    entrada = input("ingrese el nombre del archivo: ")
    archivo = open(entrada)
    for linea in archivo:
        print(linea.upper())
except:
     print("error, no existe el archivo")




#print(archivo.read())
#encoding: f_8 normalmente usado r read a applicate
#por cada línea en el archivo ,,entrada,"r", "names.text", "a", encoding="UTF-8"
    
