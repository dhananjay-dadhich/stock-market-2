# -*- coding: utf-8 -*-
"""Stock_Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UWA8l-al09gt2y12HkILHbTfrx8Np9cK

<a href="https://colab.research.google.com/github/roshank1605A04/Stock-Market-Predictions/blob/master/Stock_Prediction.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

training_data = pd.read_csv('/content/MSFT - MSFT.csv')

training_data.shape
training_data.head()

training_data = training_data.iloc[:, 2:3]

training_data.shape
training_data.head()

# feature scaling

from sklearn.preprocessing import MinMaxScaler

mm = MinMaxScaler(feature_range = (0, 1))
training_data = mm.fit_transform(training_data)

# Getting the inputs and outputs

x_train = training_data[0:8856]
y_train = training_data[1:8857]

print(x_train.shape)
print(y_train.shape)

# reshaping

x_train = np.reshape(x_train, (8856, 1, 1))

print(x_train.shape)

# importing the keras libraries and packages

import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

# initializing the model
model = Sequential()

# adding the input layer and the LSTM layer
model.add(LSTM(units = 4, activation = 'sigmoid', input_shape = (None, 1)))

# adding the output layer
model.add(Dense(units = 1))

# compiling the model
model.compile(optimizer = 'adam', loss = 'mean_squared_error')

# fitting the RNN to the training data
model.fit(x_train, y_train, batch_size = 32, epochs = 200)

# getting the real stock of 2017 i.e., importing the test dataset

test_data = pd.read_csv('/content/DataFrame - DataFrame.csv')
real_stock_price = test_data.iloc[:,1:2]
real_stock_price.head()

# getting the predicted stock price of 2017

inputs = real_stock_price
inputs = mm.transform(inputs)
inputs = np.reshape(inputs, (22805, 1, 1))


predicted_stock_price = model.predict(inputs)
predicted_stock_price = mm.inverse_transform(predicted_stock_price)

predicted_stock_price

# visualizing the results

plt.plot(real_stock_price, color = 'red', label = 'Real Google Stock Price')
plt.plot(predicted_stock_price, color = 'blue', label = 'Predicted Google Stock Price')
plt.title('Stock Prediction')
plt.xlabel('Time')
plt.ylabel('Google Stock Price')
plt.legend()
plt.show()

# getting the real stock price of 2012 - 2016

training_data = pd.read_csv('/content/MSFT - MSFT.csv')

training_data.shape
training_data.head()

training_data = training_data.iloc[:, 1:3]

training_data.shape
training_data.head()

# getting the predicted stock price of 2012-2016

predicted_stock_price = model.predict(x_train)
predicted_stock_price = mm.inverse_transform(predicted_stock_price)

# visualizing the whole training data results

plt.plot(training_data, color = 'red', label = 'Real Google Stock Price')
plt.plot(predicted_stock_price, color = 'blue', label = 'Predicted Google Stock Price')
plt.title('Stock Prediction')
plt.xlabel('Time')
plt.ylabel('Google Stock Price')
plt.legend()
plt.show()