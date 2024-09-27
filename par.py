LIMITE_VALIDACION = 0

def es_par(num):
    return num%2==0

def es_valido(num):
    return num > LIMITE_VALIDACION

def solicitar_numero():
    num = int(input('Ingrese numero positivo para evaluar paridad: '))
    while not es_valido(num):
        print('Ingreso invalido')
        num = int(input('Ingrese numero positivo para evaluar paridad: '))
    return num

def main():
    num = solicitar_numero()

    if es_par(num):
        print('el numero es par')
    else:
        print('el numero no es par')

main()
