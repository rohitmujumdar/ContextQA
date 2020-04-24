# FlowQA_Attention 

Here we try to add the concept of attention to the historical flow of the conversation so far. The intuiton behind this is that only some of the previous question are contextually important when a new question has to be answered. 

**Experimental Setup**

1. The model was trained on Google Cloud. The computing engine had the following configurations tuned\
   (a) Machine type : n1-highmem-8 (8 vCPUs, 52 GB memory)\
   (b) GPUs : 1 x NVIDIA Tesla V100\
   (c) Zone : us-west1-a\
   (d) Boot Disk : ubuntu-1604-xenial-v20200407,SSD persistent disk, Google managed, Boot, read/write\
	
 2. Requirements : While the pip freeze of the requirements can be found in the requirments.txt, the following were the basic essential requirements.\
    a) allennlp==0.9.0\
    b) torch==1.4.0 \
    c) Python 3.5.1 |Anaconda 4.0.0 (64-bit)|
    d) msgpack-python==0.5.6


**Steps to be performed**

1) Make sure you are in the correct directory
	> cd FlowQA_Attention
	
2) To install requirements
	> pip install -r requirements.txt \
	>./download.sh 
	
3) Preprocess data. This 
	> python preprocess_QuAC.py

4) Train the model. This will save the best model in the *models* folder
	> python FlowQA_Attention/code/train_QuAC.py
    
5) Predict using this trained model. This will store the trained predictions file *pred_1.pckl* in *pred_out* folder. 
	> python predict_QuAC_with_meta.py -m models/best_model.pt

6) Unpickle this file and convert JSON file using the following. This will create file *pred_1.json* in *pred_out* folder.
	> python read_pred_pickle.py
	
7) The QUAC scorer can be downloaded from the QUAC website. It requires the predictions JSON to be in a certain format. The following script will take care of that and create *pred_eval_out.json* in *pred_out*
	> python convert_pred_to_scorer.py
	
8) Run the scorer to obtain results. "*model_output*" is the predictions output we had in the previous step. "*val_file*" is the dev dataset in *Quac_data* folder.  
	> python scorer.py --val_file code/QuAC_data/dev.json --model_output pred_out/pred_eval_out.json --o eval.json
	
9) To analyse any particular instance of the results run the following. 
	> python examine_prediction_instance instance_number
	

**Results**

| Metric                         | FlowQA with attention |
|--------------------------------|-----------------------|
| Overall F1                     | 59.1                  |
| Unfiltered F1                  | 57.9                  |
| Yes/No Accuracy                | -                     |
| Followup Accuracy              | -                     |
| Accuracy On "Cannot   answer"  | 20.7                  |
| Human F1                       | 80.8                  |
| HEQ-Q                          | 54.4                  |
| HEQ-D                          | 3.8                   |
