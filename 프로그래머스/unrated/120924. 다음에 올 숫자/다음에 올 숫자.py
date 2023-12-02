def solution(common):
    answer = 0
    if (common[-1] - common[-2] == common[-2] - common[-3]):
        return common[-1] + (common[-1] - common[-2])
    return common[-1] * (common[-1] / common[-2])