import unittest
from Reachable_Nodes import reachable


class TestReachable(unittest.TestCase):

  def test_1(self):
    #example
    adj_list = [[1, 3], [2], [0], [4], [3], []]
    
    result = reachable(adj_list, 0)
    self.assertEqual(result, {0,1,2,3,4}, 'The reachable nodes are wrong.')
  
  def test_2(self):
    #circle
    adj_list = [[1], [2], [0]]
    
    result = reachable(adj_list, 1)
    self.assertEqual(result, {0,1,2}, 'The reachable nodes are wrong.')
  
  def test_3(self):
    #disconnected
    adj_list = [[], [], [], []]
    
    result = reachable(adj_list, 2)
    self.assertEqual(result, {2}, 'The reachable nodes are wrong.')
  
  def test_4(self):
    #fully connected
    adj_list = [[1, 2, 3],[0, 2, 3],[0, 1, 3],[0, 1, 2]]
    
    result = reachable(adj_list, 3)
    self.assertEqual(result, {0,1,2,3}, 'The reachable nodes are wrong.')
  
  def test_5(self):
    #complex
    adj_list = [[1,4],[0,2],[1,3],[2,4,5],[0,3],[3]]
    
    result = reachable(adj_list, 4)
    self.assertEqual(result, {0,1,2,3,4,5}, 'The reachable nodes are wrong.')

if __name__ == '__main__':
  unittest.main()