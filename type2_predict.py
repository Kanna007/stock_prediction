import quandl
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import datetime
import random


style.use('ggplot')
df = quandl.get('NSE/RCOM', start_date="2006-06-30", end_date="2014-01-01",api_key='-pQJsBYvTAsU-cSopBvA')
df = df[['Close']]
forecaste_col='Close'
df.fillna(-99999,inplace=True)
df.dropna(inplace=True)
forecast_out= int (math.ceil(0.01*len(df)))
df['Forecast']=df[forecaste_col].shift(-forecast_out)
# Prepare variables for loop
last_close = df['Close'][-1]
print(last_close)
last_date = df.iloc[-1].name.timestamp()
print(last_date)
df['Forecast'] = np.nan
print(df)
for i in range(1000):
    # Create np.Array of current predictions to serve as input for future predictions
    modifier = random.randint(-100, 105) / 10000 + 1
    last_close *= modifier
    next_date = datetime.datetime.fromtimestamp(last_date)
    last_date += 86400

    # Outputs data into DataFrame to enable plotting
    df.loc[next_date] = [np.nan, last_close]
df['Close'].plot()
df['Forecast'].plot()
plt.legend(loc=10)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()