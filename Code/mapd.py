import os
import glob
import pandas as pd
import numpy as np
import sklearn as sk
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.svm import SVC

plt.style.use('ggplot')








path = "/u/au/sa/liamwarfield/Desktop/Programs/Python/heatmap"
allFiles = glob.glob(path + "/y*.csv")
frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    print(file_)
    df = pd.read_csv(file_)
    list_.append(df)
frame = pd.concat(list_)
print(frame)
frame = frame.drop(0)
frame = frame[frame[' total_amount'] >= 0]
frame = frame[frame[' tip_amount'] >= 0]
#frame[' tip_frac'] = frame[' tip_amount']/frame[' fare_amount']
#frame = frame[frame[' tip_frac'] <= 50.0]

path = "/u/au/sa/liamwarfield/Desktop/Programs/Python/heatmap"
allFiles = glob.glob(path + "/g*.csv")
frame2 = pd.DataFrame()
list_ = []
for file_ in allFiles:
    print(file_)
    df = pd.read_csv(file_)
    list_.append(df)
frame2 = pd.concat(list_)
print(frame2)
#frame2 = frame2.drop(0)
#frame2 = frame2[frame2['Total_amount'] >= 0]
#frame2 = frame2[frame2['Tip_amount'] >= 0]
#frame2[' tip_frac'] = frame2['Tip_amount']/frame2['Fare_amount']
#frame2 = frame2[frame2[' tip_frac'] <= 50.0]


frame = frame.rename(index=str, columns={" dropoff_longitude": "Dropoff_longitude", " dropoff_latitude": "Dropoff_latitude"})
print(frame)

frame2 = frame2[frame2['Dropoff_longitude'] != 0]
frame2 = frame2[frame2['Dropoff_latitude'] != 0]
frame2 = frame2[frame2['Dropoff_longitude'] <= -73.5]
frame2 = frame2[frame2['Dropoff_longitude'] >= -74.2]
frame2 = frame2[frame2['Dropoff_latitude'] <= 41.2]
frame2 = frame2[frame2['Dropoff_latitude'] >= 40.5]


frame = frame[frame['Dropoff_longitude'] != 0]
frame = frame[frame['Dropoff_latitude'] != 0]
frame = frame[frame['Dropoff_longitude'] <= -73.5]
frame = frame[frame['Dropoff_longitude'] >= -74.2]
frame = frame[frame['Dropoff_latitude'] <= 41.2]
frame = frame[frame['Dropoff_latitude'] >= 40.5]

result = pd.concat([frame2[["Dropoff_longitude", "Dropoff_latitude"]],frame[["Dropoff_longitude", "Dropoff_latitude"]]]) 
print(result)


plt.rcParams["figure.figsize"] = (20,20)
heatmap, xedges, yedges = np.histogram2d(result["Dropoff_longitude"], result["Dropoff_latitude"], bins=200)
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
heatmap = heatmap + 1
heatmap = np.log(heatmap)
plt.clf()
plt.xlim(-74.2,-73.5)
plt.ylim(40.5,41.2)
plt.title("Latitude vs Longitude")
plt.ylabel("Lat")
plt.xlabel("Long")
plt.imshow(heatmap.T, extent=extent, origin='lower')
plt.savefig('MAP!!d',dpi=300)
print("hi")

heatmap, xedges, yedges = np.histogram2d(result["Dropoff_longitude"], result["Dropoff_latitude"], bins=500)
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
heatmap = heatmap + 1
heatmap = np.log(heatmap)
plt.clf()
plt.xlim(-74.2,-73.5)
plt.ylim(40.5,41.2)
plt.title("Latitude vs Longitude")
plt.ylabel("Lat")
plt.xlabel("Long")
plt.imshow(heatmap.T, extent=extent, origin='lower')
plt.savefig('MAP!!!!d',dpi=300)
print("hi")

heatmap, xedges, yedges = np.histogram2d(result["Dropoff_longitude"], result["Dropoff_latitude"], bins=2000)
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
heatmap = heatmap + 1
heatmap = np.log(heatmap)
plt.clf()
plt.xlim(-74.2,-73.5)
plt.ylim(40.5,41.2)
plt.title("Latitude vs Longitude")
plt.ylabel("Lat")
plt.xlabel("Long")
plt.imshow(heatmap.T, extent=extent, origin='lower')
plt.savefig('MAP!!!!!d',dpi=300)
print("hi")