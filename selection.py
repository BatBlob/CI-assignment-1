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

        probability = []
        previous_prob = 0
        for agent in Population:
            probability.append(previous_prob+(agent.fitness/fitness_sum))
        
        selected_agents = []

        while len(selected_agents) < number_of_agents:
            random_no = random.random()
            for i in range(len(probability)):
                if probability[i] < random_no:
                    if Population[i] not in selected_agents:
                        selected_agents.append(Population[i])
                        break
        
        return selected_agents
            
         