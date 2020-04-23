import json

def convert_json():
	#val =  read_val()
	with open('pred_eval_out.json','w') as outfp:
		for i in range(1,1000):
			infile = 'out/pred_'+str(i)+'.json'
			c = {}
			with open(infile, 'r')  as fp:
				c = json.load(fp)
				obj = {}
				obj['best_span_str'] = c['best_span_str']
				obj["qid"] = c['qid']
				obj["yesno"] = c['yesno']
				obj["followup"] = c['followup']

				json.dump(obj, outfp)
				outfp.write("\n")

convert_json()



