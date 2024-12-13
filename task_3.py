import time 
M = 5
N = 10
timer = time.time()
for a in range (M+1):
    print(f"Внешний цикл: , {a}")
    time.sleep(1)
    for i in range (N+1):
        print(f"Внутренний цикл: , {i}")
        time.sleep(1)

print(f"Общее время: {time.time() - timer} секунд")