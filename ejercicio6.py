numero = float(input("ingrese un numero: "))

def positivo (numero):
    if numero >0 :
        return("True")
    elif numero <0 :
        return("False")

def primo (numero):
    if numero % 2 == 0:
        return("False")
    else:
        return("True")

print("¿El numero ingresado es positivo?: ",positivo(numero))

if (positivo(numero)) == "True":
    print ("¿El numero ingresado es primo?: ",primo(numero))
