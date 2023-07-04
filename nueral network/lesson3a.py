'''
 the dots product

 simplifying last session code from lesson 2

'''

input = [1,2,3,2.5]

weights = [
    [0.2,0.8,-0.5,1.0],
    [0.5,0.91,0.26,-0.5],
    [0.1,0.4,-0.6,0.2]
]

biases = [2,3,0.5]

layer_outputs = [] #output of current layer

# print(list(zip(weights,biases)))

for nueron_weights,nueron_bias in zip(weights,biases):
    nueron_output = 0 
    for n_input,weight in zip(input,nueron_weights):
        nueron_output += n_input * weight
    nueron_output += nueron_bias
    layer_outputs.append(nueron_output)


print(layer_outputs)