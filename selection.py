from os import stat
from agent import *

#selection procedures
class selection:
    @staticmethod
    def random(Population: list, number_of_agents: int) -> list:
        random_agents = []
        while len(random_agents) < number_of_agents:
            random_no = random.randint(0, len(Population)-1)
            if Population[random_no] not in random_agents:
                random_agents.append(Population[random_no])
        return random_agents
        
    
    @staticmethod
    def truncation(Population: list,  start: int, end: int) -> list:
        return sorted(Population, key=lambda x: x.fitness)[start:end]

    @staticmethod
    def fitness_proportional(Population: list, number_of_agents: int) -> list:
        fitness_sum = 0
        for agent in Population:
            fitness_sum += agent.fitness
        sorted_population = sorted(Population, key=lambda x: x.fitness, reverse=True)
        probability = []
        previous_prob = 0
        for agent in sorted_population:
            probability.append(previous_prob+(agent.fitness/fitness_sum))
        
        selected_agents = []

        while len(selected_agents) < number_of_agents:
            random_no = random.random()
            for i in range(len(probability)):
                if probability[i] > random_no:
                    if sorted_population[i] not in selected_agents:
                        selected_agents.append(sorted_population[i])
                        break
        
        return selected_agents
            
    @staticmethod
    def binary_tournament(Population: list, number_of_agents: int):
        selected_agents = []
        while len(selected_agents) < number_of_agents:
            agent_1 = random.randint(0, len(Population)-1)
            agent_2 = random.randint(0, len(Population)-1)

            if agent_1 != agent_2:
                winner_agent = min(Population[agent_1], Population[agent_2], key = lambda x: x.fitness)

                if winner_agent not in selected_agents:
                    selected_agents.append(winner_agent)
        
        return selected_agents
    
    @staticmethod
    def rank_based(Population: list, number_of_agents: int):
        ranks = [x for x in range(1,len(Population)+1)]
        rank_sum = (len(Population)*(len(Population)+1))/2
        sorted_population = sorted(Population, key=lambda x: x.fitness, reverse=True)

        probability = []
        previous_prob = 0
        for i in range(1, len(Population)+1):
            probability.append(previous_prob+(i/rank_sum))
        
        selected_agents = []

        while len(selected_agents) < number_of_agents:
            random_no = random.random()
            for i in range(len(probability)):
                if probability[i] > random_no:
                    if sorted_population[i] not in selected_agents:
                        selected_agents.append(sorted_population[i])
                        break
        
        return selected_agents