import sys

num_of_sgcard = int(input())

cards_numbers = set(input().split())

cards_numbers

num_of_test_card = int(input())

test_cards = input().split()

test_cards

print(' '.join('1' if test_card in cards_numbers else '0' for test_card in test_cards)) 