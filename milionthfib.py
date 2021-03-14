#https://www.codewars.com/kata/53d40c1e2f13e331fc000c26
import unittest

class Test(unittest.TestCase):
    def test_fib(self):
        assert fib(100) == fib(100)

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
def fibnaiv(n): #O(n)
    a = 0
    b = 1
    i = 1
    switch = False
    while i < n:
        if switch == False:
            a += b
            switch = True
        else:
            b += a
            switch = False
        i += 1
    if a > b: return a
    return b


def main():
    print(fib(10001))
    #print(fibnaiv(10))
    #print(43466557686938914862637500386755014010958388901725051132915256476112292920052539720295234060457458057800732025086130975998716977051839168242483814062805283311821051327273518050882075662659534523370463746326528 - 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875)


if __name__ == '__main__':
    main()
