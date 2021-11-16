import sample
from util import *
import matplotlib.pyplot as plt



def knn(p, data, k):
    """ Compute the distance between p to every sample in data,
        set p's label to be the average value of the k nearest neibors' labels
        # p is a SAMPLE object
        # data is a list of SAMPLE object
        # k is int
    """
    # p the new observation that want to make prediction
    # Calculating the distances b/w p & every pt. in data
    distances = {}
    for d in data:
        if d.distance(p) not in distances.keys():
            distances[d.distance(p)] = [d]
        else:
            distances[d.distance(p)].append(d)

    # Find the k nearest neighbours
    result = []
    for key in sorted(distances.keys()):
        result.extend(distances[key])
    k_nearest_neighbours = result[:k]

    """Need to Implement here (Task 2)
    Calculate the predicted label(i.e., price) for p and return the prediction 
    """
    # ===================== start implementation ====================
    label_votes = { l:0 for l in data.keys() }
    for x in k_nearest_neighbours:
        label_votes[x.getLabel()] += 1
    p_label = max(label_votes, key = label_votes.get)
    return p_label
    # =====================       end  ==============================

""" NEED to implement here (Task 1)
Load data from the housing_data.txt.
Note:
    the dataset in the txt file contains head and index, which are not needed.
    data is a list of samples, and you should use the Sample class in sample.py.
    When initialize a sample, you need to set a lable for it.
    what is the label of a sample in this case? 
    Remember to convert strings to numbers.
"""
def load_data():
    data = []
    # ===================== start implementation ====================
    with open('.\KNN_material\housing_data.txt', 'r') as f:
        raw_lines = map(lambda line: line.strip().split(','), f.readlines()[1:])
    
    data = [sample.Sample(str(float(x[0])), [ str(float(x[2])), str(float(x[1])) ] ) for x in raw_lines]
    
    # =====================       end  ==============================
    return data


# read data and split the data into train set and test set
data = load_data()

train_size = round(len(data) * 0.8)
train_dt, test_dt = data[:train_size], data[train_size:]
plotSamples(train_dt)

"""NEED to implement (Task 3)
   To calculate the testing MSE
"""

def compute_test_mse(train_dt, test_dt, k=5):
    test_mse = 0
    # ===================== start implementation ====================
    n = len(train_dt)
    test_mse = sum((train_dt[i]- test_dt[i])**2 for i in range(n))/(n)
    # =====================       end  ==============================
    return test_mse

print('the testing mse for k={} is {}'.format(5, compute_test_mse(train_dt, test_dt, k=5)))


"""
NEED TO IMPLEMENT (Task 4)
Performace with differnt k.
for k = 1, 2, ..., 20, calcuate the MSE of the model on the testing data 
and store it in the list mse_all 
"""
K_upper_bound = 21
mse_all = []
# ===================== start implementation ====================

for k in range(K_upper_bound):
    mse_all.append(compute_test_mse(train_dt, test_dt, k))


# =====================       end  ==============================
## Once you complete the task 4, the following statements 
## will plot the expected figure.
if mse_all:
    plt.plot(range(1, K_upper_bound), mse_all, c='g')
    plt.title('mse vs. k')
