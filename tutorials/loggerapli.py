import logging as lg
lg.basicConfig(level=lg.DEBUG,filename="app12.log",filemode="w")
l1=lg.getLogger("add1")
l1.setLevel(lg.DEBUG)
def a(a,b):
    l1.debug("addition is comp")
    return a+b
def d(a,b):
    try:
        result=a/b
        return result
    except ZeroDivisionError:
        l1.warning("one element is 0")
        return None
print(a(5,3))
print(d(5,0))
