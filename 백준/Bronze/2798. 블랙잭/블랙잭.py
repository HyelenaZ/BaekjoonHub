def blackjack(n, m, cards):
    max_sum = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                card_sum = cards[i] + cards[j] + cards[k]
                if card_sum <= m:
                    max_sum = max(max_sum, card_sum)
    return max_sum

n, m = map(int, input().split())
cards = list(map(int, input().split()))

if not (3 <= n <= 100 and 10 <= m <= 300000):
    print("입력값이 유효하지 않음")
else:
    result = blackjack(n, m, cards)
    print(result)