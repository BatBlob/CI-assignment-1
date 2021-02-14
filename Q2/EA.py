from reproduction import *
from selection import *

#main EA algo

# EA Parameters
Population_no = 30
Offspring_each_gen = 10
Total_generations = 2000
Mutation_rate = 0.5
Data_type = 0
Agent_size = 500

class EA:
    Population: list
    Dataset: Data

    def __init__(self):
        global Agent_size
        self.Population = []
        self.Dataset = Data(Data_type, 'mona_lisa_reference.jpg')

        # if Data_type == 1: Agent_size = self.Dataset.total_agents
        # Agent_size = self.Dataset.agent_size

        for _ in range(Population_no):
            self.Population.append( Agent(dataset = self.Dataset, size = Agent_size) )

    def generate_offspring(self):
        # Generate offsprings
        for i in range(0, Offspring_each_gen, 2):
            # Random
            # parent_1, parent_2 = selection.random(self.Population, 2)

            # Truncation
            # parent_1, parent_2 = selection.truncation(self.Population, i, i+2)
            # parent_1, parent_2 = selection.truncation(self.Population, 0, 2)

            # Fitness Proportional
            # parent_1, parent_2 = selection.fitness_proportional(self.Population, 2)

            # Binary Tournament
            parent_1, parent_2 = selection.binary_tournament(self.Population, 2)

            # Rank Based Selection
            # parent_1, parent_2 = selection.rank_based(self.Population, 2)

            # Create child
            child_1, child_2 = reproduction.crossover(self.Dataset, Agent_size, parent_1, parent_2)
            # reproduction.mutation(child_1, Agent_size, dataset=self.Dataset)
            # reproduction.mutation(child_2, Agent_size, self.Dataset)


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

        
        
Evol_Algo = EA()

# a = float("inf")
# for i in Evol_Algo.Population:
#     a = min(i.fitness, a)
# print(a)

for x in range(Total_generations):
    Evol_Algo.generate_offspring()
    Evol_Algo.kill_agents()
    if x % 50 == 0:
        print(x)
        a = float("inf")
        j = -1
        for i in Evol_Algo.Population:
            if a > i.fitness:
                a = i.fitness
                j = i
        string= 'my_img'+str(x)+'.jpg'
        j.img.save(string)


# print(Evol_Algo.Population[-4].fitness)
# print(sorted(Evol_Algo.Population, key=lambda x: x.fitness)[0])

# for i in Evol_Algo.Population:
#     print(i.fitness)

a = float("inf")
j = -1
for i in Evol_Algo.Population:
    if a > i.fitness:
        a = i.fitness
        j = i

j.img.show()

print(a)
print(1/a)

# print(len(Evol_Algo.Population))