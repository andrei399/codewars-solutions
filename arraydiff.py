#https://www.codewars.com/kata/523f5d21c841566fde000009
def remove_all_values_from_list(a, val):
   return [value for value in a if value != val]

def array_diff(a, b):
    if not a or not b:
        return a
    for numberdiff in b:
        a = remove_all_values_from_list(a, numberdiff)
    return a



def main():
    print(array_diff([1, 2, 1], [1]))
    print(pow(2, 38))

if __name__ == "__main__":
    main()
