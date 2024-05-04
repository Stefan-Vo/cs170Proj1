import problem
import node
import math
import tree

def euclideanDistance(startState, goalState):
    eucDist = eucDistX = eucDistY = x1 = x2 = y1 = y2 = 0
    sizeOfPuzzle = math.sqrt(len(startState)) #because its a square the square root would be the dimensions
    for i in range(sizeOfPuzzle):
        x1 = startState.index(i) // sizeOfPuzzle # find the row of the state that we are in 
        y1 = startState.index(i) % sizeOfPuzzle # find the column of the state that we are in 
        x2 = goalState.index(i) // sizeOfPuzzle #inneficient but we calculate the goal state index every time in the for loop
        y2 = goalState.index(i) % sizeOfPuzzle
        eucDistX = pow(x2 - x1,2)
        eucDistY = pow(y2 - y1,2)
        eucDist += math.sqrt(eucDistX + eucDistY)
    return eucDist
def ASearchEucDist(startState, goalState):
    #setting the scope
    problem = Problem(startState, goalState, operators)
    tree = Tree()
    startNode = Node(problem.initial_state)
    tree.add_node(startNode)
    path = []
    explored = set()
    
    #A* heuristic search (Euclidean Distance)
    while tree.priority_queue:
        curr = tree.pop_node()
        if curr.state == goalState:
            path = []
            while curr.parent:
                path.append(curr.operator)
                curr = curr.parent
            path.reverse()
            return path
            
        explored.add(curr.state)
        
        problem_child = problem.Problem(curr.state, goalState, operators)
        for child in curr.expand(problem_child):
            if child.state not in explored:
                total_cost = child.g_cost + euclideanDistance(child.state, goalState)
                tree.add_node(child, total_cost)
                
    return []
    