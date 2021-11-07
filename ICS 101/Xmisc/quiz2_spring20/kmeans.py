import random
import sample


# Cluster class
class Cluster(object):

    def __init__(self, samples):
        """Assumes samples is a list"""
        self.samples = samples
        """ centrold is also an instance of Sample class """
        self.centroid = self.computeCentroid()

    def size(self):
        return len(self.samples)

    def getCentroid(self):
        return self.centroid

    def getMembers(self):
        return self.samples

    #### Implement the centroid computing function here!
    def computeCentroid(self):
        '''
        return an instance of Sample, its features should be
        the center of all the samples in the cluster
        '''
        #return helper.computeCentroid(self)
        dim = self.samples[0].dimensionality()
        centroid = sample.Sample('centroid', [0.0]*dim)
        for e in self.samples:
            centroid += e
        centroid /= len(self.samples)
        return centroid

    #### Implement the centroid updating function here!
    def update(self, samples):
        """Replace the samples in the cluster by new samples
           Return: how much the centroid has changed"""
        oldCentroid = self.centroid
        self.samples = samples
        if len(samples) > 0:
            self.centroid = self.computeCentroid()
            return oldCentroid.distance(self.centroid)
        else:
            return 0.0

    def __str__(self):
        names = []
        for e in self.samples:
            names.append(e.getName())
        names.sort()
        result = 'Cluster with centroid '\
                 + str(self.centroid.getFeatures()) + ' contains:\n  '
        for e in names:
            result = result + e + ', '
        return result[:-2]



def kmeans_iter(samples, clusters, k):
    '''
        implement one iteration of kmeans:
        - each sample finds the closest cluster by computing
          its distance to the centroids of all the clusters
        - then compute every cluster's new centroid
        - the algorithm converges if cluster's centroid does not
          move any more
    '''
    #Create a list containing k distinct empty lists

    newClusters = []
    for i in range(k):
        newClusters.append([])

    #Associate each sample with closest centroid
    for e in samples:
        #Find the centroid closest to e
        smallestDistance = e.distance(clusters[0].getCentroid())
        index = 0
        for i in range(1, k):
            distance = e.distance(clusters[i].getCentroid())
            if distance < smallestDistance:
                smallestDistance = distance
                index = i
        #Add e to the list of samples for the appropriate cluster
        newClusters[index].append(e)

    #Update each cluster; check if a centroid has changed
    converged = True
    for i in range(len(clusters)):
        if clusters[i].update(newClusters[i]) > 0.0:
            converged = False
    return converged

# Kmeans: take a list of samples and make k clusters
def kmeans(samples, k, verbose):
    # this is just to make results repeatable
    random.seed(0)
    """Assumes samples is a list of samples of class Sample,
         k is a positive int, verbose is a Boolean
       Returns a list containing k clusters. """

    #Get k randomly chosen initial centroids
    initialCentroids = random.sample(samples, k)

    #Create a singleton cluster for each centroid
    clusters = []
    for e in initialCentroids:
        clusters.append(Cluster([e]))

    #Iterate until centroids do not change
    converged = False
    numIterations = 0
    while not converged:

        numIterations += 1

        # replace the following line by implementing
        # kmeans_iter(samples, clusters, k) in this file
        converged = kmeans_iter(samples, clusters, k)
        #converged = kmeans_iter(samples, clusters, k)

        if verbose:
            print('Iteration #' + str(numIterations))
            for c in clusters:
                print(c)
            print('\n') #add blank line
    return clusters


if __name__ == "__main__":
    random.seed(0)
