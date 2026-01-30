# Behavioural Pattern Extractor - Team Programming project

An application for creating, responding and analysing surveys.

**Code structure:**

It uses 3-layer architecture (with Domain Model), which is composed of persistence layer, domain layer and presentation layer. The communication between layers is achieved by using controllers. The entire project uses Java as the main programming language.

In the directory [structure/class-diagram](https://github.com/jiawen-main/portfolio/tree/main/behavioural-pattern-extractor/structure/class-diagram), you may find the class diagram of the project.

**My main contribution:**

Designer of clustering algorithms. Concretely,
- K-Means algorithm
- K-Medoids algorithm
- K-Means++ algorithm

Moreover, K-Means++ algorithm is combined with K-Means/K-Medoids algorithm and the use of elbow method on WCSS (Within-Cluster Sum of Squares) to create the final algorithm to extract an optimal number of clusters classified by behaviours from a set of survey answers.

Designer of distance algorithms. Concretely,

- Jaccard distance
- Levenshtein distance
- Manhattan normalized distance

Designer of MDS (Multidimensional Scaling) algorithm to project high-dimensional survey answers into 2D graphics, visualizing the clusters.

Designer of Metric and Reducer data structures.

- Metric is a function of distance. It allows to personalize the calculation of the distance between two objects.
- Reducer is a function that extracts the centre from a set of homogeneous object. It allows to personalize the method to determine the centre.

In the directory [pseudocodes](https://github.com/jiawen-main/portfolio/tree/main/behavioural-pattern-extractor/pseudocodes) you may find the pseudocodes in Python that illustrate my algorithms. These are simplified to show only the main purpose.