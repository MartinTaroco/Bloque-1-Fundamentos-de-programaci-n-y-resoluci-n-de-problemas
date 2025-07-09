#Desafío 1: Suma de los primeros n números naturales
#Descripción: Escribe un algoritmo que calcule la suma de los primeros n números naturales.


def suma(n):     
  suma = 0       #Inicia en 0
  for i in range(n+1):   #Uso la función range que genera una secuencia de números iterables.
    suma += i    #Le agrega a la suma cada número natural iterado hasta el número n dado
  return suma    #Devuelve la suma final
    
    
resultado = suma(4)

print(resultado)
