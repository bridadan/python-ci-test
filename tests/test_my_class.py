import mymodule

class TestMyClass(object):
    def test_hello(self):
        inst = mymodule.MyClass()
        assert inst.hello("test") == "Hello, tester!"
