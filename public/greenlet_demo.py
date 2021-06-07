from  greenlet import greenlet

def func1():
    print(1)
    gr2.switch()
    print(2)
    gr2.switch()

def func2():
    print(3)
    gr1.switch()
    print(4)

gr1 = greenlet(func1)
gr2 = greenlet(func2)

gr1.switch()


# yield 关键字 返回生成器
def func_y1():
    yield 1
    yield from func_y2()
    yield 2

def func_y2():
    yield 3
    yield 4

f1 = func_y1()
for item in f1:
    print(item)