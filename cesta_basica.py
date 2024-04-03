
from geneticEDIT import *   #importa as funções executadas no algoritmo genético.

A = '1.arroz'
B = '2.feijão'
C = '3.café'
D = '4.leite'
E = '5.macarrão'          # descrimina cada item possível da cesta básica .
F = '6.óleo'
G = '7.açúcar'
H = '8.farinha'
I = '9.biscoito'
J = '10.chocolate'

#LISTA COMPLETA
listaItens = [A, B, C, D, E, F, G, H, I, J]
listaValores = [[25], [25], [15], [15], [10], [10], [5], [5], [25], [50]]       # define cada valor de cada item.
listaCompleta = []



valor_maximo = 150                      # valor máximo da cesta básica.
n_de_cromossomos = 100                  # número de cromossomos/ indíviduos por geração.
geracoes = 50                           # número de gerações.
tamanho_da_lista = len(listaValores)    # tamanho da lista item/valor.


#POPULAÇÃO
populacao = population(n_de_cromossomos, tamanho_da_lista)  #gera população aleatória.
historico_de_fitness = [media_fitness(populacao, valor_maximo, listaValores)] #atribuição de valor e calculo a média de pontuação da geração, e armazena no histórico.
for i in range(geracoes):
    populacao = evolucao(populacao, valor_maximo, listaValores, n_de_cromossomos) # capta os indivíduos e providencia a nova geração.
    historico_de_fitness.append(media_fitness(populacao, valor_maximo, listaValores)) # atribui valor para a nova geração e armazena no histórico, até finalizar.



for indice,dados in enumerate(historico_de_fitness):
   print ("Geracao: ", indice," | Media de valor da cesta básica: R$", dados)  # exibe as gerações 

print("\nValor máximo:  R$",valor_maximo,"\n\nItens disponíveis:")
for indice,i, in enumerate(listaValores) :                                  # exibe valor máximo, itens disponíveis e valores 
        print("Item ",indice+1,":| R$",i)

for i in range(10):
    listagem=(listaItens[i],listaValores[i])
    listaCompleta.append(listagem)
print(f'\nLista completa:\n\n{listaCompleta}\n')        # exibe a listagem dos itens possíveis para a cesta básica, associando cada item ao seu valor.
    
print("\nExemplos de boas solucoes: ")                  # exibe as cinco melhores soluções
for i in range(5):
    print(populacao[i])