def sortSentence(s):
    words = s.split()
    sorted_words = sorted(words, key=lambda x: int(x[-1]))
    return ' '.join(word[:-1] for word in sorted_words)
