from environment import coloringNinja
from Node import Node
from BFS import breadth_first_graph_search
from DFS import depth_first_graph_search
from IDS import iterative_deepening_search

# Initialize the environment
ninja_env = coloringNinja(lineSize=6)

# Create the root node from the environment instance
root = Node.root(ninja_env)

# Run IDS (Iterative Deepening Search)
actions, explored, max_depth = iterative_deepening_search(ninja_env, verbose=True)

# Display results
if actions is not None:  # Checking if a solution was found
    print("Solution found!")
    print("Actions:", actions)
   # Assuming cost is calculated somewhere in your code
else:
    print("No solution found.")

# Print the maximum frontier size encountered
print("Max Frontier Size:", max_depth)