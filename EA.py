from reproduction import *
from selection import *
import matplotlib.pyplot as plt

#main EA algo

# EA Parameters
Population_no = 30
Offspring_each_gen = 10
Total_generations = 100
Mutation_rate = 0.5
Data_type = 0
Agent_size = 194
Iterations = 10

class EA:
    Population: list
    Dataset: Data

    def __init__(self):
        global Agent_size
        self.Population = []
        self.Dataset = Data(Data_type)

        if Data_type == 1: Agent_size = self.Dataset.total_agents
       
        for _ in range(Population_no):
            self.Population.append( Agent(dataset = self.Dataset, size = Agent_size) )

    def generate_offspring(self):        
        # Generate offsprings
        
        # Random
        # parents = selection.random(self.Population, Offspring_each_gen)

        # Truncation
        parents = selection.truncation(self.Population, 0, Offspring_each_gen)

        # Fitness Proportional
        # parents = selection.fitness_proportional(self.Population, Offspring_each_gen)

        # Binary Tournament
        # parents = selection.binary_tournament(self.Population, Offspring_each_gen)

        # Rank Based Selection
        # parents = selection.rank_based(self.Population, Offspring_each_gen)

        for i in range(0, Offspring_each_gen, 2):
            
            parent_1, parent_2 = parents[i], parents[i+1]
            
            # Create child
            child_1, child_2 = reproduction.crossover(self.Dataset, Agent_size, parent_1, parent_2)
            reproduction.mutation(child_1, Agent_size, dataset=self.Dataset)
            reproduction.mutation(child_2, Agent_size, self.Dataset)

            # Add child to Population
            self.Population.append(child_1); self.Population.append(child_2)


    def kill_agents(self):
        # Kill agents

        # Random
        # agents_to_die = selection.random(self.Population, len(self.Population) - Population_no)

        # Truncation
        agents_to_die = selection.truncation(self.Population, Population_no, len(self.Population))

        # Fitness Proportional
        # agents_to_die = selection.fitness_proportional(self.Population, Offspring_each_gen)

        # Binary Tournament
        # agents_to_die = selection.binary_tournament(self.Population, Offspring_each_gen)

        # Rank Based Selection
        # agents_to_die = selection.rank_based(self.Population, Offspring_each_gen)

        for i in agents_to_die:
            self.Population.remove(i)

    def best_fitness(self):
        # Find current best fitness
        best_fitness = float("inf")
        for i in self.Population:
            best_fitness = min(best_fitness, i.fitness)
        
        if self.Dataset.data_type == 0:
            return best_fitness
        elif self.Dataset.data_type == 1:
            return 1/best_fitness

    def average_fitness(self):
        # Find current average fitness
        average_fitness = 0
        for i in self.Population:
            average_fitness += i.fitness
        average_fitness /= len(self.Population)
        
        if self.Dataset.data_type == 0:
            return average_fitness
        elif self.Dataset.data_type == 1:
            return 1/average_fitness
        
average_best_fitness = [[] for i in range(Total_generations)]
average_average_fitness = [[] for i in range(Total_generations)]

for _ in range(Iterations):
    Evol_Algo = EA()

    for j in range(Total_generations):
        Evol_Algo.generate_offspring()
        Evol_Algo.kill_agents()
        average_average_fitness[j].append(Evol_Algo.average_fitness())
        average_best_fitness[j].append(Evol_Algo.best_fitness())        

    del Evol_Algo

for i in range(Total_generations):
    average_best_fitness[i] = sum(average_best_fitness[i])/len(average_best_fitness[i])
    average_average_fitness[i] = sum(average_average_fitness[i])/len(average_average_fitness[i])

plt.ylabel('Fitness')
plt.xlabel('Generation No.')
plt.plot(average_average_fitness, label="Average Fitness")
plt.plot(average_best_fitness, label="Best Fitness")
plt.legend()
plt.show()