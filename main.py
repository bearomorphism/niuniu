from itertools import combinations
import random

# 發出任意五張，每個點數的機率

DOCK = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4

'''
Result range from 0 to 10 (inclusive)
'''
def count_score(hand):
    for cards in combinations(hand, 3):
        if sum(cards) % 10 == 0:
            ret = sum(hand)
            if ret % 10 == 0:
                return 10
            return ret % 10
    return 0


def randomized_version():
    N = 10000000 # 自己改數字
    result = [0] * 11
    for _ in range(N):
        hand = random.choices(DOCK, k=5)
        result[count_score(hand)] += 1

    # print result
    total_times = sum(result)
    print(f'{total_times=}')
    for score, times in enumerate(result):
        print(f'{score=}, {times=}, ratio={times/total_times}')


def main():
    # There are 2,598,960 ways that 5 items chosen from a set of 52 can be combined.
    result = [0] * 11
    for hand in combinations(DOCK, 5):
        result[count_score(hand)] += 1

    # print result
    total_times = sum(result)
    for score, times in enumerate(result):
        print(f'{score=}, {times=}, ratio={times/total_times}')


# main()
randomized_version()
