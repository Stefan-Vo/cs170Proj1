from problem import Problem
from node import Node
from tree import Tree
from uniformCostSearch import uniformCostSearch
from ASearchMisplacedtiles import ASearchHeuristic
from ASearchEucDist import ASearchEucDist


def main():

    goal_state = [1,2,3,4,5,6,7,8,0]

    operators = ["UP", "DOWN", "LEFT", "RIGHT"]


    print("Welcome to project group 8,  8 puzzle solver.")
    choice = input("Type '1' to use a default puzzle, or '2' to enter your own puzzle: ")

    if choice == '1':
        # Use default puzzle
        initial_state = [1, 0, 3, 4, 2, 6, 7, 5, 8]  # Example default puzzle
    elif choice == '2':
        # Enter custom puzzle
        print("Enter your puzzle, use a zero to represent the blank")
        initial_state = []
        for i in range(3):
            row = input(f"Enter the {ordinal(i+1)} row, use space or tabs between numbers: ").split()
            initial_state.extend(map(int, row))
    else:
        print("Invalid choice. Please enter '1' or '2'.")
        return

    problem = Problem(initial_state, goal_state, operators)
    tree = Tree()
    initial_node = Node(initial_state)
    tree.add_node(initial_node)

    print("Choose algorithm:")
    print("1. Uniform Cost Search:")
    print("2. A* with the Misplaced Tile Heuristic")
    print("3. A& with the Euclidean distance Heuristic")
    choice2 = input()
    if choice2 == '1':
        path = uniformCostSearch(problem)
    elif choice2 == '2':
        path = ASearchHeuristic(problem)
    elif choice2 == '3':
        path = ASearchEucDist(problem)
    else: 
        print("Invalid choice")
        return

    print(path)


def ordinal(n):
    suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    return str(n) + suffix

#def print_state(state):
    #for i in range(0, len(state), 3):
        #print(state[i:i+3])

if __name__ == "__main__":
    main()
