import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    x=len(A)
    y=len(A[0])
    res=np.empty((y,x))
    for i in range(0,x):
        for j in range(0,y):
            res[j][i]=A[i][j]
    return res
    
