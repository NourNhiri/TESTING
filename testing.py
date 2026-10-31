import asyncio
from random import randint
async def  wait_max_n_seconds_for_max_number(n):
    seconds=randint(0,n)
    await asyncio.sleep(seconds)
    return randint(0,n)


async def main():
    tasks=[]

    for i in range(21):
        tasks.append(wait_max_n_seconds_for_max_number(20))
        
 
    
    executed=await asyncio.gather(*tasks)
    for i,task in enumerate(executed,0):
        print(f"taak {i} getal is {task}")
        
    


if __name__=="__main__":
    asyncio.run(main())
    


