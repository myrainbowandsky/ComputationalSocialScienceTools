import matplotlib
ax=sns.scatterplot(data=score[['cap.english','indegree']], x='cap.english',y='indegree', alpha=0.5,s=25)
plt.xticks(rotation=45)
#plt.xscale('log')
plt.yscale('log')

ax.set_xlabel("CAP")
ax.set_yticks([100, 200, 500])
ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.tick_params(axis='both', which='major', labelsize=15)
#ax.set_xlabel('CAP', labelpad=40)
ax.set_xlabel('CAP', fontsize = 22)
ax.set_ylabel('indegree', fontsize = 20)

# 设置新的图像尺寸
new_size = (4, 3)  # 新的宽度为6英寸，高度为4英寸
fig.set_size_inches(new_size)
#设置新的点的尺寸
scatters = plt.gca().collections[0]
scatters.set_sizes([10])

plt.axvline(x=.7,color='red',linestyle ='--') 

plt.savefig('../Project7/figs/indegree_cap.jpg',bbox_inches='tight')