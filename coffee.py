import plotly.express as px
import numpy as np
import csv

def getDataSource(data_path):
    coffee_in_ml = []
    sleep_in_hours = []
    with open(data_path) as csv_files:
        csv_reader = csv.DictReader(csv_files)
        for row in csv_reader:
            coffee_in_ml.append(float(row["Coffee in ml"]))
            sleep_in_hours.append(float(row["sleep in hours"]))

    return{"x":coffee_in_ml,"y":sleep_in_hours}

def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation between Coffee in ML vs Sleep in hours")

def setup():
    data_path='./coffee.csv'

    datasource=getDataSource(data_path)
    findCorrelation(datasource)

setup()
        