import copy 


def validNum(num, signs, idx):
    if idx == 0:
        return True
    if signs[idx-1] == ">":
        # print(idx, signs[idx-2], signs[idx-1], num)
        if signs[idx-2] > num:
            return True
    if signs[idx-1] == "<":
        # print(idx, signs[idx-2], signs[idx-1], num)
        if signs[idx-2] < num:
            return True
    return False

# def getNumAndSigns(signs):
#     return

def insertNums(nums, signs, idx=0, res=[]):
    # print(signs)
    if len(nums) == 0:
        res.append(signs[:])
        return 
    # preNum, currentSign = getNumAndSigns(signs)
    # print(idx)
    temp1 = copy.deepcopy(signs)
    for n in nums:
        signs = copy.deepcopy(temp1)
        if validNum(n, signs, idx):
            # temp1 = copy.deepcopy(signs)
            signs.insert(idx, n)
            temp2 = copy.deepcopy(nums)
            temp2.remove(n)
            signs = insertNums(temp2, signs, idx+2)
            # break
    return res


##test
if __name__ == "__main__":
    nums = [2, 3, 0, 1, 5]
    signs = ['<', '<', '>', '<']
    res = insertNums(nums, signs)
    print(res)


    