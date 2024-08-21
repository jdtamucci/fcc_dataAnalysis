import numpy as np

test = [9,1,5,3,3,3,2,9,0]

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
 
    square = np.array([list[0:3],list[3:6],list[6:9]])
    #print(square.shape)
 
    mean = []
    mean.extend([np.mean(square, axis=0).tolist(), np.mean(square, axis=1).tolist(), np.mean(square)])
    #print(mean)
 
    var = []
    var.extend([np.var(square, axis=0).tolist(), np.var(square, axis=1).tolist(), np.var(square)])
    #print(var)
    
    std = []
    std.extend([np.std(square, axis=0).tolist(), np.std(square, axis=1).tolist(), np.std(square)])
    #print(std)

    maxi = []
    maxi.extend([np.max(square, axis=0).tolist(),np.max(square, axis=1).tolist(), np.max(square)])
    #print(maxi)

    mini = []
    mini.extend([np.min(square, axis=0).tolist(), np.min(square, axis=1).tolist(), np.min(square)])
    #print(mini)

    suma = []
    suma.extend([np.sum(square, axis=0).tolist(), np.sum(square, axis=1).tolist(), np.sum(square)])
    #print(suma)

    calculations = {
          'mean': mean,
          'variance': var,
          'standard deviation': std,
          'max': maxi,
          'min': mini,
          'sum': suma
        }
    
    for key, value in calculations.items():
        print((key, value))
    return calculations
 

calculate([0,1,2,3,4,5,6,7,8])

