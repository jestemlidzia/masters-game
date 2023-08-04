import logging
import threading
import time
import stm

class Threadss(object):
    def __init__(self):

        # self.thread_number = thread_number
        format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    def run_thread(self, func):
        
        logging.info("Main    : before creating thread")
        x = threading.Thread(target=func, args=(1,))
        logging.info("Main    : before running thread")
        x.start()
        logging.info("Main    : wait for the thread to finish")
        # x.join()
        logging.info("Main    : all done")

    def thread_function(name):
        logging.info("Thread %s: starting", name)
        time.sleep(2)
        logging.info("Thread %s: finishing", name)


# x = threading.Thread(target=thread_function, args=(1,))
# x.start()