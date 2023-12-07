from players import Players
from game import Game
from player_individual import PlayerIndividual
def main_test():
    player = Players()
    player.add_player()
    game = Game()
    print(game.test_getting_players())
    object_lst = player.return_player_objects()
    for players in object_lst:
        print(players.return_player_name())


main_test()

