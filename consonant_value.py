#https://www.codewars.com/kata/59c633e7dcc4053512000073/train/python
import re
def solve(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    sum = 0
    s = re.split('a|e|i|o|u', s)
    for _ in range(len(s)):
        try:
            s.remove('')
        except:
            break
    max_sum = 0
    for letter_group in s:
        sum = 0
        for letter in letter_group:
            if letter not in 'aeiou':
                sum += alphabet.index(letter) + 1
        if sum > max_sum:
            max_sum = sum
    # sum = [alphabet.index(letter) + 1 for letter in s if letter not in 'aeiou' and alphabet.index(letter) + 1 > ] Attemt at list comprehensioning it, probably should use a map() function or sth
    return max_sum


def main():
    print(solve('zodiacs'))

if __name__ == '__main__':
    main()