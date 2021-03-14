#https://www.codewars.com/kata/5aec1ed7de4c7f3517000079
def first_n_smallest(arr, n):
    array = sorted(arr)
    array = array[:n]
    nsmallestarray = []
    for numbers in arr:
        if numbers in array:
            array.remove(numbers)
            nsmallestarray.append(numbers)
    return nsmallestarray


def main():
    print(first_n_smallest([1,2,3,4,5],3), ' should be: [1,2,3]')

if __name__ == "__main__":
    main()
