import unittest
import Project

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual([Project.top3.index[0], Project.top3.index[1], Project.top3.index[2]], [' United Kingdom ', ' Germany ', ' Scandinavia '])

    def test_somethings(self):
        self.assertTrue([Project.top3.index[0], Project.top3.index[1], Project.top3.index[2]], [' United Kingdom ', ' Germany ', ' Scandinavia '])



if __name__ == '__main__':
    unittest.main()
