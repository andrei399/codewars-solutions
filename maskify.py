#https://www.codewars.com/kata/5412509bd436bd33920011bc
def maskify(cc):
    return '#' * (len(cc) - 4) + cc[-4:]

def main():
    print(maskify("4556364607935616"))

if __name__ == '__main__':
    main()