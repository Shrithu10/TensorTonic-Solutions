def remove_stopwords(tokens: list, stopwords: list) -> list:
    """
    Returns a list of tokens.
    """
    stopwords=set(stopwords)
    res=[]
    for i in range(0,len(tokens)):
        if tokens[i] not in stopwords:
            res.append(tokens[i])
    return res
            