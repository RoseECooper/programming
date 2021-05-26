#practice at threading in python 
#using info from real python website: https://realpython.com/intro-to-python-threading/

import logging 
import threading
import time 
import concurrent.futures

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

#fake database to look at race conditions, it keeps track of a single number: .value
#Solve the race condition with a lock
class FakeDatabase: 
    def __init__(self):
        self.value=0
        self._lock=threading.Lock()

    def locked_update(self, name):
        logging.info("Thread %s: starting update", name)
        logging.debug("Tread %s about to lock", name)
        with self._lock:
            logging.debug("Thread %s has lock", name)
            local_copy=self.value
            local_copy+=1
            time.sleep(0.1)
            self.value=local_copy
            logging.debug("Thread %s about to release lock", name)
        logging.debug("Thread %s after release", name)
        logging.info("Thread %s: finishing update", name)

    #running this sections causes the race condition that the locking update above solves
    # def update(self,name):
    #     logging.info("Thread %s: starting update", name)
    #     local_copy=self.value
    #     local_copy+=1
    #     time.sleep(0.1)
    #     self.value=local_copy
    #     logging.info("Thread %s: finishing update", name)


if __name__ =="__main__":
    format="%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.DEBUG, datefmt="%H:%M:%S")
    #logging.getLogger().setLevel(logging.WARNING)

    database=FakeDatabase()
    logging.info("Testing locked update. Starting value is %d.", database.value)
    
    #multiple threads with a ThreadPoolExecuter
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.locked_update, index)
    logging.info("Testing update. Ending value is %d.", database.value)


#block for working with a single thread
#     logging.info("Main      :before creating thread")
#     x=threading.Thread(target=thread_function, args=(1,), daemon=True)
#     logging.info("Main         :before running thread")
#     x.start()
#     logging.info("Main      :wait for the thread to finnish")
#     x.join()
#     logging.info("Main      :all done")

#Dealing with multiple threads - clunky/hard way
    # threads=list()
    # for index in range (3):
    #     logging.info("Main      :create and start thread %d.", index)
    #     x=threading.Thread(target=thread_function, args=(index,))
    #     threads.append(x)
    #     x.start()

    # for index, thread in enumerate(threads):
    #     logging.info("Main      :before joining thread %d.", index)
    #     thread.join()
    #     logging.info("Main      :thread %d done", index)