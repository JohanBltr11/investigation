import random

#parameters
POPULATION_SIZE = 100
INDIVIDUAL_SIZE = 10
ITERATIONS = 10 

#population

def create_indivual():
    temp = [random.randint(0,1) for i in range(INDIVIDUAL_SIZE)]
    return temp

def create_population():
    population = [create_indivual() for i in range(POPULATION_SIZE)]
    return population

#fitness - objective function

def fitness_function_maxones(individual: list) -> int:
    sum(individual)

#selection
def roullete(individual_1:list,individual_2:list)->list:
    fitness_1 = fitness_function_maxones(individual_1)
    fitness_2 = fitness_function_maxones(individual_2)
    break_point = fitness_1 / (fitness_1 + fitness_2)
    return individual_1 if random.random() < break_point else individual_2

def tournament_selection(population: list):
    ind_1 = random.choice(population)
    ind_2 = random.choice(population)
    ind_3 = random.choice(population)
    ind_4 = random.choice(population)

    semifinal_1 = roullete(ind_1, ind_2)
    semifinal_2 = roullete(ind_3, ind_4)
    

#genetic operators

def mutation_operator(individual: list)-> list:
    gen = random.randint(0, INDIVIDUAL_SIZE - 1)
    individual[gen] = 0 if individual[gen] == 1 else 1
    return individual

def crossover_operator(parent_1: list, parent_2: list) -> list:
    cut = random.randint(1, INDIVIDUAL_SIZE-1)
    offspring_1 = parent_1[:cut] + parent_2[cut:]
    offspring_2 = parent_2[cut:] + parent_1[:cut]
    return offspring_1, offspring_2


#replacement
def replacement():
    pass

if __name__ == '__main__':
    population = create_population()
    for i in range(ITERATIONS):
        parent_1 = tournament_selection(population)
        parent_2 = tournament_selection(population)
        parent_mutated_1 = mutation_operator(parent_1)
        parent_mutated_2 = mutation_operator(parent_2)}
        offspring_1, offspring_2 = crossover_operator(parent_mutated_1,parent_mutated_2)