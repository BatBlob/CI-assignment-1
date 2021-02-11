from agent import *

#selection procedures
class selection:
    @staticmethod
    def random(Population: list) -> Agent:
        return (Population[randint(0, len(Population)-1)], Population[randint(0, len(Population)-1)])
    
    @staticmethod
    def truncation(Population: list,  start: int, end: int) -> Agent:
        return sorted(Population, key=lambda x: x.fitness)[start:end]