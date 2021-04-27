#https://www.codewars.com/kata/559a28007caad2ac4e000083
def fib(n):
    fib_sum = 0
    a = 1
    b = 1
    for _ in range(n-2):
        aux = a
        a += b
        b = aux
        fib_sum += a
    return fib_sum
def perimeter(n):
    return fib(n+1)*4 + 8 # I Have no IDEA why this works like this.
def main():
    print(perimeter(5))

if __name__ == '__main__':
    main()