import math
import mapping_algorithm
import battleship_game
from datetime import datetime

def all(xx):
    global errors
    game_finished_with_x_shots = []

    runs = 1
    errors = 0

    def add_vectors(v1,v2):
        return [v1[0]+v2[0],v1[1]+v2[1]]

    def test_adjacent(v1,v2,i):
        xm = [0,i,0,-i]
        ym = [i,0,-i,0]
        for j in range(len(xm)):
            if add_vectors(v1, [xm[j],ym[j]]) == v2:
                return True
        return False



    def display_game_board():
        for row in game_board:
            for x in row:
                if x == 'm': print(f'{battleship_game.colors.BLUE}m{battleship_game.colors.ENDC}',end=' ')
                elif x == 'h': print(f'{battleship_game.colors.YELLOW}h{battleship_game.colors.ENDC}',end=' ')
                elif x == 'x': print(f'{battleship_game.colors.RED}x{battleship_game.colors.ENDC}',end=' ')
                else: print(x,end=' ')
            print()

    for i in range(runs):
        #print('new run')
        actual_board = battleship_game.get_board()
        game_board = []
        for i in range(10):
            row = []
            for i in range(10):
                row.append('0')
            game_board.append(row)
        debug = False
        sunkboats = 0
        shot_count = 0
        while sunkboats < 5:
            
            if shot_count>=100:
                print("ERROR-------------------------------------------------------")
                print("ship locations:")
                battleship_game.visual_board()
                print("gameboard status:")
                display_game_board()
                print("probablity value chart:")
                mapping_algorithm.display_probabilites()
                errors += 0
                break
            else:
                #see if shot hit or miss
                shot_count+= 1
                algorithm_shot = (mapping_algorithm.select_execute_mode(game_board))
                #print('shot',shot_count,f'\t@{algorithm_shot}')
                #print('\ngame_board')
                #display_game_board()
                #input()
                
                if debug: print(f'\nshot at: {algorithm_shot}')
                if debug: input()
                if battleship_game.get_pos_val(algorithm_shot) == 's':
                    game_board[algorithm_shot[0]][algorithm_shot[1]] = 'h'
                else:
                    game_board[algorithm_shot[0]][algorithm_shot[1]] = 'm'

                #see if any boats are sunk
                hit_count = 0
                hit_positions = []
                for i in range(len(game_board)):
                    for j in range(len(game_board[i])):
                        if game_board[i][j] == 'h': 
                            hit_count+=1
                            hit_positions.append([i,j])
                for boat in battleship_game.positions_of_boats:
                    hits = 0
                    for boat_pos in battleship_game.positions_of_boats[boat]:
                        if boat_pos in hit_positions:
                            hits += 1
                    if hits == len(battleship_game.positions_of_boats[boat]):
                        for boat_pos in battleship_game.positions_of_boats[boat]:
                            game_board[boat_pos[0]][boat_pos[1]] = 'x'
                        sunkboats += 1
                if debug: print('\nship board')
                if debug: battleship_game.visual_board()
                if debug: input()

        #print('shot',shot_count,f'\t@{algorithm_shot}')
        #print('\ngame_board')
        #display_game_board()
        #print(f'{battleship_game.colors.BLUE}FINISHED WITH {shot_count} SHOTS{battleship_game.colors.ENDC}')
        print(f'\riter {battleship_game.colors.BLUE}{xx}{battleship_game.colors.ENDC}', end='')
        game_finished_with_x_shots.append(shot_count)

    result = sum(game_finished_with_x_shots)/len(game_finished_with_x_shots)
    #print(type(result))
    return(result)

def get_errors():
    return errors
'''
m   miss
x   sunk
0   empty
'''