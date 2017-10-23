"""Kata: Good vs Evil.

#1 Best Practices Solution by M.Gaidamaka, nickmariner

def goodVsEvil(good, evil):

    points_good = [1, 2, 3, 3, 4, 10]
    points_evil = [1, 2, 2, 2, 3, 5, 10]

    good = sum([int(x)*y for x, y in zip(good.split(), points_good)])
    evil = sum([int(x)*y for x, y in zip(evil.split(), points_evil)])

    result = 'Battle Result: '

    if good < evil:
        return result +'Evil eradicates all trace of Good'
    elif good > evil:
        return result + 'Good triumphs over Evil'
    else:
        return result + 'No victor on this battle field'
"""


def good_vs_evil(good, evil):
    """Return whether good or evil won, given numbers of forces."""
    good_scores = [1, 2, 3, 3, 4, 10]
    evil_scores = [1, 2, 2, 2, 3, 5, 10]

    good_nums = good.split()
    evil_nums = evil.split()
    good_total = 0
    evil_total = 0

    def find_score(nums, scores):
        """Get total score for forces."""
        tally = 0
        for i in range(len(nums)):
            tally += int(nums[i]) * scores[i]
        return tally

    good_total = find_score(good_nums, good_scores)
    evil_total = find_score(evil_nums, evil_scores)
    print(good_total)
    print(evil_total)

    outcome = ['Battle Result: No victor on this battle field',
               'Battle Result: Good triumphs over Evil',
               'Battle Result: Evil eradicates all trace of Good']
    if good_total == evil_total:
        return outcome[0]
    elif good_total > evil_total:
        return outcome[1]
    else:
        return outcome[2]
