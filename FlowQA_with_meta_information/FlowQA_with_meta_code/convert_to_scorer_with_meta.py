import json


def read_json():
    c = {}
    val = {}
    with open('pred_out/predictions.json','r') as fp:
        c = json.load(fp) 
    with open('../QuAC_data/dev.json','r') as fp:
        val = json.load(fp) 
    
    return c, val

def process_json():
    c, val = read_json()

    val_data = val['data']
    predictions = c['predictions']
    yesnos = c['yes_no_scores']
    followups = c['follow_up_scores']

    dict_answers = []

    with open('pred_out/pred_eval_out.json','w') as fp:
        for i,p in enumerate(predictions):
            corresponding_val_section = val_data[i]['paragraphs'][0]
            questions = corresponding_val_section['qas']
            
            qids = list(map(lambda q: q['id'], questions))

            followup = list(map(lambda q: 'n' if q == 0 else ('y' if q == 1  else 'm'), followups[i]))
            yesno = list(map(lambda q: 'y' if q == 1 else ('n' if q == 2  else 'x'), yesnos[i]))

            obj = {}
            obj['best_span_str'] = p
            obj["qid"] = qids
            obj["yesno"] = yesno
            obj["followup"] = followup
            # dict_answers.append(obj)
            json.dump(obj, fp)
            fp.write("\n")



process_json()


    

""""""



# =======================
# Overall F1: 61.0
# Yes/No Accuracy : 44.0
# Followup Accuracy : 22.7
# Unfiltered F1 (7354 questions): 59.4
# Accuracy On Unanswerable Questions: 33.0 %% (1486 questions)
# Human F1: 80.8
# Model F1 >= Human F1 (Questions): 3704 / 6573, 56.4%
# Model F1 >= Human F1 (Dialogs): 49 / 1000, 4.9%
# =======================


""""""