"""Practica 7"""
num1=int(input("Introduce un numero: "))
num2=int(input("Introduce un numero mayor que "+str(num1)+": "))
while num2>num1:
    num1=num2
    num2=int(input("Escriba un numero mayor que "+str(num1)+": "))
print()
print(num2, "no es mayor que",str(num1))
