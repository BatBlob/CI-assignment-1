from agent import *

#crossover and mutation
class reproduction:
    @staticmethod
    def crossover(Population: list, dataset: Data, agent_size: int, parent1: int, parent2: int):
        point1 = randint(0, agent_size-1)
        point2 = randint(0, agent_size-1)
        point1, point2 = min(point1, point2), max(point1, point2)

        chromosomes_1 = parent1.chromosomes[0:point1] + parent2.chromosomes[point1:point2] + parent1.chromosomes[point2:agent_size]
        chromosomes_2 = parent2.chromosomes[0:point1] + parent1.chromosomes[point1:point2] + parent2.chromosomes[point2:agent_size]
        
        return ( Agent(dataset = dataset, chromosomes = chromosomes_1), Agent(dataset = dataset, chromosomes = chromosomes_2) )

    @staticmethod
    def mutation(child: Agent, agent_size: int) -> None:
        if randint(1,10) <= 5:
            point1 = randint(0, agent_size-1)
            point2 = randint(0, agent_size-1)

            child.chromosomes[point1], child.chromosomes[point2] = child.chromosomes[point2], child.chromosomes[point1] 

