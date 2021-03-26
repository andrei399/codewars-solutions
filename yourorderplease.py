#https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python
import re
def order(sentence):
    result_list = []
    for i in range(len(sentence.split())):
        result_list.append('')
    for word in sentence.split():
        result_list[int(re.findall(r'\d', word)[0]) - 1] = word
    return ' '.join(result_list)

def main():
    print(order("4of Fo1r pe6ople g3ood th5e the2") == "Fo1r the2 g3ood 4of th5e pe6ople")

if __name__ == '__main__':
    main()