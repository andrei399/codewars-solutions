#https://www.codewars.com/kata/53368a47e38700bd8300030d/train/python
def namelist(names):
    names_len = len(names)
    if names_len == 0:
        return ''
    if names_len == 1:
        return names[0]['name']
    return_string = names[0]['name']
    for i in range(1, names_len):
        if i == len(names) - 1:
            return return_string + ' & ' + names[i]['name']
        else:
            return_string += ', ' + names[i]['name']
    return return_string

def main():
    print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]))

if __name__ == '__main__':
    main()