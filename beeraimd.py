#https://www.codewars.com/kata/51e04f6b544cf3f6550000c1/train/python
def beeramid(bonus, price):
    beers = int(bonus//price)
    layers = 0
    for i in range(beers):
        beers -= i ** 2
        if beers >= 0:
            layers += 1
        else:
            return layers - 1    
    return layers

print(beeramid(9, 2))