import unittest

class TestCaseDemo2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("I will run only once before all tests")
        print("#" * 30)

    def test_methodA(self):
        print("Running method A")

    def test_methodB(self):
        print("Running method B")

    @classmethod
    def tearDownClass(cls):
        print("#" * 30)
        print("I will run after all tests")

if __name__ == '__main__':
    unittest.main