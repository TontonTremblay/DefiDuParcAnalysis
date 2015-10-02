import csv
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import time


sns.set(style="white", palette="muted", color_codes=True)



df = pd.DataFrame.from_csv('data.csv')


#Clean the data, remove the NaN in pos. 
df_gpm = df["GPM"]

a1 = []
for i in df_gpm:

	a1.append(float(i[3:5])*60 + float(i[6:8]) + float(i[8:-1]))
df["GPM_s"] = a1
dft = df[df["GPM_s"]>0]

#My performance
per_john =  df[df["Dossard"] == 2065]["GPM_s"].irow(0)

ax = sns.distplot(dft["GPM_s"], color="b")


#Arrange title etc. 
values = ax.xaxis.get_majorticklocs()
labels2 = []
for v in values:
    labels2.append(time.strftime('%M:%S',time.gmtime(v)))
ax.set_xticklabels(labels2)
ax.set_xlabel("Perfomance (minutes : seconds)")
ax.set_ylabel("Distribution (percent)")

#Draw a vertical bar
# sns.plt.axvline(dft["GMP_s"].median(), color='#101010', linestyle='--', linewidth=1.3,alpha=0.5)
sns.plt.axvline(per_john, color='r', linestyle='-', linewidth=1.3,alpha=0.9)
ax.annotate(time.strftime('%M:%S',time.gmtime(per_john)),ha="right",xy=(per_john-20,0.0012))


# sns.plt.show()
sns.plt.savefig("output/simple_dist.png")