import threading

def cpu_stress():
    while True:
        x = 0
        for i in range(1_000_000):
            x += i

def ram_stress(size_mb):
    a = []
    amount = size_mb * 1024 * 1024 // 8
    while True:
        a.extend([1] * amount)  # Will eat memory as fast as possible

def print_counter():
    count = 1
    while True:
        print(f"Stress test running... Count: {count}")
        count += 1  # Prints extremely fast, flooding the console

if __name__ == "__main__":
    cpu_threads = []
    ram_threads = []
    num_cpu_stress_threads = 4
    num_ram_stress_threads = 1
    mb_per_thread = 500

    for _ in range(num_cpu_stress_threads):
        t = threading.Thread(target=cpu_stress)
        t.daemon = True
        cpu_threads.append(t)
        t.start()
    for _ in range(num_ram_stress_threads):
        t = threading.Thread(target=ram_stress, args=(mb_per_thread,))
        t.daemon = True
        ram_threads.append(t)
        t.start()

    print_thread = threading.Thread(target=print_counter)
    print_thread.daemon = True
    print_thread.start()

    while True:
        try:
            pass  # No sleeping here!
        except KeyboardInterrupt:
            pass  # Ignore Ctrl+C, continue running
