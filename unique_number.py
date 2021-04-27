#https://www.codewars.com/kata/585d7d5adb20cf33cb000235/
from collections import Counter
arr = [ 1, 1, 1, 2, 1, 1 ]
print(Counter(arr).most_common()[-1][0])