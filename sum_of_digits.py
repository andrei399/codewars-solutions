#https://www.codewars.com/kata/541c8630095125aba6000c00/solutions/python
digital_root = lambda n: digital_root(sum(int(i) for i in str(n))) if n > 9 else n