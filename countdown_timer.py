import time
timer = int(input("How long do you want to sleep for:\n"))
remaining = timer
for t in range(0, timer):
    remaining -= 1
    time.sleep(1)
    hours = int(remaining / 3600)
    minutes = int(remaining / 60) % 60
    seconds = remaining % 60
    print(f"{hours:02}:{minutes:02}:{seconds:02}")

print("Time up")