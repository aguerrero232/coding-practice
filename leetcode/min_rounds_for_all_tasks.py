# %%
import numpy as np
import time
from collections import Counter
from final_boss_arr import final_boss

# %%
# arrays to use

# used for testing
arr1 = list(np.random.randint(0, 4, 8))

# expected 5
arr2 = [2, 2, 3, 3, 2, 4, 4, 4, 4, 4, 1, 1, 1]

# expected: 2
arr3 = [7, 7, 7, 7, 7, 7]

# expected: 38
arr4 = [119, 115, 115, 119, 118, 113, 118, 120, 110, 113, 119, 115, 116, 118, 120, 117, 116, 111, 113, 119, 115, 113, 115, 111, 112, 119, 111, 111, 110, 112, 113, 120, 110, 111, 112, 111, 119, 112, 113, 112, 115, 116, 113, 114, 118, 119, 115, 114, 114,
        112, 110, 117, 120, 110, 117, 116, 120, 118, 110, 120, 119, 113, 119, 120, 113, 110, 120, 114, 119, 115, 119, 117, 120, 116, 113, 113, 110, 118, 117, 116, 114, 114, 111, 116, 119, 112, 113, 116, 112, 116, 119, 112, 114, 114, 112, 118, 116, 113, 117, 116]


# %%
#  recursive way

def minimum_rounds_recursive(tasks):
    min_rounds = 0
    task_map = {k: tasks.count(k) for k in set(tasks)}
    while task_map:
        current_task = task_map.popitem()
        if current_task[1] == 1:
            return -1
        if current_task[1] == 2 or current_task[1] == 3:
            new_val = 0
        elif current_task[1] > 3:
            min_rm2 = minimum_rounds(
                ([current_task[0]] * (current_task[1] - 2)) + [x for x in tasks if x != current_task[0]])
            min_rm3 = minimum_rounds(
                ([current_task[0]] * (current_task[1] - 3)) + [x for x in tasks if x != current_task[0]])
            if min_rm2 == -1 and min_rm3 == -1:
                return -1
            if min_rm2 == -1:
                new_val = current_task[1] - 3
            elif min_rm3 == -1:
                new_val = current_task[1] - 2
            else:
                new_val = current_task[1] - (3 if min_rm2 > min_rm3 else 2)
        if new_val > 0:
            task_map[current_task[0]] = new_val
        min_rounds += 1
    return min_rounds

# %%
# dictionary comprehension way


def minimum_rounds(tasks):
    rev_map = {}
    unique_tasks = set(tasks)
    count = 0
    for t in unique_tasks:
        v = tasks.count(t)
        if v in rev_map:
            rev_map[v].append(t)
        else:
            rev_map[v] = [t]
    if 1 in rev_map:
        return -1
    if 2 in rev_map:
        count += len(rev_map[2])
        rev_map.pop(2)
    if 3 in rev_map:
        count += len(rev_map[3])
        rev_map.pop(3)
    task_map = {}
    for k, v in rev_map.items():
        for x in v:
            task_map[x] = k
    if len(task_map) == 0:
        return count
    return (count + sum((x+2)//3 for x in task_map.values())) if 1 not in task_map.values() else -1

# %%
# collections way


def minimum_rounds_best(tasks):
    task_map = Counter(tasks)
    return sum((x+2)//3 for x in task_map.values()) if 1 not in task_map.values() else -1

# %%


start_time = time.time()
min_rnds = minimum_rounds(final_boss)
end_time = time.time()

print(f"minimum rounds for all tasks: {min_rnds}")
print(f"time elapsed: {round(end_time - start_time)} seconds")

# %%

start_time = time.time()
min_rnds = minimum_rounds_best(final_boss)
end_time = time.time()

print(f"minimum rounds for all tasks: {min_rnds}")
print(f"time elapsed: {round(end_time - start_time)} seconds")

# %%
