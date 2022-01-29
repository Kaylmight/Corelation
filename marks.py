import csv
import plotly.express as px
import numpy as np

def plotFigure(data_path):
    with open(data_path) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df, x = 'Days Present', y = 'Marks In Percentage')
        fig.show()

def getDataSource(data_path):
    days_present = []
    marks = []
    with open(data_path) as f:
        csv_reader = csv.DictReader(f)
        for i in csv_reader:
            days_present.append(float(i['Days Present']))
            marks.append(float(i['Marks In Percentage']))
        
    return{'x': days_present, 'y': marks}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource['x'], datasource['y'])
    print("Correlation between Days present and marks in percentage :- \n--->",correlation[0,1])

def setup():
    data_path = './marks.csv'
    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()