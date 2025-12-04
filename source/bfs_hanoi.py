# bfs_hanoi.py
from collections import deque

# Use fully immutable states for hashing
initial = ((3, 2, 1), (), ())
goal = ((), (), (3, 2, 1))

def to_mutable(state):
    """Convert immutable tuple-state -> mutable list-state"""
    return [list(peg) for peg in state]

def to_immutable(state):
    """Convert mutable list-state -> immutable tuple-state"""
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

def bfs():
    queue = deque([(initial, [initial])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        visited.add(state)

        for nxt in get_neighbors(state):
            if nxt not in visited:
                queue.append((nxt, path + [nxt]))

solution = bfs()

print("\nBFS Solution:")
for idx, state in enumerate(solution):
    print(f"Step {idx}: {state}")
