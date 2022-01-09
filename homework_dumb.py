import copy
import matplotlib.pyplot as plt
import timeit

pos_infinity = float('inf')
neg_infinity = float('-inf')
up_left = (-1,-1)
up_right = (-1,1)
down_left = (1,-1)
down_right = (1,1)
board_dimension = 8
b_moves = [down_left, down_right]
w_moves = [up_left, up_right]
king_moves = [down_left, down_right, up_left, up_right]
opponent_color = {"BLACK":"WHITE", "WHITE":"BLACK"}
move_map = {'b':b_moves, 'w': w_moves, 'W':king_moves, 'B':king_moves}
opponent_coins = {'b':['W','w'], 'w':['b','B'],'B':['W','w'], 'W':['b','B']}
king_row = {'w':0,'b':board_dimension - 1}
board_positions = {(0, 1): 'b8', (0, 3): 'd8', (0, 5):'f8', (0, 7):'h8',
                   (1, 0): 'a7', (1, 2): 'c7', (1, 4): 'e7', (1, 6):'g7',
                   (2, 1): 'b6', (2, 3): 'd6', (2, 5): 'f6', (2, 7):'h6',
                   (3, 0): 'a5', (3, 2): 'c5', (3, 4): 'e5', (3, 6): 'g5',
                   (4, 1): 'b4', (4, 3): 'd4', (4, 5): 'f4', (4, 7): 'h4',
                   (5, 0): 'a3', (5, 2): 'c3', (5, 4): 'e3', (5, 6): 'g3',
                   (6, 1): 'b2', (6, 3): 'd2', (6, 5): 'f2', (6, 7): 'h2',
                   (7, 0): 'a1', (7, 2): 'c1', (7, 4): 'e1', (7, 6): 'g1',
                   }

