import matplotlib.pyplot as plt

# data prep (I made up data no accuracy in these stats)
mobile = ['Iphone','Galaxy','Pixel']

# Data for the mobile units sold for 4 Quaters in Million
units_sold = (('2016',12,8,6),
('2017',14,10,7),
('2018',16,12,8),
('2019',18,14,10),
('2020',20,16,5),)
# data prep - splitting the data
Years, IPhone_Sales, Galaxy_Sales, Pixel_Sales = zip(*units_sold)

# set the position
Position = list(range(len(units_sold)))

# set the width
Width = 0.2

plt.subplot(2, 1, 1)
Iphone = plt.bar(Position, IPhone_Sales,color='green')
plt.ylabel('IPhone Sales')
plt.xticks(Position, Years)

plt.twinx()
Galaxy = plt.plot(Position, Galaxy_Sales, 'o-', color='blue')
plt.ylabel('Galaxy Sales')
plt.xticks(Position, Years)


plt.show()
#plt.savefig('CombiningGraphs.png', dpi=72)