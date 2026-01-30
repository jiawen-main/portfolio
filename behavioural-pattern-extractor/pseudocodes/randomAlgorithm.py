import numpy as np

def randomPick(probabilityDistribution):
    L = len(probabilityDistribution)
    for i in range (1, L):
        probabilityDistribution[i] += probabilityDistribution[i-1]
    r = np.random.rand()
    for i in range (0, L):
        if r < probabilityDistribution[i]: return i
    return L - 1