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
    pass

    """
    1. fill the array allSamples to hold the samples
    2. each sample is corresponding to a type of wine and takes two attributes of the wine
    """
    allSamples = [sample.Sample('', [0.0, 0.0])] # replace this line

    # ---- end of your code --- #



    verbose = False
    k = 3
    unclustered = [kmeans.Cluster(allSamples)]
    print("before clustering")
    util.plot_cluster(unclustered)

    clusters = unclustered
    # IMPLEMENTATION: apply k means to cluster the samples
    # ---- start your code ---- #
    pass
    # ---- end of your code --- #
    print("after clustering")
    util.plot_cluster(clusters, verbose)





    """ bonus: this requires the completion of question 7"""
    normalized_allSamples = allSamples
    normalized_clusters = clusters
    # IMPLEMENTATION: normalizing the data
    # ---- start your code ---- #
    pass
    # ---- end of your code --- #
    print("after normalizing")
    util.plot_cluster(normalized_clusters, verbose)
