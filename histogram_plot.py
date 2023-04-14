import seaborn as sns
import matplotlib.pyplot as plt

sns.set(rc={'figure.figsize':(16,9)})

fig, ax = plt.subplots()
sns.histplot(data=results, x="Foo", ax=ax).set_title("Foo")

ax2 = ax.twinx()
sns.histplot(data=results, cumulative = True, stat='percent', element = 'poly', fill=False, x="perf_cumulative", ax=ax2)
ax2.grid(False)

plt.tight_layout()
plt.show()
