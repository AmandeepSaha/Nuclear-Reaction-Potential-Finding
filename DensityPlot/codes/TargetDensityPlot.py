
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ==========================================
# Nuclear density distributions
# ==========================================

# 16O
def density_O(r, rho_0=0.181, a=0.45, R_0=2.525):
    return rho_0 / (1 + np.exp((r - R_0) / a))

# 12C
def density_C(r, rho_0=0.207, a=0.425, R_0=2.1545):
    return rho_0 / (1 + np.exp((r - R_0) / a))

# 40Ca
def density_Ca(r, rho_0=0.17, a=0.5, R_0=3.593):
    return rho_0 / (1 + np.exp((r - R_0) / a))

# 58Ni
def density_Ni(r, rho_0=0.172, a=0.540, R_0=4.094):
    return rho_0 / (1 + np.exp((r - R_0) / a))


# ==========================================
# Numerical calculation
# ==========================================

r = np.linspace(0, 12, 1500)

rhoO = density_O(r)
rhoC = density_C(r)
rhoCa = density_Ca(r)
rhoNi = density_Ni(r)


# ==========================================
# Publication-quality plot settings
# ==========================================

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 13,
    'axes.labelsize': 15,
    'axes.titlesize': 16,
    'legend.fontsize': 12,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'mathtext.fontset': 'stix',
    'axes.linewidth': 1.2,
    'savefig.dpi': 600,
    'savefig.bbox': 'tight'
})


# ==========================================
# Create figure
# ==========================================

fig, ax = plt.subplots(figsize=(8, 6))

# 16O
ax.plot(r, rhoO,
        color='black', linestyle='-',
        linewidth=2.2, label=r'$^{16}\mathrm{O}$')

# 12C
ax.plot(r, rhoC,
        color='black', linestyle='--',
        linewidth=2.2, label=r'$^{12}\mathrm{C}$')

# 40Ca
ax.plot(r, rhoCa,
        color='black', linestyle='-.',
        linewidth=2.2, label=r'$^{40}\mathrm{Ca}$')

# 58Ni
ax.plot(r, rhoNi,
        color='black', linestyle=':',
        linewidth=2.5, label=r'$^{58}\mathrm{Ni}$')


# ==========================================
# Axis formatting
# ==========================================

ax.set_xlabel(r'Radial distance $r$ (fm)')
ax.set_ylabel(r'Nuclear density $\rho(r)$ (fm$^{-3}$)')

ax.set_title('Woods-Saxon Nuclear Density Distributions')

ax.set_xlim(0, 12)
ax.set_ylim(0, 0.22)


# ==========================================
# Ticks and grid
# ==========================================

ax.minorticks_on()

ax.tick_params(axis='both', which='major',
               direction='in', length=6,
               width=1.1, top=True, right=True)

ax.tick_params(axis='both', which='minor',
               direction='in', length=3,
               width=0.8, top=True, right=True)

ax.grid(True, which='major',
        linestyle=':', linewidth=0.7, alpha=0.45)


# ==========================================
# Legend
# ==========================================

ax.legend(loc='upper right',
          frameon=True,
          edgecolor='black',
          fancybox=False)


# ==========================================
# Save figures
# ==========================================

output_dir = Path(
    "/home/aman/Desktop/Research/Code/DensityPlot/plots"
)

output_dir.mkdir(parents=True, exist_ok=True)

# PNG - 600 DPI
fig.savefig(
    output_dir / "Woods_Saxon_Density.png",
    dpi=600,
    facecolor='white'
)

# PDF - Vector format
fig.savefig(
    output_dir / "Woods_Saxon_Density.pdf",
    format='pdf',
    facecolor='white'
)

print("Plot saved successfully!")
print(f"Location: {output_dir}")

plt.show()

