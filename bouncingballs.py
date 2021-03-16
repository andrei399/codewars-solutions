#https://www.codewars.com/kata/5544c7a5cb454edb3c000047
import unittest
def bouncing_ball(h, bounce, window):
    if h < 0 or bounce <= 0 or bounce >= 1 or window > h:
        return -1
    bounces = 0
    while h > window:
        h *= bounce
        bounces += 2
    return bounces - 1

def testing(h, bounce, window, exp):
    actual = bouncing_ball(h, bounce, window)
    print(actual == exp)


def main():
    testing(2, 0.5, 1, 1)
    testing(3, 0.66, 1.5, 3)
    testing(30, 0.66, 1.5, 15)
    testing(30, 0.75, 1.5, 21)
    testing(3, 1, 1.5, -1)

if __name__ == '__main__':
    main()