class problem_struct:
    def __init__(self, game_type="SINGLE", ):
        self.game_type = game_type

    time_left = 0
    my_color = "BLACK"
    board = []
    board_size = board_dimension
    white_coins_pos = {}
    black_coins_pos = {}
    move_no = 0
    max_depth = 3

    def plot_board(self):
        self.move_no+=1
        for x in range(0,self.board_size):
            for y in range(0,self.board_size):
                if(self.board[x][y]=='B'):
                    plt.plot( (y), (0-x), 'o', color ='#17becf', markersize=25, label=board_positions[(x,y)])
                    plt.annotate(board_positions[(x, y)], ((y), (0 - x)), fontsize=12)
                elif (self.board[x][y] == 'b'):
                    plt.plot((y), (0-x), 'o', color='#1f77b4', markersize=25, label=board_positions[(x,y)])
                    plt.annotate(board_positions[(x,y)],( (y) , (0-x)), fontsize=12)
                elif (self.board[x][y] == 'W'):
                    plt.plot((y), (0-x), 'o', color='#ff9e6e', markersize=25, label=board_positions[(x,y)])
                    plt.annotate(board_positions[(x, y)], ((y), (0 - x)), fontsize=12)
                elif (self.board[x][y] == 'w'):
                    plt.plot((y), (0-x), 'o', color='#d44600', markersize=25, label=board_positions[(x,y)])
                    plt.annotate(board_positions[(x, y)], ((y), (0 - x)), fontsize=12)
                else:
                    if (x%2==0 and y%2!=0) or (x%2!=0 and y%2==0):
                        plt.plot((y), (0 - x), 'o', color='#c5dbad', markersize=25, label=board_positions[(x,y)])
                        plt.annotate(board_positions[(x, y)], ((y), (0 - x)), fontsize=12)
                    else:
                        plt.plot((y), (0 - x), 'o', color='#f0ebeb', markersize=25)


        plt.savefig("board_move" +str(self.move_no)+".png")


    def check_out_of_bounds(self, pos, move):
        x = pos[0] + move[0]
        y = pos[1] + move[1]
        if (x,y) not in board_positions:                    #need to check if this also works
            return False, (-1, -1)
        '''if x < 0 or x >= self.board_size or y <0 or y >= self.board_size:
            return False,(-1,-1)'''
        return True, (x,y)

    def map_coins(self):
        for i in range(0,self.board_size):
            for j in range(0,self.board_size):
                val =self.board[i][j]
                if val!='.':
                    if val == 'W' or val == 'w':
                        self.white_coins_pos[(i,j)]=val
                    elif val == 'b' or val == 'B':
                        self.black_coins_pos[(i,j)]=val
        #print(self.white_coins_pos,self.black_coins_pos)

    def reset_board(self):                                      # may not be required if you'll only use white_coin_pos and black_coin_pos
        for i in range(0,self.board_size):
            for j in range(0,self.board_size):
                self.board[i][j] = '.'

    def take_move_on_board(self,white_coin_pos,black_coin_pos):
        self.reset_board()
        for key,value in white_coin_pos.items():
            self.board[key[0]][key[1]]=value
        for key,value in black_coin_pos.items():
            self.board[key[0]][key[1]]=value
        self.white_coins_pos = white_coin_pos
        self.black_coins_pos = black_coin_pos

    def to_output_file(self, from_pos, moves_sequence, board_state):
        f2 = open("output_dumb.txt", "w")
        if len(moves_sequence)>1 or abs(from_pos[0] - moves_sequence[0][0])>1:              # jump moves chosen
            for to_pos in moves_sequence:
                output = "J " + str(board_positions[from_pos])+" "+ str(board_positions[to_pos])
                print(output)
                f2.write(output)
                f2.write("\n")
                from_pos = to_pos
        else:                                                                               # normal move chosen
            to_pos = moves_sequence[0]
            output = "E "+ str(board_positions[from_pos])+ " "+ str(board_positions[to_pos])
            print(output)
            f2.write(output)
            f2.write("\n")

        f3 = open("input_smart.txt", "w")
        self.take_move_on_board(board_state[0], board_state[1])
        f3.write("GAME\n")
        f3.write("BLACK\n")
        f3.write("23.3\n")
        for i in range(0, self.board_size):
            for j in range(0, self.board_size):
                f3.write(str(self.board[i][j]))
            f3.write("\n")





    def take_move(self, coin, jump, from_pos, to_pos, white_coin_pos, black_coin_pos):        # modifies board state according to move and returns
        new_white_state = copy.deepcopy(white_coin_pos)
        new_black_state = copy.deepcopy(black_coin_pos)
        if coin=='w' or coin=='W':
            if coin=='w' and to_pos[0]==0:
                white_coin_pos[from_pos] ='W'
                coin = 'W'# crowned king
            new_white_state[to_pos] = white_coin_pos[from_pos]
            del new_white_state[from_pos]
            if jump:
                del new_black_state[((from_pos[0]+to_pos[0])//2,(from_pos[1]+to_pos[1])//2)]  # deleting jumped coins
        if coin=='b' or coin=='B':
            if coin=='b' and to_pos[0]==7:                                                     # crowned king
                black_coin_pos[from_pos] ='B'
                coin = 'B'
            new_black_state[to_pos] = black_coin_pos[from_pos]
            del new_black_state[from_pos]
            if jump:
                del new_white_state[((from_pos[0]+to_pos[0])//2,(from_pos[1]+to_pos[1])//2)]   # need to delete jumped coins as well
        #print(new_white_state,new_black_state)
        return new_white_state, new_black_state, coin

    def is_empty_in_board(self,x,y, white_coin_pos, black_coin_pos):
        if (x, y) in white_coin_pos or (x, y)  in black_coin_pos:
            return False
        return True

    def whats_here(self,x,y,white_coin_pos, black_coin_pos):
        if (x, y) in white_coin_pos:
            return white_coin_pos[(x,y)]
        elif(x, y)  in black_coin_pos:
            return black_coin_pos[(x,y)]
        return '.'

    def score_board(self, color, state):
        white_coin_pos, black_coin_pos = state[0], state[1]
        points = 0
        if color == "BLACK":
            for key, value in black_coin_pos.items():
                if value.isupper():
                    points+=15
                else:
                    points+=10

            for key, value in white_coin_pos.items():
                if value.isupper():
                    points-=15
                else:
                    points-=10

        elif color == "WHITE":
            for key, value in white_coin_pos.items():
                if value.isupper():
                    points += 15
                else:
                    points += 10

            for key, value in black_coin_pos.items():
                if value.isupper():
                    points -= 15
                else:
                    points -= 10
        #print("for state color",color ,state,"point",points)
        return points

    def jump_recursive(self,pos,coin,white_coin_pos, black_coin_pos, jump_moves, final_jump_list ):
        #print("jump_recursive",pos,jump_moves)
        rec_flag = False
        for move in move_map[coin]:
            valid, (x, y) = self.check_out_of_bounds(pos, move)
            if valid:
                new_val = self.whats_here(x,y,white_coin_pos, black_coin_pos)  # new_val is coin at new move position
                if new_val in opponent_coins[coin]:  # opponents so we coin can jump
                    valid, (x, y) = self.check_out_of_bounds((x, y),
                                                             move)  #recursively call jump function to return sequence of jumps
                    if (valid):
                        #jump = self.board[x][y]

                        jump = self.whats_here(x, y, white_coin_pos, black_coin_pos)
                        if jump =='.':
                            rec_flag = True
                              # needs to be valid and empty
                            coin_jump_series = copy.deepcopy(jump_moves)
                            coin_jump_series.append((x, y))
                            tmp_white_state = copy.deepcopy(white_coin_pos)
                            tmp_black_state = copy.deepcopy(black_coin_pos)
                            new_white, new_black,new_coin = self.take_move(coin, True, pos, (x, y), tmp_white_state,
                                                                  tmp_black_state)
                            #print("coin",coin)
                            # if new_coin!=coin:
                            #     print("changed_to_king")
                            ret_list,(white_state,black_state) = self.jump_recursive((x, y), coin, new_white, new_black, coin_jump_series, final_jump_list)
                            if ret_list !=None:
                                final_jump_list.append((ret_list,(white_state,black_state)))

        if not rec_flag:                    #jump_moves.append(coin_jump_series)
            # if len(final_jump_list)==0:
            #     final_jump_list.append(jump_moves)
            return jump_moves, (white_coin_pos, black_coin_pos)
        else:
            return None, ({},{})


    def gen_coins_moves(self,pos, coin, state):                      # if you see any jump move ignore all other moves
        white_coin_pos, black_coin_pos = state[0], state[1]
        basic_moves =[]
        jump_moves = []
        for move in move_map[coin]:
            valid, (x,y) = self.check_out_of_bounds(pos, move)
            if valid:
                new_val = self.whats_here(x, y, white_coin_pos, black_coin_pos)                                  ## new_val is coin at new move position
                ##!check this maybe you need a temporary board copy here also ???
                if new_val in opponent_coins[coin]:                          # opponents coin so can jump
                    valid, (x,y) = self.check_out_of_bounds((x,y), move) # need to recursively call jump function to return sequence of jumps
                    if(valid):
                        jump = self.whats_here(x, y, white_coin_pos, black_coin_pos)
                        if jump == '.':
                            coin_jump_series=[]
                            coin_jump_series.append((x, y))
                            final_jump_list =[]
                            tmp_white_state = copy.deepcopy(white_coin_pos)
                            tmp_black_state = copy.deepcopy(black_coin_pos)
                            new_white, new_black, coin = self.take_move(coin, True, pos, (x, y), tmp_white_state, tmp_black_state)
                            self.jump_recursive((x,y),coin,new_white, new_black,coin_jump_series,final_jump_list)
                            if len(final_jump_list) == 0:
                                white_state, black_state, coin = self.take_move(coin, True, pos, (x, y), tmp_white_state, tmp_black_state)
                                final_jump_list.append(([(x, y)], (white_state, black_state)))
                            for moves_series in final_jump_list:
                                jump_moves.append(moves_series)
                elif new_val == '.' :                             # empty space basic move check pnly if no jump moves found. or else dont waste time populating this
                    tmp_white_state = copy.deepcopy(white_coin_pos)
                    tmp_black_state = copy.deepcopy(black_coin_pos)
                    white_state,black_state, coin = self.take_move( coin, False, pos, (x,y), tmp_white_state, tmp_black_state)
                    basic_moves.append(([(x,y)],(white_state,black_state)))
        return basic_moves, jump_moves

    def generate_board_moves(self, color, state):
        #do something
        white_coin_pos, black_coin_pos = state[0], state[1]
        all_moves = {}
        jump_moves = {}
        if color == "WHITE":
            #print("playing whites turn")
            for key,value in white_coin_pos.items():
                #print(key)
                tmp_white_state = copy.deepcopy(state[0])
                tmp_black_state = copy.deepcopy(state[1])
                tmp_state = (tmp_white_state, tmp_black_state)
                basic_moves, jumping_moves = self.gen_coins_moves(key, value, tmp_state)
                if(len(basic_moves)!=0):
                    all_moves[key]=basic_moves
                if (len(jumping_moves)!= 0):
                    jump_moves[key]=jumping_moves
                #print(all_moves[key], jump_moves[key] )

        elif color =="BLACK":
            #print("playing blacks turn")
            for key,value in black_coin_pos.items():
                #print(key)
                tmp_white_state = copy.deepcopy(state[0])
                tmp_black_state = copy.deepcopy(state[1])
                tmp_state = (tmp_white_state, tmp_black_state)
                basic_moves, jumping_moves= self.gen_coins_moves(key, value, tmp_state)
                if (len(basic_moves) != 0):
                    all_moves[key] = basic_moves
                if (len(jumping_moves) != 0):
                    jump_moves[key] = jumping_moves
                #print(self.understand_jump_moves(jump_moves[key]))
                #print(all_moves[key], jump_moves[key] )

        if(len(jump_moves)!=0):
            #print("hurray jumps possible")
            # for key,value in jump_moves.items():
            #     print(key,"value", value)
                # for moves in value:
                #     print(moves)
                #     print("\n")
            return jump_moves, True
        else:
            #print("yippes some basic moves",all_moves)
            return all_moves, False


    def terminal_test(self, state,depth):
        ##! need to check if all pawns blocked also
        white_coin_pos,black_coin_pos=state[0],state[1]
        if depth > self.max_depth:
            return True
        if len(white_coin_pos)==0 or len(black_coin_pos)==0 :
            return True
        else:
            return False


    def alpha_beta_search(self, state):
        depth = 0
        path_list =[]

        v, from_pos, action, ret_state = self.max_value(state,(-8,-8),[(-7, -7)], neg_infinity, pos_infinity, depth,path_list)
        print("final_eval", v)
        return from_pos, action, ret_state  ##! based on the value v chosen which action is to be taken

    def max_value(self, state, from_pos, action_taken, alpha, beta, depth,path_list):
        depth+=1
        action = action_taken
        ret_from_pos = from_pos
        ret_state = state

        #print("depth", depth)

        if self.terminal_test(state,depth):
            v_s = self.score_board(self.my_color, state)
            #print("move", action_taken)
            #print("path_list FROM MAX",path_list, v_s, state,"\n")
            return v_s, ret_from_pos, action, state
        v = neg_infinity
        gen_temp_state = copy.deepcopy(ret_state)
        my_actions, was_jump = self.generate_board_moves(self.my_color, gen_temp_state)
        #print("my_action", my_actions)
        for a_key,a_value in my_actions.items():
            #print(a_key, "value", a_value)
            for (move, state_temp) in a_value:
                temp_v = v
                path_list.append(move)
                tmp_white_state = copy.deepcopy(state_temp[0])
                tmp_black_state = copy.deepcopy(state_temp[1])
                tmp_state = (tmp_white_state,tmp_black_state)
                tmp_move = copy.deepcopy((move))
                v_m, from_pos_m, action_m, state_m = self.min_value(tmp_state, a_key, tmp_move, alpha,beta,depth, path_list)
                path_list.pop()
                v = max(v, v_m)
                if v!= temp_v:
                    action = move
                    ret_state = state_temp
                    ret_from_pos = a_key
                if v >= beta:
                    return v, ret_from_pos, action, ret_state
                alpha = max(alpha,v)
        return v, ret_from_pos, action, ret_state

    def min_value(self, state, from_pos, action_taken, alpha, beta, depth, path_list ):
        depth+= 1
        action = action_taken
        ret_from_pos = from_pos
        ret_state = state
        #print("depth",depth)
        if self.terminal_test(state, depth):
            #print("move", action_taken, "from", from_pos, "board state",state)
            v_s = self.score_board(self.my_color, state)
            #print("path_list FROM MIN", path_list, v_s, "\n")
            return v_s, ret_from_pos, action, state
        v = pos_infinity
        gen_temp_state = copy.deepcopy(ret_state)
        opp_actions, was_jump = self.generate_board_moves(opponent_color[self.my_color], gen_temp_state)
        #print("opp_action", opp_actions)
        for a_key, a_value in opp_actions.items():
            #print(a_key, "value", a_value)
            for (move, state_temp) in a_value:
                temp_v = v
                path_list.append(move)

                tmp_white_state = copy.deepcopy(state_temp[0])
                tmp_black_state = copy.deepcopy(state_temp[1])
                tmp_state = (tmp_white_state, tmp_black_state)
                tmp_move = copy.deepcopy(move)
                v_m, from_pos_m, action_m, state_m =self.max_value(tmp_state, a_key, tmp_move, alpha, beta, depth, path_list)
                path_list.pop()
                v = min(v, v_m)
                if v != temp_v:
                    action = move
                    ret_state = state_temp
                    ret_from_pos = a_key
                if v <= alpha:
                    #print("something")
                    return v, ret_from_pos, action, ret_state
                beta = min(beta,v)
        return v, ret_from_pos, action, ret_state



def main():
    starttime = timeit.default_timer()
    f = open("input_dumb.txt", "r")
    #f2 = open("output.txt", "w")

    game_type = f.readline().rstrip()
    problem = problem_struct(game_type)
    problem.my_color = f.readline().rstrip()
    problem.time_left = f.readline()
    problem.time_left= float(problem.time_left)
    for i in range(0,problem.board_size):
        problem.board.append([ i for i in f.readline().rstrip()])
    #print(problem.game_type)
    #print(problem.my_color)
    #print(problem.time_left)
    #print(problem.board)
    problem.map_coins()
    problem.plot_board()
    #problem.generate_board_moves(problem.my_color,(problem.white_coins_pos,problem.black_coins_pos))
    if problem.game_type == "SINGLE":
        result_moves = problem.generate_board_moves(problem.my_color,(problem.white_coins_pos,problem.black_coins_pos))[0]
        start_pos = next(iter(result_moves))
        moves_seq = result_moves[start_pos][0][0]
        board_state = result_moves[start_pos][0][1]
        #print("moves_seq",moves_seq)
        problem.to_output_file(start_pos, moves_seq,board_state)

    elif problem.game_type == "GAME":
        chosen_move = problem.alpha_beta_search((problem.white_coins_pos, problem.black_coins_pos))
        problem.to_output_file(chosen_move[0],chosen_move[1],chosen_move[2])

    print("The time difference is :", timeit.default_timer() - starttime)


if __name__ == "__main__":
    main()