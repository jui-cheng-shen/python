#計算 x ** 2 + y ** 2 + z ** 2 = 100 and y=6平面形成之球帽體積

from sympy import symbols , pi , integrate

y = symbols('y')
R = 10
y_plane = 6
h = R - y_plane

volume_formula = (1/3) * pi * h**2 * (3*R - h)
print("體積=", volume_formula.evalf())

voloume_integral = integrate(pi * ( R**2 - y**2), (y , y_plane ,R))
print("體積=", voloume_integral.evalf())