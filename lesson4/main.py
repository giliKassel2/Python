import matplotlib.pyplot as plt
#1
# month = [1,2,3,4,5,6,7,8,9,10,11,12];
# temp = [20,22,23,27,30,28,25,15,10,9,8,7];
# plt.plot(month,temp);
# plt.show()

#2
# category = ["food","dishes" ,"clothes" ,"home"]
# sales = [100,250,50,200];
# plt.bar(category,sales )
# plt.xlabel('Categories')
# plt.ylabel('sales')
# plt.show()

#3
# houers = [4,5,6,7,2,1]
# grade = [80,50,90,100,50,60]
# plt.scatter(houers,grade ,s=[1000,1000,1000,1000,1000,1000],alpha=0.5, cmap='viridis')
# plt.show()

#4
# ages = [22, 45, 30, 35, 50, 41, 28, 33, 55, 65, 29, 42, 48, 31]
# plt.hist(ages, bins=[20, 30, 40, 50, 60, 70], edgecolor='black')
# plt.show()

#5
years = range(2010, 2021)
consumption_oil = [100, 105, 110, 120, 125, 130, 135, 140, 145, 150, 155]
consumption_gas = [80, 82, 85, 88, 90, 95, 100, 105, 110, 115, 120]
consumption_renewable = [20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90]
fig ,axs = plt.subplot(2,2)
axs[0,0].plot(2010,consumption_oil,'tab:blue')
plt.show()