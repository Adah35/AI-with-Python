'''
 creating a nueral network from scratch
 the nueral network has 4 inputs and 3 nuerons
 for each specific nuerons comes with a specific input and weight

 so for nueron one it has four inputs and 4 weights
 same for the remaining 2 inputs

 the inputs might be outputs from other nuerons
'''

input = [1,2,3,2.5]

weight1 = [0.2,0.8,-0.5,1.0]
weight2 = [0.5,0.91,0.26,-0.5]
weight3 = [0.1,0.4,-0.6,0.2]


bias1 = 2
bias2 = 3
bias3 = 0.5

output = [
    input[0] * weight1[0] + input[1] * weight1[1] + input[2] * weight1[2] + input[3] * weight1[3] + bias1,
    input[0] * weight2[0] + input[1] * weight2[1] + input[2] * weight2[2] + input[3] * weight2[3] + bias2,
    input[0] * weight3[0] + input[1] * weight3[1] + input[2] * weight3[2] + input[3] * weight3[3] + bias3
]
print(output)