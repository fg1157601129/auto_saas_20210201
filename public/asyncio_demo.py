import asyncio
# @asyncio
async def hello():
    while True:
        print("A1A1A1A1A1A1")
        await asyncio.sleep(0.1)    # 等待io
        print("A2A2A2A2A2A2")
        await asyncio.sleep(0.1)

# @asyncio
async def hello1():
    while True:
        print("B1B1B1B1B1B1")
        await asyncio.sleep(0.1)
        print("B2B2B2B2B2B2")
        await asyncio.sleep(0.1)

# 创建Task对象 三种方法
# python3.7之前用 ensure_future()
# asyncio.create_task(hello(),name="Task1") name参数python3.8可使用
# loop.create_task()

# tasks = [
#     asyncio.ensure_future(hello()), # 创建Task对象，python3.7之前用 ensure_future()
#     asyncio.ensure_future(hello1())
# ]

tasks = [
    hello(), # 创建Task对象，python3.7之前用 ensure_future()
    hello1()
]

# get_event_loop()
# 生成或获取一个事件循环
# 3.7之前写法
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))

# asyncio.run(tasks) 等价与 # loop = asyncio.get_event_loop()  loop.run_until_complete(asyncio.wait(tasks))

asyncio.run(asyncio.wait(tasks))

# hello()
# hello1()