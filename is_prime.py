#https://www.codewars.com/kata/5262119038c0985a5b00029f/train/python
def is_prime(nr):
    if nr < 2: return False
    elif nr == 2 or nr == 3: return True
    elif nr % 2 == 0 or nr % 3 == 0: return False
    i = 5
    while i**2 <= nr:
        if nr % i == 0 or nr % (i + 2) == 0: return False
        i += 6
    return True