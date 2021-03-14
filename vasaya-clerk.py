#https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8
def tickets(people):
    if people[0] != 25: return 'NO'
    twenties = 0
    fifties = 0
    moneys = []
    i = 0
    for money in people:
        moneys.append(money)
        if money == 50:
            if twenties == 0: return 'NO'
            else:
                 twenties -= 1
                 fifties += 1
        elif money == 100:
            if fifties >= 1 and twenties >= 1:
                twenties -= 1
                fifties -= 1
            elif twenties >= 2:
                 twenties -= 2
            else:
                 return 'NO'
        else:
             twenties += 1
    return moneys

def main():
    print(tickets([25, 25, 50]))
    print(tickets([25, 50, 100]))

if __name__ == "__main__":
    main()
