
import numpy as np
import matplotlib.pyplot as plt

# 16O density distribution
def density_O(r, rho_0=0.181, a=0.45, R_0=2.525):
    return rho_0 / (1 + np.exp((r - R_0) / a))

# 12C density distribution
def density_C(r, rho_0=0.207, a=0.425, R_0=2.1545):
    return rho_0 / (1 + np.exp((r - R_0) / a))

# 40Ca density distribution
def density_Ca(r, rho_0=0.17, a=0.5, R_0=3.593):
    return rho_0 / (1 + np.exp((r - R_0) / a))

# 58Ni density distribution
def density_Ni(r, rho_0=0.172, a=0.540, R_0=4.094):
    return rho_0 / (1 + np.exp((r - R_0) / a))


# Radial distance (fm)
r = np.linspace(0, 12, 1000)

# Calculate densities
rhoO = density_O(r)
rhoC = density_C(r)
rhoCa = density_Ca(r)
rhoNi = density_Ni(r)


# Plot all density distributions
plt.figure(figsize=(9, 6))

plt.plot(r, rhoO, linestyle='-', linewidth=2, color='black',
         label=r'$^{16}$O')

plt.plot(r, rhoC, linestyle='--', linewidth=2, color='black',
         label=r'$^{12}$C')

plt.plot(r, rhoCa, linestyle='-.', linewidth=2, color='black',
         label=r'$^{40}$Ca')

plt.plot(r, rhoNi, linestyle=':', linewidth=2, color='black',
         label=r'$^{58}$Ni')

plt.xlabel(r'Radial distance $r$ (fm)', fontsize=13)
plt.ylabel(r'Nuclear density $\rho(r)$ (fm$^{-3}$)', fontsize=13)

plt.title('Woods-Saxon Nuclear Density Distributions', fontsize=14)

plt.grid(True, linestyle=':', alpha=0.4)
plt.legend(fontsize=12)

plt.xlim(0, 12)
plt.ylim(0, 0.22)

plt.tight_layout()
plt.show()
