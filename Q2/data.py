from PIL import Image, ImageDraw
import numpy
import functools
import operator

#mona_lisa_reference.jpg
class Data:

    def __init__(self, data_type: int, path:str):
        self.data_type = data_type
        self.total_agents = -1

        #open image and store as numpy array
        image = Image.open(path).convert('L')
        img_data = numpy.asarray(image)
        
        #store converted pixel data into array
        self.width, self.height = image.size
        self.orig_img = self.image_to_chromo(img_data)

        # self.agent_size = len(self.orig_img)


    #convert image data to a 1D vector
    def image_to_chromo(self, img_arr):
        chromosome = numpy.reshape(a=img_arr,\
             newshape=(functools.reduce(operator.mul, img_arr.shape)))
        return chromosome
    
    #convert 1D vector to image
    def chromo_to_image(self, chromosome):
        img_arr = numpy.reshape(a=chromosome, newshape=self.orig_shape)
        return img_arr


    def fitness_calc(self, m_agent):
        #difference between current iteration and target
        
        temp_arr = numpy.asarray(m_agent.img)
        current_chromosomes = self.image_to_chromo(temp_arr)
        
        fitness = numpy.mean(numpy.abs(self.orig_img - current_chromosomes))
        return fitness

# data = Data(0, 'mona_lisa_reference.jpg')
# print(data.nodes)