def longest_positive_streak(nums: list[int]):
    max_streak = 0
    current = 0
    for n in nums:
        if n > 0:
            current += 1
            if current > max_streak:
                max_streak = current
        else:
            current = 0
    return max_streak
