

def main():
    num = int(input('Ingrese numero para evaluar paridad: '))
    es_par = num%2==0
    if es_par:
        print('el numero es par')
    else:
        print('el numero no es par')

main()
