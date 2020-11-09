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
    fib1 =0
    fib2 = 1
    for __ in range(n+1):
        fib1, fib2 = fib2, fib1 + fib2
    t2 = time()
    print('time simple ',t2-t1)
    return fib1

def climb_req(n):
    M = {0: 0, 1: 1}
    if n in M:
        return M[n]
    M[n] = climb_req(n - 1) + climb_req(n - 2)
    return M[n]


if __name__ == "__main__":
    n = 20
    pr = cProfile.Profile()
    pr.enable()
    print(climb_matrix(n))
    print(climb_simple(n))
    t1 = time()
    print(climb_req(n+1))
    t2 = time()
    print('time req ', t2 - t1)
    pr.disable()
    pr.print_stats(sort="calls")
