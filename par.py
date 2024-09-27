
def es_par(num):
    return num%2==0

def main():
    num = int(input('Ingrese numero para evaluar paridad: '))

    if es_par(num):
        print('el numero es par')
    else:
        print('el numero no es par')

main()
