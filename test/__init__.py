import unittest
import mymodule

class TestMyClass(unittest.TestCase):

    def test_hello(self):
        inst = mymodule.MyClass()
        self.assertEqual(inst.hello("test"), "Hello, test!")

if __name__ == '__main__':
    unittest.main()
