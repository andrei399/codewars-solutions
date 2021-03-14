#https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python

def sum_of_intervals(intervals):
    pythonisacheatcode = []
    for interval in intervals:
        for i in range(interval[0], interval[1]):
            pythonisacheatcode.append(i)
    return len(set(pythonisacheatcode))



def main():
    print(sum_of_intervals([(1,     5), (6, 10)]), ' should be: 8')

if __name__ == '__main__':
    main()
