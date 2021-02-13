
class Data:
    nodes: dict
    data_type: int      # 0 = TSP, 1 = knapsack

    def __init__(self, data_type: int):
        self.data_type = data_type
        self.nodes = {}
        self.total_agents = -1

        if data_type == 0:
            f = open('tsp_datasets/Qatar_Dataset.tsp', 'r')
            lines = f.read().splitlines()
            f.close()

            for i in lines[7 : len(lines)-1]:
                node = i.split()
                self.nodes[int(node[0])] = ( float(node[1]), float(node[2]) )
        
        elif data_type == 1:
            f = open('knapsack_instances/low-dimensional/f2_l-d_kp_20_878', 'r')
            lines = f.read().splitlines()
            f.close()
            
            tmp_line = lines[0].split()
            
            #total items, knapsack max capacity
            self.total_agents, self.max_cap = int(tmp_line[0]), int(tmp_line[1] )

            for i in range(1, len(lines)):
                node = lines[i].split()
                # index : (profit, weight)
                self.nodes[i] = ( int(node[0]), int(node[1]) ) 

    def fitness_calc(self, node1=None, node2=None, iter=None):
        if self.data_type == 0:
            return ( ( self.nodes[node2][0] - self.nodes[node1][0] )**2 + \
                 ( self.nodes[node2][1] - self.nodes[node1][1] )**2 ) ** 0.5

        elif self.data_type == 1:
            total = 0
            for item in iter:
                total += self.nodes[item][0]
            return 1/total
    
    def weight_cal(self, iter):
        total = 0
        for item in iter:
            if item != -1:
                total += self.nodes[item][1]
        return total

# data = Data(1)
# print(data.nodes)