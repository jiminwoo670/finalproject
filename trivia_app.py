from flask import Flask, request,redirect, url_for
from players import Players
from player_individual import PlayerIndividual

app = Flask(__name__)
players = Players()

@app.route('/')
def home():
    return """
    <html><body>
             <h1>Welcome to the Jimin's Trivia Game </h1>
             <br>
             <a href="/instructions">Instructions</a>
             <br><br>
             <a href="/play_game">Play_Game</a>
    """

@app.route('/play_game', methods=["GET", "POST"])
def play_game():
    players_list = request.args.getlist('players')
    if request.method == 'POST':
        if 'start_game' in request.form:
            return redirect(url_for('start_game', players=players_list))

    return """
     <form action=/add_players method="post">
        <label for="player_name">Enter Player Name:</label>
        <input type="text" id="player_name" name="player_name">
        <button type="submit">Add Player</button>
        </form>
        <form action=/start_game method="get">
        <button type="submit" name="start_game">Start Game</button>
        <input type="hidden" name="players" value="{{ players|join(',') }}">
        </form>
    """

@app.route('/start_game')
def start_game():

    name_and_scores = []



    for player in players.return_player_objects():
        name_and_scores.append({player.return_player_name(): player.get_player_score()})

    return f"Players and Scores: {', '.join(str(item) for item in name_and_scores)}"

@app.route('/add_players', methods=["POST"])
def add_players():
    if request.method == 'POST':
        # Get the player name from the form
        player_name = request.form.get('player_name')

        # Add the player to the Players instance
        players.add_players(player_name)

    # Get the current list of players
    players_list = players.return_player_objects()


    # Redirect to the /play_game route with the updated list of players in the URL
    return redirect(url_for('play_game', players=players_list))

@app.route('/instructions')
def instructions():
    return """
    Hello players, this game is very similar to CDSK's trivia board game. Each player will take turns
    <br>
    answer trivia question. Each trivia question is associated with a category in which you will be asked 
    <br>
    on a scale of 1 to 3, how well you know that category. Depending on how well you know that category, 
    <br>
    you will earn points. Example: On a scale of 1 to 3 you choose 2 for the science category,
    """

if __name__ == "__main__":
    app.run(host="localhost", debug=True)
