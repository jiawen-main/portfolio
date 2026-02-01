import numpy as np

def arithmeticMean(listFloat):
    """Calculate the arithmetic mean of a number list"""
    pass

def modaWithHashMap(list):
    """
    Calculate moda of a list.
    It is used for string list
    """
    L = len(list)
    if L == 0: return None
    freq = {} # Hash map
    moda = list[0]
    maxFreq = 0
    for element in list:
        freq[element] += 1
        newFreq = freq[element]
        if freq[element] > maxFreq:
            maxFreq = newFreq
            moda = element
    
def modaWithBooleanArray(listArrayBoolean):
    """
    Calculate moda of a list of boolean arrays.
    """
    L = len(listArrayBoolean)
    if L == 0: return None
    L2 = len(listArrayBoolean[0])
    moda = np.empty(L, dtype = bool)
    freq = np.empty((L, 2), dtype = int)
    for i in range(0, L):
        for j in range(0, L2):
            if (listArrayBoolean[i][j]): freq[j][1] += 1
            else: freq[j][0] += 1
    for j in range(0, L2):
        if freq[j][0] > freq[j][1]: moda[j] = False
        else: moda[j] = True
    return moda