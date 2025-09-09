from time import sleep


def leiaInt(frase=0):
    while True:
        try:
            num = int(input(frase))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print(
                '\n\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return num


def cabeçalho(txt):
    print('-' * 42)
    print(txt.center(42))
    print('-' * 42)


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print('-' * 42)
    opc = leiaInt('Opção desejada: ')
    return opc


def opc3():
    print('-' * 42)
    print(f'{'FINALIZANDO..... ':^42}')
    sleep(1)
    print()
    print(f'{'ATÉ LOGO!':^39}')
    print('-' * 42)
