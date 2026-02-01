import numpy as np
from assets import Point

def generateRandomPoints(size):
    """ Random points in space [-0.5, 0.5] x [-0.5, 0.5] """
    randomPoints = []
    for i in range(0,size):
        x = np.random.rand() - 0.5
        y = np.random.rand() - 0.5
        randomPoints[i] = Point(x, y)
    return randomPoints

def distance(p1: Point, p2: Point):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2.0) ** 0.5

def processMds(distanceMatrix : np):
    K = 100 # Number of refinement iterations
    UMBRAL_ERROR = 0.0
    LEARNING_RATE = min(0.01, 2.5*(1.0 / n_rows))

    n_rows, n_cols = np.shape
    resultPoints = generateRandomPoints(n_rows)
    for k in range(0,K):
        for i in range(0,n_rows):
            for j in range(i+1, n_rows):
                estimatedDist = distance(resultPoints[i], resultPoints[j])
                err = distanceMatrix[i][j] - estimatedDist
                if (abs(err) > UMBRAL_ERROR):
                    vec = Point(
                        resultPoints[i].x - resultPoints[j].x,
                        resultPoints[i].y - resultPoints[j].y, )
                    factor = LEARNING_RATE * (err / estimatedDist)
                    resultPoints[i].x += vec.x * factor
                    resultPoints[i].y += vec.y * factor
                    resultPoints[j].x -= vec.x * factor
                    resultPoints[j].y -= vec.y * factor
    return resultPoints
