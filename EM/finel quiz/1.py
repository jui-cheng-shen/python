from sympy import symbols ,diff ,solve

x = symbols('x')
P = 3.5* x - (x**2) / 20000 - 5000
dP_dx = diff(P,x)
print("利潤函數 P(x) =", dP_dx)
critical_points = solve(dP_dx, x)
print("臨界點:", critical_points)

if critical_points:
    max_x = critical_points[0]
    if 0 < max_x < 50000:
        max_profit = P.subs(x, max_x)
        print("最大利潤的銷售量為:", max_x)
        print("最大利潤為:", max_profit)