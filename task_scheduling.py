from collections import deque
def find(task, time_slice):
    queue = deque(task)
    ids = deque(range(1, len(task) + 1))
    print("task case 1:")
    total_runs = 0
    while queue:
        curr_time = queue.popleft()
        curr_id = ids.popleft()
        run_time = min(time_slice, curr_time)
        print(f"    task {curr_id} runs for {run_time} units")
        total_runs += 1
        remaining = curr_time - run_time
        if remaining > 0:
            queue.append(remaining)
            ids.append(curr_id)
    print(f"Total runs taken: {total_runs}")
task = (10, 5, 8)
time = 4
find(task, time)
