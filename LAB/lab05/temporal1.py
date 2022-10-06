# Tendencias e innovación en Tecnología Agrícola (TEA)
# Autor : Victoria Alejandra Zavala
# Fecha : 2022.09.29
# Editado : 2022.08.29 

cadena = "X-DSPAM-Confidence:0.8475"
inicio = cadena.find(":") + 1 #posición
final = len(cadena) #cantidad
numero = float(cadena[inicio:final])


print(type(numero))
