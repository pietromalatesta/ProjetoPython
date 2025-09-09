from interface import cabeçalho


def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def arqCriar(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def arqLer(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Ocorreu um erro ao ler o arquivo.')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dados = linha.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0]:<32}{dados[1]:>3} anos')
    finally:
        a.close()


def arqCadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro no cadastro dos dados.')
        else:
            print(f'Novo cadastro de {nome} feito com sucesso!')
            a.close()
