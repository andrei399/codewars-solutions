#https://www.codewars.com/kata/5264d2b162488dc400000001/train/python
def spin_words(sentence):
    sentence = str(sentence).split()
    finished_sentence = ''
    for word in sentence:
        if len(word) < 5:
            finished_sentence += word + ' '
        else:
            finished_sentence += ''.join(reversed(word)) + ' '
    return finished_sentence[:-1]

def main():
    print(spin_words('Hey fellow warriors'))

if __name__ == '__main__':
    main()