# Behavioural Pattern Extractor - Team Programming project

An application for creating, responding and analysing surveys.

**Code structure:**

It uses 3-layer architecture (with Domain Model), which is composed of persistence layer, domain layer and presentation layer. The communication between layers is achieved by using controllers. The entire project uses Java as the main programming language.

In the directory [structure/class-diagram][link-1], you may find the class diagram of the project.

**My main contribution:**

Designer of clustering algorithms for mixed data (numbers, multiple-choice and text). Concretely,

- [K-Means algorithm][link-2]
- [K-Medoids algorithm][link-3]
- [K-Means++ algorithm][link-4]

Moreover, K-Means++ algorithm is combined with K-Means/K-Medoids algorithm and the use of [elbow method][link-5] on [WCSS (Within-Cluster Sum of Squares)][link-5] to create the [final algorithm][link-6] to extract an optimal number of clusters classified by behaviours from a set of survey answers.

Designer of [distance algorithms][link-7]. Concretely,

- Jaccard distance
- Levenshtein distance
- Manhattan normalized distance

Designer of [reduction algorithms][link-8] that determine the centre of a homogeneous data set. Concretely,
 
- Arithmetic mean (for numerical data)
- Moda (for string data and boolean arrays)

Designer of [MDS (Multidimensional Scaling) algorithm][link-9] to project high-dimensional survey answers into 2D graphics, visualizing the clusters.

Designer of [Silhouette coefficient][link-5] as the metric to evaluate the quality of clustering.

Designer of [Metric][link-10] and [Reducer][link-11] data structures.

- Metric is a function of distance. It allows to personalize the calculation of the distance between two objects.
- Reducer is a function that extracts the centre from a set of homogeneous object. It allows to personalize the method to determine the centre.

In the directory [pseudocodes][link-12] you may find the pseudocodes in Python that illustrate my algorithms. These are simplified to show only the main purpose.

[link-1]: https://github.com/jiawen-main/portfolio/tree/main/behavioural-pattern-extractor/structure/class-diagram
[link-2]: https://github.com/jiawen-main/portfolio/tree/main/behavioural-pattern-extractor/pseudocodes/kMeansAlgorithm.py
[link-3]: https://github.com/jiawen-main/portfolio/tree/main/behavioural-pattern-extractor/pseudocodes/kMedoidsAlgorithm.py
[link-4]: https://github.com/jiawen-main/portfolio/tree/main/behavioural-pattern-extractor/pseudocodes/kMeansPlusPlusAlgorithm.py
[link-5]: https://github.com/jiawen-main/portfolio/tree/main/behavioural-pattern-extractor/pseudocodes/clusteringQuality.py
[link-6]: https://github.com/jiawen-main/portfolio/tree/main/behavioural-pattern-extractor/pseudocodes/finalAlgorithm.py
[link-7]: https://github.com/jiawen-main/portfolio/tree/main/behavioural-pattern-extractor/pseudocodes/distances.py
[link-8]: https://github.com/jiawen-main/portfolio/tree/main/behavioural-pattern-extractor/pseudocodes/reductionAlgorithm.py
[link-9]: https://github.com/jiawen-main/portfolio/tree/main/behavioural-pattern-extractor/pseudocodes/mdsAlgorithm.py
[link-10]: https://github.com/jiawen-main/portfolio/tree/main/behavioural-pattern-extractor/pseudocodes/metrics.py
[link-11]: https://github.com/jiawen-main/portfolio/tree/main/behavioural-pattern-extractor/pseudocodes/reducers.py
[link-12]: https://github.com/jiawen-main/portfolio/tree/main/behavioural-pattern-extractor/pseudocodes