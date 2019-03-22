from easyAI import TwoPlayersGame, Human_Player
from easyAI import AI_Player, Negamax
from Element import ElementClass
import random
class Battleship(TwoPlayersGame):


    def __init__(self, players):
        self.players = players
        self.nplayer = 1 # player 1 starts.
        self.board1=[]
        self.board2=[]
        self.l1=[]
        self.l2=[]
        self.nr_boats_hit1=0
        self.nr_boats_hit2=0
        self.nr_of_locations_hit1=0
        self.nr_of_locations_hit2=0
        self.score1=0
        self.score2=0


    def possible_moves(self):
        return [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,1),(1,2),(1,3),(1,4),
        (2,0),(2,1),(2,2),(2,3),(2,4),(3,0),(3,1),(3,2),(3,3),(3,4),(4,0),(4,1),(4,2),(4,3),(4,4)]

    def make_move(self, move):
        if self.nplayer==1:
            if move in self.l1:
                self.nr_of_locations_hit1+=1

            elif self.board2[move[0]][move[1]].type=='O':
                self.nr_of_locations_hit1+=1
                self.l1.append(move)

            elif  self.board2[move[0]][move[1]].type=='*':
                self.nr_boats_hit1+=1
                self.nr_of_locations_hit1+=1
                self.board2[move[0]][move[1]].destroy()
                self.l1.append(move)

        else:
            if move in self.l2:
                self.nr_of_locations_hit2+=1

            elif self.board1[move[0]][move[1]].type=='O':
                self.nr_of_locations_hit2+=1
                self.l2.append(move)

            elif  self.board1[move[0]][move[1]].type=='*':
                self.nr_boats_hit2+=1
                self.nr_of_locations_hit2+=1
                self.board1[move[0]][move[1]].destroy()
                self.l2.append(move)


    def win(self):
        if self.nr_boats_hit1==6 or self.nr_boats_hit2==6:
            return 1
        else:
             return 0

    def is_over(self): return self.win()
    def scoring(self):
        if self.nplayer==1:
            self.score1=self.nr_boats_hit1/self.nr_of_locations_hit1
            return self.score1
        elif self.nplayer==2:
            self.score2=self.nr_boats_hit2/self.nr_of_locations_hit2
            return self.score2

    def show(self):
        for i in range(5):
            print(str(self.board1[i])+'\n')
        print("Number of boats hit "+str(self.nr_boats_hit1))

    def generate_random_objects(self,board):
        i=0
        while (i<3):
            x=random.randint(0,4)
            y=random.randint(0,4)
            if board[x][y].type=='O':
                board[x][y].type='*'
                if y>0 and board[x][y-1].type=='O':
                    board[x][y-1].type="*"
                    i+=1
                elif y<4 and board[x][y+1].type=='O':
                    board[x][y+1].type='*'
                    i+=1
                elif x<4 and board[x+1][y].type=='O':
                    board[x+1][y].type='*'
                    i+=1
                elif x>0 and  board[x-1][y].type=='O':
                    board[x-1][y].type='*'
                    i+=1



    def initialize_board(self):
        for i in range(5):
            self.board1.append([])
            self.board2.append([])
            for j in range(5):
                self.board1[i].append(ElementClass('O'))
                self.board2[i].append(ElementClass('O'))


    def check(self):
        self.initialize_board()
        self.generate_random_objects(self.board1)
        self.generate_random_objects(self.board2)
    """    print('Self board 1:')
        print(self.board1)
        print("------------------------------")
        print('Self board 2:')
        print(self.board2)
    """
ai = Negamax(4) # The AI will think 13 moves in advance
game = Battleship( [ Human_Player(), AI_Player(ai) ] )
game.check()
history = game.play()
