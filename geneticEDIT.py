
from random import getrandbits, random, randint

#Cria um membro da população
def individual(tamanho_da_lista):
    return [getrandbits(1) for x in range(tamanho_da_lista)]

#Cria população
def population(n_de_individuos, tamanho_da_lista):
    return [individual(tamanho_da_lista) for x in range(n_de_individuos)]

#Avaliação de cada indivíduo, função de aptidão - É válido ou não
def fitness(individuo, valor_maximo, listaValores):
    valor_total = 0                                     # cada item que é armazenado na cesta recebe valor 1
    for indice, valorTotal in enumerate(individuo):
        valor_total += (individuo[indice] * listaValores[indice][0])
    
    if (valor_maximo - valorTotal) < 0:
        return -1 # retorna -1 no caso de valor excedido, invalidando o individuo
    return valor_total # individuo válido

def media_fitness(populacao, valor_maximo, listaValores): #leva em consideração apenas indivíduos válidos - faz a avaliação média da população
    somatorio = sum(fitness(x, valor_maximo, listaValores) for x in populacao if fitness(x, valor_maximo, listaValores) >= 0)
    return somatorio / (len(populacao) * 1.0)

def evolucao(populacao, valor_maximo, listaValores, n_de_cromossomos, mutate=0.1): 
    pais = [ [fitness(x, valor_maximo, listaValores), x] for x in populacao if fitness(x, valor_maximo, listaValores) >= 0]
    # avaliação do individuo e armazenamento do mesmo num vetor, levando em consideração a sua pontuação atribuída e o código genético do indivíduo
    pais.sort(reverse=True)

    # REPRODUÇÃO
    filhos = []
    while len(filhos) < n_de_cromossomos:
        macho, femea = selecao(pais)
        meio = len(macho) // 2
        filho = macho[:meio] + femea[meio:]
        filhos.append(filho)

    # MUTAÇÃO
    for individuo in filhos:
        if mutate > random():
            pos_to_mutate = randint(0, len(individuo)-1)
            if individuo[pos_to_mutate] == 1:
                individuo[pos_to_mutate] = 0
            else:
                individuo[pos_to_mutate] = 1

    return filhos

# SELEÇÃO
def selecao(pais): #seleciona um pai e uma mãe por método randômico
    def sortear(fitness_total, indice_a_ignorar=-1): #'indice_a_ignorar' garante que não vai selecionar o mesmo elemento
        """Monta roleta para realizar o sorteio"""
        roleta, acumulado, valor_sorteado = [], 0, random()

        if indice_a_ignorar!=-1: #Desconta do total, o valor que sera retirado da roleta
            fitness_total -= valores[0][indice_a_ignorar]

        for indice, i in enumerate(valores[0]):
            if indice_a_ignorar==indice: #ignora o valor ja utilizado na roleta, evita repetição e preferência na seleção
                continue
            acumulado += i
            roleta.append(acumulado/fitness_total)
            if roleta[-1] >= valor_sorteado:
                return indice
    
    valores = list(zip(*pais)) #cria 2 listas com os valores fitness e os cromossomos
    fitness_total = sum(valores[0])

    indice_pai = sortear(fitness_total) 
    indice_mae = sortear(fitness_total, indice_pai)

    pai = valores[1][indice_pai]
    mae = valores[1][indice_mae]
    
    return pai, mae