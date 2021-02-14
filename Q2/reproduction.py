from agent import *

#crossover and mutation
class reproduction:

    @staticmethod
    def crossover(dataset: Data, agent_size: int, parent1: Agent, parent2: Agent):
        len_parent1 = len(parent1.chromosomes)
        len_parent2 = len(parent2.chromosomes)
        if len_parent1 == 0 or len_parent2 == 0:
           print(0)
       

        min_size = min(len_parent1, len_parent2)

        
        point1 = random.randint(0, min_size)
        point2 = random.randint(0, min_size)
        point1, point2 = min(point1, point2), max(point1, point2)

        #parent pointers
        p1_ptr, p2_ptr = 0, 0 

        #same length as parents we will iterate on
        chromosomes_1 = [-1] * point1 + parent2.chromosomes[point1:point2] + [-1] * (len_parent1 - point2)
        chromosomes_2 = [-1] * point1 + parent1.chromosomes[point1:point2] + [-1] * (len_parent2 - point2)

        
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


        while p1_ptr < len_parent1 and c1_ptr < len_parent1 and not skip_p1:
            tmp = parent1.chromosomes[p1_ptr]
            
            if tmp not in chromosomes_1:
                chromosomes_1[c1_ptr] = tmp
                c1_ptr += 1
                
                #when pointer reaches copied section
                if not skipped and c1_ptr >= point1:
                    c1_ptr = point2
                    skipped = True

            else:
                counter +=1

            p1_ptr = (p1_ptr + 1)

        skipped = False


        while p2_ptr < len_parent2 and c2_ptr < len_parent2 and not skip_p2:

            tmp = parent2.chromosomes[p2_ptr]
            
            if tmp not in chromosomes_2:
                chromosomes_2[c2_ptr] = tmp
                c2_ptr += 1

                
                #when pointer reaches copied section
                if not skipped and c2_ptr >= point1:
                    c2_ptr = point2
                    skipped = True

            else:
                counter +=1

            p2_ptr = (p2_ptr + 1)

        if c1_ptr < 2 or c2_ptr <2:
            print(1)
        

        c1_chromo = chromosomes_1[:c1_ptr]
        c2_chromo = chromosomes_2[:c2_ptr]


        reproduction.mutation(c1_chromo, agent_size, dataset)
        reproduction.mutation(c2_chromo, agent_size, dataset)
        m_agent = Agent(dataset = dataset, chromosomes = c1_chromo), Agent(dataset = dataset, chromosomes = c2_chromo)


        return m_agent


    @staticmethod
    def mutation(child: "list[Polygon]", agent_size: int, dataset: Data) -> None:
        if random.randint(1,10) <= 5:
            point1 = random.randint(0, len(child)-1)

            pts_lst = []
            gene_orig = (random.randint(0, dataset.width), random.randint(0, dataset.height)) # (x, y)
            pts_lst.append(gene_orig)
            
            for i in range(2):
                gene = (gene_orig[0] + random.randint(-15, 15), gene_orig[1] + random.randint(-15, 15))
                pts_lst.append(gene)

            # color = f"#{random.randrange(0x1000000):06x}"
            color = tuple(numpy.random.choice(range(256), size=1))

            new_poly = Polygon(pts_lst, color)

            child[point1] = new_poly



