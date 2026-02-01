import numpy as np
from Assets import AnswerSurvey, ArrayBoolean
from Metrics import Metric, FloatMetric, BooleanArrayMetric, StringMetric
from Reducers import FloatReducer, BooleanArrayReducer, StringReducer
from Distances import manhattanDistance, levenshteinNormalizedDistance, jaccardDistance
from ReductionAlgorithm import arithmeticMean, modaWithHashMap, modaWithBooleanArray
from KMeansAlgorithm import getCentroid as KMeansGetCentroid
from KMedoidsAlgorithm import getCentroid as KMedoidsGetCentroid
from kMeansPlusPlusAlgorithm import getCentroids as KMeansPlusPlusGetCentroids
from ClusteringQuality import wcss, elbowReached, silhouetteCoefficient

def toMatrix(answerSurveyList : list[AnswerSurvey]):
    """Transform the list of answers to a data matrix"""
    pass
def toIdArray(answerSurveyList : list[AnswerSurvey]):
    """Transform the list of answers to a id list"""
    pass
def getNormalizationValue(answerSurveyList : list[AnswerSurvey]):
    """
    Get a list of normatization values 
    for each question of this survey
    """
    pass
def getDistanceMatrix(matrix, metrics : dict[Metric], normValues):
    """
    Get a distance matrix from a data matrix, using
    corresponding metrics
    """
def updateState(
    distanceMatrix : np,
    matrix : np,
    idList,
    centroidsPosition,
    clusterSizes
):
    """
    Update all parameters according to the centroids position.
    It ensures that matrix and distance matrix are structured in cluster format 
    (implicitly divided into blocks), where the first element of each block 
    is the cluster centroid.
    It ensures that the position of idList corresponds to the row position of matrix
    (and distanceMatrix)
    """
    pass

def fromStructuredMatrix(idList, clusterSizes):
    """
    Generate a list of clusters, given an id array
    and the size of each cluster
    """
    pass

def structureByClusters(
    distanceMatrix : np,
    matrix : np,
    idList,
    centroidsPosition,
    clusterSizes
):
    """
    Structure the matrix data into clusters by assigning each data point to its nearest centroid
    from centroidsPosition.
    It ensures that matrix and distance matrix are structured in cluster format 
    (implicitly divided into blocks), where the first element of each block 
    is the cluster centroid.
    It ensures that the position of idList corresponds to the row position of matrix 
    (and distanceMatrix).
    Update all parameters according to the structured matrix.
    """
    pass

def processClustering(
    answerSurveyList : list[AnswerSurvey],
    isKMedoids : bool 
):
    """
    Core procedure to extract behavioural patterns
    
    :param answerSurveyList: a list of answers from a survey
    :type answerSurveyList: list[AnswerSurvey]
    :param isKMedoids: Determines which clustering algorithm is used. 
        If false, then K-Means clustering algorithm is used.
        Otherwise K-Medoids clustering algorithm is used.
    :type isKMedoids: bool
    :returns:
        A pair composed of: a list of clusters, and
        the Silhouette coefficient for this list
    """
    metrics, reducers = {}, {}
    metrics[float] = FloatMetric(manhattanDistance)
    metrics[str] = StringMetric(levenshteinNormalizedDistance)
    metrics[ArrayBoolean] = BooleanArrayMetric(jaccardDistance)
    if not isKMedoids:
        reducers[float] = FloatReducer(arithmeticMean)
        reducers[str] = StringReducer(modaWithHashMap)
        reducers[ArrayBoolean] = BooleanArrayReducer(modaWithBooleanArray)
    
    wcssValues = [0.0] * (MAX_NUM_CLUSTERS + 2)
    old_matrix = toMatrix(answerSurveyList)
    old_idList = toIdArray(answerSurveyList)
    normValues = []
    size = len(answerSurveyList)
    if size > 0: normValues = getNormalizationValue(answerSurveyList)
    old_distanceMatrix = getDistanceMatrix(old_matrix, metrics, normValues)
    n_rows, n_cols = old_matrix.shape

    # Check extreme cases
    if n_rows == 0: return ([], 0.0)
    if n_rows == 1: return (old_idList, 0.0)
    old_clusterSizes = [n_rows]
    centroids = (KMedoidsGetCentroid(old_distanceMatrix) if isKMedoids else
                 KMeansGetCentroid(old_matrix, metrics, reducers, normValues))
    updateState(old_distanceMatrix, old_matrix, old_idList, centroids, old_clusterSizes)
    norm_wcss = wcss(old_distanceMatrix, old_clusterSizes)
    wcssValues[1] = 1.0
    if norm_wcss == 0: return (old_idList, 0.0)

    # Compute the optimal number of clusters and the list of clusters
    MAX_NUM_CLUSTERS = 64
    for numberClusters in range(2, MAX_NUM_CLUSTERS): 
        distanceMatrix = old_distanceMatrix.copy()
        matrix = old_matrix.copy()
        idList = old_idList.copy()
        clusterSizes = []

        # K-Means++ algorithm for initialization of centroids
        centroids = KMeansPlusPlusGetCentroids(distanceMatrix, numberClusters)
        structureByClusters(distanceMatrix, matrix, idList, centroids, clusterSizes)

        # Apply K-Means or K-Medoids for better approximation
        offset = 0
        for i in range(0,numberClusters):
            BS = clusterSizes[i]
            centroids[i] = (KMedoidsGetCentroid(distanceMatrix[offset:offset+BS, :]) if isKMedoids else 
                            KMeansGetCentroid(matrix[offset:offset+BS, :], metrics, reducers, normValues))
            offset += BS
        updateState(distanceMatrix, matrix, idList, centroids, clusterSizes)

        # Calculate normalized wcss value
        wcssValues[numberClusters] = wcss(distanceMatrix, clusterSizes) / norm_wcss
        
        # Check whether elbow is reached
        if elbowReached(wcssValues, numberClusters): break

        old_matrix = matrix
        old_distanceMatrix = distanceMatrix
        old_idList = idList
        old_clusterSizes = clusterSizes
    
    return (
        fromStructuredMatrix(old_idList, old_clusterSizes),
        silhouetteCoefficient(old_distanceMatrix, old_clusterSizes)
    )