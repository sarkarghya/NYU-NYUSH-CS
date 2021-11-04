
import sample_student as sample
import util
import helper

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
        return helper.computeCentroid(self)

    #### Implement the centroid updating function here!
    def update(self, samples):
        """Replace the samples in the cluster by new samples
           Return: how much the centroid has changed"""
        return helper.update(self, samples)
     
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

if __name__ == "__main__":
    test_samples = util.genDistribution()
    c = Cluster(test_samples)
    print(c.centroid)
    print("cluster center: ", c.centroid.features)
    util.plot_cluster([c])
    
    # now assign the cluster new samples, and move it
    test_samples2 = util.genDistribution(1, 1, 1, 1, 30)
    diff = c.update(test_samples2)
    print("center moved: ", diff)
    # plot_cluster expects an array of cluster...
    util.plot_cluster([c])