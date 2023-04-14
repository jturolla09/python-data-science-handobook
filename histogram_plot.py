import seaborn as sns
import matplotlib.pyplot as plt

sns.set(rc={'figure.figsize':(16,9)})
fig, ax = plt.subplots()

sns.histplot(data=results, x="foo", hue = 'reference_date', hue_order = [datetime.date(2023,4,13), datetime.date(2022,12,31)], ax=ax).set_title("foo")

ax2 = ax.twinx()
sns.histplot(data=results, cumulative = True, stat='percent', element = 'poly', fill=False, x="foo", hue = 'reference_date', hue_order = [datetime.date(2023,4,13), datetime.date(2022,12,31)], ax=ax2)
ax2.grid(False)
ax2.get_legend().remove()

plt.tight_layout()
plt.show()
