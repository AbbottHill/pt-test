
"""
try:
    ...
except Exception as e:
    ...
else:
    ...
"""

import random
import time

exceps = 0

def buy():
    random_num = random.random()
    if random_num < 0.2:
        print(random_num, 'normal')
        return
    else:
        print(random_num, 'error')
        raise ValueError("http error")


while True:
    try:
        buy()
    except Exception as e:
        # print(e)
        time.sleep(1)
        exceps +=1
        if exceps >= 3:
            print('fail')
            break
    else:
        print('success')
        exceps = 0
        break


