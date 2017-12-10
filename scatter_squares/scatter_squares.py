import matplotlib.pyplot as plt

x_values=list(range(1,1001))
y_values=[x*x for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors=None,s=4)
#颜色映射(colormap)用来突出数据的规律
#将参数c设置成了一个y值列表，并使用参数cmap告诉pyplot使用那个颜色映射
#将y值较小的点显示为浅色，将y值较大的显示为深蓝

#设置图表标题并给坐标轴加上标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both',which='major',labelsize=14)

#设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])

plt.savefig('Squares_plot.png',bbox_inches='tight')