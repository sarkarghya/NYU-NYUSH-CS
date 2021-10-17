import random
random.seed(0)

def get_pancake(a,b,n):
    return [random.randint(a,b) for i in range(n)]


def main():
    pancake = get_pancake(1, 40, 5)
    print("pancake", pancake)
    sorted_list = pancake_sorting(pancake)
    # sorted_list = pancake_sorting_recursive(pancake)

    print(sorted_list)
    # print(pancake)

## complete the code, feel free to define your own functions.
def pancake_sorting(l):
    for i in range(len(l)):
        temp1 = l[:len(l)-i]  ##take the first n-i elements
        max_idx = find_max_idx(temp1) ## find the index of the max values
        temp2 = flip(temp1[:max_idx+1])## flip the max value to the top
        l[:max_idx+1] = temp2   ## replace the elements in l by the flipped elements
        temp3 = flip(l[:len(l)-i]) ## flip the first n-i elements in l
        l[:len(l)-i] = temp3 ## replace the first n-i elements in l
    return l

# def pancake_sorting_recursive(l):
#     if len(l) == 1:
#         return l
#     idx = l.index(max(l))
#     l[:idx+1] = flip(l[:idx+1])
#     flip(l)
#     return pancake_sorting_recursive(l[:-1]) + [l[-1]]
    
    
def flip(l):
    for i in range(len(l)//2):
        l[i], l[-i-1] = l[-i-1], l[i]
    return l


def find_max_idx(l):
    return l.index(max(l))



main()
    
        
                      
    
    
