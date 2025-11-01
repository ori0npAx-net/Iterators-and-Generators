from GeneratorExample import FactorDemo
    
if __name__=="__main__": 
    obj = FactorDemo(12)
    print("\nCASE 1 : Modern `return` in generator (StopIteration.value demo):")
    g = obj.bad_generator_mix()
    while True:
        try:
            print(next(g))
        except StopIteration as e:
            print(" Generator stopped. Hidden return value ", e.value)
        break
    print("\nCASE 2 : Logical Error (compiles but wrong behavior):")
    for x in obj.bad_generator_logic():
        print(x)
    print("\nCASE 3 : Correct Generator:")
    for x in obj.good_generator():
        print(x) 