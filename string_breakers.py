#https://www.codewars.com/kata/59d398bb86a6fdf100000031/train/python
string_breakers = lambda n, st: '\n'.join([st.replace(' ', '')[i:i+n] for i in range(0, len(st.replace(' ', '')), n)])