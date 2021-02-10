from reproduction import *
from selection import *

#main EA algo

# EA Parameters
Population_no = 30
Offspring_each_gen = 10
Total_generations = 100
Mutation_rate = 0.5
Data_type = 0
Data_size = 194

class EA:
    Population = []
    Dataset: Data

    def __init__(self):
        self.Dataset = Data(Data_type)
        for _ in range(Population_no):
            self.Population.append( Agent(Data_size, self.Dataset) )    

        

Evol_Algo = EA()
print(Evol_Algo.Population)