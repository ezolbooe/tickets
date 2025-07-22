def find_most_frequent_word(text):
    """
    Returns the most frequently occurring word in a string of text.
    Words are considered case-insensitive and punctuation should be ignored.
    """
    import re
    words = text.lower().split()
    word_counts = {}

    for word in words:
        word = re.sub(r'\W+', '', word)  # remove punctuation
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Return the word with the highest count
    most_frequent = max(word_counts, key=word_counts.get)
    return most_frequent