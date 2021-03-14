#https://www.codewars.com/kata/5541f58a944b85ce6d00006a



def productFib(prod):
    switch = False
    a = 0
    b = 1
    while True:
        if a * b == prod:
            if a > b: return [b, a, True]
            else: return [a, b, True]
        elif a * b > prod:
            if a > b: return [b, a, False]
            else: return [a, b, False]
        else:
            if switch == False:
                switch = True
                a += b
            else:
                switch = False
                b += a

def main():
    print(productFib(100))

if __name__ == "__main__":
    main()
