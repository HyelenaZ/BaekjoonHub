from itertools import combinations

def find_blackjack(N, M, cards):
    nearest_M = 0
    for comb in combinations(cards, 3):
        current_sum = sum(comb)
        if current_sum <= M and current_sum > nearest_M:
            nearest_M = current_sum
    return nearest_M

N, M = map(int, input().split())
cards = list(map(int, input().split()))

result = find_blackjack(N, M, cards)
print(result)