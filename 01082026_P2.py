import asyncio
import time


async def boil_water_async():
    print("⏳ [Water] Put pot on stove. Waiting...")
    await asyncio.sleep(3)  # PAUSES THIS FUNCTION ONLY. Yields control!
    print("🔥 [Water] Water is boiling!")


async def chop_veggies_async():
    print("🔪 [Veggies] Chopping carrots...")
    await asyncio.sleep(1)
    print("🥕 [Veggies] Carrots are ready!")


async def main_async():
    start_time = time.time()

    # Fire off both tasks at the exact same time
    await asyncio.gather(
        boil_water_async(),
        chop_veggies_async()
    )

    print(f"⏱️ Total kitchen time: {time.time() - start_time:.2f} seconds")


asyncio.run(main_async())
