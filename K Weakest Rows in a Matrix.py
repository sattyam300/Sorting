def kWeakestRows(mat, k):
    strength = [(sum(row), idx) for idx, row in enumerate(mat)]
    strength.sort()
    return [idx for _, idx in strength[:k]]
