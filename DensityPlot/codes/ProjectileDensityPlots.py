
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ==================================================
# Nuclear density functions
# ==================================================

# Alpha particle density (Gaussian)
def density_alpha(r):
    return 0.4229 * np.exp(-0.7024 * r**2)

# 16O density (Woods-Saxon)
def density_O(r, rho_0=0.181, a=0.45, R_0=2.525):
    return rho_0 / (1 + np.exp((r - R_0) / a))


# ==================================================
# Radial distance and density calculations
# ==================================================

r = np.linspace(0, 10, 1500)

rho_alpha = density_alpha(r)
rho_O = density_O(r)


# ==================================================
# Output directory
# ==================================================

save_dir = Path(
    "/home/aman/Desktop/Research/Code/DensityPlot/plots"
)

save_dir.mkdir(parents=True, exist_ok=True)


# ==================================================
# Plot configuration
# ==================================================

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 13,
    "mathtext.fontset": "stix",
    "axes.linewidth": 1.2,
    "xtick.direction": "in",
    "ytick.direction": "in",
    "xtick.top": True,
    "ytick.right": True,
    "xtick.major.width": 1.2,
    "ytick.major.width": 1.2,
    "xtick.minor.width": 0.8,
    "ytick.minor.width": 0.8,
    "xtick.major.size": 6,
    "ytick.major.size": 6,
    "xtick.minor.size": 3,
    "ytick.minor.size": 3,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.08
})


# ==================================================
# Create figure
# ==================================================

fig, ax = plt.subplots(figsize=(8, 5.5))

# Alpha particle
ax.plot(
    r, rho_alpha,
    color="black",
    linestyle="-",
    linewidth=2.2,
    label=r"$\alpha$ particle"
)

# Oxygen-16
ax.plot(
    r, rho_O,
    color="black",
    linestyle="--",
    linewidth=2.2,
    label=r"$^{16}\mathrm{O}$"
)


# ==================================================
# Axes formatting
# ==================================================

ax.set_xlabel(
    r"Radial distance $r$ (fm)",
    fontsize=15,
    labelpad=8
)

ax.set_ylabel(
    r"Nuclear density $\rho(r)$ (fm$^{-3}$)",
    fontsize=15,
    labelpad=8
)

ax.set_title(
    r"Projectile and Target Nuclear Density Distributions",
    fontsize=15,
    pad=12
)

ax.set_xlim(0, 10)
ax.set_ylim(0, 0.45)

# Major and minor ticks
ax.minorticks_on()

# Grid
ax.grid(
    True,
    which="major",
    linestyle=":",
    linewidth=0.7,
    alpha=0.45
)

# Legend
ax.legend(
    loc="upper right",
    fontsize=12,
    frameon=True,
    fancybox=False,
    edgecolor="black",
    framealpha=1
)

# ==================================================
# Save figures
# ==================================================

# High-resolution raster image
fig.savefig(
    save_dir / "Alpha_16O_Density.png",
    dpi=600
)

# Vector PDF (recommended for LaTeX)
fig.savefig(
    save_dir / "Alpha_16O_Density.pdf"
)

# Vector SVG
fig.savefig(
    save_dir / "Alpha_16O_Density.svg"
)

print("Figures successfully saved in:")
print(save_dir)

plt.show()

