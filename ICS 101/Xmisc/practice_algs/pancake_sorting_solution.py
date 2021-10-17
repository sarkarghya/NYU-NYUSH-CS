
def find_max(lst):
    # this return index of max
    idx = 0
    m = lst[0]
    for i in range(len(lst)):
        if lst[i] > m:
            idx = i
            m = lst[i]
    return idx, m


def flip(lst):
    # this funttion flip lst upside down
    # or use reverse() method
    # complexity: O(n)
    new = []
    for i in lst:
        new.insert(0, i)
    return new

def main():
    pck = [1, 8, 2, 3, 4]
    new = pck[:]
    # bottom --> top
    for i in range(len(new)):
        tmp = new[i:]
        idx, m = find_max(tmp) # complexity n-i
        new_tmp = tmp[:idx] + flip(tmp[idx:]) # complexity: n-i
        tmp = flip(new_tmp) # complexity: n
        new = new[:i] + tmp # now new[0] has the max number
        print(new)
main()
