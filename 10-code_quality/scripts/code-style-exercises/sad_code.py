"""
You need to refactor the function zero_insert to pass
the pep8 and pylint checks
"""
import numpy as np
def zero_insert(x, n):
    r = np.array([])
    zeroes = np.zeros(n)
    for i in np.arange(0, len(x)):
        r = np.append(r, x[i])
        if i < len(x)-1:
            r = np.append(r, zeroes)
    return r
if __name__ == "__main__":
    print(zero_insert([1,2,3,4,5], 4))

