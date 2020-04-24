import sys

import json 
with open('QuAC_data\\dev.json') as f_in:
    r_list = json.load(f_in)['data']
    
import ast
fp = open('FlowQA_with_meta_code\\pred_out\\pred_eval_out.json')
wh_dict = {"who":0,"how":0,"what":0,"when":0,"why":0, "where":0}
wh_yn_dict_TP = {"who":0,"how":0,"what":0,"when":0,"why":0, "where":0}
wh_yn_dict_TN = {"who":0,"how":0,"what":0,"when":0,"why":0, "where":0}
wh_yn_dict_FP = {"who":0,"how":0,"what":0,"when":0,"why":0, "where":0}
wh_yn_dict_FN = {"who":0,"how":0,"what":0,"when":0,"why":0, "where":0}
yn_TP,yn_TN,yn_FP,yn_FN = 0,0,0,0

total_qas,total_yn_qas = 0,0
for reqd_instance, line in enumerate(fp):
    pred_data = ast.literal_eval(line)
    r_dict = r_list[reqd_instance]
    title = r_dict['title']
    context = r_dict['paragraphs'][0]['context']
    #print("CONTEXT : ",context)
    
    qas = r_dict['paragraphs'][0]['qas']
    total_qas = total_qas + len(qas)
    for i in range(0,len(qas)):
        qa_pair_dict = qas[i]
        
        first_questions_token = qa_pair_dict['question'].lower().split()[0]
        #POSITIVE
        if qa_pair_dict['yesno'] == 'y':
            #TRUE POSITVE
            if qa_pair_dict['yesno'] == pred_data['yesno'][i]:
                yn_TP = yn_TP + 1
                if "how" == first_questions_token:
                    wh_yn_dict_TP["how"] = wh_yn_dict_TP["how"] + 1
                elif "what" == first_questions_token:
                    wh_yn_dict_TP["what"] = wh_yn_dict_TP["what"] + 1
                elif "when" == first_questions_token:
                    wh_yn_dict_TP["when"] = wh_yn_dict_TP["when"] + 1
                if "why" == first_questions_token:
                    wh_yn_dict_TP["why"] = wh_yn_dict_TP["why"] + 1
                if "where" == first_questions_token:
                    wh_yn_dict_TP["where"] = wh_yn_dict_TP["where"] + 1
                if "who" == first_questions_token:
                    wh_yn_dict_TP["who"] = wh_yn_dict_TP["who"] + 1
            #FALSE NEGATIVE
            else:
                yn_FN = yn_FN + 1
                if "how" == first_questions_token:
                    wh_yn_dict_FN["how"] = wh_yn_dict_FN["how"] + 1
                elif "what" == first_questions_token:
                    wh_yn_dict_FN["what"] = wh_yn_dict_FN["what"] + 1
                elif "when" == first_questions_token:
                    wh_yn_dict_FN["when"] = wh_yn_dict_FN["when"] + 1
                if "why" == first_questions_token:
                    wh_yn_dict_FN["why"] = wh_yn_dict_FN["why"] + 1
                if "where" == first_questions_token:
                    wh_yn_dict_FN["where"] = wh_yn_dict_FN["where"] + 1
                if "who" == first_questions_token:
                    wh_yn_dict_FN["who"] = wh_yn_dict_FN["who"] + 1
                    
                
        #NEGATIVE
        if qa_pair_dict['yesno'] != 'y':
            #TRUE NEGATIVE
            if 'y' != pred_data['yesno'][i]:
                yn_TN = yn_TN + 1
                if "how" == first_questions_token:
                    wh_yn_dict_TN["how"] = wh_yn_dict_TN["how"] + 1
                elif "what" == first_questions_token:
                    wh_yn_dict_TN["what"] = wh_yn_dict_TN["what"] + 1
                elif "when" == first_questions_token:
                    wh_yn_dict_TN["when"] = wh_yn_dict_TN["when"] + 1
                if "why" == first_questions_token:
                    wh_yn_dict_TN["why"] = wh_yn_dict_TN["why"] + 1
                if "where" == first_questions_token:
                    wh_yn_dict_TN["where"] = wh_yn_dict_TN["where"] + 1
                if "who" == first_questions_token:
                    wh_yn_dict_TN["who"] = wh_yn_dict_TN["who"] + 1
            else:
                #FALSE POSITIVE
                yn_FP = yn_FP + 1
                if "how" == first_questions_token:
                    wh_yn_dict_FP["how"] = wh_yn_dict_FP["how"] + 1
                elif "what" == first_questions_token:
                    wh_yn_dict_FP["what"] = wh_yn_dict_FP["what"] + 1
                elif "when" == first_questions_token:
                    wh_yn_dict_FP["when"] = wh_yn_dict_FP["when"] + 1
                if "why" == first_questions_token:
                    wh_yn_dict_FP["why"] = wh_yn_dict_FP["why"] + 1
                if "where" == first_questions_token:
                    wh_yn_dict_FP["where"] = wh_yn_dict_FP["where"] + 1
                if "who" == first_questions_token:
                    wh_yn_dict_FP["who"] = wh_yn_dict_FP["who"] + 1
                     
        

fp.close()
print("TRUE POSITIVE : ",wh_yn_dict_TP)
print("FALSE POSITIVE : ",wh_yn_dict_FP)
print("TRUE NEGATIVE : ",wh_yn_dict_TN)
print("FALSE NEGATIVE : ",wh_yn_dict_FN)
print(total_qas)
print(yn_TN+yn_FN+yn_FP+yn_TP)
