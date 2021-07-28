# closure func
# nested funciton

def main_func(param):
    def nested_func():
        print("it is now decorated")
        param()
    return nested_func

@main_func
def normal_func():
    print("normal function")
# message = main_func("this is argument of parameter")
# message()

# parent func must return the nested func
# and nested func must call the param of main_func

normal_func()






