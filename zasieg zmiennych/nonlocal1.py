def test(c):
        def add(b):
                nonlocal c
                a = 10
                a += 1
                return a+b
        return add
a = 20
func= test(0)
print(func(3))

