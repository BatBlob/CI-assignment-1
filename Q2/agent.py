from data import *
import random
class Polygon:
    
    def __init__(self, points, color):
        self.points = points
        self.color = color 

    def __eq__(self, o: object) -> bool:
        if o == -1:
            return False
        
        if sorted(o.points, key=lambda x:x[0]) ==  sorted(self.points, key=lambda x:x[0])\
         and o.color == self.color:
            return True
        return False
        

class Agent:

    def __init__(self, dataset: Data, chromosomes: list = False, size: int = False):
        self.fitness:int = 0
        self.chromosomes: "list[Polygon]" = [] #list of polygons (x,y)
        self.img = Image.new("RGB", (dataset.width,dataset.height) )


        if chromosomes:
            self.chromosomes = chromosomes[:]

        else:
            
            while len(self.chromosomes) < size:
                pts_lst = []
                for i in range(3):
                    gene = (random.randint(0, dataset.width), random.randint(0, dataset.height)) # (x, y)
                    pts_lst.append(gene)

                # color = f"#{random.randrange(0x1000000):06x}"
                color = tuple(numpy.random.choice(range(256), size=3))
                self.chromosomes.append(Polygon(pts_lst, color))
            
        self.draw_polygons()
        self.fitness = dataset.fitness_calc(self)
                    
    def draw_polygons(self):
        
        draw = ImageDraw.Draw(self.img)
        
        for polygon in self.chromosomes:
            draw.polygon(polygon.points, polygon.color)


l1 = [(0,1), (2,3), (1, 4)]
l2 = [(0,1), (1, 4), (2,3)]
l3 = [(0,1), (1, 4), (2,2)]

color = 122
p1 = Polygon(l1, color)
p2 = Polygon(l2, color)
p3 = Polygon(l3, color)

my_l = [p1]


print(p1 in my_l)
print(p2 in my_l)
print(p3 in my_l)