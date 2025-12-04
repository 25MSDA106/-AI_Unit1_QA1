# astar_hanoi.py
import heapq

# Immutable states
initial = ((3, 2, 1), (), ())
goal = ((), (), (3, 2, 1))

def to_mutable(state):
    """Convert tuple-state → list-state"""
    return [list(peg) for peg in state]

def to_immutable(state):
    """Convert list-state → tuple-state"""
    return tuple(tuple(peg) for peg in state)

def get_neighbors(state):
    state_list = to_mutable(state)
    neighbors = []

    for i in range(3):
        if not state_list[i]:
            continue

        disk = state_list[i][-1]

        for j in range(3):
            if i == j:
                continue

            if not state_list[j] or state_list[j][-1] > disk:
                new_state = to_mutable(state)
                new_state[i].pop()
                new_state[j].append(disk)
                neighbors.append(to_immutable(new_state))

    return neighbors

def heuristic(state):
    """Count how many disks are NOT on the goal peg (peg 3)"""
    count = 0
    for peg in range(3):
        for disk in state[peg]:
            if peg != 2:
                count += 1
    return count

def astar():
    pq = []
    # priority, index, state, path
    counter = 0
    heapq.heappush(pq, (0, counter, initial, [initial]))
    visited = set()

    while pq:
        _, _, state, path = heapq.heappop(pq)

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        for nxt in get_neighbors(state):
            g = len(path)
            h = heuristic(nxt)
            f = g + h
            counter += 1
            heapq.heappush(pq, (f, counter, nxt, path + [nxt]))

solution = astar()

print("\nA* Solution:")
for idx, state in enumerate(solution):
    print(f"Step {idx}: {state}")
