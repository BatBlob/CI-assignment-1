from reproduction import *
from selection import *

#main EA algo

# EA Parameters
Population_no = 30
Offspring_each_gen = 10
Total_generations = 100
Mutation_rate = 0.5
Data_type = 0
Agent_size = 194

class EA:
    Population: list
    Dataset: Data

    def __init__(self):
        self.Population = []
        self.Dataset = Data(Data_type)
        for _ in range(Population_no):
            self.Population.append( Agent(dataset = self.Dataset, size = Agent_size) )    

    def generate_offspring(self):
        # Select Parents
        # parent_1, parent_2 = selection.random(self.Population)
        parent_1, parent_2 = selection.truncation(self.Population)

        # Create child
        child_1, child_2 = reproduction.crossover(self.Population, self.Dataset, Agent_size, parent_1, parent_2)

        # Add child to Population
        self.Population.append(child_1); self.Population.append(child_2)
        
Evol_Algo = EA()
Evol_Algo.generate_offspring()
print(Evol_Algo.Population[-4].fitness)