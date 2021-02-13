from data import *
import random

class Agent:
    chromosomes: list
    fitness: int

    def __init__(self, dataset: Data, chromosomes: list = False, size: int = False):
        self.fitness = 0
        self.chromosomes = []

        if chromosomes:
            self.chromosomes = chromosomes[:]
            if dataset.data_type == 0:
                for i in range(1, len(dataset.nodes)-1):
                    self.fitness += dataset.fitness_calc(self.chromosomes[i-1], self.chromosomes[i])
            else:
                self.fitness = dataset.fitness_calc(iter=self.chromosomes)
                self.weight = dataset.weight_cal(self.chromosomes)
        else:
            if dataset.data_type == 0:
                while len(self.chromosomes) < size:
                    node = random.randint(1, size)

                    if node not in self.chromosomes:
                        self.chromosomes.append(node)

                        if len(self.chromosomes) > 2:
                            self.fitness += dataset.fitness_calc(self.chromosomes[-2], self.chromosomes[-1])

            elif dataset.data_type == 1:
                self.weight = 0
                blacklist = set()

                stop_flag = False
                while len(self.chromosomes) < size and not stop_flag:
                    node = random.randint(1, size)

                    if node not in self.chromosomes:
                        current_weight = dataset.nodes[node][1]
                        #if exceeds weight limit, blacklist node
                        if current_weight + self.weight > dataset.max_cap:
                            blacklist.add(node)
                        else:
                            self.chromosomes.append(node)
                            self.weight += current_weight
                        
                        #all nodes traversed
                        if len(blacklist) + len(self.chromosomes) == size:
                            stop_flag = True

                for gene in self.chromosomes:
                    self.fitness += dataset.nodes[gene][0]
                    

                     
