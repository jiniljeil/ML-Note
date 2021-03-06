from keras.models import Sequential
from keras.layers import Dense
from tensorflow.keras.optimizers import SGD
import numpy as np

x_data = np.array([[1, 2],
          [2, 3],
          [3, 1],
          [4, 3],
          [5, 3],
          [6, 2]]) 
y_data = np.array([[0],
          [0],
          [0],
          [1],
          [1],
          [1]])

model = Sequential() 
model.add(Dense(1, input_dim=2, activation='sigmoid')) 

sgd = SGD(lr=0.1) 
model.compile(optimizer=sgd, loss='binary_crossentropy', metrics=['accuracy'], loss_weights=None,
              sample_weight_mode=None, weighted_metrics=None)

model.summary() 
model.fit(x_data, y_data, epochs=2000) 

print("2,1", model.predict(np.array([[2, 1]])))
print("6,5", model.predict(np.array([[6, 5]])))
