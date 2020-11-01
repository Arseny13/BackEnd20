import numpy as np
import cProfile
from time import  time

def climb_matrix(n: int) -> int:
    t1 = time()
    a = np.array([[1, 1], [1, 0]])
    result = np.linalg.matrix_power(a, n)[0][0]
    t2 = time()
    print('time matr', t2 - t1)
    return result

def climb_simple(n:int) -> int:
    if n in (1, 2):
        return 1
    t1 = time()
    fib1 = fib2 = 1
    for i in range(2, n+1):
        fib1, fib2 = fib2, fib1 + fib2
    t2 = time()
    print('time simple ',t2-t1)
    return fib2


if __name__ == "__main__":
    pr = cProfile.Profile()
    pr.enable()
    print(climb_simple(10005))
    print(climb_matrix(10005))
    pr.disable()
    pr.print_stats(sort="calls")
