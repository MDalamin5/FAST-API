def deco(x):
    return 2*x

@deco        
def test():
    deco(4)
