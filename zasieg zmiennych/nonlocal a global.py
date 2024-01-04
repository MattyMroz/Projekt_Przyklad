def method():
  
    global value
    value = 100

value = 0
method()


print(value)


def method():

    def method2():
       
        nonlocal value
        value = 100

   
    value = 10
    method2()

  
    print(value)


method()
