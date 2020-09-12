import sys
reqd_instance = int(sys.argv[1])

import json 
with open('QuAC_data\\dev.json') as f_in:
    r_list = json.load(f_in)['data']
    
import ast
fp = open('pred_eval_out.json')
for i, line in enumerate(fp):
    if i == reqd_instance:
        pred_data = ast.literal_eval(line)
        break
fp.close()

r_dict = r_list[reqd_instance]
title = r_dict['title']
context = r_dict['paragraphs'][0]['context']
print("CONTEXT : ",context)

qas = r_dict['paragraphs'][0]['qas']
print(len(qas))
for i in range(0,len(qas)):
    qa_pair_dict = qas[i]
    print("QUESTION : ",qa_pair_dict['question'])
    print("ORIGINAL ANSWER : ",qa_pair_dict['orig_answer']['text'])
    print("MODEL ANSWER : ",pred_data['best_span_str'][i])
    print("ORIGINAL FOLLOW UP : ",qa_pair_dict['followup'])
    print("MODEL FOLLOW UP : ",pred_data['followup'][i])
    print('ORIGINAL YES/NO : ',qa_pair_dict['yesno'])
    print("MODEL YES/NO : ",pred_data['yesno'][i])
    print("-------------------------------------------------\n")


'''
import ast
with open('C:\\Users\\rohit\\Documents\\GitHub\\ContextQA\\pred_outa\\pred_eval_out.json') as f_in:
    for line in f_in:
        pred_data = ast.literal_eval(line)
        break
for i in len(pred_data['best_span_str']):
    print("model answer : ",pred_data['best_span_str'][i])
    print("follow up : ",pred_data['followup'][i])
    print('yesno : ',pred_data['yesno'][i])'''
        