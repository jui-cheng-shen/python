import sympy
from sympy import symbols, Function, Eq, laplace_transform, inverse_laplace_transform, solve, exp, simplify, apart
from sympy.abc import t, s

y = Function('y')
Y = Function('Y')


y0 = -1     # y(0)
dy0 = 2     # y'(0)

f_t = t**2 * exp(-t)

L_y2 = s**2 * Y(s) - s * y0 - dy0
L_y1 = s * Y(s) - y0
L_y  = Y(s)
L_f, cond, _ = laplace_transform(f_t, t, s)


eq_s = Eq(L_y2 + 3 * L_y1 - 4 * L_y, L_f)


Y_s = solve(eq_s, Y(s))[0]
Y_s = simplify(Y_s)
print(f"Y(s) = {Y_s}")


y_t = inverse_laplace_transform(Y_s, s, t)
y_t = simplify(y_t)
print(f"\n微分方程的最終解 y(t) = {y_t}")
