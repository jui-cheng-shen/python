import sympy
from sympy import symbols, pi, I
import numpy as np
import matplotlib.pyplot as plt

# --- 全域參數 ---
T = 20e-6  # 方波週期
omega0 = 2 * np.pi / T  # 基波角頻率
a0 = 0.5  # 直流分量

print(f"方波週期 T = {T} s")
print(f"基波角頻率 omega0 = {omega0:.2f} rad/s")

# --- 1. 傅立葉係數 ---
def get_fourier_coefficients(n_val):
    if n_val == 0:
        return 0.5, 0.0
    if n_val % 2 == 0:
        return 0.0, 0.0
    else:
        an_val = (2 / (n_val * pi)) * sympy.sin(n_val * pi / 2)
        return float(an_val), 0.0

# --- 2. 傳遞函數 H(jω) ---
omega_sym = symbols('omega')
R_sym, L_sym, C_sym = symbols('R L C')
Z_C = 1 / (I * omega_sym * C_sym)
Z_CR_parallel = R_sym / (1 + I * omega_sym * R_sym * C_sym)
Z_L = I * omega_sym * L_sym
H_omega_sym = sympy.simplify(Z_CR_parallel / (Z_L + Z_CR_parallel))

# --- 3. 計算阻尼係數 ξ ---
def calculate_zeta(L, C, R):
    if R == 0 or C == 0:
        return float('inf')
    if L < 0 or C < 0:
        return float('nan')
    zeta = (1 / (2 * R)) * np.sqrt(L / C)
    return zeta

# --- 4. 主函數 ---
def calculate_and_plot_vo_t(L_val, C_val, R_val, case_label, num_harmonics=201):
    print(f"\n--- 子問題 {case_label} ---")
    print(f"L = {L_val} H, C = {C_val} F, R = {R_val} Ω")

    zeta = calculate_zeta(L_val, C_val, R_val)
    print(f"阻尼係數 ξ = {zeta:.4f}")

    if zeta > 1:
        system_type = "過阻尼 (Overdamped)"
    elif zeta == 1:
        system_type = "臨界阻尼 (Critically damped)"
    elif 0 < zeta < 1:
        system_type = "欠阻尼 (Underdamped)"
    else:
        system_type = "特殊/不穩定 (Unstable)"
    print(f"系統類型: {system_type}")

    # 數值化 H(jω)
    H_func = sympy.lambdify((omega_sym, L_sym, C_sym, R_sym), H_omega_sym, 'numpy')
    t_vals = np.linspace(0, 0.001, 1000)
    vo_t = np.zeros_like(t_vals)

    # 直流分量
    H_at_dc = np.complex128(H_func(0, L_val, C_val, R_val))
    vo_t += a0 * np.real(H_at_dc)
    vo_series_terms = [f"{a0 * np.real(H_at_dc):.4f}"]

    # 諧波疊加
    for n in range(1, num_harmonics, 2):
        an, bn = get_fourier_coefficients(n)
        H_n = np.complex128(H_func(n * omega0, L_val, C_val, R_val))
        H_mag = np.abs(H_n)
        H_phase = np.angle(H_n)

        vo_t += H_mag * an * np.cos(n * omega0 * t_vals + H_phase)
        if abs(an) > 1e-9 and H_mag > 1e-9:
            coeff = H_mag * an
            phase_deg = np.degrees(H_phase)
            vo_series_terms.append(f"{coeff:.4f} * cos({n * omega0:.1f}t + {phase_deg:.1f}°)")

    # --- 繪圖 ---
    plt.figure(figsize=(10, 5))
    plt.plot(t_vals * 1e3, vo_t, label='Vo(t)', color='blue')
    plt.title(f'輸出電壓 Vo(t) - 子問題 {case_label} (ξ={zeta:.4f}, {system_type})')
    plt.xlabel('時間 (ms)')
    plt.ylabel('Vo(t) (V)')
    plt.grid(True)
    plt.xlim(0, 1)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # --- 顯示傅立葉級數 ---
    print("\n輸出電壓 Vo(t) 的傅立葉級數近似 (前幾項):")
    print("Vo(t) ≈ " + " + ".join(vo_series_terms[:10]))
    if len(vo_series_terms) > 10:
        print(" + ... (更多項省略)")

# --- 執行三個案例 ---
calculate_and_plot_vo_t(1e-1, 2e-6, 50, 'a')   # 子問題 a
calculate_and_plot_vo_t(1e-3, 1e-9, 10, 'b')   # 子問題 b
calculate_and_plot_vo_t(1e-5, 3e-5, 2,  'c')   # 子問題 c
