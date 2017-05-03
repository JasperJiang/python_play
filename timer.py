import time
import threading
def a():
    print time.time()
threading.Timer(10,a).start()