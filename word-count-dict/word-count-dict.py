def word_count_dict(sentences: list) -> dict:
    """
    Returns a dictionary of token counts.
    """
    # Write code here
    word_count = {}
    for s in sentences:
        for t in s:
            word_count[t] = word_count.get(t, 0) + 1
    return word_count