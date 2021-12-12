import random
random.seed(0) # fix seed for reproducibility

class Dice:
    def __init__(self, bias=0.5):
        self.bias = bias

    def roll(self):
        return random.uniform(0, 1) < self.bias

def main():

    # the Dice instance to decide when to explore and when to exploit
    epsilon = 0.1
    greedy_dice = Dice(epsilon)

    # set the true degree of interests
    # if degree of interest = 0.1, then 10% of chance the neighbour will pick up the Ads

    interests = [ random.uniform(0,1) for i in range(5) ]

    num_neighbours = len(interests)
    neighbors = []
    for i in range(num_neighbours):
       m = Dice(interests[i])
       neighbors.append(m)

    # warm-up phase gives each neighbor 0.5 degree of interest

    neighbor_data = {}
    warm_up = 10
    for i in range(num_neighbours):
        neighbor_data[i] = {}
        neighbor_data[i]['pick-up'] = warm_up * 0.5
        neighbor_data[i]['drop-off'] = warm_up

    print("+++++++ warm-up phase")
    for k,v in neighbor_data.items(): print(k,v)
    print("------- true degree of interests: ")
    for i in range(num_neighbours):
        print(i, interests[i])


    # makes num_iter bigger (e.g. 100000) gives better results (as in the exam sheet).
    num_iter = 100000

    for i in range(num_iter):
        # pick_neighbor() is the function you need to implement
        pick = pick_neighbor(greedy_dice, neighbor_data)
        neighbor_data[pick]['drop-off'] += 1
        neighbor_data[pick]['pick-up'] += neighbors[pick].roll()

    print("\n")
    print("++++++++ after simulation ", num_iter)
    for i in range(num_neighbours): print(i, neighbor_data[i])
    print("-------- estimated degree of interests:")
    for i in range(num_neighbours):
        print(i, neighbor_data[i]['pick-up']/neighbor_data[i]['drop-off'])

def pick_neighbor(greedy_dice, neighbor_data):
    #----------your code below----------#
    # IMPLEMENT THE FOLLOWING PART
    # the variable "pick" is the neighbor your algorithm
    # selected in each round.
    # pick-ups/drop-offs gives the estimated degree of interest

    # COMMENT OUT the following 2 lines and implement e-greedy
    if greedy_dice.roll():
        lis = [float(list(v.values())[0])/float(list(v.values())[1]) for v in neighbor_data.values()]
        pick = lis.index(max(lis))
    else:
        pick = random.randrange(5)
    #----------your code below----------#
    return pick


##---test of your code---##
main()
