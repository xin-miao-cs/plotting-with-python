import matplotlib.pyplot as plt
import numpy as np

fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(6, 3))

color = {
    "R-BERT": (46/255, 117/255, 181/255),
    "R-RoBERTa": (197/255, 90/255, 17/255)
}

marker = {
    "R-BERT": "o-",
    "R-RoBERTa": "^-"
}

x = np.arange(1, 4)  # the label locations
alpha = 0.6
linewidth = 2
fontsize = 10

# 3% setting
per0 = {
    "R-BERT": [66.91, 66.94, 66.87],
    "R-RoBERTa": [68.61, 70.07, 70.00]
}

for method, result in per0.items():
    ax0.plot(x, per0[method], marker[method], color=color[method], label=method, alpha=alpha, linewidth=linewidth)

ax0.tick_params(left=False)
ax0.spines['right'].set_visible(False)
ax0.spines['top'].set_visible(False)
ax0.grid(axis='y', linestyle='--')
ax0.set_axisbelow(True)
ax0.set_xticks([1, 2, 3])
ax0.set_yticks([66, 67, 68, 69, 70])
ax0.set_title("(a) 3% Setting", fontsize=fontsize)

# 5% setting
per1 = {
    "R-BERT": [72.11, 74.85, 74.14],
    "R-RoBERTa": [75.15, 76.52, 76.41]
}

for method, result in per1.items():
    ax1.plot(x, per1[method], marker[method], color=color[method], label=method, alpha=alpha, linewidth=linewidth)

ax1.tick_params(left=False)
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.grid(axis='y', linestyle='--')
ax1.set_axisbelow(True)
ax1.set_xticks([1, 2, 3])
ax1.set_title("(b) 5% Setting", fontsize=fontsize)

plt.legend(bbox_to_anchor=(1.0, 1.3), ncol=2, fontsize=fontsize)
plt.savefig("instance_quantity_analysis.pdf", bbox_inches="tight")
plt.show()
