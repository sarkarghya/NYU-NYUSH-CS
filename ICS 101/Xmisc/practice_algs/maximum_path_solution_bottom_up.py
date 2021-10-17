def maxpath(triangle):
    # Bottom up approach will be able to solve this problem without much hassle
    # Compare to brute force or a naive "greedy" top-down approach
    for x in range(len(triangle)-2, -1, -1):
        for y in range(len(triangle[x])):
            if triangle[x+1][y] > triangle[x+1][y+1]:
                triangle[x][y] += triangle[x+1][y]
            else:
                triangle[x][y] += triangle[x+1][y+1]

    return triangle[0][0]


if __name__ == "__main__":

    triangle = open("triangle.txt","r").read().split("\n")

    for x in range(len(triangle)):
        triangle[x] = triangle[x].split(" ")
        for y in range(len(triangle[x])):
            triangle[x][y] = int(triangle[x][y])

    for row in triangle:
        print(row)

    print()
    print("The maximum path results in: ", maxpath(triangle))
    # Answer is 538 for the test case in triangle.txt

    for row in triangle:
        print(row)
