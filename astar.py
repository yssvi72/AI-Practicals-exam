import heapq

class Node:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic=0):
        self.state, self.parent, self.action, self.cost, self.heuristic = state, parent, action, cost, heuristic

    def __lt__(self, other): return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def print_iteration(iteration, steps, min_fn, max_fn, action_taken, matrices):
    print(f"\nIteration {iteration}:")
    print(f"Number of possible steps: {steps}")
    print(f"Final action taken: {action_taken}")
    print(f"Matrices:")
    for matrix in matrices: print('\n'.join(map(' '.join, matrix)), end='\n\n')
    print(f"Min f(n) in this iteration: {min_fn}")
    print(f"Max f(n) in this iteration: {max_fn}")

def misplaced_tiles(state, goal_state):
    return sum(state[i][j] != goal_state[i][j] and state[i][j] != 'e' for i in range(3) for j in range(3))

def get_neighbors(node, goal_state):
    zero_row, zero_col = [(i, j) for i, row in enumerate(node.state) for j, val in enumerate(row) if val == 'e'][0]
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neighbors = []
    for move in moves:
        new_row, new_col = zero_row + move[0], zero_col + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [row[:] for row in node.state]
            new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]
            neighbors.append(Node(new_state, node, move, node.cost + 1, misplaced_tiles(new_state, goal_state)))
    return neighbors

def a_star(initial_state, goal_state):
    initial_node = Node(initial_state, None, None, 0, misplaced_tiles(initial_state, goal_state))
    heap = [initial_node]
    iteration = 1
    while heap:
        current_node = heapq.heappop(heap)
        if current_node.state == goal_state:
            print("Goal state reached!")
            print(f"f(n) of the goal state: {current_node.cost + current_node.heuristic}")
            return
        neighbors = get_neighbors(current_node, goal_state)
        min_fn_neighbor = min(neighbors, key=lambda x: x.cost + x.heuristic)
        max_fn_neighbor = max(neighbors, key=lambda x: x.cost + x.heuristic)
        min_fn = min_fn_neighbor.cost + min_fn_neighbor.heuristic
        max_fn = max_fn_neighbor.cost + max_fn_neighbor.heuristic
        print_iteration(iteration, len(neighbors), min_fn, max_fn, max_fn_neighbor.action, [neighbor.state for neighbor in neighbors])
        for neighbor in neighbors: heapq.heappush(heap, neighbor)
        iteration += 1

if __name__ == "__main__":
    print("Enter the initial state (3x3 matrix with 'e' for empty tile):")
    initial_state = [input().split() for _ in range(3)]
    print("Enter the goal state (3x3 matrix with 'e' for empty tile):")
    goal_state = [input().split() for _ in range(3)]
    a_star(initial_state, goal_state)
