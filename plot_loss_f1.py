import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def read_files():
    meta =  pd.read_csv('./FlowQA_with_meta_information/FlowQA_with_meta_code/flow_f1_loss_values.csv')
    attn =  pd.read_csv('./FlowQA_Attention/code/attention_f1_loss_values.csv')
    bidaf =  pd.read_csv('./BiDAF/log/bidaf_los_f1_values.csv')

    return meta, attn, bidaf


def plot_loss_values(meta, attn, bidaf):
    df = pd.DataFrame({
        'Flow_with_meta': meta['Loss'],
        'Flow_with_attention': attn['Loss'],
        'BiDAF': bidaf['Loss']
    }, index = bidaf['Epoch'])

    ax = df.plot.line()
    ax.set_ylabel('Loss per epoch')
    ax.set_xlabel('Epoch')
    ax.set_title("Loss vs Epochs for all models")
    ax.set_xticks(bidaf['Epoch'])
    ax.grid(True)

    fig = ax.get_figure()
    fig.savefig('Loss_Plot.png')

def plot_f1_values(meta, attn, bidaf):
    df = pd.DataFrame({
        'Flow_with_meta': meta['F1'],
        'Flow_with_attention': attn['F1'],
        'BiDAF': bidaf['F1']
    }, index = bidaf['Epoch'])

    ax = df.plot.line()
    ax.set_ylabel('F1 on validation set per epoch')
    ax.set_xlabel('Epoch')
    ax.set_title("F1 vs Epochs for all models")
    ax.set_xticks(bidaf['Epoch'])
    ax.grid(True)

    fig = ax.get_figure()

    fig.savefig('F1_Plot.png')



meta, attn, bidaf = read_files()
plot_loss_values(meta, attn, bidaf)
plot_f1_values(meta, attn, bidaf)