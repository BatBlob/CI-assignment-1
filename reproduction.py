from agent import *

#crossover and mutation
class reproduction:

    @staticmethod
    def crossover(dataset: Data, agent_size: int, parent1: Agent, parent2: Agent):
        len_parent1 = len(parent1.chromosomes)
        len_parent2 = len(parent2.chromosomes)
        if len_parent1 == 0 or len_parent2 == 0:
           print(0)
       
        if dataset.data_type == 1:
            min_size = min(len_parent1, len_parent2)
        else:
            min_size = agent_size - 1
        
        point1 = random.randint(0, min_size)
        point2 = random.randint(0, min_size)
        point1, point2 = min(point1, point2), max(point1, point2)

        #parent pointers
        p1_ptr, p2_ptr = 0, 0 

        if dataset.data_type == 1:
            #same length as parents we will iterate on
            chromosomes_1 = [-1] * point1 + parent2.chromosomes[point1:point2] + [-1] * (len_parent1 - point2)
            chromosomes_2 = [-1] * point1 + parent1.chromosomes[point1:point2] + [-1] * (len_parent2 - point2)

        else:
            chromosomes_1 = [-1] * point1 + parent2.chromosomes[point1:point2] + [-1] * (agent_size - point2)
            chromosomes_2 = [-1] * point1 + parent1.chromosomes[point1:point2] + [-1] * (agent_size - point2)
        
        #find first free slot in offspring chromosomes
        skipped = False
        counter = 0
        
        skip_p1, skip_p2 = False, False

        if -1 not in chromosomes_1:
            skip_p1 = True
            c1_ptr = len_parent1
        else:
            c1_ptr = chromosomes_1.index(-1)

        if -1 not in chromosomes_2:
            skip_p2 = True
            c2_ptr = len_parent2
        else:
            c2_ptr = chromosomes_2.index(-1)

        
        if dataset.data_type == 1:
            blacklist = set()

            while p1_ptr < len_parent1 and c1_ptr < len_parent1 and not skip_p1:
                tmp = parent1.chromosomes[p1_ptr]
                current_weight = dataset.nodes[tmp][1]
                
                if tmp not in chromosomes_1:
                    if dataset.weight_cal(chromosomes_1) + current_weight <= dataset.max_cap:
                        chromosomes_1[c1_ptr] = tmp
                        c1_ptr += 1

                    
                    #when pointer reaches copied section
                    if not skipped and c1_ptr >= point1:
                        c1_ptr = point2
                        skipped = True

                else: #weight exceeded with current gene
                    counter +=1

                p1_ptr = (p1_ptr + 1)

            skipped = False


            while p2_ptr < len_parent2 and c2_ptr < len_parent2 and not skip_p2:

                tmp = parent2.chromosomes[p2_ptr]
                current_weight = dataset.nodes[tmp][1]
                
                if tmp not in chromosomes_2:
                    if dataset.weight_cal(chromosomes_2) + current_weight <= dataset.max_cap:
                        chromosomes_2[c2_ptr] = tmp
                        c2_ptr += 1

                    
                    #when pointer reaches copied section
                    if not skipped and c2_ptr >= point1:
                        c2_ptr = point2
                        skipped = True

                else: #weight exceeded with current gene
                    counter +=1

                p2_ptr = (p2_ptr + 1)

            if c1_ptr < 2 or c2_ptr <2:
                print(1)
            return ( Agent(dataset = dataset, chromosomes = chromosomes_1[:c1_ptr]), Agent(dataset = dataset, chromosomes = chromosomes_2[:c2_ptr]) )


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
    def mutation(child: Agent, agent_size: int, dataset: Data) -> None:
        if random.randint(1,10) <= 5:
            
            if dataset.data_type == 1:
                rand_idx = random.randint(0, len(child.chromosomes)-1) #gene to mutate
                rand_node = child.chromosomes[rand_idx]
                new_weight = child.weight - dataset.nodes[rand_node][1] #weight after rmv gene
                
                set1, set2 = set(dataset.nodes.keys()), set(child.chromosomes)
                list1 = list(set1 - set2)

                while len(list1) > 0:
                    new_gene = random.choice(list1)
                    list1.remove(new_gene)
                    if new_gene not in child.chromosomes:
                        current_weight = dataset.nodes[new_gene][1] #weight of rand gene
                        
                        if current_weight + new_weight <= dataset.max_cap:
                            child.chromosomes[rand_idx] = new_gene
                            break
                child.fitness = dataset.fitness_calc(iter = child.chromosomes)
                child.weight = dataset.weight_cal(child.chromosomes)


            elif dataset.data_type == 0:
            
            
                point1 = random.randint(0, agent_size-1)
                point2 = random.randint(0, agent_size-1)

                child.chromosomes[point1], child.chromosomes[point2] = child.chromosomes[point2], child.chromosomes[point1]

                for i in range(1, len(dataset.nodes)-1):
                    child.fitness += dataset.fitness_calc(child.chromosomes[i-1], child.chromosomes[i])

