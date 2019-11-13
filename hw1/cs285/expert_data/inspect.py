import os
import pickle


filename = "expert_data_Ant-v2.pkl"

with open(filename, 'rb') as f:
    data = pickle.loads(f.read())

print(data[0])
print(type(data))
print(type(data[0]))