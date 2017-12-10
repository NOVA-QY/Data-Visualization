import matplotlib.pyplot as plt

# x_values=[1,2,3,4,5]
# y_values=[1,8,27,64,125]

x_values=list(range(1,5001))
y_values=[x*x*x for x in x_values]

plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=4)

plt.axis([0,5500,0,100000000])

plt.savefig('cube_of_numbers',bbox_inches='tight')