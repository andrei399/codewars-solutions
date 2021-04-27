#https://www.codewars.com/kata/598d91785d4ce3ec4f000018/train/python
def name_value(my_list):
    letter_index = 'abcdefghijklmnopqrstuvwxyz'
    return_list = []
    i = 0
    for string in my_list:
        i += 1
        sum = 0
        for letter in string:
            try:
                sum += letter_index.index(letter) + 1
            except:
                pass
        return_list.append(sum*i)
    return return_list

def main():
    print(name_value(["codewars","abc","xyz"]))

if __name__ == '__main__':
    main()