def findRelativeRanks(score):
    sorted_score = sorted(score, reverse=True)
    rank_map = {score: str(i+1) for i, score in enumerate(sorted_score)}
    top = ["Gold Medal", "Silver Medal", "Bronze Medal"]
    for i in range(min(3, len(score))):
        rank_map[sorted_score[i]] = top[i]
    return [rank_map[sc] for sc in score]
