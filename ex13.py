import requests
import json

def lista_filmes(titulo):
    lista = []

    for i in range(1, 101):
        try:
            req = requests.get('https://www.omdbapi.com/?apikey=1a957694&s=' + titulo + '&type=movie&page=' + str(i))
            resposta = json.loads(req.text)
            if resposta['Response'] == 'False':
                break
            else:
                for filme in resposta['Search']:
                    titulo_atual = filme['Title']
                    ano = filme['Year']
                    string = titulo_atual + ' (' + ano +')'
                    lista.append(string)
        except:
            print('Conexao falhou')
    return lista

sair = False
while not sair:
    op = input('Pesquisa por um filme ou digite SAIR: ')
    if op == 'SAIR':
        sair = True
    else:
        lista_de_filmes = lista_filmes(op)
        print('Filmes encontrados', len(lista_de_filmes))
        for filme in lista_de_filmes:
            print(filme)