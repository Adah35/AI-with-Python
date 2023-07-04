import numpy as np


np.random.seed(0)

def create_data(points,classes):
    x = np.zeros((points*classes,2))
    y = np.zeros(points*classes,dtype='uint8')
    for class_number in range(classes):
        ix = range(points*classes,points*(classes+1))
        r = np.linspace(0.0,1,points)
        t = np.linspace(class_number*4,(class_number+1)*4,points) + np.random.rand(points)*0.2
        x[ix] = np.c_[r*np.sin(t*2.5),r*np.cos(t*2.5)]
        y[ix] = class_number
    return x,y

x,y = create_data(100,3)
print(x)