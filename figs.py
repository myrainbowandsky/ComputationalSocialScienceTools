#!/usr/bin/env python

import matplotlib
ax=sns.scatterplot(data=score[['cap.english','indegree']], x='cap.english',y='indegree', alpha=0.5,s=10)
plt.xticks(rotation=45)
plt.plot( markersize=0.2)
#plt.xscale('log')
plt.yscale('log')

ax.set_xlabel("CAP")
ax.set_yticks([100, 200, 500])
ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
