from random import random
from agent import *

#selection procedures
class selection:
    @staticmethod
    def random(Population: list, number_of_agents: int) -> list:
        random_agents = []
        while len(random_agents) < number_of_agents:
            random_no = randint(0, len(Population)-1)
            if Population[random_no] not in random_agents:
                random_agents.append(Population[random_no])
        return random_agents
        
    
    @staticmethod
    def truncation(Population: list,  start: int, end: int) -> Agent:
        return sorted(Population, key=lambda x: x.fitness)[start:end]