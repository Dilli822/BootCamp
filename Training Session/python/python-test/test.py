

# this is test.py
# importing the built in packages


# import unittest

#our main function to be tested

# def add(x,y):
#     return x+y

#creating a Testadd named class
# class TestAdd(unittest.TestCase):

    # adding two methods inside it to check the main function
    # def test_positive(self):
        #test 2+6 = 8 which is true 
        # self.assertEqual(add(2,6,), 8)

    # def test_negative(self):
        #test 2+6 is 7 which is not true
        # self.assertNotEqual(add(2,6), 7)

# this means run this file to execute above block of code
# if __name__ == '__main__':
    # unittest.main()

#up above the method must start with test_



# this is test.py
# importing the built in packages

import unittest

#our main function to be tested

# def add(x,y):
#     return x+y

#creating a Testadd named class
# class TestAdd(unittest.TestCase):

    # adding two methods inside it to check the main function
    # def test_positive(self):
    #     #test 2+6 = 8 which is true 
    #     self.assertEqual(add(2,6,), 8)

    # def test_negative(self):
        #test 2+6 is 7 which is not true
    #     self.assertNotEqual(add(2,6), 7)
    
    # def test_exception(self):
        # add takes 2 args
        # putting only one should raise TypeError
        # if typeerror comes exception will araises
        # here we only passed one args so it passed the test
        # will ran 3 test passed
        # self.assertRaises(TypeError, add, 2)

# this means run this file to execute above block of code
# if __name__ == '__main__':
#     unittest.main()

#up above the method must start with test_
# $ python -m unittest test.TestAdd
# ...
# ----------------------------------------------------------------------
# Ran 3 tests in 0.000s

# OK


# We have added a new test,test_exception() 
# which tests if our code raises TypeError

class Demo:
    cls_var1 = "delta"
    cls_var2 = "force"
    cls_var3 = 2.4

    @staticmethod
    def two():
        return 2

    def __str__(self):
        return "test"

class TestDemo(unittest.TestCase):

    def setUp(self) -> None:
        # creating an object of Demo class
        # we did setup for testing 
        # if error araises from beginning only
        # it throw the errors without delay
        self.demo = Demo()
    
    def test_cls_variables(self):

        self.assertEqual(self.demo.cls_var1, 'delta')
        self.assertEqual(self.demo.cls_var1, 'force')
        self.assertEqual(self.demo.cls_var1, 2.4)
    
    def test_str(self):
        self.assertEqual(self.demo.__str__(), 'test')

     
    #use of decorator 
    #this will not run the unittest iniside the
    #decorator block of code
    @unittest.skip("demonstarting skipping")
    def test_nothing(self):
        print("Skip this")

    def test_two(self):
        self.assertEqual(self.demo.two(), 2)
        self.assertEqual(self.demo.two(), 3)
    
    def tearDown(self) -> None:
        #deleting the object
        #at last it is called to test
        del self.demo


