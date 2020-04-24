import pickle
import json
import torch

data = pickle.load(open('pred_out/pred1.pckl', 'rb'))
data_json = {}

for k in data.keys():
    data_json[k] = []

    for i in data[k]:
        arr = []
        for j in i:
            if isinstance(j, torch.Tensor):
                j = j.tolist()
            
            arr.append(j)
        data_json[k].append(arr.copy())

# print(data_json)

with open('pred_out/predictions.json', 'w') as fp:
    json.dump(data_json, fp)