import chess
import chess.engine
from stockfish import Stockfish
import asyncio

engine = chess.engine.SimpleEngine.popen_uci("stockfish")


win = 0
loss = 0
draw = 0
a = input("Enter a valid chess move ")
SampleSize = 10 #Could be increased to increase the efficiency of our prediction
for i in range(SampleSize):
    board = chess.Board()
    print(board)
    board.push_san(str(a))

    while board.is_game_over() == False:

        apo = engine.play(board, chess.engine.Limit(time=0.01))
        board.push(apo.move)
        print(apo.move)


    print(board.result())
    if board.result() == "1-0":
        win = win + 1
    elif board.result() == "0-1":
        loss = loss + 1
    elif board.result() == "1/2-1/2":
        draw = draw + 1
    print("Wins",win)
    print("Losses",loss)
    print("Draws",draw)
    board.is_game_over() == False

winrate = win/SampleSize * 100
drawrate = draw/SampleSize * 100
print("Rate of winning = " + str(winrate)+"%")
print("Rate of draws = " + str(drawrate)+"%")
