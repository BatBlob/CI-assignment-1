#main EA algo
def initialize():
    f = open('tsp_datasets/Qatar_Dataset.tsp', 'r')
    lines = f.read().splitlines()
    f.close()

    for i in lines: print(i)

initialize()