import math

def elu(x: list, alpha: float = 1.0) -> list:
    """
    Returns ELU applied elementwise to the input values.
    """
    res=[]
    for i in x:
        if(i<0):
            res.append(alpha*(math.exp(i)-1))
        else:
            res.append(i)
    return res