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
# V if yes, draw another card
# if no, end game- open all cards compare scores
# V if dealer has less than 17, they must draw another card
# v ace can be 1 or 11 depending on the score
import random

def draw_card(hand):
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  hand.append(random.choice(cards))

def calculate_score(hand):
  score = sum(hand)
  
  if 11 in hand and score > 21:
    hand[hand.index(11)] = 1
    return score
  elif score > 21:
    score = 0
    return score
  elif score == 21:
    return score
  else:
    return score


def compare_score(user_score, dealer_score, dealer_hand):
  if user_score > dealer_score:
    print("You win!")
    print(f"your score is {user_score}, higher than the dealer's {dealer_score}")
    print(f"dealer's hand: {dealer_hand}")
    
  elif user_score < dealer_score:
    print("you lose!")
    print(f"your score is {user_score}, lower than the dealer's {dealer_score}")
    print(f"dealer's hand: {dealer_hand}")
  else:
    print("it' a draw!")
    print(f"your score is {user_score}, same as the dealer's {dealer_score}")
    print(f"dealer's hand: {dealer_hand}")


def new_game():
  game_over = False

  user_hand = []
  dealer_hand = []

  for _ in range(2):
    draw_card(user_hand)
    draw_card(dealer_hand)

  dealer_hand_view = [str(dealer_hand[0])]

  if sum(dealer_hand) < 17:
    draw_card(dealer_hand)
    dealer_hand_view.append('X')
    dealer_hand_view.append('X')
  else:
    dealer_hand_view.append('X')
    
  user_score = calculate_score(user_hand)
  dealer_score = calculate_score(dealer_hand)

  if user_score == 0 or dealer_score == 0 or user_score > 21:
    print("game over")
    print(f"your hand: {user_hand} your score: {user_score}")
    print(f"dealer hand: {dealer_hand} dealer score: {dealer_score}")
    game_over = True
    
  while not game_over:
    
    
    print(f"Your hand is {user_hand}, your score is {user_score}")
    print(f"Dealer hand is {dealer_hand_view}")
    
    draw_another = input("Do you want to draw another card? 'y' or 'n': ")
    if draw_another == 'y':
      draw_card(user_hand)
      user_score = calculate_score(user_hand)
      
      if user_score == 0 or user_score > 21:
        print("game over")
        print(f"your hand: {user_hand} your score: {user_score}")
        print(f"dealer hand: {dealer_hand} dealer score: {dealer_score}")
        game_over = True
    else:
      compare_score(user_score, dealer_score, dealer_hand)
      game_over = True

  play_again = input("would you like to play again? 'y' or 'n': ")
  if play_again == 'y':
    new_game()
  else:
    print("goodbye")
new_game()