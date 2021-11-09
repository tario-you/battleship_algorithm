import run_algorithm_on_game
from datetime import datetime
from threading import Thread
import battleship_game
import time

runs = 6700

sum_num = 0
start_time = 0
i = 0
durations = []
finished = True
loop = True

time.sleep(1)

potential_timeouts = [[['0', '0', 's', 's', '0', '0', '0', '0', '0', '0'], ['s', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['s', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['s', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['s', '0', '0', '0', '0', 's', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', 's', '0', '0', 's', '0'], ['0', '0', '0', '0', '0', 's', '0', '0', 's', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', 's', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', 's', 's', 's', 's', 's', '0']]]

def run():
    global finished
    finished = False
    global sum_num
    global i
    val = run_algorithm_on_game.all(i+1)
    if val != 100:
        sum_num += val
    finished = True
    print(f'\riter {battleship_game.colors.BLUE}{i}{battleship_game.colors.ENDC}',end='')
    i += 1

def timer():
    global start_time
    global loop
    while not finished:
        if start_time == 0:
            start_time = datetime.now()
        elif not finished and start_time != 0:
            current_duration = (datetime.now() - start_time).total_seconds()
            if current_duration == 5: #longer than one second
                print(f"\n{battleship_game.colors.YELLOW}Timeout{battleship_game.colors.ENDC}")
                print(battleship_game.get_board())
                loop = False
    current_duration = (datetime.now() - start_time).total_seconds()
    start_time = 0
    durations.append(current_duration)
    return current_duration

for i in range(runs):
    if loop:
        t1 = Thread(target=run)
        t2 = Thread(target=timer)

        t1.start()
        t2.start()

        t1.join(timeout=5)
        t2.join()

print(f'avg duration {sum(durations)/len(durations)}')