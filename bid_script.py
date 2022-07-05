# importing required libraries
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import sys
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

bid_data = pd.read_excel('/home/ganaidu/Pictures/Assignment_1_2/Assignment_1 2/chit_fund_exercise.xlsx')
 
print("Column headings:")
print(bid_data.columns)
print("\n")

#Task1
#Annualized return of the person who bids in the last month
last_month_return = bid_data['Net amount recd by Bid winner']
print("Annualized return of the person who bids in the last month = "+ str(last_month_return[24]))
print("\n")

#Task2
#Annualized return of the person who bids in the first month
last_month_return = bid_data['Net amount recd by Bid winner']
print("Annualized return of the person who bids in the first month = "+ str(last_month_return[0]))
print("\n")

# Task3
#Annualized return of chit fund participant and Return % for each month's bid winner.
for i in bid_data.index:
    print("Annualized return of the participant " + str(bid_data['Month'][i]) + " is " + str(bid_data['Net amount recd by Bid winner'][i]))
print("\n")
for i in bid_data.index:
    print("For month Participant" + str(bid_data['Month'][i])+ " got " + str((bid_data['Net amount recd by Bid winner'][i]/50000.0)*100) + str(" %"))

#Plot
def autolabel(rects):
	"""
	Attach a text label above each bar displaying its height
	"""
	for rect in rects:
		height = rect.get_height()
		ax.text(rect.get_x() + rect.get_width() / 2., 1 * height,'%d' % int(height),ha='center', va='bottom')
        
x = []
y = []

for i in bid_data.index:
	x.append(bid_data['Month'][i])
	y.append(bid_data['Net amount recd by Bid winner'][i])


fig, ax = plt.subplots()
rects = ax.bar(x, y, color='lightskyblue',align='center', edgecolor = None)

majorLocator = MultipleLocator(1)
majorFormatter = FormatStrFormatter('%d')
minorLocator = MultipleLocator(10000)

#calling function
autolabel(rects)

ax.xaxis.set_major_locator(majorLocator)
ax.xaxis.set_major_formatter(majorFormatter)
ax.yaxis.set_major_locator(minorLocator)
ax.yaxis.set_major_formatter(majorFormatter)
plt.title('Bidding Details')
plt.ylabel('Bid Amount')
plt.xlabel('Month')
plt.grid()
plt.show()
