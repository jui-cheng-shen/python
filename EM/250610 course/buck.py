import sympy as sp

L = 1e-3
C = 1e-3
R = 1
T = 50e-6
f = 1/T
n,t,s = sp.symbols('n t s') #symbols 意思是將變數 t 宣告為符號變數
wn = 2*sp.pi*(2*n-1)*f
N = 21

vcp1 = 0
a1n = R / (L*wn)
a2n = 1 - L*C*wn**2
vcp1n = ((-1)**n / (2*n - 1)) * (a1n * (-a2n) * sp.sin(wn*t) + sp.cos(wn*t) / (a1n * a2n - a1n))


for i in range(1,N):
    vcp1 += vcp1n.subs({n:i}) #subs 意思是將變數 n 代入 i 的值
    # {n:i} 是一個字典，表示將 n 替換為 i 的值


vcp2 = 5/2
v0 = 0
v_0 = 0
vcc = sp.inverse_laplace_transform(1/(L*C*s**2 + (L/R - L*C*v_0)*s + (1-L*C*v0)),s,t)
vs = vcp1 + vcp2

sp.plot(vs, ( t,0,10*T))