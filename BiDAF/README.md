# Enhancing BiDAF++

## Descriptions
An original BiDAF++ model uses Char-CNN for character embedding and GLoVe for word embedding. It is also equipped with contextualized embeddings and self attention. In this model, marker embeddings corresponding to previous answer words are used, while question turn numbers are encoded into question embeddings.

We've used [AllenNLP](https://github.com/allenai/allennlp) library to modify the BiDAF++ and used enhanced models to train on [QuAC](https://quac.ai/) dataset. 

## Platform and tools
### Launching a Deep Learning VM on GCP
- 2 vCPUs with 13GB memory
- 1 NVIDIA Tesla V100 GPU
- PyTorch 1.0 + fast.ai 1.0(CUDA 10.0)
- Install NVIDIA GPU driver automatically on first startup 

### Setting up an AllenNLP virtual environment

1.  Create a Conda environment with Python 3.6

    ```bash
    conda create -n allennlp python=3.6
    ```

2.  Activate the Conda environment. You will need to activate the Conda environment in each terminal in which you want to use AllenNLP.

    ```bash
    source activate allennlp
    ```
## Usage

### Dataset
[Train data](https://s3.amazonaws.com/my89public/quac/train_5000.json)  
[Validation data](https://s3.amazonaws.com/my89public/quac/val.json)

### Training
Train a enhanced model with QuAC dataset which includes training and validation dataset
```
nohup allennlp train <your_path_to_jsonnet_file>  --serialization-dir <your_path_to_log_file> > output.log &
```
As [QuAC](https://arxiv.org/pdf/1808.07036.pdf) mentioned，Questions in the training set have one reference answer, while validation and test questions have five references each, which makes the F1 score on validation dataset has a higher score then that on training set.

Best model's configuration is [here](https://github.com/deepnlp-cs599-usc/quac/blob/master/BiDAF/BiDAFF%2B%2B_with_glove%2Bbert.jsonnet).
## Results
### F1 score
Enhanced model by BERT
<p align="center">
    <img src="Figures/enhenced.png" width="200%"/>
</p>
Enhanced model by ELMo 
<p align="center">
    <img src="Figures/enhenced_elmo.png" width="200%"/>
</p>
Baseline model
<p align="center">
    <img src="Figures/baseline.png" width="200%"/>
</p>

### Performance on baseline and enhanced models

| | F1 score on training set | F1 score on validation set|
| --- | --- | --- |
| Baseline model | 49.40 | 55.59 |
| Enhanced by BERT | **53.05** | **63.85**|

## Related works

* [Bidirectional attention ﬂow for machine comprehension](https://arxiv.org/abs/1611.01603) by Minjoon Seo et. al.
* [Simple and effective multi-paragraph reading comprehension](https://arxiv.org/abs/1710.10723) by Christopher Clark et. al.
* [Deep contextualized word representations](https://arxiv.org/abs/1802.05365) by Matthew E. Peters et. al.
* [Bert: Pre-training of deep bidirectional transformers for language understanding](https://arxiv.org/abs/1810.04805) by  Jacob Devlin et. al.
