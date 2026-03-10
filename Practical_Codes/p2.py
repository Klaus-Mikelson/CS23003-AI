from collections import deque
def water_jug(jug1, jug2, target):
    visited = set()
    queue = deque()
    # parent dictionary: child_state -> parent_state
    parent = {}
    # initial state
    start = (0, 0)
    queue.append(start)
    visited.add(start)
    parent[start] = None
    while queue:
        x, y = queue.popleft()
        current = (x, y)
        # goal check
        if x == target or y == target:
            print("Goal Reached:", current)
            print("States used to solve the problem:")
            # backtrack to print path
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            for state in path:
                print(state)
            return
        # possible actions
        states = [
            (jug1, y),  # fill jug1
            (x, jug2),  # fill jug2
            (0, y),     # empty jug1
            (x, 0),     # empty jug2
            (x - min(x, jug2 - y), y + min(x, jug2 - y)),  # pour jug1 → jug2
            (x + min(y, jug1 - x), y - min(y, jug1 - x))   # pour jug2 → jug1
        ]
        for state in states:
            if state not in visited:
                visited.add(state)
                queue.append(state)
                parent[state] = current   # important line
    print("No solution possible")
water_jug(4,3,2)