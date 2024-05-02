def main():
    num_blocks = int(input("Enter the number of blocks: "))
    blocks = [input("Enter the names of blocks:") for _ in range(num_blocks)]
    initial_state = {block: input(f"Enter the initial state of {block}:").strip() for block in blocks}
    goal_state = {block: input(f"Enter the goal state of {block}:").strip() for block in blocks}
    block_world = BlockWorld(blocks)
    block_world.set_initial_state(initial_state)
    print("\nInitial State:")
    draw_table(blocks, block_world.state)
    plan = block_world.find_plan(goal_state)
    print("\nFinal Plan:")
    for step, action in enumerate(plan, start=1):
        print(f"\nStep {step}: Move block {action[0]} to {action[1]}")
   
    print("\nGoal State:")
    draw_table(blocks, goal_state)

class BlockWorld:
    def __init__(self, blocks):
        self.blocks = blocks
        self.state = {block: None for block in blocks}

    def set_initial_state(self, initial_state):
        self.state.update(initial_state)

    def is_goal_state(self, goal_state):
        return all(self.state[block] == goal_state[block] for block in self.blocks)

    def apply_action(self, action):
        block, destination = action
        self.state[block] = destination

    def find_plan(self, goal_state):
        plan = []
        while not self.is_goal_state(goal_state):
            for block, position in goal_state.items():
                if self.state[block] != position:
                    if self.state[block] is not None:
                        plan.append((block, self.state[block]))
                    plan.append((block, position))
                    self.apply_action((block, position))
                    break
        return plan

    def remove_threats(self, plan):
        return [(block, destination) for block, destination in plan if destination is not None]

def draw_table(blocks, state):
    max_width = max(len(block) for block in blocks) + 2
    table = '+' + '-' * (max_width * len(blocks) + len(blocks) + 1) + '+'
    print(table)
    for block in blocks:
        position = state[block] if block in state and state[block] else 'table'
        print(f"| {block:^{max_width}}({position:^{max_width}})", end=' ')
    print('|')
    print(table)

if __name__ == "__main__":
    main()

