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

Best model's configuration is [here](https://github.gatech.edu/schaudhuri34/ContextQA/blob/master/BiDAF/config.jsonnet).

### Testing
To run prediction, firstly, you will need the model and test data. Our pre-trained model can be downloaded from here -  https://drive.google.com/file/d/1OBcop4LdjXkuE6pmoXht5a49EBm5FFZE/view?usp=sharing 
```bash
allennlp predict model.tar.gz <your_input_file> --output-file <your_output_file>
```

To evaluate the model on your test predictions, run the following command. The scorer script can be downloaded from here - https://s3.amazonaws.com/my89public/quac/scorer.py

```bash
python scorer.py --val_file <path_to_val> --model_output <path_to_predictions> --o eval.json
```
## Related works

* [Bidirectional attention ﬂow for machine comprehension](https://arxiv.org/abs/1611.01603) by Minjoon Seo et. al.
* [Simple and effective multi-paragraph reading comprehension](https://arxiv.org/abs/1710.10723) by Christopher Clark et. al.
* [Deep contextualized word representations](https://arxiv.org/abs/1802.05365) by Matthew E. Peters et. al.
* [Bert: Pre-training of deep bidirectional transformers for language understanding](https://arxiv.org/abs/1810.04805) by  Jacob Devlin et. al.
