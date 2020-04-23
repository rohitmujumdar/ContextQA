import pickle
pred_1 = pickle.load(open('pred_out/pred1.pckl', 'rb'))

import json
with open('pred_out/pred1.json', 'w') as fp:
    json.dump(pred_1, fp)