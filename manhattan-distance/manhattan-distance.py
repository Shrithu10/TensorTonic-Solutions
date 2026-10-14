import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    xx=np.array(x)
    yy=np.array(y)
    new=xx-yy
    pos=(new<0)
    new[pos]*=-1
    return float(np.sum(new))