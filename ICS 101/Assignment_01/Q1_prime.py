import math
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n))+1)) and n>1
    #faster sieves are available

if __name__ == "__main__":
    
    def list_prime(n):
        p = []
        for i in range(1, n):
            if is_prime(i):
                p.append(i)
        return p

    print(list_prime(10000))