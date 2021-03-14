#https://www.codewars.com/kata/541af676b589989aed0009e7
def count_change(money, coins):
    ways = [1] + [0]*money
    for coin in coins:
        for i in range(coin, money + 1):
            ways[i] += ways[i-coin]
    return ways[money]

def main():
    print(count_change(4, [1,2]))

if __name__ == '__main__':
    main()
