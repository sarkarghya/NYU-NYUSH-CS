import sample
import random
import util
# import knn_helper
import matplotlib.pylab as pylab
import cluster as cl

def knn(p, data, k): 
    """ Compute the distance between p to every sample in data,
        set p's label to the label of the maximum of samples
        within the k nearest neighbors

        # p is a SAMPLE object
        # data is a list of SAMPLE object
        # k is int
    """

    """ Steps:
        1. Iterate through samples in data and store the
           distance from p in the dictionary "distance"; key is the
           distance, value is the sample.
        2. Creat a sorted list of samples according to ascending
           order of the distances.
        3. In the dictioary "label_votes", stores number of votes
           in each label among the top-k nearest samples
        4. Assign p the most popular label
    """
    # Calculating the distances b/w p & every pt. in data
    distances = {}
    for d in data:
        if d.distance(p) not in distances.keys():
            distances[ d.distance(p) ] = [ d ]
        else:
            distances[ d.distance(p) ].append(d)

    # Sorting the k nearest neighbours
    result = []        
    for key in sorted(distances.keys()):
        result.extend( distances[key] )

    k_nearest_neighbours = result[:k]

    # Assigning a label to the new point based on the k neighbours
    label_votes = { l:0 for l in util.LABELS }
    for x in k_nearest_neighbours:
        label_votes[x.getLabel()] += 1
    max_label = sorted(label_votes, key = label_votes.get, reverse = True)[0]
    
#    max_vote = 0
#    for k , v in label_votes.items():
#        if v > max_vote:
#            max_label = k
    p.setLabel(max_label)

if __name__ == "__main__":

    # make data
    random.seed(0)
    n = 100
    K = 3
    LABELS = ('a', 'b', 'c')
    all_cluster = []
    data = []
    for i in range(K):
        tmp_data = util.genDistribution(i*2+1, 1, i*2+1, 1, n=20, label = LABELS[i])
        all_cluster.append(cl.Cluster(tmp_data))
        data += tmp_data

    def onclick(event):
        # Creating a new point and finding the k nearest neighbours
        new = sample.Sample('', [event.xdata, event.ydata], '')
        knn(new, data, K)

        # draw the new point
        data.append(new)
        pylab.scatter([new.getFeatures()[0]], \
                      [new.getFeatures()[1]], \
                      label = new.getLabel(), \
                      marker = util.make_cmarkers()[LABELS.index(new.getLabel())], \
                      color = util.make_cmap()[LABELS.index(new.getLabel())])
        pylab.draw()

    # start plotting
    fig = pylab.figure()
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    util.plot_cluster(all_cluster, centroid = False)
    pylab.show()

    # new_pt = sample.Sample('', [0.2, 0.3], '')
    # knn(new_pt, data, K)
    #
    # data.append(new_pt)
    # print("\nafter....")
    # util.plotSamples(data)
    # plt.show()
