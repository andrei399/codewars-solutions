#https://www.codewars.com/kata/556deca17c58da83c00002db
def tribonacci(signature, n):
    if n == 0: return []
    if n == 1: return signature[0]
    if n == 2:
        a = signature.pop(0)
        return a
    i = 2
    while i < n:
        signature.append(signature[i-2] + signature[i-1] + signature[i])
        i += 1
    return signature

def main():
    print(tribonacci([1, 1, 1], 10), '[1, 1, 1, 3, 5, 9, 17, 31, 57, 105]')

if __name__ == "__main__":
    main()
