import time

def boil_water_sync():
    print("⏳ [Water] Put pot on stove. Waiting...")
    time.sleep(3)  # 🛑 ENTIRE PROGRAM FREEZES HERE FOR 3 SECONDS
    print("🔥 [Water] Water is boiling!")


def chop_veggies_sync():
    print("🔪 [Veggies] Chopping carrots...")
    time.sleep(1)
    print("🥕 [Veggies] Carrots are ready!")


def main_sync():
    start_time = time.time()

    boil_water_sync()  # Takes 3 seconds (Program is frozen)
    chop_veggies_sync()  # Takes 1 second (Starts only AFTER water finishes)

    print(f"⏱️ Total kitchen time: {time.time() - start_time:.2f} seconds")

main_sync()
