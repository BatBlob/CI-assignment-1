from agent import *

#selection procedures
class selection:
    @staticmethod
    def random(Population: list):
        return (Population[randint(0, len(Population)-1)], Population[randint(0, len(Population)-1)])
    
    @staticmethod
    def truncation(Population: list):
        return sorted(Population, key=lambda x: x.fitness)[0:2]