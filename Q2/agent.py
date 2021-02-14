from data import *
import random
class Polygon:
    
    def __init__(self, points, color):
        self.points = points
        self.color = color 


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
