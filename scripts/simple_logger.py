import time

def log(message):
    with open("robot_log.txt", "a") as f:
        f.write(f"{time.ctime()} - {message}\n")

def main():
    print("[INFO] Logging robot activity...")

    events = [
        "Robot started",
        "Reached Room A",
        "Obstacle avoided",
        "Reached Room B",
        "Delivery completed"
    ]

    for event in events:
        log(event)
        print(f"[LOG] {event}")
        time.sleep(1)

    print("[DONE] Logs saved.")

if __name__ == "__main__":
    main()