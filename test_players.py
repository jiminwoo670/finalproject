from players import Players
from get_question import GetQuestions
from player_individual import PlayerIndividual
def test_adding_players():
    """no assert function but checks to see if the adding players method works.
    also check if the return_player_name method in PlayerIndividual class works.
    also checks if the Game class recieves the player objects
    """
    player = Players()
    player.add_players()
    object_lst = player.return_player_objects()
    for players in object_lst:
        print(players.return_player_name())

def test_find_player():
    """checks if finding player works
    will use this in the future for seeing player stats and leaderbaord
    in the case when name is not found is tested by inputing a name not inputted when asking for player names
    """
    player = Players()
    player.add_players()
    assert player.find_player("jimin") == "jimin"
    assert player.find_player("cheese") == "Player not found"



def main():
    test_adding_players()
    test_find_player()


main()

