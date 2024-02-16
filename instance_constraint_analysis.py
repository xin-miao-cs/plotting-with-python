import matplotlib.pyplot as plt
import numpy as np

fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(7, 4))

plms = ("R-BERT", "R-RoBERTa")
color = {
    "W/ Constraint": (156/255, 195/255, 229/255),
    "W/O Constraint": (244/255, 177/255, 131/255)
}

x = np.arange(1, len(plms) + 1)  # the label locations
width = 0.3  # the width of the bars
multiplier = 0

# 3% setting
per0 = {
    "W/ Constraint": [66.91, 68.61],
    "W/O Constraint": [63.22, 67.12]
}

for method, result in per0.items():
    offset = width * multiplier
    ax0.bar(x + offset, result, width, color=color[method], label=method)
    for i, xi in enumerate(x + offset):
        ax0.text(xi - 0.4 * width, result[i] + 0.4, str(result[i]), color='gray')
    multiplier += 1

ax0.tick_params(bottom=False, left=False)
ax0.spines['right'].set_visible(False)
ax0.spines['left'].set_visible(False)
ax0.spines['top'].set_visible(False)
ax0.grid(axis='y', linestyle='--')
ax0.set_axisbelow(True)
ax0.set_xticks(x + 0.5 * width, plms)
ax0.set_ylim(60, 70)
ax0.set_title("(a) 3% Setting", fontsize=10)

# 5% setting
per1 = {
    "W/ Constraint": [72.11, 75.15],
    "W/O Constraint": [70.96, 73.73]
}

multiplier = 0
for method, result in per1.items():
    offset = width * multiplier
    ax1.bar(x + offset, result, width, color=color[method], label=method)
    for i, xi in enumerate(x + offset):
        ax1.text(xi - 0.4 * width, result[i] + 0.4, str(result[i]), color='gray')
    multiplier += 1

ax1.tick_params(bottom=False, left=False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.grid(axis='y', linestyle='--')
ax1.set_axisbelow(True)
ax1.set_xticks(x + 0.5 * width, plms)
ax1.set_ylim(66, 76)
ax1.set_title("(b) 5% Setting", fontsize=10)

plt.legend(bbox_to_anchor=(1.0, 1.25), ncol=2)
plt.savefig("instance_constraint_analysis.pdf", bbox_inches="tight")
plt.show()
