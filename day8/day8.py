import numpy as np

with open('input' ,'r') as f:
    digits = list(f.readline().rstrip(' \n'))

shape = (6, 25)
size = shape[0]*shape[1]

arr = np.array(digits)
layers = []

min_0_count = {'0': size}

# part 1

for i in range(0, len(digits), size): 
    
    layers.append(np.reshape(arr[i:i+size],shape))
    count = dict(zip(*np.unique(layers[-1], return_counts=True)))

    if count['0'] < min_0_count['0']:
        min_0_count = count

print('part 1: {}'.format(min_0_count['1']*min_0_count['2']))

# part 2:

# 0 is black, 1 is white, 2 is transparent

message = layers[-1]

for layer in layers[-2::-1]: # loop over layers in reverse direction
    message = np.where(layer == '2', message, layer)

for l in range(message.shape[0]): # loop over lines for printing
    print(''.join(message[l, :]).replace('0', ' ').replace('1', '#'))