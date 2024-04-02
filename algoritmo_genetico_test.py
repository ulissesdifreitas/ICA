import random

def fitness(individual, items, max_weight):
    weight, value = 0, 0
    for i in range(len(individual)):
        if individual[i] == 1:
            weight += items[i][0]
            value += items[i][1]
    if weight > max_weight:
        return 0
    return value

def selection(population, items, max_weight):
    return random.choices(
        population,
        weights=[fitness(individual, items, max_weight) for individual in population],
        k=len(population))

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1)-2)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutation(individual):
    mutation_point = random.randint(0, len(individual)-1)
    individual[mutation_point] = 1 if individual[mutation_point] == 0 else 0

def genetic_algorithm(items, max_weight, population_size, generations):
    population = [random.choices([0, 1], k=len(items)) for _ in range(population_size)]
    for _ in range(generations):
        population = selection(population, items, max_weight)
        for i in range(0, len(population), 2):
            if len(population) > i+1:
                population[i], population[i+1] = crossover(population[i], population[i+1])
                mutation(population[i])
                mutation(population[i+1])
    return max(population, key=lambda individual: fitness(individual, items, max_weight))

# Exemplo de uso
items = [(10, 60), (20, 100), (30, 120)]  # (peso, valor)
max_weight = 50
population_size = 100
generations = 500

best_individual = genetic_algorithm(items, max_weight, population_size, generations)
print("Melhor indivíduo: ", best_individual)
print("Valor total: ", fitness(best_individual, items, max_weight))

"""
Este código cria uma população de indivíduos, onde cada indivíduo é uma solução potencial para o problema (uma lista de 0s e 1s, onde 1 significa que o item correspondente é incluído na mochila). A função de fitness avalia o valor total dos itens na mochila, desde que o peso total não exceda o peso máximo. A seleção é feita com base na aptidão, o cruzamento é feito trocando partes dos indivíduos e a mutação é feita invertendo um bit aleatório. O algoritmo retorna o melhor indivíduo após um número fixo de gerações.
"""
