'''
pytest is a unit testing framework for python.

the rules fr :
-file name should always start with test_
-fn name and method name should also start with test_
-class name should start with Test

->when we follow these rules pytest will recognize the files and methods following the rules so without giving fn call we can execute the test fn
and same goes for class without creating an object
-> in case of test clases we need not create object and call the fn , if we do so execution will happen twice

"-v" : give detail descibtion of the test (verobos)
"-s":  print the print statement
'''


# def test_registor():
#     print("hello world")
# def test_login():
#     print("logged in..........")
# def test_logout():
#     print("logged out..........")

class Test_demo:
    # def __init__(self):
    #     print("he")
    def test_registor(self):
        print("hello world")
        l=[2,5,6]
        assert 3 in l

        if 5 not in l:
            print("working")
        assert 2==2

    def test_login(self):
        print("logged in..........")

    def test_logout(self):
        print("logged out..........")
        # assert "s" == "a"
