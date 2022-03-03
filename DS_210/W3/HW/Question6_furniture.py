def mirari(num, idy, dic): #takes number and index and adds them to dictionary
    if len(dic) == 0:
        return {(idy,):[num]}
    k, v = list(dic.items())[0]
    del dic[k]
    return {**{(*k,idy): [*v,num]}, **mirari(num, idy, dic)}

def lis_itr(ls, idy, dic): #takes  list and adds it to dictionary using mirari
    first = ls.pop(0)
    idy += 1
    if len(ls) == 0:
        return mirari(first, idy, dic)
    return {**mirari(first, idy, dic.copy()), **lis_itr(ls, idy, dic.copy())}

def supl_itr(ls, idy, dic): #takes  lists and adds it to dictionary
    first = ls.pop(0)
    if len(ls) == 0:
        return lis_itr(first, -1, dic.copy())
    return lis_itr(first, -1, supl_itr(ls, idy+1, dic.copy()))

def getSum(piece):
    if len(piece)==0:
        return 0
    else:
        return piece[0] + getSum(piece[1:]) 

def filt(dic, X, Z):
    if len(dic) == 0:
        return []
    else:
        k = list(dic.keys())[0]
        v = dic.pop(k)
        if Z <= getSum(v) <= X:
            return [k] + filt(dic,X,Z)
        else:
            return [] + filt(dic,X,Z)

def purchase_combination(Y_cost, X, Z):
    """
    Y_cost: a list of costs of each appliance brand. e.g. Y_cost = [[1, 5], [2, 4, 3, 6]]. All costs are > 0
    The number of brands for appliance type 0 is 2, which corresponds to cost [1, 5] from Y_cost[0].
    The number of brands for appliance type 1 is 4, which corresponds to cost [2, 4, 3, 6] from Y_cost[1].
    X: Total money you have
    Z: Minimum spending, and Z < X
    Return: A list of tuples containing the index of each appliance selected.
    """
    # TODO
    return filt(supl_itr(Y_cost, -1, {}), X, Z)

def main():
    Y_cost = [[1,5], [2,4,3,6]]
    X = 12
    Z = 9
    print(purchase_combination(Y_cost, X, Z)) # Expect: results = [(1,1), (1,3)]

if __name__ == "__main__":
    main()