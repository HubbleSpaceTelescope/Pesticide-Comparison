import numpy as np
import matplotlib.pyplot as plt
import csv
import matplotlib

plt.rcParams["font.family"] = "Bahnschrift"
cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ["dodgerblue","lightgrey"])

pesticide = []
pathway = []
enrichmentratio = []
pval = []

headers = input('Does your data contain a header row (y/n)? : ')

with open('dotplotdata.csv', 'r', newline='') as fp:
    reader = csv.reader(fp)
    if headers == 'y':
        next(reader)
    for line in reader:
        pesticide.append(line[0])
        pathway.append(line[1])
        enrichmentratio.append(float(line[2])*3) #NOTE: This is being multiplied by 3. Edit labels (Inkscape/Adobe) after generating figure.
        pval.append(float(line[3]))

fig, ax = plt.subplots(1)
p = ax.scatter(pathway, pesticide, c=pval, s=enrichmentratio, cmap=cmap, vmin=0, vmax=0.05)
plt.legend(loc="lower left", markerscale=2., scatterpoints=1, fontsize=10)
plt.xticks(rotation='vertical')

# Legend:
handles, labels = p.legend_elements(prop="sizes", alpha=0.6, num=4)
legend2 = ax.legend(handles, labels, loc="upper right", title="Enrichment Ratio", bbox_to_anchor=(1.4, 1.1))

# Colorbar:
cbar = fig.colorbar(p, shrink=0.5)
cbar.ax.set_ylabel('p Value', rotation=270, labelpad=15)

# Title, labels, and visual modifications:
plt.title('Metabolic Pathway Enrichment')
plt.xlabel('Metabolic Pathway')
plt.ylabel('Pesticide')
ax.grid(axis='x', linestyle='dotted')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.savefig('dotplot.jpg', dpi=300, bbox_inches='tight')
plt.show()