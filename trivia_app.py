from flask import Flask, request


app = Flask(__name__)
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
@app.route('/play_game')
def play_game():


    return"""
    
    """

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

