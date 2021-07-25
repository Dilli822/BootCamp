
    # we can change the attributes through methods

   # here rover is object with attributes
   # color and modified the color to blue
   # with the help of method


   # combining all the things at together

# class Vehicle:
#     doors = 4

#     def __init__(self, color, mileage):
#           self.color = color
#           self.mileage = mileage

#           def make_it_blue(self):
#                self.color = "blue"

        
#     def get_info(self):
#             return f"{self.color} vehicle has mileage {self.mileage}"

#             Vehicle1 = Vehicle("red", 25)
#             vehicle2 = Vehicle("white", 20)

#             print(Vehicle1.color)
#             print(Vehicle1.mileage)
   


print("hello world")

class A:
    def __init__(self, n):
        self.n = n

        def info(self):
            return 'info method from class A'

            def result(self):
                return self.n * self.n
        
class B(A):
    def result(self):
        #calling base class method
        result_from_base = A.result(self)
        # modifying on super class's behaviour
        return -result_from_base

        obj_a = A(2)
        print(obj_a.info())