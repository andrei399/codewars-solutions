#https://www.codewars.com/kata/5297bf69649be865e6000922/
def make_sentences(parts):
    parts_len = len(parts)
    for i in range(parts_len):
        if i != parts_len - 1:
            if parts[i+1] != ',' and parts[i+1] != '.':
                parts[i] += ' '
    for i in range(parts_len - 1, 0, -1):
        if parts[i] == '.' and parts[i-1] == '.':
            parts.remove('.')
    if parts[len(parts) - 1] != '.':
        parts.append('.')
    return ''.join(parts)

def main():
    print(make_sentences(['The', 'Earth', 'rotates', 'around', 'The', 'Sun', 'in', '365', 'days', ',', 'I', 'know', 'that', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']))

if __name__ == '__main__':
    main()