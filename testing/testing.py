import asyncio
async def taskHello():
    await asyncio.sleep(2)
    print("helloworld")

async def main():
    await taskHello()



if __name__=="__main__":
    asyncio.run(main())