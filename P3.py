"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def largestPrimeFactor(n):
    factors = []
    tmp = 2
    while (n > 1):
        while (n % tmp == 0):
            factors.append(tmp)
            n = n/tmp
        tmp = tmp + 1
        if (tmp * tmp > n):
            if (n > 1):
                factors.append(n)
            break
    return max(factors)

def main():
    print(largestPrimeFactor(600851475143))
    
if __name__ == "__main__":
    main()