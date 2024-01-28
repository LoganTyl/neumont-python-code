import moduleA
moduleA.hello()
print(moduleA.suzette)

import moduleB as mb
print(mb.adder(5, 7))
print(mb.harry)

from moduleC import bob
print(bob)

from moduleC import *       # least reliable way to import
print(multiplier(3, 4))