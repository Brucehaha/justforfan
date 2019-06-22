import time

def consumer(name):
    print('%s read for eat'%name)
    while True:
        baozi = yield
        print("baozi[%s] is coming, have by [%s]"%(baozi, name))
# c = consumer("Bruce")
# c.__next__()
#
# b1="chives baozi"
# c.send(b1)

def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("making baozi")
    for i in range(10):
        time.sleep(1)
        print("baozi, cut into half")
        c.send(i)
        c2.send(i)

producer("bruce")