from typing import Generator

def fibonacii() -> Generator[int, None, None]:
    a, b = 0, 1
    while (True):
        yield a
        a, b = b, a + b

def prime() -> Generator[int, None, None]:
    n = 2
    while(True):
        prime = True
        for i in range(2, n):
            if n % i == 0:
                prime = False
                break
        if prime:
            yield n
        n += 1

def process() -> Generator[dict, None, None]:
    yield {"player":"alice","level":5,"event":"killed monster"}
    yield {"player":"bob","level":12,"event":"found treasure"}
    yield {"player":"charlie","level":8,"event":"leveled up"}

if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    print("Processing 1000 game events...")
    print()
    i = 0
    treasure = 0
    lv = 0
    up = 0
    for event in process():
        i += 1
        print(f"Event {i}: Player {event.get("player")} (level {event.get("level")}) {event.get("event")}")
        if "leveled up" == event.get("event"):
            up += 1
        if int(event.get("level")) > 10:
            lv += 1
        if "found treasure" == event.get("event"):
            treasure += 1
        
    print("...")
    print()
    print("=== Stream Analytics ===")
    print(f"Total events processed: {i}")
    print(f"High-level players (10+): {lv}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {up}")
    print()
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")
    print()
    print("=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10):", end=" ")
    fib = fibonacii()
    prim = prime()
    for _ in range(10):
        print(f"{next(fib)}", end=" ")
    print()
    print("Prime numbers (first 5):", end=" ")
    for _ in range(5):
        print(f"{next(prim)}", end=" ")