#https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python
def valid_parentheses(string):
    count = 0
    for char in string:
        if char == '(':
            count += 1
        if char == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0

def main():
    print(valid_parentheses('dl(e)iiku)lrqs(ih(av)klssm'))

if __name__ == '__main__':
    main()