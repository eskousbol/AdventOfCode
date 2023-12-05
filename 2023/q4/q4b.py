import re

class GameCard:
  def __init__(self, game_number, ticket_numbers, winning_numbers):
    self.game_number = game_number
    self.winning_numbers = winning_numbers
    self.ticket_numbers = ticket_numbers
    self.cards = 0
    for number in winning_numbers:
      if number in ticket_numbers:
        self.cards += 1
  
  def __str__(self):
    return  f"Game {self.game_number + 1} ({self.cards} cards won)"

def checkCard(cards, card_number):
  total_cards = 1
  if (card_number >= len(cards)):
    return 0

  matches = cards[card_number].cards
  
  for number in range(1, matches + 1):
    if (card_number + number < len(cards)):
      total_cards += checkCard(cards, card_number + number)
  
  return total_cards

def main():
  f = open("./q4_input.txt", "r")

  total_cards = 0
  cards = []
  game_number = 1
  for line in f:
    all_numbers = line.split(':')[1].strip()
    all_numbers_split = all_numbers.split('|')

    winning_numbers = re.findall("\d+", all_numbers_split[0]) 
    ticket_numbers = re.findall("\d+", all_numbers_split[1])

    game_card = GameCard(game_number, winning_numbers, ticket_numbers)
    cards.append(game_card)
    game_number += 1

  for i in range(0, game_number):
    total_cards += checkCard(cards, i)
  print(total_cards)

main()