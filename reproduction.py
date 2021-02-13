from agent import *

#crossover and mutation
class reproduction:
    @staticmethod
    def crossover(dataset: Data, agent_size: int, parent1: Agent, parent2: Agent):
        point1 = random.randint(0, agent_size-1)
        point2 = random.randint(0, agent_size-1)
        point1, point2 = min(point1, point2), max(point1, point2)

        #parent pointers
        p1_ptr, p2_ptr = 0, 0 

        chromosomes_1 = [-1] * point1 + parent2.chromosomes[point1:point2] + [-1] * (agent_size - point2)
        chromosomes_2 = [-1] * point1 + parent1.chromosomes[point1:point2] + [-1] * (agent_size - point2)
        
        #find first free slot in offspring chromosomes
        c1_ptr = chromosomes_1.index(-1)
        c2_ptr = chromosomes_2.index(-1)

        skipped = False
        counter = 0
        while p1_ptr < agent_size and c1_ptr < agent_size and chromosomes_1[-1] == -1 :
            tmp = parent1.chromosomes[p1_ptr]
            if tmp not in chromosomes_1:
                chromosomes_1[c1_ptr] = tmp
                c1_ptr += 1
                # print(sorted(chromosomes_1) == sorted(parent1.chromosomes))

                
                #when pointer reaches copied section
                if not skipped and c1_ptr >= point1:
                    c1_ptr = point2
                    skipped = True

            else:
                point3 = point2 - point1
                counter +=1

            p1_ptr = (p1_ptr + 1) % agent_size

        skipped = False
        while p2_ptr < agent_size and c2_ptr < agent_size and chromosomes_2[-1] == -1:
            tmp = parent2.chromosomes[p2_ptr]
            if tmp not in chromosomes_2:
                chromosomes_2[c2_ptr] = tmp
                c2_ptr += 1
                
                #when pointer reaches copied section
                if not skipped and c2_ptr >= point1:
                    c2_ptr = point2
                    skipped = True
            
            p2_ptr = (p2_ptr + 1) % agent_size


        return ( Agent(dataset = dataset, chromosomes = chromosomes_1), Agent(dataset = dataset, chromosomes = chromosomes_2) )

    @staticmethod
    def mutation(child: Agent, agent_size: int) -> None:
        if random.randint(1,10) <= 5:
            point1 = random.randint(0, agent_size-1)
            point2 = random.randint(0, agent_size-1)

            child.chromosomes[point1], child.chromosomes[point2] = child.chromosomes[point2], child.chromosomes[point1] 

