#!/usr/bin/env python3

# Pedir al usuario que ingrese un número romano
numero_romano = input("Ingresa un número romano: ")

# Definir un diccionario que mapea los símbolos romanos a sus valores decimales
simbolos = {'I': 1,
           'V': 5,
           'X': 10,
           'L': 50,
           'C': 100,
           'D': 500,
           'M': 1000}

# Inicializar una variable para almacenar el resultado
resultado = 0

# Recorrer cada carácter en el número romano
for i in range(len(numero_romano)):
    # Verificar si el valor actual es mayor que el valor anterior
    if i > 0 and simbolos[numero_romano[i]] > simbolos[numero_romano[i - 1]]:
        # Restar dos veces el valor anterior para corregir el exceso sumado previamente
        resultado += simbolos[numero_romano[i]] - 2 * simbolos[numero_romano[i - 1]]
    else:
        # Sumar el valor del símbolo actual al resultado
        resultado += simbolos[numero_romano[i]]

# Imprimir el resultado
print(resultado)
