from time import sleep
from interface import *
from arquivo import *

arq = 'bancodedados.txt'
if not arqExiste(arq):
    arqCriar(arq)

while True:
    resp = (menu(['Ver pessoas cadastradas',
                 'Cadastrar nova Pessoa', 'Sair do Sistema']))
    if resp == 1:
        arqLer(arq)
    elif resp == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        arqCadastrar(arq, nome, idade)
    elif resp == 3:
        opc3()
        break
    else:
        print('\033[0;31mERRO: Digite uma opção válida.\033[m')
    sleep(1.5)
