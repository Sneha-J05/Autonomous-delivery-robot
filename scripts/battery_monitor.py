import random
import time

battery = 100

def check_battery():
    global battery
    battery -= random.randint(5, 15)
    print(f"[INFO] Battery: {battery}%")

    if battery < 20:
        print("[WARNING] Low battery! Return to charging station.")
        return False
    return True

def main():
    print("[INFO] Starting battery monitor...")

    while True:
        if not check_battery():
            print("[ACTION] Returning to base...")
            break
        time.sleep(2)

    print("[DONE] Battery routine finished.")

if __name__ == "__main__":
    main()