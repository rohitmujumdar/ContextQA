# FlowQA enhanced to predict meta information about questions #

A good answering agent must be able to understand not only the question but the scope of the question too. That was the intuition behind enhancing FlowQA to also predict metainformation such as whether the question is a yes/no question and whether there is scope to follow up and learn more about the subject.

We have modified the implementation of FlowQA provided by [here](https://github.com/momohuang/FlowQA) to add units that predict the meta information. We have also incorportated that into our loss and training optimizations.
The meta information that the network now predicts is based on the QuAC dataset and comprises:
1. Is the question a yes/no question? Possible answers: y/n/x
2. Should a follow-up question be asked? Possible answers: y/n/m
3. Can this question be answered in this scope? Possible answer: a probability score of "CannotAnswer", which is False if lesser than the threshold.


**Experimental Setup**

1. The model was trained on Google Cloud. The computing engine had the following configurations tuned\
   (a) Machine type : n1-highmem-8 (8 vCPUs, 52 GB memory)\
   (b) GPUs : 1 x NVIDIA Tesla V100\
   (c) Zone : us-west1-a\
   (d) Boot Disk : ubuntu-1604-xenial-v20200407,SSD persistent disk
	
 2. Requirements : While the pip freeze of the requirements can be found in the requirments.txt, the following were the basic essential requirements.\
    a) allennlp\
    b) torch\
    c) pandas\
    d) msgpack\
    
 

**Initial Set-up**

1. Set up initial requirements:

cd FlowQA_with_meta_code\
pip install -r requirements.txt\
./download.sh\

2. Preprocess the data (The preprocessing differs as we now need to store and convert the meta information about the QA pair)

python preprocess_QuAC_with_meta.py\

3. Train the model

python train_QuAC_with_meta.py --name baseline_flow --epochs 20\

4. Predict using the trained model

python predict_QuAC_with_meta.py -m ./models_baseline_flow/best_model.pt \

5. Convert the pckl file to json

6. Use json to run the scorer

python convert_to_scorer_with_meta.py\
scorer.py --val_file ../QuAC_data/dev.json --model_output pred_out/pred_eval_out.json --o eval.json


