
#     RELU ACTIVATION FUNCTION

#     inputs = [0,2,3,4,2,1,4,5,-4]
# output = []
# for i in inputs:
#     if i > 0:
#         output.append(i)
#     elif i <= 0:
#         output.append(0)

# print(output)

import numpy as np
np.random.seed(0)

x = [
    [1,2,3,2.5],
    [2.0,5.0,-1.0,2.0],
    [1.5,2.7,3.3,0.8]      
]



class Layer_Dense:
    def __init__(self,n_inputs,n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs,n_neurons)
        self.biases = np.zeros((1,n_neurons))
    def forword(self,inputs):
        self.output = np.dot(inputs,self.weights) + self.biases

class Activation_Relu:
    def forward(self,inputs):
        self.output = np.maximum(0,inputs)    

layer1 = Layer_Dense(4,5)
activation1 = Activation_Relu()

layer1.forword(x)
activation1.forward(layer1.output)

# layer2 = Layer_Dense(5,2)
# layer2.forword(layer1.output)
print(activation1.output)

