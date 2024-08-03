# CS 7650 - Spring 2020 #
## NL Project : Team 5 : Rohit Mujumdar, Sushmita Singh, Shalini Chaudhuri##

Information-seeking QA dialogue systems are an important application for natural language query systems[[1]], when users have limited or no access to an underlying corpus [[2]]. In such systems, there is a Questioning-agent (Q-bot) that has access to the corpus that contains relevant and important information, and an Answering-agent (A-bot) which seeks to know more about a particular topic or entity. Unlike regular QA systems, contextual dialogue QA pairs are often meaningful only within the context of the dialog with questions often being abstract, open-ended or unanswerable. In our project, we aim to build an A-bot capable of participating in a human-like, information-seeking conversation[[3]] about a particular subject. The goal of this project is to develop an A-bot that can provide answers and give information to an agent that has no prior knowledge of a subject.

### Models ###

We have implemented three different models for the task:

1. BiDAF enhanced with BERT embeddings
2. FlowQA enhanced with prediction of meta information about the question
3. FlowQA enhanced with attention

Instructions to run each model : Please refer to the READMEs inside each individual folder. 

### Project Video ### 


### References ###

1. C. Xiong, S. Merity, and R. Socher, “Dynamic mem-ory networks for visual and textual question answer-ing,”CoRR, vol. abs/1603.01417, 2016.
2. D.  Chen,  J.  Bolton,  and  C.  D.  Manning,  “A  thor-ough  examination  of  the  CNN/daily  mail  readingcomprehension task,” inProceedings of the 54th An-nual Meeting of the Association for ComputationalLinguistics (Volume 1:  Long Papers), (Berlin, Ger-many),  pp.  2358–2367,  Association  for  Computa-tional Linguistics, Aug. 2016.
3. M.  Stede  and  D.  Schlangen,  “Information-seekingchat: Dialogues driven by topic-structure,” 2004
