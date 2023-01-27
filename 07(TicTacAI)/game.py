from player import Human_Player,  Unbeatable_AI
# from player import Random_Comp_Player1
import time


class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)] #list comprehensioon to print a board..
        self.current_winner = None #checks/keeps track of any winner

    #we just print the board now
    def print_board(self):
        for row in [self.board[(i * 3) : (i+1) * 3] for i in range(3)]:
            print(f" |_{'_|_'.join(row)}_| ")

    @staticmethod
    def print_nums_board():  #board with indices on it
        number_board = [[str(i) for i in range(j*3 , (j+1) * 3)] for j in range(3)]
        for row in number_board:
            print(f" |_{'_|_'.join(row)}_| ")

    #this function will return the available number of moves
    def available_moves(self):
        moves = []
        for(i, spot) in enumerate(self.board):
            if spot == " ":
                moves.append(i)
            
        return moves

    def empty_spaces(self):
        return " " in self.board
    
    def num_empty_spaces(self):
        return self.board.count(" ")

    #making a function to make a move
    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square,letter):
                    self.current_winner = letter
            return True 
        return False


    def winner(self,square,letter):
        #this function checks the winning possibilities
        #checking rows
        row_index = square // 3
        row = self.board[row_index*3:(row_index + 1)* 3]

        if all([spot == letter for spot in row]):
            return True

        #checking columns
        column_index = square % 3
        column = [self.board[column_index + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        #checking diagonals
        #diagonals occur at 0,2,4,6,8
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0 , 4 , 8]]   #left diagonal
            if all([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2 , 4 , 6]]   #right disgonal
            if all([spot == letter for spot in diagonal2]):
                return True


        #if nothing is true
        return False

        
def play(game, x_player, o_player, print_game = True):
        
        if print_game:
            game.print_nums_board()

        letter = "X"  #assigning a starting letter

            #now we iterate while the game has empty spaces
        while game.empty_spaces():
            if letter == "X":
                square = x_player.get_move(game)
            else:
                square = o_player.get_move(game)

            if game.make_move(square, letter):
                    if print_game:
                        print(f"{letter} makes a move to square {square}")
                        game.print_board() #shows board after performing a move
                        print("")    # a line
                    
                    if game.current_winner:
                        if print_game:
                            print(f"{letter} wins") 
                        return letter

                    #alternating the turn
                    letter = "O" if letter == "X" else "X"  # switches player
        
            time.sleep(1)
        if print_game:
            print("It's a tie!!")

    

if __name__ == '__main__':
        x_player = Human_Player("X")
        o_player = Unbeatable_AI("O")
        u = TicTacToe()
        play(u, x_player, o_player, print_game = True)
