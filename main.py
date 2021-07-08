import plotly.figure_factory as ff
import pandas as pd
import csv 
import random
import statistics
import plotly.graph_objects as go
df = pd.read_csv('medium_data.csv')
data = df['reading_time'].tolist()
mean = statistics.mean(data)
sd = statistics.stdev(data)
def randomsetofdata(counter):
    dataset = []
    for i in range(0,counter):
        index = random.randint(0,(len(data)-1))
        value = data[index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
meanlist = []
for i in range(0,1000):
    setofmeans = randomsetofdata(100)
    meanlist.append(setofmeans)
sdofmeanlist = statistics.stdev(meanlist)
sd1_start, sd1_end = mean-sdofmeanlist, mean+sdofmeanlist
sd2_start, sd2_end = mean-sdofmeanlist, mean+sdofmeanlist
sd3_start, sd3_end = mean-sdofmeanlist, mean+sdofmeanlist
print(sd1_start)
fig = ff.create_distplot([meanlist], ['Mean'], show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.17], mode='lines', name = 'Mean'))
fig.add_trace(go.Scatter(x=[sd1_start, sd1_start], y=[0,0.17], mode='lines', name = 'Sd1'))
fig.add_trace(go.Scatter(x=[sd1_end, sd1_end], y=[0,0.17], mode='lines', name = 'Sd1'))
fig.add_trace(go.Scatter(x=[sd2_start, sd2_start], y=[0,0.17], mode='lines', name = 'Sd2'))
fig.add_trace(go.Scatter(x=[sd2_end, sd2_end], y=[0,0.17], mode='lines', name = 'Sd2'))
fig.add_trace(go.Scatter(x=[sd3_start, sd3_start], y=[0,0.17], mode='lines', name = 'Sd3'))
fig.add_trace(go.Scatter(x=[sd3_end, sd3_end], y=[0,0.17], mode='lines', name = 'Sd3'))
fig.show()





df2 = pd.read_csv('data1.csv')
data = df2['Math_score'].tolist()
meanofsample1 = statistics.mean(data)
fig = ff.create_distplot([meanlist], ['Mean'], show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.17], mode='lines', name = 'Mean'))
fig.add_trace(go.Scatter(x=[meanofsample1, meanofsample1], y=[0,0.17], mode='lines', name = 'Mean'))
fig.add_trace(go.Scatter(x=[sd1_start, sd1_start], y=[0,0.17], mode='lines', name = 'Sd1'))
fig.add_trace(go.Scatter(x=[sd1_end, sd1_end], y=[0,0.17], mode='lines', name = 'Sd1'))
fig.add_trace(go.Scatter(x=[sd2_start, sd2_start], y=[0,0.17], mode='lines', name = 'Sd2'))
fig.add_trace(go.Scatter(x=[sd2_end, sd2_end], y=[0,0.17], mode='lines', name = 'Sd2'))
fig.add_trace(go.Scatter(x=[sd3_start, sd3_start], y=[0,0.17], mode='lines', name = 'Sd3'))
fig.add_trace(go.Scatter(x=[sd3_end, sd3_end], y=[0,0.17], mode='lines', name = 'Sd3'))
print(meanofsample1)
fig.show()



"""df = pd.read_csv('data2.csv')
data = df['Math_score'].tolist()
meanofsample2 = statistics.mean(data)
fig = ff.create_distplot([meanlist], ['Mean'], show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.17], mode='lines', name = 'Mean'))
fig.add_trace(go.Scatter(x=[meanofsample2, meanofsample2], y=[0,0.17], mode='lines', name = 'Mean'))
fig.add_trace(go.Scatter(x=[sd1_start, sd1_start], y=[0,0.17], mode='lines', name = 'Sd1'))
fig.add_trace(go.Scatter(x=[sd1_end, sd1_end], y=[0,0.17], mode='lines', name = 'Sd1'))
fig.add_trace(go.Scatter(x=[sd2_start, sd2_start], y=[0,0.17], mode='lines', name = 'Sd2'))
fig.add_trace(go.Scatter(x=[sd2_end, sd2_end], y=[0,0.17], mode='lines', name = 'Sd2'))
fig.add_trace(go.Scatter(x=[sd3_start, sd3_start], y=[0,0.17], mode='lines', name = 'Sd3'))
fig.add_trace(go.Scatter(x=[sd3_end, sd3_end], y=[0,0.17], mode='lines', name = 'Sd3'))
print(meanofsample2)
fig.show()



df = pd.read_csv('data3.csv')
data = df['Math_score'].tolist()
meanofsample3 = statistics.mean(data)
fig = ff.create_distplot([meanlist], ['Mean'], show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.17], mode='lines', name = 'Mean'))
fig.add_trace(go.Scatter(x=[meanofsample3,meanofsample3], y=[0,0.17], mode='lines', name = 'Mean'))
fig.add_trace(go.Scatter(x=[sd1_start, sd1_start], y=[0,0.17], mode='lines', name = 'Sd1'))
fig.add_trace(go.Scatter(x=[sd1_end, sd1_end], y=[0,0.17], mode='lines', name = 'Sd1'))
fig.add_trace(go.Scatter(x=[sd2_start, sd2_start], y=[0,0.17], mode='lines', name = 'Sd2'))
fig.add_trace(go.Scatter(x=[sd2_end, sd2_end], y=[0,0.17], mode='lines', name = 'Sd2'))
fig.add_trace(go.Scatter(x=[sd3_start, sd3_start], y=[0,0.17], mode='lines', name = 'Sd3'))
fig.add_trace(go.Scatter(x=[sd3_end, sd3_end], y=[0,0.17], mode='lines', name = 'Sd3'))
print(meanofsample3)
fig.show()"""


zscore = (meanofsample1-mean )/sdofmeanlist
print('Z-SCORE = ',zscore)