def outside():
        d = {"outside": 1}
        def inside():
            d["inside"] = 2
            print(d)
        inside()
        print(d)
