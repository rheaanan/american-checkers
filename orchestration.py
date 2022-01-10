import subprocess
import time
import timeit
import matplotlib.pyplot as plt
dumb_time = 100
smart_time = 100
def change_time (input_file, time):
    with open(input_file, 'r') as file:
        # read a list of lines into data
        data = file.readlines()

    print(data)
    # now change the 2nd line, note that you have to add a newline
    data[2] = str(time) + "\n"

    # and write everything back
    with open(input_file, 'w') as file:
        file.writelines( data )

for i in range(0,50):
    if dumb_time<0 or smart_time<0:
        print("time_up")
    change_time("input_dumb.txt", dumb_time)
    starttime = timeit.default_timer()
    subprocess.call(['python3', 'checkers_agent_dumb.py'])
    dumb_time -= (timeit.default_timer() - starttime)*10

    print("dumb one played")
    time.sleep(1)
    change_time("input_smart.txt", smart_time)
    starttime = timeit.default_timer()
    subprocess.call(['python3','checkers_agent_smart.py'])
    smart_time -= timeit.default_timer() - starttime
    print("smart one played")
    time.sleep(1)
