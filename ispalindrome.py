def ispalindrome(s):
    return s == s[::-1]

def main():
    s = 'sdagsB'
    print(ispalindrome(s))

if __name__ == '__main__':
    main()
