import unittest
from naive import *
from dijkstra import *
from astar import *

class UnitTestsForMazeSolveComponents(unittest.TestCase):
    """docstring for UnitTestsForMazeSolveComponents"""
    
    def test_naiverec(self):
        self.assertEqual(naiverec([[0, 0, 0, 0, 1],
                               [0, 0, 0, 0, 1],
                               [0, 0, 0, 0, 1]]), 
                               [(0, 4), (1, 4),(2, 4)])
        
        self.assertEqual(naiverec([[0, 1, 0, 0, 0, 0, 0],
                               [0, 0, 1, 0, 0, 0, 0],
                               [0, 0, 1, 0, 0, 0, 0],
                               [0, 0, 0, 1, 0, 0, 0],
                               [0, 0, 0, 1, 0, 0, 0],
                               [0, 0, 0, 0, 1, 0, 0]]), False)
        
        self.assertEqual(naiverec([[0, 1, 0, 0, 0, 0, 0],
                               [0, 1, 1, 0, 0, 0, 0],
                               [0, 0, 1, 1, 0, 0, 0],
                               [0, 0, 0, 1, 0, 0, 0],
                               [0, 0, 0, 1, 1, 0, 0],
                               [0, 0, 0, 0, 1, 0, 0]]),
                               [(0, 1), (1, 1), (1, 2), (2, 2), (2, 3), 
                               (3, 3), (4, 3), (4, 4),  (5, 4)])

        self.assertEqual(naiverec([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]), 
                               [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), 
                               (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), 
                               (10, 1), (11, 1), (12, 1), (13, 1), (14, 1), 
                               (14, 2), (14, 3), (14, 4), (14, 5), (14, 6), 
                               (14, 7), (14, 8), (14, 9), (14, 10), (14, 11) 
                               (14, 12), (14, 13), (14, 14), (15, 14)])

        self.assertEqual(naiverec([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]),
                               [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), 
                               (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), 
                               (10, 1), (11, 1), (12, 1), (13, 1), (14, 1), 
                               (14, 2), (14, 3), (14, 4), (14, 5), (14, 6), 
                               (14, 7), (14, 8), (14, 9), (14, 10), (14, 11) 
                               (14, 12), (14, 13), (14, 14), (15, 14)])


if __name__ == '__main__':
    unittest.main()