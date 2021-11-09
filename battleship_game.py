import random
import cv2

class colors:
    BLUE = '\033[94m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    YELLOW = '\033[93m'
    PURPLE = '\033[35m'

manual = False
manual_board = [
    ['0','0','s','s','0','0','0','0','0','0'],
    ['s','0','0','0','0','0','0','0','0','0'],
    ['s','0','0','0','0','0','0','0','0','0'],
    ['s','0','0','0','0','0','0','0','0','0'],
    ['s','0','0','0','0','s','0','0','0','0'],
    ['0','0','0','0','0','s','0','0','s','0'],
    ['0','0','0','0','0','s','0','0','s','0'],
    ['0','0','0','0','0','0','0','0','s','0'],
    ['0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','s','s','s','s','s','0']
]



#print(board)

boats = [2,3,3,4,5]

def add_vectors(v1,v2):
    return [v1[0]+v2[0],v1[1]+v2[1]]

def multiple_vector(v1,m):
    return [v1[0]*m,v1[1]*m]


def visual_board():
    for row in board:
        for a in row:
            if a == 's': print(f'{colors.BLUE}s{colors.ENDC}', end=' ')
            else: print(a,end=' ')
        print()

def get_pos_val(position):
    return board[position[0]][position[1]]

def get_board():
    global positions_of_boats
    global board
    board = []
    boats = [2,3,3,4,5]
    positions_of_boats = {}
    for i in range(10):
        row = []
        for i in range(10):
            row.append(0)
        board.append(row)

    positions_of_boats = {}
    boat_index = 0
    for boat in boats:
        im = [-1,0,1,1,1,0,-1,-1]
        jm = [1,1,1,0,-1,-1,-1,0]
        iteration = 0
        #print(f'boat{boats.index(boat)}')
        while True:
            iteration += 1
            #print(f'\riteration {iteration}',end='')
            try:
                if random.randint(0,1) == 1:
                    addition_vector = [0,1]
                else:
                    addition_vector = [1,0]
                boat_positions = []
                pos = [random.randint(0,9),random.randint(0,9)]
                for i in range(boat):
                    new_pos = add_vectors(multiple_vector(addition_vector,i), pos)
                    x = board[new_pos[0]][new_pos[1]]
                    boat_positions.append(new_pos)
                surrounding_spaces = []
                free_count = 0
                #print(0)
                
                for boatpos in boat_positions:
                    alist = []
                    for i in range(len(im)):
                        try:
                            a = [boatpos[0]+im[i], boatpos[1]+jm[i]]
                            alist.append(a)
                            x = board[a[0]][a[1]]
                            surrounding_spaces.append(a)
                        except IndexError:
                            pass
                        except Exception as e:
                            print(f"some other error {e}")
                    #print('alist\t\t',boatpos,alist)
                #print('available\t',positions_of_boats,'\n',surrounding_spaces)
                #input()
                    
                    
                #print(1)
                
                for i in range(len(surrounding_spaces)):
                    if board[surrounding_spaces[i][0]][surrounding_spaces[i][1]] != 's':
                        free_count += 1
                #print(2)
                #print(f'{free_count}free / {len(surrounding_spaces)}total')
                if free_count == len(surrounding_spaces):
                    #all surrounding spaces are empty and we can place the boat
                    for boatpos in boat_positions:
                        #print(f'before s{boatpos[0],boatpos[1]}')
                        board[boatpos[0]][boatpos[1]] = 's'
                    dict_insertion_index = boats.index(boat)
                    
                    positions_of_boats[boat_index] = boat_positions
                    
                    break
            except IndexError:
                pass
            except Exception as e:
                print(f"some other error {e}")
        boat_index += 1
    #print(board)
    if manual: return manual_board
    else: return board

def get_boat_positions(i):
    return positions_of_boats[i]

'''if __name__ == "__main__":
    print(board)'''