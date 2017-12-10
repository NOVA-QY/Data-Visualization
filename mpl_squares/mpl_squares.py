import matplotlib.pyplot as plt

#plot()假设第一个数据点对应的x坐标值为0,可以给plot()同时提供输入值和输出值
input_values=[1,2,3,4,5]
squares=[1,4,9,16,25]
plt.plot(input_values,squares,linewidth=5)#设置宽度

#设置图标标题
plt.title("Square Numbers",fontsize=24)
#为x、y轴设置标签
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#设置刻度处标记的大小
plt.tick_params(axis='both',labelsize=14)

plt.savefig('mpl_Squares.png',bbox_inches='tight')