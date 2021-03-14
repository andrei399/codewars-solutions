#https://www.codewars.com/kata/52449b062fb80683ec000024
def generate_hashtag(s):
    if not s:
        return False
    s = '#' + ''.join(word[0].upper() + word[1:].lower() for word in s.split())
    if len(s) > 140:
        return False
    return s

def main():
    print(generate_hashtag('bagamias pula'))

if __name__ == "__main__":
    main()
