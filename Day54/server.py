from flask import Flask

app= Flask(__name__)

game_list=[{
    "id":1,
    "name":"LOL"
    },{
    "id":2,
    "name":"WarCraft"
    }]
@app.route("/")
def home():
    return "Home Page"
@app.route("/games")
def games():
    return game_list
@app.route("/games/<game>")
def show_game(game):
    for g in game_list:
        if g["name"]==game:
             return  f"Name:{game}"
    return f"Name:{game} not found"
if __name__=="__main__":
    app.run(debug=True)
