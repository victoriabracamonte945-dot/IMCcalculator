print("Vamos a calcular tu IMC")
peso = float(input("Inserte su peso (en kilográmos): "))
altura = float(input("Inserte su altura (en metros): "))

IMC = float(peso/altura**2)

print("Su IMC es de", IMC)

if IMC<18.5:
    print("Usted tiene bajo peso")
elif 18.5 <= IMC < 24.9:
    print("Usted tiene peso normal")
elif 24.9 <= IMC < 29.9:
    print("Usted tiene sobrepeso")
else:
    print("Usted tiene obesidad")

print("Gracias por probar la calculadora :)")
input("Presione enter para salir...")