def outside():
        msg = "Outside!"
        def inside():
            nonlocal msg
            msg = "Inside!"
            print(msg)
        inside()
        print(msg)
