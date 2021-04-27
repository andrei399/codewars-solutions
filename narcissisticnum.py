#https://www.codewars.com/kata/5287e858c6b5a9678200083c
def narcissistic( value ):
    return sum(int(x)**len(str(value)) for x in str(value)) == value


def main():
    print(narcissistic(153))

if __name__ == '__main__':
    main()
