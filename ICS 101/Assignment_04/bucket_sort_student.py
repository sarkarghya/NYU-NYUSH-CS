import random
random.seed(0)

def bucket_sort(mylist):
    # initialize the buckets
    mydict = {}
    # place the values to be sorted in the buckets
    for item in mylist:
        mydict.setdefault(item//10, []).append(item)
    # sort each bucket 
    mydict = {key: sorted(mydict[key]) for key in mydict}
    # concatenate your bucket to the result
    result = []
    for key in sorted(mydict.keys()):
        result.extend(mydict[key])
    return result

def main():
    """ this is not exactly relevant, but the following 4 lines of
    code can be replaced by one line:
    list_a = [random.randint(0, 100) for i in range(100)]
    """
    list_a = []
    for i in range(100):
        list_a.append(random.randint(0,100))
    print(list_a)

    list_a = bucket_sort(list_a)
    print("SORTED:", list_a)    

main()
