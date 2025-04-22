import threading
import time


count = 0


lock=threading.Lock()




def inc(name):
   global count
   for _ in range(5):
       time.sleep(0.5)
       with lock:
           count = count + 1
           print(f"[{name}]:{count}")




def monitor(name):
   time.sleep(0.75)
   print(f"[{name}]:{count}")




t1 = threading.Thread(target=inc, args=("Thread-1",))
t2 = threading.Thread(target=inc, args=("Thread-2",))
threading.Thread(target=monitor,args=("Moni",),daemon=True).start()
t1.start()
t2.start()


t1.join()
t2.join()
