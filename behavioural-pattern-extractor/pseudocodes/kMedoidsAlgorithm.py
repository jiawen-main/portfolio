import numpy as np
from metrics import Metric
from distances import normalizedDistance

def getCentroid(*args):

    if (len(args) == 3 and
        isinstance(args[0], np) and
        isinstance(args[1], dict[type, Metric])):
        matrix = args[0], metrics = args[1], normValues = args[2]
        n_rows, n_cols = matrix.shape

        minDist = 0.0
        for j in range(0, n_cols):
            minDist += normalizedDistance(matrix[0], matrix[j],
                                          metrics, normValues)
        
        centroidPos = 0
        for i in range(1, n_rows):
            dist = 0.0
            for j in range(0, n_cols):
                dist += normalizedDistance(matrix[i], matrix[j],
                                           metrics, normValues)
            if dist < minDist:
                minDist = dist
                centroidPos = i
        return centroidPos
    
    if (len(args) == 1 and isinstance(args[0], np)):
        distanceMatrix = args[0]
        n_rows, n_cols = distanceMatrix.shape

        minDist = 0.0
        for j in range(0, n_cols):
            minDist += distanceMatrix[0][j]

        centroidPos = 0
        for i in range(1, n_rows):
            dist = 0.0
            for j in range(0, n_cols):
                dist += distanceMatrix[i][j]
            if dist < minDist:
                minDist = dist
                centroidPos = i
        return centroidPos
