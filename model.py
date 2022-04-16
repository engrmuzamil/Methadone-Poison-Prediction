
import pandas as pd

import pickle
with open('model_pkl' , 'rb') as f:
    model = pickle.load(f)

def check_file(file):
    data = pd.read_csv(file)
    if data.shape != (1,144):
        return "Invalid File"
    result = model.predict(data)
    print(result[0])
    return result[0]
