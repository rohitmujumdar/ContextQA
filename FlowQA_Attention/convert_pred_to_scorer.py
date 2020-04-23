import json


def read_json():
    c = {}
    val = {}
    with open('pred_out/pred1.json','r') as fp:
        c = json.load(fp) 
    with open('QuAC_data/dev.json','r') as fp:
        val = json.load(fp) 
    
    return c, val

def process_json():
    c, val = read_json()

    val_data = val['data']
    predictions = c['predictions']

    dict_answers = []

    with open('pred_out/pred_eval_out.json','w') as fp:
        for i,p in enumerate(predictions):
            corresponding_val_section = val_data[i]['paragraphs'][0]
            questions = corresponding_val_section['qas']
            
            qids = list(map(lambda q: q['id'], questions))
            yesno = list(map(lambda q: q['yesno'], questions))
            followup = list(map(lambda q: q['followup'], questions))

            obj = {}
            obj['best_span_str'] = p
            obj["qid"] = qids
            obj["yesno"] = yesno
            obj["followup"] = followup
            # dict_answers.append(obj)
            json.dump(obj, fp)
            fp.write("\n")

    



process_json()