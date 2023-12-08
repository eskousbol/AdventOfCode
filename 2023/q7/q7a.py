class Hand:
  def __init__(self, cards, payout):
    self.cards = cards
    self.payout = payout

    card_counts = {}
    for char in cards:
      if char not in card_counts.keys():
        card_counts[char] = 1
      else:
        card_counts[char] += 1
    
    values = list(card_counts.values())
    values.sort(reverse=True)
    
    self.rank = values[0]
    if len(values) > 1 and values[1] == 2:
      self.rank += 0.5

  def __str__(self):
    return f"Cards {self.cards} with payout {self.payout}"


# return true if hand1 wins, false if hand2 wins
def compare_hands(hand1, hand2):
  card_order = ['1','2','3','4','5','6','7','8','9','T','J','Q','K','A']
  if hand1.rank > hand2.rank:
    return True
  elif hand1.rank < hand2.rank:
    return False
  else:
    for i in range(len(hand1.cards)):
      if card_order.index(hand1.cards[i]) > card_order.index(hand2.cards[i]):
        return True
      elif card_order.index(hand1.cards[i]) < card_order.index(hand2.cards[i]):
        return False
  return True

def main():
  f = open("./q7_input.txt", "r")

  hands = []
  winnings = 0
  for line in f:
    data = line.strip().split(' ')
    hands.append(Hand(data[0], int(data[1])))

  sorted_hands = []
  for i in range(len(hands)):
    for j in range(len(sorted_hands)):
      if compare_hands(sorted_hands[j], hands[i]):
        sorted_hands.insert(j, hands[i])
        break
    if hands[i] not in sorted_hands:
      sorted_hands.append(hands[i])

  for i in range(len(sorted_hands)):
    print(sorted_hands[i])
    winnings += (i + 1) * sorted_hands[i].payout
  print(winnings)

main()