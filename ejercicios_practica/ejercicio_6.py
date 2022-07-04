# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicio de secuencias numéricas

# Pedir por consola dos números que representen el principio y fin de una
# secuencia numérica.
# Realizar un bucle "for" que recorra esa secuencia armada con "range"
# y cuante cuantos números son negativos y cuantos números son mayor o igual a cero
# Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
# sino que va hasta el anterior

inicio = int(input('Ingrese el primer número de la secuencia\n'))
fin = int(input('Ingrese el último número de la secuencia\n'))

cantidad_numeros_positivos = 0  # Inicializo el contador en 0
cantidad_numeros_negativos = 0
# for ... in range(....)
for i in range(inicio,fin+1):
    if i >= 0:
        cantidad_numeros_positivos += 1  
    else:
        cantidad_numeros_negativos += 1
        
# Imprimir el valor de la cantidad de números positivos y negativos
print("numeros negativos:",cantidad_numeros_negativos )
print("numeros positivos:",cantidad_numeros_positivos )


print("terminamos!")
