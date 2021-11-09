import cv2
import numpy as np
#board_input = [
#    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
#    ['0', 'm', '0', '0', '0', '0', '0', '0', '0', '0'],
#    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
#    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
#    ['0', '0', '0', '0', 'm', '0', 'h', '0', '0', '0'],
#    ['0', '0', '0', '0', '0', '0', 'h', '0', '0', '0'],
#    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
#    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
#    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
#    ['0', '0', 'x', 'x', 'x', '0', '0', '0', 'm', '0']
#]

#board_input = [['0', 'm', 'x', '0', '0', 'm', '0', '0', '0', '0'], ['0', 'm', 'x', '0', 'm', 'x', 'x', 'x', 'x', '0'], ['0', '0', 'm', '0', '0', '0', '0', '0', 'm', '0'], ['m', 'm', 'm', 'm', 'm', '0', '0', '0', 'x', '0'], ['x', 'x', 'x', 'm', '0', 'm', 'm', '0', 'x', '0'], ['0', '0', 'm', '0', 'm', '0', '0', '0', 'x', '0'], ['0', 'm', 'm', 'm', '0', '0', 'm', '0', 'x', '0'], ['0', 'x', 'x', 'x', 'm', '0', '0', '0', 'x', '0'], ['0', '0', 'm', '0', '0', 'm', '0', 'm', '0', '0'], ['m', '0', 'm', '0', '0', '0', 'm', '0', '0', 'm']]
already_shot = []
board_output = []

def get_hunt_shot(board_input):
    #print("finding boat")
    global board_output
    board_output = []

    #print(f'boardinput {board_input}')

    def reset_board(board, string = False):
        for i in range(10):
            a = []
            for i in range(10):
                if string: a.append(('0'))
                else: a.append((0))
            board.append(a)

    def get_max_2d_arr(array):
        max_val = np.amax(array)
        for i in range(len(array)):
            if max_val in array[i]:
                return [i, array[i].index(max_val)]
        return -1

    def display_board(board):
        print()
        print()
        for i in board:  
            for j in board[board.index(i)]:
                print(board[board.index(i)][i.index(j)], end=' ')
            print()

    boats_left = [2,3,3,4,5]

    '''
    m   miss
    x   sunk
    0   empty
    '''

    def fit_boats():
        i_m = [0,1,1,1,0,-1,-1,-1]
        j_m = [1,1,0,-1,-1,-1,0,1]
        board_processing()
        for boat_length in boats_left:
            for i in range (10):
                for j in range(10):
                    free_spaces = 0
                    for l in range(boat_length):
                        try: 
                            a = board_input[i][j+l]
                            hits_around_me = 0
                            for p in range (len(i_m)):
                                try:
                                    b = board_input[i+i_m[p]][j+l+j_m[p]]
                                    if i+i_m[p]>=0 and j+l+j_m[p]>=0:
                                        if b == 'x': hits_around_me += 1
                                except IndexError:
                                    pass
                                except Exception as e:
                                    print(f"some other error {e}")
                            if a == '0' and hits_around_me == 0: free_spaces += 1
                        except IndexError:
                            pass
                        except:
                            print('some other error')
                    if free_spaces == boat_length:
                        for l in range(boat_length):
                            try: 
                                a = board_output[i][j+l]
                                board_output[i][j+l] += 1
                                #if i == 9 and j == 0: print('h')
                            except IndexError:
                                pass
                            except Exception as e:
                                print(f"some other error {e}")
                    #vertical
                    free_spaces = 0
                    for l in range(boat_length):
                        try: 
                            a = board_input[i+l][j]
                            hits_around_me = 0
                            for p in range (len(i_m)):
                                try:
                                    b = board_input[i+i_m+l[p]][j+j_m[p]]
                                    if i+i_m+l[p]>=0 and j+j_m[p]>=0:
                                        if b == 'x': hits_around_me += 1
                                except:
                                    pass
                            if a == '0' and hits_around_me == 0: free_spaces += 1
                        except IndexError:
                            pass
                        except:
                            print('some other error')
                    if free_spaces == boat_length:
                        for l in range(boat_length):
                            try: 
                                a = board_output[i+l][j]
                                board_output[i+l][j] += 1
                            except IndexError:
                                pass
                            except Exception as e:
                                print(f'some other error{e}')
        board_processing()

    def board_processing():
        for i in range(len(board_input)):
            for j in range(len(board_input[i])):
                if board_input[i][j] == 'x':
                    i_modded = [i,i+1,i+1,i+1,i,i-1,i-1,i-1]
                    j_modded = [j+1,j+1,j,j-1,j-1,j-1,j,j+1]
                    for k in range(len(i_modded)):
                        try:
                            if i_modded[k] >= 0 and j_modded[k] >= 0:
                                board_output[i_modded[k]][j_modded[k]] = 0
                        except:
                            pass

    def visual_board(board):
        img = np.zeros((10,10,3), dtype=np.uint8)
        for i in range(len(board)):  
            for j in range(len(board[i])):
                max_val = np.amax(board_output)
                if board_input[i][j] == 'h': result = (0,255,255)
                elif board_input[i][j] == 'x': result = (0,0,255)
                elif board_input[i][j] == 'm': result = (255,255,0)
                else:
                    val1 = 255-(board[i][j]*(255/max_val))
                    result = (val1,val1,val1)
                img[i][j] = result
        img = cv2.resize(img,(0,0),fx=80,fy=80,interpolation= cv2.INTER_NEAREST)
        cv2.imshow('board',img)
        cv2.waitKey(0)

    reset_board(board_output)
    fit_boats()
    #board_processing()
    #display_board(board_input)
    #print('\nboard probability values')
    #display_board(board_output)
    #print(get_max_2d_arr(board_output))
    result = get_max_2d_arr(board_output)
    return result

