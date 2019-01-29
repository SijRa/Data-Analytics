# File
import csv

## Libraries
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go


#### Filter list
ignore = [',,','Da','To','Null','Deliveries', '013.28', 'Day', 'tal Sales','-']

#### Data containers
orderDate = []
orderDay = []
orderTotalSales = []
orderDeliveries = []

orderMonths = [
    'August',
    'September',
    'October',
    'November',
    'December',
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July'
    ]

salesTotalMonth = []
salesDeliveryMonth = []

CSV_List = [
    'January.csv',
    'February.csv',
    'March.csv',
    'April.csv',
    'May.csv',
    'June.csv',
    'July.csv',
    'August.csv',
    'September.csv',
    'October.csv',
    'November.csv',
    'December.csv'
    ]

def SortDate(orderDate,orderMonth):
    with open(orderMonth, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
        for row in spamreader:
            string = row[0]
            if(string[0:2] not in ignore):
                orderDate.append(string)


def SortDay(orderDay,orderMonth):
    with open(orderMonth, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
        for row in spamreader:
            try:
                value = row[1]
                if(value not in ignore):
                    orderDay.append(value.replace(" ", ""))
            except IndexError:
                pass
        del orderDay[-1]

def SortDeliveries(orderDeliveries,orderMonth):
    with open(orderMonth, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
        for row in spamreader:
            try:
                value = row[6]
                if(value not in ignore):
                    orderDeliveries.append(value)
            except IndexError:
                pass
        del orderDeliveries[-1]

def SortTotalSales(orderTotalSales,orderMonth):
    with open(orderMonth, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
        for row in spamreader:
            try:
                string = row[5]
                value = string[2:]
                if(value not in ignore):
                    orderTotalSales.append(value)
            except IndexError:
                pass
        del orderTotalSales[-1]

def CustomSalesTotalMonth(orderMonths,salesDeliveryMonth):
    orderMonth = orderMonths + '.csv'
    with open(orderMonth, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
        totalDeliveries = 0
        totalSales = 0
        for row in spamreader:
            try:
                string = row[5]
                totalSale = string[2:]
                if(totalSale not in ignore and len(totalSale) > 5):
                    totalSales+=float(totalSale)
                    value = row[6]
                    if(value != '-'):
                        totalDeliveries+=int(value[0:2])
            except IndexError:
                pass
        valuePerDelivery = totalSales/totalDeliveries
        salesDeliveryMonth.append(round(valuePerDelivery,2))
    
def CreateScatter(orderMonths,salesTotalMonth):
    py.sign_in('Sijra', 'BlVwF1zNWBAJyJXQNufv')
    #Create a trace
    trace = go.Scatter(
        x = orderMonths,
        y = salesTotalMonth,
        mode = 'lines'
        )
    data = [trace]
    py.plot(data, filename='Average Delivery Value 2017-18')

def CreateBoxPlots(orderDay,orderTotalSales):
    py.sign_in('Sijra', 'BlVwF1zNWBAJyJXQNufv')
    #Create a trace
    trace = go.Box(
        x = orderDay,
        y = orderTotalSales,
        )
    data = [trace]
    py.plot(data, filename='sfasfweerwf')


for month in orderMonths:
    CustomSalesTotalMonth(month,salesDeliveryMonth)
CreateScatter(orderMonths,salesDeliveryMonth)

##CREATE GRAPH##
#for month in CSV_List:
#    SortDay(orderDay,month)
#    SortTotalSales(orderTotalSales,month)

#SortDay(orderDay,'July.csv')
#SortTotalSales(orderTotalSales,'July.csv')
#CreateBoxPlots(orderDay,orderTotalSales)

