import statistics
import pandas as pd
import plotly.figure_factory as ff
import csv
import random

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()

fig = ff.create_distplot([data], ["Reading time"], show_hist = False)
fig.show()

populationmean = statistics.mean(data)
print("Population mean is: " + str(populationmean))

def randomsetofmean(count):
    dataset = []
    for i in range(0, count):
        randomindex = random.randint(0, len(data))
        value = data[randomindex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def showfig(meanlist):
    df = meanlist
    fig = ff.create_distplot([df], ["Reading time"], show_hist = False)
    fig.show()

def setup():
    meanlist = []
    for i in range(0, 100):
        setofmeans = randomsetofmean(30)
        meanlist.append(setofmeans)
    showfig(meanlist)
    print("Sample mean is: " + str(statistics.mean(meanlist)))

setup()