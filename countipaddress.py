#https://www.codewars.com/kata/526989a41034285187000de4/
#efficient solution rather than pretty. (also import ipaddress exists.)
def ips_between(start, end):
    start = [int(x) for x in start.split('.')]
    end = [int(x) for x in end.split('.')]
    return (end[0] * 16777216 + end[1] * 65536 + end[2] * 256 + end[3]) - (start[0] * 16777216 + start[1] * 65536 + start[2] * 256 + start[3])


def main():
    print(ips_between("20.0.0.10", "20.0.1.0"))


if __name__ == '__main__':
    main()
