import threading
import time


class myThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        print("running on number:%s" % self.num)
        time.sleep(3)


if __name__ == '__main__':
    t1 = myThread(1)
    t2 = myThread(2)
    t1.start()
    t2.start()
    print('ending.....')