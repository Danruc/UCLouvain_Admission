import unittest
from Adjacency_Matrix import matrix_to_list

class TestMatrix(unittest.TestCase):

  def test_1(self):
    #example
    adj_mat =   [[0, 1, 0, 1, 0, 0],
       [0, 0, 1, 0, 0, 0],
       [1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0],
       [0, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0]]
    list = [[1, 3], [2], [0], [4], [3], []]
    
    result = matrix_to_list(adj_mat)
    self.assertEqual(result, list, 'The adjacency list is wrong.')

  def test_2(self):
    #circle
    adj_mat =   [[0,1,0],
                 [0,0,1],
                 [1,0,0]]
    list = [[1], [2], [0]]

    result = matrix_to_list(adj_mat)
    self.assertEqual(result, list, 'The adjacency list is wrong.')
  
  def test_3(self):
    #disconnected
    adj_mat =   [[0,0,0,0,0],
                 [0,0,0,0,0],
                 [0,0,0,0,0],
                 [0,0,0,0,0],
                 [0,0,0,0,0]]
    list = [[], [], [], [], []]
    
    result = matrix_to_list(adj_mat)
    self.assertEqual(result, list, 'The adjacency list is wrong.')
  
  def test_4(self):
    #fully connected
    adj_mat =   [[0,1,1,1],
                 [1,0,1,1],
                 [1,1,0,1],
                 [1,1,1,0]]
    list = [[1, 2, 3],[0, 2, 3],[0, 1, 3],[0, 1, 2]]

    result = matrix_to_list(adj_mat)
    self.assertEqual(result, list, 'The adjacency list is wrong.')
  
  def test_5(self):
    #complex
    adj_mat = [[0,1,0,0,1,0],
               [1,0,1,0,0,0],
               [0,1,0,1,0,0],
               [0,0,1,0,1,1],
               [1,0,0,1,0,0],
               [0,0,0,1,0,0]]
    list = [[1,4],[0,2],[1,3],[2,4,5],[0,3],[3]]

    result = matrix_to_list(adj_mat)
    self.assertEqual(result, list, 'The adjacency list is wrong.')

if __name__ == '__main__':
  unittest.main()