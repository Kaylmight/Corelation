import csv
import plotly.express as px
import numpy as np

def plotFigure(coffee_sleep):
    with open(coffee_sleep) as f:
        reader = csv.DictReader(f)
        fig = px.scatter(reader, x = 'Coffee in ml', y = 'sleep in hours')
        fig.show()

def getDataSources(coffee_sleep):
    coffee = []
    sleep = []

    with open(coffee_sleep) as f:
        csv_reader = csv.DictReader(f)
        for i in csv_reader:
            coffee.append(float(i['Coffee in ml']))
            sleep.append(float(i['sleep in hours']))

    return{ 'x' : coffee, 'y' : sleep}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource['x'], datasource['y'])
    print('Correlation between Coffee taken in ml and Duration of sleep in hours : \n-->', correlation[0,1])

def setup():
    coffee_sleep = "./coffee.csv"
    datasource = getDataSources(coffee_sleep)
    findCorrelation(datasource)
    plotFigure(coffee_sleep)

setup()