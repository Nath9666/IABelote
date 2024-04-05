class Player:
    def __init__(self, name):
        self.name = name
        self.donneur = False
        self.hand = []

    def receive_card(self, card):
        self.hand.append(card)

    def play_card(self, index):
        return self.hand.pop(index)