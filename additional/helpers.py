import time
import random
def random_sleep(from_sec=2, to_sec=7):
    time.sleep(from_sec + (to_sec - from_sec) * random.random())