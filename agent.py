from data import *
from random import randint

class Agent:
    chromosomes: list = []
    fitness: int = -1

    def __init__(self, size: int, dataset: Data, chromosomes: list = False):
        if chromosomes:
            self.chromosomes = chromosomes[:]
        else:
            while len(self.chromosomes) < size:
                node = randint(0, size-1)

                if node not in self.chromosomes:
                    self.chromosomes.append(node)

                    if len(self.chromosomes) > 2:
                        self.fitness += dataset.fitness_calc(self.chromosomes[-2], self.chromosomes[-1])