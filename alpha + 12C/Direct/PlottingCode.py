
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# =====================================================
# 1. USER SETTINGS
# =====================================================

TITLE = r"$\alpha + {}^{12}\mathrm{C}$"

CSV_FILE = "data.csv"
OUTPUT_FILE = "Direct_Potential.png"

INTERPOLATION_POINTS = 2000

FIGURE_SIZE = (12, 8)
DPI = 600

# =====================================================
# 2. LOAD AND VALIDATE DATA
# =====================================================

df = pd.read_csv(CSV_FILE)

# Clean column names
df.columns = (
    df.columns.str.strip()
    .str.replace("\ufeff", "", regex=False)
    .str.lower()
)

# Identify range column
if "range" not in df.columns:
    raise ValueError("CSV must contain a 'range' column.")

# Identify all model columns automatically
models = [col for col in df.columns if col != "range"]

if not models:
    raise ValueError("No model columns found in CSV.")

# Convert data into numerical format
df = df.apply(pd.to_numeric, errors="raise")

# Extract range
x = df["range"].to_numpy(dtype=float)

# Sort according to range
sort_idx = np.argsort(x)
x = x[sort_idx]

# Check for duplicate range values
if len(np.unique(x)) != len(x):
    raise ValueError("Duplicate range values found.")

# High-resolution interpolation grid
x_fine = np.linspace(
    x.min(),
    x.max(),
    INTERPOLATION_POINTS
)

# =====================================================
# 3. LINE STYLES AND MARKERS
# =====================================================

# Six distinct line patterns
line_styles = [
    "-",
    "--",
    "-.",
    ":",
    (0, (5, 1)),
    (0, (3, 1, 1, 1))
]

# Six distinct marker shapes
markers = [
    "o",
    "s",
    "^",
    "D",
    "v",
    "P"
]

# =====================================================
# 4. PLOT ALL MODELS
# =====================================================

fig, ax = plt.subplots(figsize=FIGURE_SIZE)

for i, model in enumerate(models):

    y = df[model].to_numpy(dtype=float)[sort_idx]

    # Check for invalid values
    if not np.all(np.isfinite(y)):
        raise ValueError(f"Invalid numerical values in {model}.")

    # Cubic spline interpolation
    spline = CubicSpline(x, y)
    y_fine = spline(x_fine)

    # Plot interpolated curve
    ax.plot(
        x_fine,
        y_fine,
        color="black",
        linestyle=line_styles[i % len(line_styles)],
        linewidth=2.0,
        label=model.upper()
    )

    # Plot original numerical data points
    ax.scatter(
        x,
        y,
        marker=markers[i % len(markers)],
        s=38,
        facecolors="white",
        edgecolors="black",
        linewidths=1.1,
        zorder=3
    )

# =====================================================
# 5. GRAPH FORMATTING
# =====================================================

ax.set_title(
    TITLE,
    fontsize=18,
    pad=15
)

ax.set_xlabel(
    r"Range (fm)",
    fontsize=16
)

ax.set_ylabel(
    r"$V_{\mathrm{direct}}$ (MeV)",
    fontsize=16
)

# Remove horizontal margins
ax.set_xlim(x.min(), x.max())

# Major ticks
ax.tick_params(
    axis="both",
    which="major",
    labelsize=13,
    direction="in",
    length=6,
    width=1.2
)

# Minor ticks
ax.tick_params(
    axis="both",
    which="minor",
    direction="in",
    length=3
)

ax.minorticks_on()

# Four-sided ticks
ax.tick_params(
    top=True,
    right=True
)

# Legend
ax.legend(
    fontsize=12,
    frameon=True,
    edgecolor="black",
    fancybox=False,
    loc="best"
)

# Graph border
for spine in ax.spines.values():
    spine.set_linewidth(1.2)

# =====================================================
# 6. SAVE AND DISPLAY
# =====================================================

plt.tight_layout()

plt.savefig(
    OUTPUT_FILE,
    dpi=DPI,
    bbox_inches="tight"
)

plt.show()

print(f"Graph saved successfully: {OUTPUT_FILE}")
print(f"Models plotted: {len(models)}")
print("Model names:", [m.upper() for m in models])
