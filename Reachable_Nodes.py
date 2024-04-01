
def reachable(adj_list, start_node):
  reach_nodes = set()
  reach_nodes.add(start_node)
  not_visited_nodes = adj_list[start_node]

  while(len(not_visited_nodes) > 0):
    node = not_visited_nodes.pop(0)
    if node not in reach_nodes:
      reach_nodes.add(node)
      for i in adj_list[node]:
        if i not in reach_nodes:
          not_visited_nodes.append(i)

  return reach_nodes

def reachable_recursive(adj_list, start_node):
  def dfs(node,visited):
    visited.add(node)
    for neighbor in adj_list[node]:
      if neighbor not in visited:
        dfs(neighbor,visited)

  visited_nodes = set()
  dfs(start_node,visited_nodes)
  return visited_nodes


      
        
  