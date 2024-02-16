import matplotlib.pyplot as plt
import numpy as np

fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(9, 3))

color = {
    "R-BERT": (46/255, 117/255, 181/255),
    "R-RoBERTa": (197/255, 90/255, 17/255)
}

marker = {
    "R-BERT": "o-",
    "R-RoBERTa": "^-"
}

x = np.arange(1, 6)  # the label locations
alpha = 0.6
linewidth = 2
fontsize = 10

# 3% setting
per0 = {
    "R-BERT": [55.73, 62.91, 66.91, 64.61, 61.32],
    "R-RoBERTa": [62.95, 67.83, 68.61, 67.44, 66.97]
}

for method, result in per0.items():
    ax0.plot(x, per0[method], marker[method], color=color[method], label=method, alpha=alpha, linewidth=linewidth)

ax0.tick_params(left=False)
ax0.spines['right'].set_visible(False)
ax0.spines['top'].set_visible(False)
ax0.grid(axis='y', linestyle='--')
ax0.set_axisbelow(True)
ax0.set_yticks([56, 60, 64, 68])
ax0.set_title("(a) 3% Setting", fontsize=fontsize)

# 5% setting
per1 = {
    "R-BERT": [64.90, 70.46, 72.11, 72.72, 69.38],
    "R-RoBERTa": [68.28, 75.43, 75.15, 76.03, 74.37]
}

for method, result in per1.items():
    ax1.plot(x, per1[method], marker[method], color=color[method], label=method, alpha=alpha, linewidth=linewidth)

ax1.tick_params(left=False)
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.grid(axis='y', linestyle='--')
ax1.set_axisbelow(True)
ax1.set_yticks([65, 68, 72, 76])
ax1.set_title("(b) 5% Setting", fontsize=fontsize)

plt.legend(bbox_to_anchor=(1.0, 1.3), ncol=2, fontsize=fontsize)
plt.savefig("aspect_quantity_analysis.pdf", bbox_inches="tight")
plt.show()
