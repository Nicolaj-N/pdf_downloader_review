from typing import Optional

def foo(arg: str) -> str:
    return arg

def bar(arg: str = None):
    return arg

def xdd(arg: str | None):
    return arg

print(foo("foo must receive an argument and argument has to be a string"))
print(bar("argument for bar is optional if bar is called with an argument it has to be a string or None"))
print(bar())
print(bar(None))
print(xdd("xdd must receive an argument which can be a string or none"))
print(xdd(None))

five = 5
foo_five = foo(five)
bar_five = bar(5)
xdd_five = xdd(5)

print(f"{type(five)},  {type(foo_five)},  {type(bar_five)},  {type(xdd_five)}")