def display_probabilites():
    print()
    for i in board_output:  
        for j in board_output[board_output.index(i)]:
            print(board_output[board_output.index(i)][i.index(j)], end=' ')
        print()

def get_target_shot(board_input):
    #print("targetting boat")
    hit_positions = []
    miss_positions = []
    for i in range(len(board_input)):
        for j in range(len(board_input[i])):
            if board_input[i][j] == 'h': 
                hit_positions.append([i,j])
            if board_input[i][j] == 'm': 
                miss_positions.append([i,j])
    i_m = [0,1,0,-1]
    j_m = [-1,0,1,0]
    to_hit_queue = []
    if len(hit_positions) == 1:
        for hit_pos in hit_positions:
            for index in range(len(i_m)):
                try:
                    pos_m = [hit_pos[0]+i_m[index], hit_pos[1]+j_m[index]]
                    a = board_input[pos_m[0]][pos_m[1]]
                    if pos_m not in miss_positions and pos_m[0]>=0 and pos_m[1]>=0:
                        #to_hit_queue.append(pos_m)
                        return pos_m
                except:
                    pass
        #return to_hit_queue[0]
    elif len(hit_positions) > 1:
        to_hit_queue = []
        h1 = hit_positions[0]
        h2 = hit_positions[1]

        for pos in hit_positions:
            if h1[0] == h2[0]: 
                #print('horizontal')
                #horizontal
                try: 
                    a = [pos[0],pos[1]+1]
                    b = board_input[a[0]][a[1]]
                    to_hit_queue.append([a[0],a[1]])
                except: pass
                try: 
                    a = [pos[0],pos[1]-1]
                    b = board_input[a[0]][a[1]]
                    to_hit_queue.append([a[0],a[1]])
                except: pass
            if h1[1] == h2[1]: 
                #print('vertical')
                #veritcal
                try: 
                    a = [pos[0]+1,pos[1]]
                    b = board_input[a[0]][a[1]]
                    to_hit_queue.append([a[0],a[1]])
                except: pass
                try: 
                    a = [pos[0]-1,pos[1]]
                    b = board_input[a[0]][a[1]]
                    to_hit_queue.append([a[0],a[1]])
                except: pass
        #print(f'before hit queue {to_hit_queue}')
        '''for i in range (2):
            for pos in to_hit_queue:
                print('h')
                if 'h' in board_input[pos[0]][pos[1]] or 'm' in board_input[pos[0]][pos[1]] or pos[0] < 0 or pos[1] < 0 or pos in already_shot:
                    to_hit_queue.remove(pos)
        print(f'to hit queue {to_hit_queue}')
        print(f'why {to_hit_queue[-1] in already_shot}')
        print(f'already shot queue {already_shot}')
        print(f'shot_value {board_input[to_hit_queue[-1][0]][to_hit_queue[-1][1]]}')
    
        for i in range(len(to_hit_queue)):
            if to_hit_queue[i] not in already_shot:
                already_shot.append(to_hit_queue[i])
                return to_hit_queue[i]'''
        for pos in to_hit_queue:
            if board_input[pos[0]][pos[1]] == '0':
                return pos
                
        
            
    
def select_execute_mode(bi):
    hit_count = 0
    for i in range(len(bi)):
        for j in range(len(bi[i])):
            if bi[i][j] == 'h': 
                hit_count+=1
    if hit_count > 0:
        return get_target_shot(bi)
    else:   
        return get_hunt_shot(bi)