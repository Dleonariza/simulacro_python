saldo = 1000

def depositar(valor_deposito):
    if valor_deposito < 1:
        print("Valor depósito no válido.")
    else:
        valor_deposito += saldo
        return valor_deposito

def retirar(valor_retiro):
    if valor_retiro > saldo:
        print("Intenta retirar dinero mayor al saldo disponible.")
    elif valor_retiro < 0:
        print("Intenta retirar dinero en negativo.")
    else:
        valor = saldo - valor_retiro
        return valor

def menu():
    print(
"""
*** MENU ***
1. Consultar saldo
2. Depositar dinero
3. Retirar dinero
0. Salir
""")
    

def leerOpcion():
    opcion = input(">>>Opcion? ")
    while opcion < "0" or opcion > "3":
        print("--> Error. Opción no válida.")
        input("Presione enter para continuar ....")
        print("\n\n\n\n\n")
        menu()
        opcion = input(">>>Opcion? ")

    return int(opcion)


def opcion_consultar_saldo():
    print("\n\n\n 1. Consultar saldo")

    print("Su saldo es =", saldo)

def opcion_depositar_dinero():
    print("\n\n\n 2. Depositar saldo")

    deposito = int(input("\nIngrese el valor a depositar, mayor a 0: "))
    
    print("\nDeposito exitoso.", deposito, " $")
    return depositar(deposito)

def opcion_retirar_dinero():
    print("\n\n\n 2. Retirar dinero")

    retiro = int(input("\nIngrese el valor a retirar, mayor a 0: "))

    print("\nRetiro exitoso ", retiro, "$")
    return retirar(retiro)
    
### Programa principal
while True:
    menu()
    opcion = leerOpcion()
    match opcion:
        case 1:
            opcion_consultar_saldo()
        case 2:
            saldo = opcion_depositar_dinero()
        case 3:
            saldo = opcion_retirar_dinero()
        case 0:
            print("Gracias por ...")
            break

    input("Presione Enter para continuar...")
