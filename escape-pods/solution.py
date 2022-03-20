import collections
import copy
 
def get_paths(enter, exit, graph):
   dq = collections.deque()
   dq.append((enter, [enter], 0))
   all = []
   solved = False
   while len(dq):
 
       curr, path_yet, cap = dq.popleft()
       neighbors = []
       for i in range(len(graph[curr])):
           if graph[curr][i] != 0:
               neighbors.append(i)
       for neighbor in neighbors:
           if (len(path_yet) == 1):
               cap = graph[curr][neighbor]
           else:
               cap = min(cap, graph[curr][neighbor])
           if neighbor == exit:
               path_yet.append(neighbor)
               all.append((path_yet, cap))
           else:
               fake = path_yet[:]
               fake.append(neighbor)
               dq.append((neighbor, fake, cap))
   return all
def get_one_path(sources, sinks, graph):
   paths = []
   for source in sources:
       for sink in sinks:
           paths.extend(get_paths(source, sink, graph))
   if (len(paths)):
       return paths[0]
   return []
 
 
def get_min_of_path(cap, path):
   ans  = cap[path[0]][path[1]]
   for i in range(1, len(path) - 1):
       ans = min(ans, cap[path[i]][path[i + 1]])
   return ans
 
def solution(enterances, exits, graph):
 
   flow = copy.deepcopy(graph)
 
   cap = copy.deepcopy(graph)
   for i in range(len(graph)):
       for j in range(len(graph[0])):
           flow[i][j] = 0
 
   while True:
       if (len(get_one_path(enterances, exits, cap))):
           path = get_one_path(enterances, exits, cap)[0]
       else:
           break
       capacity = get_min_of_path(cap, path)
       for j in range(len(path) - 1):
           r1 = path[j]
           r2 = path[j + 1]
           if (graph[r1][r2] != 0):
               flow[r1][r2] += capacity
               cap[r1][r2] -= capacity
           else:
               cap[r1][r2] += capacity
               flow[r2][r1] -= capacity
   bunnies = 0
   for exit in exits:
       for row in flow:
           bunnies += row[exit]
   return bunnies
