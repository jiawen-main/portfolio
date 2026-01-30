import numpy as np
from metrics import Metric
from reducers import Reducer
from distances import normalizedDistance

def getCentroid(
    matrix : np,
    metrics : dict[type, Metric], 
    reducers : dict[type, Reducer],
    normValues
):
    n_rows, n_cols = matrix.shape
    if n_rows == 0:
        return -1
    
    mean = np.zeros(n_cols)
    for i in range(n_cols):
        reducer = reducers[type(matrix[0][i])]
        data = matrix[:, i] # A column of data
        mean[i] = reducer.reduce(data)
    
    minDist = normalizedDistance(mean, matrix[0], 
                                 metrics, normValues)
    centroidPos = 0
    for i in range(n_rows):
        dist = normalizedDistance(mean, matrix[i], 
                                  metrics, normValues)
        if dist < minDist:
            minDist = dist
            centroidPos = i

    return centroidPos
