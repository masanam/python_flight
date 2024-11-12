import unittest
from context import app
from app.function import Solution 

class TestFindCheapestPrice(unittest.TestCase):
    def test_simple_case(self):
        n = 3
        flights = [[0,1,100],[1,2,100],[0,2,500]]
        src = 0
        dst = 2
        k = 1
        self.assertEqual(Solution.findCheapestPrice(n, flights, src, dst, k), 200)

    def test_no_path(self):
        n = 3
        flights = [[0,1,100],[1,2,100],[0,2,500]]
        src = 0
        dst = 2
        k = 0
        self.assertEqual(Solution.findCheapestPrice(n, flights, src, dst, k), -1)

    def test_single_flight(self):
        n = 3
        flights = [[0,1,100]]
        src = 0
        dst = 1
        k = 0
        self.assertEqual(Solution.findCheapestPrice(n, flights, src, dst, k), 100)

    def test_multiple_stops(self):
        n = 4
        flights = [[0,1,100],[1,2,100],[2,3,100],[0,3,500]]
        src = 0
        dst = 3
        k = 1
        self.assertEqual(Solution.findCheapestPrice(n, flights, src, dst, k), 300)

    def test_same_source_and_destination(self):
        n = 1
        flights = []
        src = 0
        dst = 0
        k = 0
        self.assertEqual(Solution.findCheapestPrice(n, flights, src, dst, k), 0)

if __name__ == '__main__':
    unittest.main()