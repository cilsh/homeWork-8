import time


def howseconds():
    start = time.time()
    for i in range(100000000000000000000000000000000000000000):  # якщо буде задовго заберіть декілька нулів
        pass
    end = time.time()
    print(f"{round(end - start)}s")

howseconds()
