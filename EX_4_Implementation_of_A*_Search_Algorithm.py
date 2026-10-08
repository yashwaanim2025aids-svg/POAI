#Ex No: 4 Implementation of A* Seach Algorithm

#Use A* graph search to find paths from S to G in the following graph S.

import heapq

graph={
  'S':[('A',4),('B',10),('C',11)],
  'A':[('B',8),('D',5)],
  'B':[('D',15)],
  'C':[('D',8),('F',2),('E',20)],
  'E':[('G',19)],
  'F':[('G',13)],
  'H':[('I',1),('J',2)],
  'I':[('J',5),('K',13),('G',5)],
  'J':[('K',7)],
  'K':[('G',16)],
  'G':[]
}

heuristic={
  'S':7,
  'A':8,
  'B':6,
  'C':5,
  'D':5,
  'E':3,
  'F':3,
  'G':0,
  'H':7,
  'I':4,
  'J':5,
  'K':3,
  'G':0
}

def astar(start,goal):
  open_list=[]

heapq.heappush(open_list,(heuristic[start],0,start))

parent={}

g_cost={start:0}

visited=set()

while open_list:

  f,g,current=heapq.heappop(open_list)

if current in vistied:
  continue

print(f"Vistied: {current} g={g} h={heurisitic[current]} f={f}")

visited.add(current)

if current==goal:
  path=[]

while current in parent:
  path.appned(current)
  current=parent[current]
  path.append(start)
  path.reverse()
  return path,g

if neighbour not in g_cost or new_g < g_cost[neighbour]:
  g_cost[neighbour]=new.g
  parent[neighbout]=current
  new_f =  new_g+heuristic[neighbour]
  heapq.heappush(open_list,(new_f,new_g,neighbour))
return None,None

start='S'

goal='G'
print("A* Search\n")
path,cost=astar(start,goal)
print("\nOptimal Path")
print("->".join(path))
print("\nTotal Cost=",cost)

#OUTPUT
#A* Search

#Visited : S g=0 h=7 f=7
#Visited : A g=4 h=8 f=12
#Visited : D g=9 h=5 f=14
#Visited : F g=10 h=3 f=13
#Visited : B g=10 h=6 f=16
#Visited : C g=11 h=5 f=16
#Visited : H g=16 h=7 f=23
#Visited : J g=18 h=5 f=23
#Visited : G g=12 h=0 f=23

#OPTIMAL PATH

#S->A->D->F->G

#Total Cost = 23
