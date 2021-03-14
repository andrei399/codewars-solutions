#https://www.codewars.com/kata/52c4dd683bfd3b434c000292/train/python
def palindrome(nr):
    return int(str(nr)[::-1]) == nr
def incremental(n):
    last = n % 10
    n //= 10
    if last == 0 and n % 10 == 9:
        n //= 10
        last = 9
    while n:
        if n % 10 + 1 != last: return False
        last = n % 10
        n //= 10
    return True
def decremental(n):
    last = n % 10
    n //= 10
    while n:
        if n % 10 - 1 != last: return False
        last = n % 10
        n //= 10
    return True
def samedigit(n):
    digit = n % 10
    n //= 10
    while n:
        if n % 10 != digit: return False
        n //= 10
    return True
def is_interesting(number, awesome_phrases):
    if number < 98: return 0
    if number == 98 or number == 99: return 1
    powersof10 = [100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000, 1000000000000, 10000000000000, 100000000000000, 1000000000000000, 10000000000000000, 100000000000000000, 1000000000000000000]
    eight_power_of_ten = [800, 8000, 80000, 800000, 8000000, 80000000, 800000000]
    seven_power_of_ten = [700, 7000, 70000, 700000, 7000000, 70000000, 700000000]
    if number in powersof10: return 2
    if number in awesome_phrases: return 2
    if number in seven_power_of_ten: return 2
    if number in eight_power_of_ten: return 2
    if palindrome(number): return 2
    if samedigit(number): return 2
    if incremental(number): return 2
    if decremental(number): return 2
    if number+1 in powersof10: return 1
    if number+2 in powersof10: return 1
    if number+1 in awesome_phrases: return 1
    if number+2 in awesome_phrases: return 1
    if palindrome(number +1): return 1
    if palindrome(number +2): return 1
    if incremental(number+1): return 1
    if incremental(number+2): return 1
    if decremental(number+1): return 1
    if decremental(number+2): return 1
    if samedigit(number + 1): return 1
    if samedigit(number + 1): return 1
    if number+1 in seven_power_of_ten: return 1
    if number+2 in seven_power_of_ten: return 1
    if number+1 in eight_power_of_ten: return 1
    if number+2 in eight_power_of_ten: return 1
    return 0


def main():
    print(is_interesting(11210, [1000000]))

if __name__ == '__main__':
    main()
