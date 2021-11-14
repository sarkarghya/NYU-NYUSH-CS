import sample

''' For question 6:
    - compute_mean
    - compute_std'''

def compute_mean(data):
    dim = data[0].dimensionality()
    mean = sample.Sample('mean', [0.0]*dim)
    for d in data:
        mean += d
    return mean/len(data)

def compute_std(data, mean):
    dim = data[0].dimensionality()
    std = sample.Sample('std', [0.0]*dim)
    for d in data:
        # you only need to sum the square of the
        # difference between d and the mean
        std += (d - mean).power(2)
    # we've done the square root and averaging for you
    return std.power(0.5)/(len(data)**0.5)

''' For question 7:
    normalization(data) '''

def normalization(data):
    new_data = []
    data_mean = compute_mean(data)
    data_std = compute_std(data, data_mean)
    for d in data:
        # IMPLEMENTATION
        d -= data_mean
        new_data.append(d.vec_div(data_std))
    return new_data

if __name__ == "__main__":
    a = sample.Sample('a', [1, 1])
    b = sample.Sample('b', [5, 3])
    print(a)
    print(b)

    data = [a, b]
    data_mean = compute_mean(data)
    data_std = compute_std(data, data_mean)
    print("mean: " + str(data_mean))
    print("std: " + str(data_std))

    normalized_data = normalization(data)
    print("after normalization...")
    for d in normalized_data:
        print(d)
