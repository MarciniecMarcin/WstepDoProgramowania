import math
import keyword

for name in dir(math):
    if callable(getattr(math, name)): print(name)

for name in dir(tuple):
    if callable(getattr(tuple, name)): print(name)

for name in dir(keyword):
    if callable(getattr(keyword, name)): print(name)