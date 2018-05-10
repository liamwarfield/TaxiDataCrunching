import pandas as pd
import numpy as np
#import matplotlib.pyplot as #plt
import sklearn as sk
from sklearn.linear_model import LinearRegression
from sklearn.metrics import classification_report
#plt.style.use('ggplot')

#%matplotlib inline
#%config InlineBackend.figure_format = 'retin


jan = pd.read_csv('yellow_tripdata_2017-01.csv', infer_datetime_format= True)
print(1)
feb = pd.read_csv('yellow_tripdata_2017-02.csv', infer_datetime_format= True)
print(2)
mar = pd.read_csv('yellow_tripdata_2017-03.csv', infer_datetime_format= True)
print(3)
apr = pd.read_csv('yellow_tripdata_2017-04.csv', infer_datetime_format= True)
print(4)
may = pd.read_csv('yellow_tripdata_2017-05.csv', infer_datetime_format= True)
print(5)
jun = pd.read_csv('yellow_tripdata_2017-06.csv', infer_datetime_format= True)
print(6)
jul = pd.read_csv('yellow_tripdata_2017-07.csv', infer_datetime_format= True)
print(7)
aug = pd.read_csv('yellow_tripdata_2017-08.csv', infer_datetime_format= True)
print(8)
sep = pd.read_csv('yellow_tripdata_2017-09.csv', infer_datetime_format= True)
print(9)
october = pd.read_csv('yellow_tripdata_2017-10.csv', infer_datetime_format= True)
print(10)
nov = pd.read_csv('yellow_tripdata_2017-11.csv', infer_datetime_format= True)
print(11)
dec = pd.read_csv('yellow_tripdata_2017-12.csv', infer_datetime_format= True)
print(12)

rawData = pd.concat([jan, feb, mar, apr, may, jun, jul, aug, sep, october, nov, dec], 
                    keys =['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])

print("Plotting (world domination)")
#rawData = rawData.drop(0)
rawData['tip_frac'] = rawData['tip_amount']/rawData['fare_amount']
print("Plotting (world domination)")
rawData = rawData[rawData['tip_frac'] <= 50.0]
rawData = rawData[np.isfinite(rawData['tip_amount'])]
print("Plotting (world domination)")
rawData = rawData[rawData['tip_amount'] > 0.01]
print("doing regression")
model = LinearRegression(n_jobs = 10)

from sklearn.model_selection import cross_val_score
model.fit(rawData[['trip_distance','fare_amount','passenger_count']], rawData['tip_frac'])
scores = cross_val_score(model, rawData[['trip_distance','fare_amount','passenger_count']], rawData['tip_frac'], n_jobs = 10)
MSE = ((rawData['tip_frac'] - model.predict(rawData[['trip_distance','fare_amount','passenger_count']])) ** 2).mean()
RMSE = np.sqrt(MSE)
print("MSE: ", MSE)
print("RMSE:", RMSE)
print(scores)
print(np.sqrt(scores))
 
# scores = cross_val_score(model, rawData[['trip_distance','fare_amount','passenger_count']], rawData['tip_frac'])
# plt.plot(rawData["tip_amount"], rawData["fare_amount"], 'r.')
# plt.title("tip amount vs Fair")
# plt.ylabel("Fair cost")
# plt.xlabel("tip")
# plt.savefig('tip_amount_vs_Fair.png')
 
# plt.plot(rawData["tip_frac"], rawData["fare_amount"], 'b.')
# plt.title("Resonable_tip_percent_vs_Fair.png")
# plt.ylabel("Fair cost")
# plt.xlabel("Tip Fration")
# plt.xlim(0,.5)
# plt.ylim(ymin=0)
# plt.savefig('Resonable_tip_percent_vs_Fair.png')
 
# plt.plot(rawData["tip_frac"], rawData["fare_amount"], 'b.')
# plt.title("tip perccent vs Fair")
# plt.ylabel("Fair cost")
# plt.xlabel("Tip Fration")
# plt.xlim(0,2.5)
# plt.ylim(ymin=0)
# plt.savefig('tip_perccent_vs_Fair')
 
# plt.plot(rawData["tip_frac"], rawData["fare_amount"], 'b.')
# plt.title("tip perccent vs Fair outliars")
# plt.ylabel("Fair cost")
# plt.xlabel("Tip Fraction")
# plt.xlim(0,12)
# plt.ylim(ymin=0)
# plt.savefig('tip_perccent_vs_Fair_outliars.png')
 
# plt.plot(rawData["tip_frac"], rawData["fare_amount"], 'b.')
# plt.title("tip perccent vs Fair Outragios outliars")
# plt.ylabel("Fair cost")
# plt.xlabel("Tip Fraction")
# plt.xlim(0,100)
# plt.ylim(ymin=0)
# plt.savefig('tip_perccent_vs_Fair_Outragios_outliars.png')
 
# print(rawData.memory_usage(index=True, deep = True).sum())