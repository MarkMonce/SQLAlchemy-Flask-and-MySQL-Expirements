# a = (1, 2)
# print (a[0])

# b=a

# print(b)

# a=(100,200)

# print(b)
# print(a)


import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Hand:
    def __init__(self):
        self.cards = []


    def add_card(self, card):
        self.cards.append(card)
        self.display_hand_value()  # Display the value of the hand each time a card is added

    def show_hand(self):
        return ', '.join(map(str, self.cards))

    def hand_value(self):
        total = 0
        ace_count = 0
        card_values = {'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
        for card in self.cards:
            if card.value.isdigit():  # For numeric cards, convert to int
                total += int(card.value)
            elif card.value == 'Ace':  # Count aces separately since they can have multiple values
                ace_count += 1
            else:
                total += card_values[card.value]
        # Adjust for Aces as needed (if total is greater than 21 and there are aces, treat them as 1)
        while total > 21 and ace_count > 0:
            total -= 10  # Reduce the value of the Ace from 11 to 1
            ace_count -= 1
        return total
    
    def total_cards(self):
        return len(self.cards)
    
    def display_hand_value(self):
        print(f"Current hand value: {self.hand_value()}\n")

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop() if self.cards else None

class Shoe:
    def __init__(self, number_of_decks):
        self.cards = []
        self.card_count = {}
        self.number_of_decks = number_of_decks
        self.build_shoe()

    def build_shoe(self):
        for _ in range(self.number_of_decks):
            deck = Deck()
            self.cards.extend(deck.cards)
        self.count_cards()
        self.shuffle_shoe()

    def shuffle_shoe(self):
        random.shuffle(self.cards)

    def count_cards(self):
        self.card_count = {}
        for card in self.cards:
            card_str = str(card)
            if card_str in self.card_count:
                self.card_count[card_str] += 1
            else:
                self.card_count[card_str] = 1

    def draw_card(self):
        if self.cards:
            card = self.cards.pop()
            card_str = str(card)
            if card_str in self.card_count:
                self.card_count[card_str] -= 1
            print(f"Card drawn: {card}. Cards remaining of this type: {self.card_count[card_str]}")
            return card
        print("No more cards in the shoe.")
        return None

    def display_remaining_cards(self):
        for card, count in sorted(self.card_count.items()):
            print(f"{card}: {count}")

    def total_cards(self):
        return len(self.cards)

    def count_specific_card(self, suit, value):
        card_str = f"{value} of {suit}"
        return self.card_count.get(card_str, 0)

# Example usage
print('New Hand: \n')
shoe = Shoe(6)  # Shoe with 6 decks
hand = Hand()
hand.add_card(shoe.draw_card())
hand.add_card(shoe.draw_card())
hand.add_card(shoe.draw_card())

# print(hand.show_hand())
# print("Remaining cards in shoe:")
# shoe.display_remaining_cards()
# print(f"Total cards remaining: {shoe.total_cards()}")
# print(f"Number of 'Ace of Spades' remaining: {shoe.count_specific_card('Spades', 'Ace')}")

print(hand.show_hand())
# print(f'You have {hand.cards_in_hand()} cards in your hand')
# print("Remaining cards in shoe:")
# shoe.display_remaining_cards()
print(f'\nTotal Cards in Hand {hand.total_cards()}\n')

if hand.hand_value() <= 21:
    print("Congratulations: You have not busted.....\n")
else:
    print ("BUST!!! You LOSE!!!\n")
print(f"Total cards remaining: {shoe.total_cards()}\n")
print("\n\nRANDOM COUNT OF SPECIFIC CARD AS EXAMPLE\n")
print(f"Number of 'Ace of Spades' remaining: {shoe.count_specific_card('Spades', 'Ace')}")

