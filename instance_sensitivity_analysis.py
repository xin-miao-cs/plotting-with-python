import matplotlib.pyplot as plt
import numpy as np

fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(2, 2, figsize=(6, 6))

name = ("First", "Second", "Third")
x = np.arange(1, 4)  # the label locations
width = 0.6
fontsize = 10
marker = 'o'
light_color = (226/255, 239/255, 217/255)
standard_color = (197/255, 224/255, 179/255)
dark_color = (168/255, 208/255, 141/255)
line_color = (83/255, 129/255, 53/255)
color = [light_color, standard_color, dark_color]

# 3% setting of r-bert
per0 = np.array([66.91, 66.66, 66.66])
for i in range(len(x)):
    ax0.bar(x[i], per0[i], width=width, color=color[i])
    ax0.text(x[i] - 0.3 * width, per0[i] + 0.3, str(per0[i]), fontsize=8, color='gray')
ax0.plot(x, per0 * 0.95, marker=marker, color=line_color)

ax0.tick_params(bottom=False, left=False)
ax0.spines['right'].set_visible(False)
ax0.spines['left'].set_visible(False)
ax0.spines['top'].set_visible(False)
ax0.grid(axis='y', linestyle='--')
ax0.set_axisbelow(True)
ax0.set_xticks(x, name)
ax0.set_ylim(60, 68)
ax0.set_title("(a) 3% Setting of R-BERT", fontsize=fontsize)

# 3% setting of r-roberta
per1 = np.array([68.61, 68.94, 68.75])
for i in range(len(x)):
    ax1.bar(x[i], per1[i], width=width, color=color[i])
    ax1.text(x[i] - 0.3 * width, per1[i] + 0.3, str(per1[i]), fontsize=8, color='gray')
ax1.plot(x, per1 * 0.95, marker=marker, color=line_color)

ax1.tick_params(bottom=False, left=False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.grid(axis='y', linestyle='--')
ax1.set_axisbelow(True)
ax1.set_xticks(x, name)
ax1.set_ylim(62, 70)
ax1.set_title("(b) 3% Setting of R-RoBERTa", fontsize=fontsize)

# 5% setting of r-bert
per2 = np.array([72.11, 74.90, 74.02])
for i in range(len(x)):
    ax2.bar(x[i], per2[i], width=width, color=color[i])
    ax2.text(x[i] - 0.3 * width, per2[i] + 0.3, str(per2[i]), fontsize=8, color='gray')
ax2.plot(x, per2 * 0.97, marker=marker, color=line_color)

ax2.tick_params(bottom=False, left=False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.grid(axis='y', linestyle='--')
ax2.set_axisbelow(True)
ax2.set_xticks(x, name)
ax2.set_ylim(68, 76)
ax2.set_title("(c) 5% Setting of R-BERT", fontsize=fontsize)

# 5% setting of r-roberta
per3 = np.array([75.15, 75.66, 75.73])
for i in range(len(x)):
    ax3.bar(x[i], per3[i], width=width, color=color[i])
    ax3.text(x[i] - 0.3 * width, per3[i] + 0.3, str(per3[i]), fontsize=8, color='gray')
ax3.plot(x, per3 * 0.96, marker=marker, color=line_color)

ax3.tick_params(bottom=False, left=False)
ax3.spines['right'].set_visible(False)
ax3.spines['left'].set_visible(False)
ax3.spines['top'].set_visible(False)
ax3.grid(axis='y', linestyle='--')
ax3.set_axisbelow(True)
ax3.set_xticks(x, name)
ax3.set_ylim(69, 77)
ax3.set_yticks([69, 71, 73, 75, 77])
ax3.set_title("(d) 5% Setting of R-RoBERTa", fontsize=fontsize)

plt.subplots_adjust(hspace=0.4)
plt.savefig("instance_sensitivity_analysis.pdf", bbox_inches="tight")
plt.show()
