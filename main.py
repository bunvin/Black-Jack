#black jack rules
#the deck is unlimited in size
#there are no jokers
#the jack/queen/king all count as 10
# V #the ace can count as 11 or 1 
#the cards in the list have equal probability of being drawn
#cards are not removed from the deck as they are drawn
#the computer is the dealer
# V if the computer gets a blackjack (0), you lose
# V If the user gets a blackjack (0), you win
# V If you go over 21, you lose
# V If the computer goes over 21, you win
# If none of the above, compare scores, highest wins
#if the score is the same, it's a draw
#the game ends when the user decides to stopdrawing or someone => 21

#start- 2 cards each open, dealer 1 close
#ask if user wants to draw another card
#if yes, draw another card
#if no, end game- open all cards compare scores
# V if dealer has less than 17, they must draw another card
# v ace can be 1 or 11 depending on the score
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card(hand):
  hand.append(random.choice(cards))

#improve printing
def calculate_score(hand):
  score = sum(hand)
  
  if 11 in hand and score > 21:
    hand[hand.index(11)] = 1
    return score
    
  elif score > 21:
    print("you lose")
    return game_over == True
    
  elif score == 0:
    print("you win")
    return game_over == True
    
  else:
    return score

#improve printing
def compare_score(user_score, dealer_score):
  if user_score > dealer_score:
    print("you win")
  elif user_score < dealer_score:
    print("you lose")
  else:
    print("draw")


def new_game():
  game_over = False

  user_hand = []
  dealer_hand = []
  
  user_hand = [random.choice(cards), random.choice(cards)]
  dealer_hand = [random.choice(cards), random.choice(cards)]
  dealer_hand_view = [str(dealer_hand[0])]

  if sum(dealer_hand) < 17:
    dealer_hand.append(random.choice(cards))
    dealer_hand_view.append('X')
    dealer_hand_view.append('X')
  else:
    dealer_hand_view.append('X')

  user_score = calculate_score(user_hand)
  dealer_score = calculate_score(dealer_hand)

  print(f"Your hand is {user_hand}, your score is {user_score}")
  print(f"Dealer hand is {dealer_hand_view}")

  while not game_over:
    draw_another = input("Do you want to draw another card? 'y' or 'n': ")
    if draw_another == 'y':
      draw_card(user_hand)
      user_score = calculate_score(user_hand)
      print(f"Your hand is {user_hand}, your score is {user_score}")
      print(f"Dealer hand is {dealer_hand_view}")
    else:
      compare_score(user_score, dealer_score)
      game_over = True

new_game()