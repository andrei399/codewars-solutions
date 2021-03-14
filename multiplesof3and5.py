
def solution(number):
    sum = 0
    if number < 3:
        return 0
    for i in range(3, number):
        if i % 3 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i
    return sum


def main():
    print(solution(10))

if __name__ == '__main__':
    main()