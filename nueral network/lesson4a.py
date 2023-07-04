import numpy as np

#3 x 4 matrix
inputs = [
    [1,2,3,2.5],
    [2.0,5.0,-1.0,2.0],
    [1.5,2.7,3.3,0.8]      
]

# both inputs and weights have the same shape so the dot product won't work
# transpose either one of them
# so we will have a 3 x 4 and 4 x 3 matrix which the output will be a 3 x 3 matrix

# weights = np.transpose(weights) or np.array(weights).T

#3 x 4 matrix
###### LAYER 1
weights = [
    [0.2,0.8,-0.5,1.0],
    [0.5,0.91,0.26,-0.5],
    [0.1,0.4,-0.6,0.2]
]

biases = [2,3,0.5]

###### LAYER 2
weights2 = [
    [0.1,-0.14,0.5],
    [-0.5,0.21,-0.33],
    [-0.44,0.73,-0.13]
]


biases2 = [1,2,-0.5]


layer1_output = np.dot(inputs,np.array(weights).T) + biases
layer2_output = np.dot(layer1_output,np.array(weights2).T) + biases2

print(layer2_output)


