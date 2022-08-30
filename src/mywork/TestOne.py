from z3 import *



x = Int('x')
y = Int('y')
z = Int('z')

solve(15*x + y + .25 * z == 100, x + y + z == 100, x > 0, y > 0, z > 0)