
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. Density range
# ==========================================

rho = np.linspace(0, 0.65, 1000)  # fm^-3

# ==========================================
# 2. Density-dependent parameters
# ==========================================

# BDM3Y1
C1 = 1.2521
gamma1 = 1.7452
n1 = 1

# BDM3Y2
C2 = 1.0664
gamma2 = 6.0296
n2 = 2

# BDM3Y3
C3 = 1.0045
gamma3 = 25.115
n3 = 3

# DDM3Y1
C4 = 0.2963
alpha4 = 3.7231
beta4 = 3.7384

# ==========================================
# 3. Density-dependent functions
# ==========================================

F_BDM3Y1 = C1 * (1 - gamma1 * rho**n1)

F_BDM3Y2 = C2 * (1 - gamma2 * rho**n2)

F_BDM3Y3 = C3 * (1 - gamma3 * rho**n3)

F_DDM3Y1 = C4 * (1 + alpha4 * np.exp(-beta4 * rho))

# ==========================================
# 4. Plot
# ==========================================

plt.figure(figsize=(11, 7))

plt.plot(rho, F_BDM3Y1, label="BDM3Y1", linewidth=2)
plt.plot(rho, F_BDM3Y2, label="BDM3Y2", linewidth=2)
plt.plot(rho, F_BDM3Y3, label="BDM3Y3", linewidth=2)
plt.plot(rho, F_DDM3Y1, label="DDM3Y1", linewidth=2)

plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0.3413, color="gray", linestyle="--",
            label=r"BDM3Y3 zero crossing")

plt.xlabel(r"Density $\rho$ (fm$^{-3}$)", fontsize=14)
plt.ylabel(r"Density dependence $F(\rho)$", fontsize=14)

plt.title("Density Dependence of M3Y-Paris Interactions",
          fontsize=15)

plt.xlim(0, 0.65)
plt.grid(alpha=0.3)
plt.legend(fontsize=11)
plt.tight_layout()

plt.savefig("Density_Dependence_Comparison.png", dpi=300)
plt.show()
