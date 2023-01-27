import random
import math

class Player:
    def __init__(self,letter):
        #for letter X or O
        self.letter = letter
    
    def get_move(self,game): #next move based on the game
        pass

class Random_Comp_Player(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):   #a random move is played by the computer
        square = random.choice(game.available_moves())
        return square

class Human_Player(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_move = False
        value = None
        while not valid_move:
            square = input(f"{self.letter}'s turn. Input move(0-8)")
            
            #here we are trying to check the validity of our move by casting it to an intege0 otherwise invalidr
            #if the spot is empty then also the move is invalid

            try:
             value = int(square)
             if value not in game.available_moves():
                 raise ValueError
             valid_move = True
            except ValueError:
                print("Invalid input!!")
  
        return value 

class Unbeatable_AI(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())  #randomly chooses a space
        else:
            #implementing minimax algorithm from here to get square
            square = self.minimax(game, self.letter)["position"]
        return square
    
    def minimax(self, state, player):
        max_player = self.letter
        other_player = "O" if player == "X" else "X"

        #checking if previous move is a winner
        if state.current_winner == other_player:
            #returning score and position
            return {"position" : None, "score" : 1 * (state.empty_spaces()+1) if other_player == max_player else -1 * (state.empty_spaces() + 1) }
        elif not state.empty_spaces(): #nobody won
            return {"position": None,
                    "score": 0}

        if player == max_player:
            best = {"position": None , "score": -math.inf} #each score should be maximized
        else:
            best = {"position": None , "score": math.inf}  

        for possible_move in state.available_moves():
            #step1: make a move and try that spot
            state.make_move(possible_move, player)
            #step2: stimulate a game using minimax by recursion after making that move
            sim_score = self.minimax(state, other_player) #other player move is being simulated
            
            #step3: UNDO the move
            state.board[possible_move] = " "
            state.current_winner = None
            sim_score["position"] = possible_move

            #step4: update the dictionary of positon and score
            if player == max_player:
                if sim_score["score"] > best["score"]: #maximising the max player
                    best = sim_score
            else:
                 if sim_score["score"] < best["score"]:
                        #minimising the other playe
                        best = sim_score    
        return best  
