import matplotlib.pyplot as plt


fig = plt.figure(figsize=(6, 3))

# figure 1
sub_plot = fig.add_subplot(121)

MICE_suggestion_x = 1
MICE_suggestion_y = 114
MICE_suggestion_label = "MICE"

AutoCAD_suggestion_x = 1.5
AutoCAD_suggestion_y = 113
AutoCAD_suggestion_label = "AutoCAD"

CoCo_suggestion_x = 2
CoCo_suggestion_y = 95
CoCo_suggestion_label = "CoCo"

CCG_suggestion_x = 2.5
CCG_suggestion_y = 90
CCG_suggestion_label = "CCG"

ChatGPT_suggestion_x = 3
ChatGPT_suggestion_y = 41
ChatGPT_suggestion_label = "ChatGPT"


sub_plot.bar(MICE_suggestion_x, MICE_suggestion_y, width=0.46, alpha=0.5, label=MICE_suggestion_label)
sub_plot.text(MICE_suggestion_x, MICE_suggestion_y + 0.5, "114", ha='center')
sub_plot.bar(AutoCAD_suggestion_x, AutoCAD_suggestion_y, width=0.46, alpha=0.5, label=AutoCAD_suggestion_label)
sub_plot.text(AutoCAD_suggestion_x, AutoCAD_suggestion_y + 0.5, "113", ha='center')
sub_plot.bar(CoCo_suggestion_x, CoCo_suggestion_y, width=0.46, alpha=0.5, label=CoCo_suggestion_label)
sub_plot.text(CoCo_suggestion_x, CoCo_suggestion_y + 0.5, "95", ha='center')
sub_plot.bar(CCG_suggestion_x, CCG_suggestion_y, width=0.46, alpha=0.5, label=CoCo_suggestion_label)
sub_plot.text(CCG_suggestion_x, CCG_suggestion_y + 0.5, "90", ha='center')
sub_plot.bar(ChatGPT_suggestion_x, ChatGPT_suggestion_y, width=0.46, alpha=0.5, label=CoCo_suggestion_label)
sub_plot.text(ChatGPT_suggestion_x, ChatGPT_suggestion_y + 0.5, "41", ha='center')

plt.xticks([])
plt.yticks([30, 60, 90, 120])
plt.ylim(30, 120)
sub_plot.spines["top"].set_visible(False)
sub_plot.spines["right"].set_visible(False)
sub_plot.spines["left"].set_linewidth(1.5)
sub_plot.spines["bottom"].set_linewidth(1.5)

sub_plot.set_xlabel("Grammatical Suggestions (↓)", fontsize=10, fontweight='bold')
sub_plot.xaxis.set_label_coords(0.5, -0.05)
sub_plot.set_ylabel("Quantity", fontsize=10, fontweight='bold')

# figure 2
sub_plot = fig.add_subplot(122)

MICE_score_x = 1
MICE_score_y = 35
MICE_score_label = "MICE"

AutoCAD_score_x = 1.5
AutoCAD_score_y = 35
AutoCAD_score_label = "AutoCAD"

CoCo_score_x = 2
CoCo_score_y = 45
CoCo_score_label = "CoCo"

CCG_score_x = 2.5
CCG_score_y = 47
CCG_score_label = "CCG"

ChatGPT_score_x = 3
ChatGPT_score_y = 76
ChatGPT_score_label = "ChatGPT"

sub_plot.bar(MICE_score_x, MICE_score_y, width=0.46, alpha=0.5, label=MICE_score_label)
sub_plot.text(MICE_score_x, MICE_score_y + 0.5, "35", ha='center')
sub_plot.bar(AutoCAD_score_x, AutoCAD_score_y, width=0.46, alpha=0.5, label=AutoCAD_score_label)
sub_plot.text(AutoCAD_score_x, AutoCAD_score_y + 0.5, "35", ha='center')
sub_plot.bar(CoCo_score_x, CoCo_score_y, width=0.46, alpha=0.5, label=CoCo_score_label)
sub_plot.text(CoCo_score_x, CoCo_score_y + 0.5, "45", ha='center')
sub_plot.bar(CCG_score_x, CCG_score_y, width=0.46, alpha=0.5, label=CCG_score_label)
sub_plot.text(CCG_score_x, CCG_score_y + 0.5, "47", ha='center')
sub_plot.bar(ChatGPT_score_x, ChatGPT_score_y, width=0.46, alpha=0.5, label=ChatGPT_score_label)
sub_plot.text(ChatGPT_score_x, ChatGPT_score_y + 0.5, "76", ha='center')

plt.xticks([])
plt.yticks([30, 50, 70, 90])
plt.ylim(30, 90)
sub_plot.spines["top"].set_visible(False)
sub_plot.spines["right"].set_visible(False)
sub_plot.spines["left"].set_linewidth(1.5)
sub_plot.spines["bottom"].set_linewidth(1.5)

sub_plot.set_xlabel("Overall Quality (↑)", fontsize=10, fontweight='bold')
sub_plot.xaxis.set_label_coords(0.5, -0.05)
sub_plot.set_ylabel("Score", fontsize=10, fontweight='bold')

plt.legend(bbox_to_anchor=(-0.1, 1.15), loc='upper center', ncol=5, fontsize=8)
# plt.savefig("readability_study.pdf", bbox_inches="tight")
plt.show()
