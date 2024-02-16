import matplotlib.pyplot as plt
import numpy as np

fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(2, 2, figsize=(9, 6))

llms = ("0301", "Instruct", "1106", "0125")
color = {
    "CF-CoT": (156/255, 195/255, 229/255),
    "PSPC": (244/255, 177/255, 131/255)
}

x = np.arange(1, len(llms) * 2, 2)  # the label locations
width = 0.6  # the width of the bars
multiplier = 0
fontsize = 8

# 3% setting of r-bert
per0 = {
    "CF-CoT": [60.07, 64.35, 67.45, 67.81],
    "PSPC": [64.49, 65.23, 68.27, 68.52]
}

for method, result in per0.items():
    offset = width * multiplier
    ax0.bar(x + offset, result, width, color=color[method], label=method)
    for i, xi in enumerate(x + offset):
        ax0.text(xi - 0.5 * width, result[i] + 0.2, str(result[i]), fontsize=6, color='gray')
    multiplier += 1

ax0.tick_params(bottom=False, left=False)
ax0.spines['right'].set_visible(False)
ax0.spines['left'].set_visible(False)
ax0.spines['top'].set_visible(False)
ax0.grid(axis='y', linestyle='--')
ax0.set_axisbelow(True)
ax0.set_xticks(x + 0.5 * width, llms, fontsize=fontsize)
ax0.set_ylim(55, 70)
ax0.set_yticks([55, 60, 65, 70])
ax0.tick_params(axis='y', labelsize=fontsize)
ax0.set_title("(a) 3% Setting of R-BERT", fontsize=fontsize)

# 3% setting of r-roberta
per1 = {
    "CF-CoT": [62.97, 65.02, 68.04, 67.06],
    "PSPC": [66.44, 66.37, 69.05, 68.63]
}

multiplier = 0
for method, result in per1.items():
    offset = width * multiplier
    ax1.bar(x + offset, result, width, color=color[method], label=method)
    for i, xi in enumerate(x + offset):
        ax1.text(xi - 0.5 * width, result[i] + 0.2, str(result[i]), fontsize=6, color='gray')
    multiplier += 1

ax1.tick_params(bottom=False, left=False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.grid(axis='y', linestyle='--')
ax1.set_axisbelow(True)
ax1.set_xticks(x + 0.5 * width, llms, fontsize=fontsize)
ax1.set_ylim(55, 70)
ax1.set_yticks([55, 60, 65, 70])
ax1.tick_params(axis='y', labelsize=fontsize)
ax1.set_title("(b) 3% Setting of R-RoBERTa", fontsize=fontsize)

# 5% setting of r-bert
per2 = {
    "CF-CoT": [64.58, 67.89, 71.18, 70.57],
    "PSPC": [70.45, 69.71, 72.21, 72.99]
}

multiplier = 0
for method, result in per2.items():
    offset = width * multiplier
    ax2.bar(x + offset, result, width, color=color[method], label=method)
    for i, xi in enumerate(x + offset):
        ax2.text(xi - 0.5 * width, result[i] + 0.2, str(result[i]), fontsize=6, color='gray')
    multiplier += 1

ax2.tick_params(bottom=False, left=False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.grid(axis='y', linestyle='--')
ax2.set_axisbelow(True)
ax2.set_xticks(x + 0.5 * width, llms, fontsize=fontsize)
ax2.set_ylim(60, 75)
ax2.set_yticks([60, 65, 70, 75])
ax2.tick_params(axis='y', labelsize=fontsize)
ax2.set_title("(c) 5% Setting of R-BERT", fontsize=fontsize)

# 5% setting of r-roberta
per3 = {
    "CF-CoT": [72.12, 73.31, 75.19, 74.84],
    "PSPC": [75.10, 74.58, 76.11, 76.01]
}

multiplier = 0
for method, result in per3.items():
    offset = width * multiplier
    ax3.bar(x + offset, result, width, color=color[method], label=method)
    for i, xi in enumerate(x + offset):
        ax3.text(xi - 0.5 * width, result[i] + 0.2, str(result[i]), fontsize=6, color='gray')
    multiplier += 1

ax3.tick_params(bottom=False, left=False)
ax3.spines['right'].set_visible(False)
ax3.spines['left'].set_visible(False)
ax3.spines['top'].set_visible(False)
ax3.grid(axis='y', linestyle='--')
ax3.set_axisbelow(True)
ax3.set_xticks(x + 0.5 * width, llms, fontsize=fontsize)
ax3.set_ylim(63, 78)
ax3.set_yticks([63, 68, 73, 78])
ax3.tick_params(axis='y', labelsize=fontsize)
ax3.set_title("(d) 5% Setting of R-RoBERTa", fontsize=fontsize)

plt.yticks(fontsize=8)
plt.subplots_adjust(hspace=0.4)
plt.legend(bbox_to_anchor=(1.0, 2.7), ncol=2, fontsize=fontsize)
plt.savefig("version_effectiveness_analysis.pdf", bbox_inches="tight")
plt.show()
