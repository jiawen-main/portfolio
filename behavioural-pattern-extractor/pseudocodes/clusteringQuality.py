def wcss(structuredDistanceMatrix, clusterSizes):
    """
    Calculates the Within-Cluster Sum of Squares

    Parameters:
    -   structuredDistanceMatrix: Distance matrix structured in cluster format 
        (implicitly divided into blocks), where the first element of each block 
        is the cluster centroid.
    -   clusterSizes: Sizes of each cluster, defining the blocks of structuredDistanceMatrix.
    """
    sum = 0.0
    offset = 0
    for BS in clusterSizes:
        for j in range(offset, offset + BS):
            sum += (structuredDistanceMatrix[offset][j] ** 2)
        offset += BS
    return sum

def elbowReached(wcss, numClusters):
    """
    The elbow method to determine the stop condition
    """
    ELBOW_IMPROVEMENT_UMBRAL = 0.25
    if numClusters > 3:
        if wcss[numClusters - 1] == 0.0:
            return True
        improvement = ((wcss[numClusters - 1] - wcss[numClusters]) 
                      / wcss[numClusters - 1])
        if improvement < ELBOW_IMPROVEMENT_UMBRAL:
            return True
    return False

def silhouetteCoefficient(structuredDistanceMatrix, clusterSizes):
    """
    Calculate the Silhouette coefficient of clusters

    Parameters:
    -   structuredDistanceMatrix: Distance matrix structured in cluster format 
        (implicitly divided into blocks), where the first element of each block 
        is the cluster centroid.
    -   clusterSizes: Sizes of each cluster, defining the blocks of structuredDistanceMatrix.
    """
    n_rows, n_cols = structuredDistanceMatrix.shape
    if n_rows <= 1: return 0.0
    L = len(clusterSizes)

    avgDistIntraCluster = [] # Average distance to points in the same cluster
    minAvgDistInterCluster = [] # Minimum average distance to points in other cluster
    offset = 0
    for BS in clusterSizes:
        if BS != 1: 
            for j in range(offset, offset+BS):
                sum = 0.0
                for k in range(offset, offset+BS):
                    sum += structuredDistanceMatrix[j][k]
                avgDistIntraCluster[j] = sum / (BS - 1)
        else: avgDistIntraCluster[offset] = 0.0
    
    offset = 0
    for i in range(0,L):
        BS1 = clusterSizes[i]
        for j in range(offset, offset+BS1):
            min = float('inf') # Positive infinity
            interOffset = 0
            for ii in range(0,L):
                BS2 = clusterSizes[ii]
                if (ii != i) and (clusterSizes[ii]>0):
                    sum = 0.0
                    for jj in range(interOffset, interOffset+BS2):
                        sum += structuredDistanceMatrix[j][jj]
                    avg = sum / BS2
                    if (avg < min): min = avg
                interOffset += BS2
            minAvgDistInterCluster[j] = min
        offset += BS1

    offset = 0, result = 0.0
    for BS in clusterSizes:
        for j in range(offset, offset+BS):
            a = avgDistIntraCluster[j]
            b = minAvgDistInterCluster[j]
            div = a if a > b else b
            if div != 0.0: result += ((b - a) / div)
        offset += BS
    
    return result/n_rows
