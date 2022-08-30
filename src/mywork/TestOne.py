from z3 import *



x = Int('x')
y = Int('y')
z = Int('z')

solve(1500*x + 100 * y + 25 * z == 10000, x + y + z == 100, x > 0, y > 0, z > 0)