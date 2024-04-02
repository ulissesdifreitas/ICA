
from geneticEDIT import *

A = 'arroz'
B = 'feijão'
C = 'café'
D = 'leite'
E = 'macarrão'
F = 'óleo'
G = 'açúcar'
H = 'farinha'
I = 'biscoito'
J = 'chocolate'

#EXIBINDO LISTA COMPLETA
listaItens = [A, B, C, D, E, F, G, H, I, J]
listaValores = [[25], [25], [15], [15], [10], [10], [5], [5], [25], [25]]
listaCompleta = []

for i in range(10):
    listagem=(listaItens[i],listaValores[i])
    listaCompleta.append(listagem)
print(f'\nLista completa:\n\n{listaCompleta}\n')


valor_maximo = 150
n_de_cromossomos = 100
geracoes = 50
tamanho_da_lista = len(listaValores)


#POPULAÇÃO
populacao = population(n_de_cromossomos, tamanho_da_lista)
historico_de_fitness = [media_fitness(populacao, valor_maximo, listaValores)]
for i in range(geracoes):
    populacao = evolve(populacao, valor_maximo, listaValores, n_de_cromossomos)
    historico_de_fitness.append(media_fitness(populacao, valor_maximo, listaValores))



for indice,dados in enumerate(historico_de_fitness):
   print ("Geracao: ", indice," | Media de valor na mochila: R$", dados)

print("\nValor máximo:  R$",valor_maximo,"\n\nItens disponíveis:")
for indice,i, in enumerate(listaValores) : 
        print("Item ",indice+1,":| R$",i)
    
print("\nExemplos de boas solucoes: ")
for i in range(5):
    print(populacao[i])