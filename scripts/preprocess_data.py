# scripts/preprocess_data.py
import numpy as np
import pandas as pd

def preprocess_data(input_data=None):
    if input_data is None:
        # Load CSV data for training
        raw_data = pd.read_csv('data/raw_data.csv')

        # Convert categorical variables to numeric values
        raw_data['device_type'] = raw_data['device_type'].map({'Laptop': 1, 'Smartphone': 0})
        raw_data['network_type'] = raw_data['network_type'].map({'5G': 1, 'WiFi': 0, '4G': 0})
        raw_data['time_of_day'] = raw_data['time_of_day'].map({'Morning': 0, 'Afternoon': 1, 'Evening': 2})
        raw_data['app_category'] = raw_data['app_category'].map({'Streaming': 0, 'Gaming': 1, 'Social Media': 2})

        processed_data = raw_data[['session_duration', 'data_usage', 'device_type', 'network_type', 'time_of_day', 'app_category']].values
        return processed_data

    elif isinstance(input_data, dict):
        # Process single sample input for prediction
        d = input_data.copy()
        d['device_type'] = 1 if d.get('device_type') == 'Laptop' else 0
        d['network_type'] = 1 if d.get('network_type') == '5G' else 0
        d['time_of_day'] = {'Morning': 0, 'Afternoon': 1, 'Evening': 2}.get(d.get('time_of_day'), -1)
        d['app_category'] = {'Streaming': 0, 'Gaming': 1, 'Social Media': 2}.get(d.get('app_category'), -1)

        return np.array([[d['session_duration'], d['data_usage'], d['device_type'], d['network_type'], d['time_of_day'], d['app_category']]])
    
    else:
        raise TypeError("Expected input_data to be None or a dictionary, got: " + str(type(input_data)))
