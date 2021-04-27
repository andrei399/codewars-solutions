#https://www.codewars.com/kata/546f922b54af40e1e90001da

def alphabet_position(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return_string = ''
    for letter in text:
        if letter.lower() in alphabet:
            if letter != ' ':
                return_string += str(alphabet.find(letter.lower())+1) + ' '
            else:
                return_string += ' '
    if return_string.endswith(' '):
        return return_string[:-1]
    return return_string


def main():
    print(alphabet_position("The sunset sets at twelve o' clock.") == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")

if __name__ == '__main__':
    main()

#20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11
#20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11