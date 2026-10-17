def interaction_features(X: list) -> list:
    """
    Returns original features followed by unique pairwise products.
    """
    res= [] 
    for row in X:
        new_row = list(row)
        num_features = len(row)
        for i in range(num_features):
            for j in range(i + 1, num_features):
                new_row.append(row[i] * row[j])
                
        res.append(new_row)
        
    return res