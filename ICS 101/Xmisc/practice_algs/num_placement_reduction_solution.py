
def main():
    lst = [9, 70, 20, 27]
    sorted_lst = sorted(lst)
    new = []
    sign = ['>', '<', '>']
    for s in sign:
        if s == '<':
            num = sorted_lst.pop(0)
        else:
            num = sorted_lst.pop()

        new +=  [num, s]

    new += sorted_lst
    print(new)
main() 
