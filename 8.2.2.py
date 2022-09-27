from typing import List
from random import randint
def transferring_columns(matr: List[List[int]]) -> List[List[int]]:
    for arr in matr:
      arr[0], arr[-1] = arr[-1], arr[0]
return matr
n: int = int(input())
matr = [[randint(1, 9) for i in range(n)]] * n
transferring_columns(matr)
