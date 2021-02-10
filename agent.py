from data import *
from random import randint

class Agent:
    chromosomes: list
    fitness: int

    def __init__(self, dataset: Data, chromosomes: list = False, size: int = False):
        self.fitness = 0
        self.chromosomes = []

        if chromosomes:
            self.chromosomes = chromosomes[:]
            for i in range(1, 193):
                self.fitness += dataset.fitness_calc(self.chromosomes[i-1], self.chromosomes[i])
        else:
            while len(self.chromosomes) < size:
                node = randint(1, size)

                if node not in self.chromosomes:
                    self.chromosomes.append(node)

                    if len(self.chromosomes) > 2:
                        self.fitness += dataset.fitness_calc(self.chromosomes[-2], self.chromosomes[-1])
