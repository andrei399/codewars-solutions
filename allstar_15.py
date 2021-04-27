#https://www.codewars.com/kata/586560a639c5ab3a260000f3/train/python
def rotate(str_):
    return_string = []
    for _ in range(len(str_)):
        str_ = str_[1:] + str_[0]
        return_string.append(str_)
    return return_string

def main():
    print(rotate("Hello") == ["elloH", "lloHe", "loHel", "oHell", "Hello"])

if __name__ == '__main__':
    main()