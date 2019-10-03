# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

##################################################################################
# dfs tree search
'''to get run this section rename the function to original and the name of earlier
function to something else'''
def TdepthFirstSearch(problem):
      """
      Search the deepest nodes in the search tree first.

      Your search algorithm needs to return a list of actions that reaches the
      goal. Make sure to implement a graph search algorithm.

      To get started, you might want to try some of these simple commands to
      understand the search problem that is being passed in:

      print("Start:", problem.getStartState())
      print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
      print("Start's successors:", problem.getSuccessors(problem.getStartState()))
      """
      frng = util.Stack()
      frng.push( (problem.getStartState(), []) )
      pn={problem.getStartState():'om'}
      
      while not frng.isEmpty():
            nd, actn = frng.pop()                
            if problem.isGoalState(nd):
                return actn

            for chld, dirn, V in problem.getSuccessors(nd):
                if pn[nd] == chld: continue
                frng.push((chld, actn + [dirn]))
                pn[chld]=nd
                         
      return []
      #"*** YOUR CODE HERE ***"
      util.raiseNotDefined()

##################################################################################
#dfs graph search section
def depthFirstSearch(problem):
      frng = util.Stack()
      frng.push( (problem.getStartState(), []) )
      vst=set()
      
      while not frng.isEmpty():
            nd, actn = frng.pop()
            vst.add(nd)
            if problem.isGoalState(nd):
                return actn

            for chld, dirn, V in problem.getSuccessors(nd):
                if chld in vst: continue
                frng.push((chld, actn + [dirn]))
                    
      return []         
      util.raiseNotDefined()


##################################################################################
# bfs tree search
'''to get run this section rename the function to original and the name of earlier
function to something else'''
def TbreadthFirstSearch(problem):
      """Search the shallowest nodes in the search tree first."""
      "*** YOUR CODE HERE ***"
      
      frng = util.Queue()
      frng.push( (problem.getStartState(), []) )
      pn={problem.getStartState():'om'}
            
      while not frng.isEmpty():
            nd, actn = frng.pop()            
            if problem.isGoalState(nd):
                return actn

            for chld, dirn, V in problem.getSuccessors(nd):
                if pn[nd] == chld: continue
                frng.push((chld, actn + [dirn]))
                pn[chld]=nd
            
      return []      
      util.raiseNotDefined()


##################################################################################
# bfs graph search      
def breadthFirstSearch(problem): 
      frng = util.Queue()
      frng.push( (problem.getStartState(), []) )
      vst=set()
            
      while not frng.isEmpty():
            nd, actn = frng.pop()
            vst.add(nd)
            if problem.isGoalState(nd):
                return actn
           
            for chld, dirn, V in problem.getSuccessors(nd):
                if chld in vst : continue
                frng.push((chld, actn+[dirn]))
                
      return []     
      util.raiseNotDefined()


##################################################################################
# ucs graph search 
def uniformCostSearch(problem):
      """Search the node of least total cost first."""
      "*** YOUR CODE HERE ***"
  
      frng = util.PriorityQueue()
      frng.push((problem.getStartState(), [], 0), 0)
      closed=set()
      
      while not frng.isEmpty():
            nd, actn, curCst = frng.pop()
            if problem.isGoalState(nd):
                return actn

            if nd in closed : continue
            for chld, dirn, V in problem.getSuccessors(nd):
                frng.push((chld, actn+[dirn], curCst + V), curCst + V)
            closed.add(nd)

      return []   
      util.raiseNotDefined()
##################################################################################



      
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

##################################################################################
# heuristic functions
def manhattanHeuristic(position, problem, info={}):
    xy1 = position
    xy2 = problem.goal
    return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])

def euclideanHeuristic(position, problem, info={}):
    xy1 = position
    xy2 = problem.goal
    return ((xy1[0] - xy2[0])**2 + (xy1[1] - xy2[1])**2)**0.5

def TeuclideanHeuristic(position, problem, info={}):
    xy1 = position
    xy2 = problem.goal
    heuV=0.5*(abs(xy1[0] - xy2[0])**0.5)+0.5*(abs(xy1[1] - xy2[1])**0.5)
    heuv=(((xy1[0] - xy2[0])**2 + (xy1[1] - xy2[1])**2)**0.5)+heuV    
    return (heuv)

##################################################################################   
# astar graph search
def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    frng = util.PriorityQueue()
    frng.push( (problem.getStartState(), [], 0), heuristic(problem.getStartState(), problem) )
    closed=set()
    
    while not frng.isEmpty():
        nd, actn, curCst = frng.pop()
        if problem.isGoalState(nd):
                return actn
            
        if chld in closed : continue    
        for chld, dirn, V in problem.getSuccessors(nd):
            g = curCst + V
            h = heuristic(chld, problem)
            frng.push((chld, actn+[dirn], g), g + h)
        closed.add(nd)
        
    return []
    util.raiseNotDefined()

##################################################################################
##################################################################################
"""This implementation is going to work same as above one because here we have almost
every action of unit cost which is the same as action cost returned by getSuccessors
function, stored in the variable V """    
# distance functions
def euclideand(node, child):
    xy1 = node
    xy2 = child
    return ((xy1[0] - xy2[0])**2 + (xy1[1] - xy2[1])**2)**0.5


##################################################################################
# ucs graph with action cost l2
'''to get run this section rename the function to original and the name of earlier
function to something else'''
def l2uniformCostSearch(problem):  
      frng = util.PriorityQueue()
      frng.push( (problem.getStartState(), [], 0), 0)
      closed=set()
      
      while not frng.isEmpty():
            nd, actn, curCst = frng.pop()            
            if problem.isGoalState(nd):
                return actn

            if chld in closed : continue
            for chld, dirn, V in problem.getSuccessors(nd):
                V=l2(nd, chld)
                frng.push((chld, actn+[dirn], curCst + V), curCst + V)
            closed.add(nd)
                 
      return []    
      util.raiseNotDefined()

##################################################################################
# astar graph with action cost l2
'''to get run rename the function to original and the name of earlier to something else'''
def l2aStarSearch(problem, heuristic=nullHeuristic):
    frng = util.PriorityQueue()
    frng.push( (problem.getStartState(), [], 0), heuristic(problem.getStartState(), problem) )
    closed=set()
    
    while not frng.isEmpty():
        nd, actn, curCst = frng.pop()
        if problem.isGoalState(nd):
                return actn
            
        if chld in closed : continue    
        for chld, dirn, V in problem.getSuccessors(nd):
            g = curCst + l2(nd, chld)
            h = heuristic(chld, problem)
            frng.push((chld, actn+[dirn], g), g + h)
        closed.add(nd)

    return []
    util.raiseNotDefined()


##################################################################################
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

# Abbreviations
nlHeu=nullHeuristic
mhHeu=manhattanHeuristic
l2Heu=euclideanHeuristic
tl2Heu=TeuclideanHeuristic       
l2=euclideand
