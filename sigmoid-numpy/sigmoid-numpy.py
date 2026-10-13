import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    if(type(x)==list):
        a=np.array(x)
        return (1/(1+np.exp(-a))) 
    return (1/(1+np.exp(-x)))