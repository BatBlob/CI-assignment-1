class Data:
    nodes: dict
    data_type: int      # 0 = TSP, 1 = knapsack

    def __init__(self, data_type: int):
        self.data_type = data_type
        self.nodes = {}

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

            for i in lines[7 : len(lines)-1]:
                node = i.split()
                self.nodes[int(node[0])] = ( float(node[1]), float(node[2]) )

    def fitness_calc(self, node1, node2):
        if self.data_type == 0:
            return ( ( self.nodes[node2][0] - self.nodes[node1][0] )**2 + ( self.nodes[node2][1] - self.nodes[node1][1] )**2 ) ** 0.5

        elif self.data_type == 1:
            pass