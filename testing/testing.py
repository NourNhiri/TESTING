import asyncio
async def task1_():
    n=0
    while True:
        print(n)
        n+=1
        await asyncio.sleep(2)
async def task2_():
    while True:
        print("ik ben taak 2")
        await asyncio.sleep(3)

async def task3_():
    while True:
        print("ik ben taak 3")
        await asyncio.sleep(5)

async def main():
    task1=asyncio.create_task(task1_())
    task2=asyncio.create_task(task2_())
    task3=asyncio.create_task(task3_())
    await task1
    await task2
    await task3


if __name__=="__main__":
    asyncio.run(main())
    loop=asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
    loop.close()