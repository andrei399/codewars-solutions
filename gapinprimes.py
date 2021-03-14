#https://www.codewars.com/kata/561e9c843a2ef5a40c0000a4/train/python - bugged.
def is_prime(nr):
    if nr == 2 or nr == 3: return True
    if nr % 2 == 0 or nr % 3 == 0: return False
    i = 5
    while i**2 <= nr:
        if nr % i == 0 or nr % (i + 2) == 0: return False
        i += 6
    return True

def gap(g, m, n):
    last_prime = -100
    for i in range(m, n + 1):
        ipr = is_prime(i)
        if i == 101: print('101 prime = ', ipr)
        if ipr == True and i - g == last_prime: return [last_prime, i]
        if ipr == True: last_prime = i
    return None

def main():
    print (gap(2,3474749660383,341550071728321))

if __name__ == '__main__':
    main()
