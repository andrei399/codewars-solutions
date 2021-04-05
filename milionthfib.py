#https://www.codewars.com/kata/53d40c1e2f13e331fc000c26
import unittest

def fastdouble(n):
    if n == 0: return (0, 1)
    a, b = fastdouble(n // 2)
    c = a * (b * 2 - a)
    d = a ** 2 + b ** 2
    if n % 2 == 0: return (c, d)
    return (d, c + d)
def fib(n): #O(log(n)) + afla si n+1
    #if n < 0:
    #    if n % 2: return fastdouble(-n)[0]
    #    return -fastdouble(-n)[0]
    return fastdouble(n)[0]

def main():
    print(fib(10001))

if __name__ == '__main__':
    main()
