import numpy as np
def find(z,A):
    index=np.unravel_index(abs(A-z).argmin(), A.shape)
    print(index)
    print(A[index])
a = np.random.randint(0, 100, (208, 26))
print(a)
find(160,a)