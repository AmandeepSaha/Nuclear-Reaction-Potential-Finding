
import numpy as np
import matplotlib.pyplot as plt

# Alpha particle density (Gaussian)
def density_alpha(r):
    return 0.4229 * np.exp(-0.7024 * r**2)

# 16O density (as provided)
def density_O(r, rho_0=0.181, a=0.45, R_0=2.525):
    return rho_0 / (1 + np.exp((r - R_0) / a))

# Radial distance (fm)
r = np.linspace(0, 10, 1000)

# Calculate densities
rho_alpha = density_alpha(r)
rho_O = density_O(r)

# Plot
plt.figure(figsize=(9, 6))

plt.plot(r, rho_alpha, color='black', linestyle='-',
         linewidth=2, label=r'$\alpha$ particle')

plt.plot(r, rho_O, color='black', linestyle='--',
         linewidth=2, label=r'$^{16}$O')

plt.xlabel(r'Radial distance $r$ (fm)', fontsize=13)
plt.ylabel(r'Target density $\rho(r)$ (fm$^{-3}$)', fontsize=13)

plt.title('Gaussian Nuclear Density Distributions', fontsize=14)

plt.grid(True, linestyle=':', alpha=0.4)
plt.legend(fontsize=12)

plt.xlim(0, 10)
plt.ylim(0, 0.45)

plt.tight_layout()
plt.show()

