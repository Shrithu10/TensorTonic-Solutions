def linear_layer_forward(X: list, W: list, b: list) -> list:
    """
    Returns the affine transformation for every input row.
    """
    n = len(X)
    d_out = len(b)
    d_in = len(W)
    
    Y = [[0.0 for _ in range(d_out)] for _ in range(n)]
    
    for i in range(n):
        for j in range(d_out):
            s = 0.0
            for k in range(d_in):
                s += X[i][k] * W[k][j]
            Y[i][j] = s + b[j]
            
    return Y
