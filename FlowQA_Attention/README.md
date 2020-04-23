# FlowQA_Attention 

Here we try to add the concept of attention to the historical flow of the conversation so far. The intuiton behind this is that only some of thr previous question are contextually important when a new question has to be answered. 

**Experimental Setup**

1. The model was trained on Google Cloud. The computing engine had the following configurations tuned \\
   (a) Machine type : n1-highmem-8 (8 vCPUs, 52 GB memory) \\
   (b) GPUs : 1 x NVIDIA Tesla V100 \\
   (c) Zone : us-west1-a \\
   (d) Boot Disk : ubuntu-1604-xenial-v20200407,SSD persistent disk, Google managed, Boot, read/write\\
	
 2. Requirements : While the pip freeze of the requirements can be found in the requirments.txt, the following were the basic essential requirements. \\
    a) allennlp==0.9.0 \\
    b) torch==1.4.0 \\
    c) Python 3.5.1 |Anaconda 4.0.0 (64-bit)| \\

How to run the code is the same as FlowQA. However, using "attention over flow" is set to be default.

From https://github.com/momohuang/FlowQA we borrow their instructions as follows

**Steps to be performed**

1) To install requirements 
 > pip install -r requirements.txt


> ./download.sh

Step 3:
preprocess the data files using:

> python preprocess_QuAC.py

Step 4:
run the training code using:

> python train_QuAC.py

To specify not using "attention over flow", run:

> python train_QuAC.py --flow_attention=0


## Results

The result shows that our attempt slightly improves FlowQA by 0.1 of F-1 value on dev set. We would like to mention that the model converges much faster, as only 10 epochs is used instead of 20.

![image](https://github.com/deepnlp-cs599-usc/quac/blob/master/FlowQA_Attention/figure/result.png)


## References

[Flowqa: Grasping flow in history for conversational machine comprehensionn.](https://arxiv.org/abs/1810.06683) By Huang H Y, Choi E, Yih W.

[Quac: Question answering in context.](https://arxiv.org/abs/1808.07036) By Choi E, He H, Iyyer M, et al. 








