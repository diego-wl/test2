
def es_par(num):
    return num%2==0

def solicitar_numero():
    return int(input('Ingrese numero para evaluar paridad: '))

def main():
    num = solicitar_numero()

    if es_par(num):
        print('el numero es par')
    else:
        print('el numero no es par')

main()
