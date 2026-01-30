import numpy as np
from metrics import Metric
from assets import ArrayBoolean

def jaccardDistance(
    a: ArrayBoolean,
    b: ArrayBoolean
):
    L = a.length()
    intersection = union = 0
    for i in range(0, L):
        if a[i]:
            if b[i]:
                intersection += 1
            union += 1
        elif b[i]:
            union += 1
    return (1.0 - intersection / union 
            if union != 0 else 0.0)

def levenshteinDistance(
    a: str,
    b: str
):
    m = len(a)
    n = len(b)
    if m == 0: return n
    if n == 0: return m

    prev = [], curr = []
    for j in range(0,n+1):
        prev[j] = j

    for i in range(1,m+1):
        curr[0] = i
        for j in range(1,n+1):
            if (a[i-1] == b[j-1]):
                curr[j] = prev[j-1]
            else:
                curr[j] = 1 + min(prev[j], prev[j-1], curr[j-1])
        # Current becomes previous for next iteration
        temp = prev
        prev = curr
        curr = temp
    
    return prev[n]

def levenshteinNormalizedDistance(
    a: str,
    b: str
):
    lenA = len(a)
    lenB = len(b)
    maxL = max(lenA, lenB)
    d = abs(lenA - lenB)
    return ((levenshteinDistance(a, b) - d) / (max - d) 
            if maxL != d else 1.0)

def manhattanDistance(
    a: float,
    b: float
):
    return abs(a - b)

def manhattanNormalizedDistance(
    a: float,
    b: float,
    normValue
):
    if normValue == 0:
        raise RuntimeError("Normalization value is 0")
    return manhattanDistance(a, b) / normValue

def normalizedDistance(
    vecA : np,
    vecB : np,
    metrics : dict[type, Metric],
    normValues
):
    L = vecA.shape
    sum = 0.0
    for i in range(L):
        if normValues[i] == 0:
            raise RuntimeError(f"Normalization value is 0 at position {i}")
        metric = metrics[type(vecA[i])]
        sum += (metric.distance(vecA[i], vecB[i]) 
                / normValues[i])
    return sum