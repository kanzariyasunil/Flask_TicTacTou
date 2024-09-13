from flask import Flask,render_template,redirect,url_for,request

app = Flask(__name__)

game_board = ['']*9
current_player = 'X'

def check_winner(board):
    winnig_combinations = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]]
    for combo in winnig_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != '':
            return board[combo[0]]
    return None
    
def reset_game():
    global game_board,current_player
    game_board = [''] * 9
    current_player = 'X'


@app.route('/',methods = ['GET','POST'])
def index():
    global game_board,current_player
    winner = check_winner(game_board)

    if request.method == "POST":
        cell = int(request.form['cell'])

        if game_board[cell] == '' and not winner:
            game_board[cell] = current_player
            current_player = 'O' if current_player == "X" else "X"
        winner = check_winner(game_board)

        if winner or '' not in game_board:
            return redirect(url_for('index'))
    return render_template('index.html',board = game_board , winner = winner , current_player = current_player)
@app.route('/reset',methods=["POST"])
def reset():
    reset_game()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)