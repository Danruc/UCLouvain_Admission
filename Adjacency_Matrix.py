
def matrix_to_list(adj_mat):
  mat_len = len(adj_mat)
  adj_list = []
  for node in range(mat_len):
    adj_list.append([])
    for connection in range(mat_len):
      if adj_mat[node][connection] != 0:
        adj_list[node].append(connection)
  return adj_list
