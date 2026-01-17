# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

loaded_model = pickle.load(open('C:/Users/Priya Kumari/Desktop/Machine Learning/trained_model.sav','rb'))

input_data = (58,1,0,114,318,0,2,140,0,4.4,0,3,1)

#changing the input_data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

#reshape the np array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction) #prediction is a form of list

if(prediction[0]== 1): print("The person has defective heart")
else : print("The person is healthy")