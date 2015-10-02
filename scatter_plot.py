import csv
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import time


sns.set(style="white", palette="muted", color_codes=True)



df = pd.DataFrame.from_csv('data.csv')


#Clean the data, remove the NaN in pos. 
df_gpm1 = df["GPM1"]
df_gpm2 = df["GPM2"]

a1 = []
a2 = []
for i in df_gpm1:
	t = time.strptime(i[0:8],"%H:%M:%S")
	print i 
	a1.append(float(i[3:5])*60 + float(i[6:8]) + float(i[8:-1]))
	
	quit()
for i in df_gpm2:
	a2.append(float(i[3:5])*60 + float(i[6:8]) + float(i[8:-1]))



df["GPM1_s"] = a1
df["GPM2_s"] = a2
dft = df[(df["GPM1_s"]>0) & (df["GPM2_s"]>0)]

#My performance

per = [{"id":2065,'name':'J.','c':'r.'},{"id":1771,'name':'H.',"c":"g."},{"id":922,'name':'D.','c':"c."},{"id":1005,'name':'M.','c':'y.'}]

for i in per:
	i["gp"] = (df[df["Dossard"] == i["id"]]["GPM1_s"].irow(0),df[df["Dossard"] == i["id"]]["GPM2_s"].irow(0)) 
print per[3]['gp']

# ax = sns.distplot(dft["GPM_s"], color="b")
ax = sns.lmplot(x="GPM1_s", y="GPM2_s",data = dft).ax

ax.set(xlim=(100, 800), ylim=(200, 1400))

for i in per:
	sns.plt.plot(i['gp'][0], i['gp'][1], i['c'], markersize=10.0,alpha=1)
	# sns.plt.annotate(i['name'],ha="left",xy=(i['gp'][0]+20,i['gp'][1]-50))

# print type(ax)

#Arrange title etc. 
values = ax.xaxis.get_majorticklocs()
labels2 = []
for v in values:
    labels2.append(time.strftime('%M:%S',time.gmtime(v)))
ax.set_xticklabels(labels2)

values = ax.yaxis.get_majorticklocs()
labels2 = []
for v in values:
    labels2.append(time.strftime('%M:%S',time.gmtime(v)))
ax.set_yticklabels(labels2)

ax.set_xlabel("Perfomance DF1 (minutes : seconds)")
ax.set_ylabel("Perfomance DF2 (minutes : seconds)")

#Draw a vertical bar
# sns.plt.axvline(dft["GMP_s"].median(), color='#101010', linestyle='--', linewidth=1.3,alpha=0.5)
# sns.plt.axvline(per_john, color='r', linestyle='-', linewidth=1.3,alpha=0.9)


sns.plt.show()
# sns.plt.savefig("output/simple_dist.png")