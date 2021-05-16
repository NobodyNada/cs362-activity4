# Returns the number of words in the given string.
# Any non-whitespace character is considered a word character.
def wordcount(s):
    # Split on whitespace and count non-empty results.
    return len([word for word in s.split() if word])
