import numpy as np
from randomAlgorithm import randomPick

def getCentroids(distanceMatrix : np, numCentroids):
    
    n_rows, n_cols = distanceMatrix.shape
    if n_rows == 0: return []
    if numCentroids == 0: return []
    if numCentroids >= n_rows:
        return np.arange(n_rows)
    
    res = np.zeros(numCentroids, dtype=int)
    probDist = np.full(n_rows, 1.0/n_rows) # Probability distribution that depends on distances 
    res[0] = randomPick(probDist)

    for i in range(1, numCentroids):
        for j in range(0, n_rows):
            minDist = distanceMatrix[ res[0] ][j]
            for k in range(1, i):
                dist = distanceMatrix[ res[k] ][j]
                if dist < minDist:
                    minDist = dist
            probDist[j] = minDist ** 2
        sum = 0.0
        for j in range(0, n_rows):
            sum += probDist[j]
        if sum > 0.0:
            for j in range(0, n_rows):
                probDist[j] = probDist[j] / sum
        else:
            for j in range(0, n_rows):
                probDist[j] = 1.0 / (n_rows - i)
            for j in range(0, i):
                probDist[ res[j] ] = 0.0     
        res[i] = randomPick(probDist)
    
    return res