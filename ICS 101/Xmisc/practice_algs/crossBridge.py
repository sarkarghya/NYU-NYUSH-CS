import copy


def crossBridge(nums, crossed=[], currentTimeSpent=0, minTime=[float("inf")], path=[]):
    '''

    Parameters
    ----------
    nums : list 
        number of people haven't crossed the bridge.
    crossed : list
        DESCRIPTION. people crossed the bridgeThe default is [].
    currentTimeSpent : int/float
        DESCRIPTION. the time spent up to now; The default is 0.
    minTime : list; we need a mutable variable here.
        DESCRIPTION. The minimum time spend; The default is [float("inf")].
    path : list of list
        DESCRIPTION. each element is a list representing a crossing that spends the fewest minutes. The default is [].

    Returns
    -------
    minTime : TYPE
        DESCRIPTION.
    path : TYPE
        DESCRIPTION.

    '''

    if len(nums) == 2: ## when there are only two persons left, we should stop
        crossed.append(nums[0])
        crossed.append(nums[1])
        currentTimeSpent += max(nums)
        if currentTimeSpent <= minTime[0]:
            minTime[0] = currentTimeSpent
            path.append(crossed)
            # print(minTime)
        return minTime, path
     ## try all feasible ways to cross the bridge
    for n in nums: ## choose one person n to cross the bridge
        temp1 = copy.deepcopy(nums) ## keep the current persons remain uncrossed
        temp1.remove(n)
        temp4 = currentTimeSpent ## keep the currentTimeSpent
        for m in temp1: ## choose another person m who will go with n
            temp3 = copy.deepcopy(temp1)
            temp2 = copy.deepcopy(crossed) ## keep the current crossed persons
            temp2.append(n)
            temp2.append(m)
            temp4 += max(n, m) + min(temp2) ## the fastest person will take the torch back
            temp3.remove(m) ## remove the m in the uncrossed list
            temp3.append(min(temp2)) ## add the person who takes the torch back into the uncrossed list
            temp2.remove(min(temp2)) ## remove the person who takes the torch back from the crossed list
            if temp4 > minTime[0]: ## no need to vist the nodes that exceed the minTime.
                continue
            crossBridge(temp3, temp2, temp4, minTime)
    return minTime, path


##test
if __name__ == "__main__":
    nums = [2, 4, 5, 6]
    print(crossBridge(nums))
        
        


