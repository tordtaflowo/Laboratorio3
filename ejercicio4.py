import random
lanzamiento = random.randint(1,6)

adivinar = int(input("adivine el numero obtenido en un lanzamiento de dado: "))

print("el numero obtenido en el lanzamiento fue: ",lanzamiento)

if lanzamiento == adivinar :
    print("¡el numero que ingresaste fue correcto!")
elif lanzamiento != adivinar:
    print("¡el numero que ingresaste fue incorrecto!")

