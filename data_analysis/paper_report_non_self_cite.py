import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from icecream import ic
import pickle


save_png_idx = 0
conf_key = {'CHI':1163450153, 'CSCW':1195049314, 'UBI':1171345118, 'UIST':1166315290}

with open('paperyear_map_conf.pickle', 'rb') as handle:
    paperyear_map_conf = pickle.load(handle)

with open('inv_paperyear_map_conf.pickle', 'rb') as handle:
    inv_paperyear_map_conf = pickle.load(handle)
    
with open('citingpatent_map_conf.pickle', 'rb') as handle:
    citingpatent_map_conf = pickle.load(handle)
    
with open('citedpaper_map_conf.pickle', 'rb') as handle:
    citedpaper_map_conf = pickle.load(handle)

ic()
ori_paperyear_conf = {}
ori_citingpatent_conf = {}

non_self_cite_patent_mag = pd.read_csv("non_self_cite_patent_mag.tsv")
df_paper_year = pd.read_csv("df_paper_year.tsv")
df_paper_pc2s_year = pd.read_csv("df_paper_pc2s_year.tsv")
ic(len(non_self_cite_patent_mag))
ic(len(df_paper_pc2s_year))
df_paper_pc2s_year = df_paper_pc2s_year.merge(non_self_cite_patent_mag, left_on=['magid', 'patent'], right_on=['magid', 'patent'])
df_paper_pc2s_year = df_paper_pc2s_year.groupby(['magid', 'patent']).first().reset_index()
ic(len(df_paper_pc2s_year))
df_paper_pc2s_year = df_paper_pc2s_year.drop_duplicates()

for conf_name,conf_id in conf_key.items():
    ori_paperyear_conf[conf_name] = df_paper_year.loc[df_paper_year['conf_id']==conf_id]
    ori_citingpatent_conf[conf_name] = df_paper_pc2s_year.loc[df_paper_pc2s_year['conf_id']==conf_id]

df_paperid = pd.read_csv('../dataAug10/mergeversiondata/HCI_paperids.tsv', sep='\t')
df_paperid = df_paperid.drop_duplicates()
# %%
# Visualization
start = 1980
end = 2019
span = end - start
fig = plt.figure(figsize=(100,100))
axes = fig.subplots(nrows=4, ncols=2)
for ax in axes:
    ax[0].set_ylabel("number", fontsize=70)
    ax[1].set_ylabel("ratio", fontsize=70)
    for ax_c in ax:
        ax_c.set_xlabel("paper_year", fontsize=70)
        ax_c.tick_params(labelsize=70)

plot_idx = 0

X_year = [i for i in range (start, end)]

for conf, paperyear_map in paperyear_map_conf.items():
    Y_papercnt = [0] * span
    Y_citingpatentcnt = [0] * span
    Y_citedportion = [0.0] * span

    citingpatent_map = citingpatent_map_conf[conf]
    citedpaper_map = citedpaper_map_conf[conf]
    for i in range (start, end):
        if str(i) in paperyear_map.keys():
            Y_papercnt[i-start] = len(paperyear_map[str(i)])
        if str(i) in citingpatent_map.keys():
            Y_citingpatentcnt[i-start] = len(citingpatent_map[str(i)])    
        if str(i) in citedpaper_map.keys():
            Y_citedportion[i-start] = len(citedpaper_map[str(i)]) / Y_papercnt[i-start]
    axes[plot_idx, 0].plot(X_year,Y_papercnt, 'o-', label='paper_number', color='r', linewidth = 10, markersize=20)
    axes[plot_idx, 0].plot(X_year,Y_citingpatentcnt, 'o-', label='patent_citation', color='g', linewidth = 10, markersize=20)
    axes[plot_idx, 0].set_title('conference_{}'.format(conf), fontsize=90)
    axes[plot_idx, 0].legend(loc = 'upper left', prop={'size': 100})
    axes[plot_idx, 1].plot(X_year,Y_citedportion, 'o-', label='cited_ratio', color='b', linewidth = 10, markersize=20)
    axes[plot_idx, 1].set_title('conference_{}'.format(conf), fontsize=90)
    axes[plot_idx, 1].legend(loc = 'upper left', prop={'size': 100})
    plot_idx += 1
save_png_idx += 1
plt.savefig('non_self_cite_fig_{}.png'.format(save_png_idx))
fig = plt.figure()
