# 총 카드와 지금 뽑을 카드 개수를 받아서,
# 이보다 하나 적은 카드 개수에서 만들 수 있는 수 리스트를 받아서(재귀n-1),
# 내가 지금 만든 것 중에 겹치지 않으면 개수 추가,
# 만든 수 개수와 만든 수 리스트를 반환
def card_arrange(cards, k, dupl):
    if k < 1:
        return []
    elif k == 1:
        return cards
    else:
        card_arrange(cards, k-1, dupl)
        for num1 in cards:
        return # ...


n = int(input())
k = int(input())
cards = []
for _ in range(n):
    cards += input()
print(card_arrange(n, k, cards))