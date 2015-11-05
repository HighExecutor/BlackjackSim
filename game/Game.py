__author__ = 'Mishanya'

from game.Deck import Shoe
from game.ActionTables import *
from game.Player import Player
from game.Hand import Hand
import numpy

class Game:
    def __init__(self, action_table, players, decks, init_bank, max_shuffles, max_win, min_bet):
        self.player = Player(action_table, init_bank)
        self.players = players
        self.decks = decks
        self.shoe = Shoe(decks)
        self.max_shuffles = max_shuffles
        self.init_bank = init_bank
        self.max_win = max_win
        self.min_bet = min_bet
        self.dealer_hand = Hand()

    def __call__(self, *args, **kwargs):
        shuffles = 0
        while shuffles < self.max_shuffles and 0 < self.player.bank < self.init_bank * self.max_win:
            print('---new shuffle---')
            print('bank: ' + str(self.player.bank))
            win = self.shuffle()
            print('win: ' + str(win))
            if win > 0:
                self.player.bank += win
            shuffles += 1
        return self.player.bank

    def shuffle(self):
        self.shoe = Shoe(self.decks)
        self.shoe.shuffle()
        self.bet = 0
        self.make_bet(self.min_bet)
        self.dealer_hand = Hand()
        self.player.hand = Hand()
        self.player.hit(self.shoe.deal())
        self.dealer_hand.append(self.shoe.deal())
        self.player.hit(self.shoe.deal())
        print("Player's hand:")
        self.player.hand.print()
        print("Dealer's hand:")
        self.dealer_hand.print()
        if self.player.hand.score() == 21:
            print("Blackjack")
            return self.blackjack()
        for _ in range(self.players - 1):
            self.shoe.deal()
            self.shoe.deal()
        dealer_state = self.dealer_state()
        shoe_state = self.shoe_state()
        print("Shoe count: " + str(self.shoe.count))
        return self.action(dealer_state, shoe_state, True)

    def make_bet(self, bet):
        self.player.bank -= bet
        self.bet += bet

    def action(self, dealer_state, shoe_state, canDoubled):
        player_state = self.player.state()
        act = self.player.act(player_state, dealer_state, shoe_state)
        if act == 's':
            print('stand')
            return self.stand()
        elif act == 'd' and canDoubled:
            print('double')
            return self.double()
        else:
            print('hit')
            return self.hit()

    def dealer_state(self):
        card = self.dealer_hand[0]
        if card.isAce():
            return '11'
        return str(card.val)

    def shoe_state(self):
        true_count = self.shoe.count / self.decks
        if true_count > 5:
            return 1
        if true_count < -5:
            return -1
        return 0

    def stand(self):
        self.dealer_play()
        if self.dealer_hand.score() > 21:
            print('Dealer over')
            return self.bet * 2
        return self.compare_hand()

    def hit(self):
        self.player.hit(self.shoe.deal())
        print("Player's hand")
        self.player.hand.print()
        cur_score = self.player.hand.score()
        if cur_score > 21:
            return self.over()
        if cur_score == 21:
            return self.stand()
        shoe_state = self.shoe_state()
        dealer_state = self.dealer_state()
        if cur_score > 21:
            pass
        return self.action(dealer_state, shoe_state, False)


    def over(self):
        print('player over')
        return 0

    def blackjack(self):
        return self.bet * 2.5

    def double(self):
        if self.player.bank > self.min_bet:
            self.make_bet(self.bet)
        return self.hit()

    def dealer_play(self):
        while self.dealer_hand.score() < 17:
            self.dealer_hand.append(self.shoe.deal())

    def compare_hand(self):
        dealer_score = self.dealer_hand.score()
        player_score = self.player.hand.score()
        print("dealer : " + str(dealer_score))
        print("player : " + str(player_score))
        if player_score > dealer_score:
            return self.bet * 2
        if player_score == dealer_score:
            return self.bet
        return 0

if __name__ == '__main__':
    #action_table, players, decks, init_bank, max_shuffles, max_win, min_bet
    # action_table = random_counted_strategy()
    action_table = basic_strategy()
    results = []
    for _ in range(100):
        game = Game(action_table, 7, 2, 100, 5, 2, 10)
        results.append(game())
    print("-------")
    loses = len([res for res in results if res <= 0])
    print('loses = ' + str(loses))
    print("result mean = " + str(numpy.mean(results)))
    print("result std = " + str(numpy.std(results)))
