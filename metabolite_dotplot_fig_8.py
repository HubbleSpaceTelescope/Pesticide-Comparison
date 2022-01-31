import numpy as np
import matplotlib.pyplot as plt
import csv
import matplotlib

plt.rcParams["font.family"] = "Bahnschrift"
cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ["dodgerblue","lightgrey"])

pesticide = []
metabolite = []
logfold = []
pval = []

with open('Metaboanalyst_Combined_Statistical_Analysis.csv', 'r', newline='') as fp:
    reader = csv.reader(fp)
    for line in reader:
        pesticide.append(line[0])
        metabolite.append(line[1])
        logfold.append(abs(float(line[2]))*20)
        pval.append(float(line[3]))

fig, ax = plt.subplots(1, figsize=(10,5))
p = ax.scatter(metabolite, pesticide, c=pval, s=logfold, cmap=cmap, vmin=0, vmax=0.05)
plt.legend(loc="lower left", markerscale=2., scatterpoints=1, fontsize=10)
plt.xticks(rotation='vertical')

# Legend:
handles, labels = p.legend_elements(prop="sizes", alpha=0.6, num=5)
legend2 = ax.legend(handles, labels, loc="upper right", title="Log2-Fold Change", bbox_to_anchor=(1.4, 1.1))

# Colorbar:
cbar = fig.colorbar(p, shrink=0.5)
cbar.ax.set_ylabel('p Value', rotation=270, labelpad=15)

# Title, labels, and visual modifications:
plt.title('Metabolite Changes')
plt.xlabel('Metabolite')
plt.ylabel('Pesticide')
ax.grid(axis='x', linestyle='dotted')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.savefig('Enrichment.jpg', dpi=300, bbox_inches='tight')
plt.show()