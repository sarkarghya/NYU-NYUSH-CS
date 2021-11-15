import kmeans
import sample
import util
import mean_std_student as mean_std

if __name__ == "__main__":
    """
    1. read and process the data
    2. read your data into an array of Sample class objects
    3. apply k means to cluster the samples
    """

    allSamples = []
    # IMPLEMENTATION: Read the data from "wine_data.txt"
    # ---- start your code ---- #
    with open('.\quiz2_spring20\wine_data.txt', 'r') as f:
        raw_lines = map(lambda line: line.strip().split(','), f.readlines()[1:])

    """
    1. fill the array allSamples to hold the samples
    2. each sample is corresponding to a type of wine and takes two attributes of the wine
    """
    allSamples = [sample.Sample('', [ float(x[0]), float(x[4]) ] ) for x in raw_lines]

    # ---- end of your code --- #



    verbose = False
    k = 3
    unclustered = [kmeans.Cluster(allSamples)]
    print("before clustering")
    util.plot_cluster(unclustered)

    clusters = unclustered
    # IMPLEMENTATION: apply k means to cluster the samples
    # ---- start your code ---- #
    clusters = kmeans.kmeans(allSamples, 3, verbose)
    # ---- end of your code --- #
    print("after clustering")
    util.plot_cluster(clusters, verbose)





    """ bonus: this requires the completion of question 7"""
    normalized_allSamples = allSamples
    normalized_clusters = clusters
    # IMPLEMENTATION: normalizing the data
    # ---- start your code ---- #
    normalized_allSamples = mean_std.normalization(allSamples)
    normalized_clusters = kmeans.kmeans(normalized_allSamples, 3, verbose)
    # ---- end of your code --- #
    print("after normalizing")
    util.plot_cluster(normalized_clusters, verbose)
