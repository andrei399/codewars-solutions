#https://www.codewars.com/kata/55c04b4cc56a697bb0000048/train/python
def scramble(s1, s2):
    for character in s2:
        place = s1.find(character)
        if place >= 0:
            s1 = s1[0:place] + s1[place + 1:]
        else: return False
    return True

def main():
    s1 = 'hello'
    a = [char for char in s1]
    print(a)

if __name__ == '__main__':
    main()
#['javscripts', 'javscrips'] should equal False
#['scriptjavx', 'scripjavx'] should equal False
