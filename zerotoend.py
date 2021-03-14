#https://www.codewars.com/kata/52597aa56021e91c93000cb0
#broken KATA
def move_zeros(array):
    pos = []
    for i in range(len(array)):
        if array[i] is False: pos.append(i)
        elif array[i] is 0:
            array.remove(0)
            array.append(0)
    for removers in pos:
        array = array[0:removers] + [False] + array[removers:-1]
    return array
#retarded kata

def main():
    print(move_zeros([0,1,None,2,False,1,0]), ' should be: [1,None,2,False,1,0,0]')

if __name__ == "__main__":
    main()
