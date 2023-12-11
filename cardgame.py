import random
class Card:
    
    def __init__(self, suit, value) -> None:
        self.suit = suit
        self.value = value
    
    def description(self)-> str:
        return f'{self.value} of {self.suit}'
    



class Deck:
    def __init__(self) -> None:
        self._suits = ['Hearts','Diamonds','Clubs','Spades']
        self._values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self._cards = []
        for x in self._values:
            for i in self._suits:
                self._cards.append(Card(i, x))
    def shuffle(self)-> None:
        random.shuffle(self._cards)
    def deal(self)-> list[str]:
        return self._cards.pop()
        
    def description(self)-> str:
        return f"{len(self._cards)} cards in the deck"

if __name__ == "__main__":
    deck = Deck()
    card = deck.deal()
    print(card.description())
    deckshuf = deck.shuffle()
    print(deck.description())