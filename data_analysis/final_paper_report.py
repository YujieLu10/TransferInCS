import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from icecream import ic
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

save_png_idx = 0
conf_key = {'CHI':1163450153, 'CSCW':1195049314, 'UbiComp':1171345118, 'UIST':1166315290}

with open('paperyear_map_conf.pickle', 'rb') as handle:
    paperyear_map_conf = pickle.load(handle)

with open('inv_paperyear_map_conf.pickle', 'rb') as handle:
    inv_paperyear_map_conf = pickle.load(handle)
    
with open('citingpatent_map_conf.pickle', 'rb') as handle:
    citingpatent_map_conf = pickle.load(handle)
    
with open('citedpaper_map_conf.pickle', 'rb') as handle:
    citedpaper_map_conf = pickle.load(handle)
    
with open('citingpaper_map_conf.pickle', 'rb') as handle:
    citingpaper_map_conf = pickle.load(handle)
    
with open('single_citingpaper_map_conf.pickle', 'rb') as handle:
    single_citingpaper_map_conf = pickle.load(handle)
    
with open('single_citingpatent_map_conf.pickle', 'rb') as handle:
    single_citingpatent_map_conf = pickle.load(handle)

with open('citedpaper_list_conf.pickle', 'rb') as handle:
    citedpaper_list_conf = pickle.load(handle)
    
with open('cited_author_map_conf.pickle', 'rb') as handle:
    cited_author_map_conf = pickle.load(handle)
    ic(len(cited_author_map_conf["CHI"]))    
with open('notcited_author_map_conf.pickle', 'rb') as handle:
    notcited_author_map_conf = pickle.load(handle)

ic(len(citedpaper_map_conf['CHI']))

ori_paperyear_conf = {}
ori_citingpatent_conf = {}


df_paper_year = pd.read_csv("df_paper_year.tsv")
df_paper_year = df_paper_year.groupby("paper_id").first().reset_index()
df_paper_pc2s_year = pd.read_csv("df_paper_pc2s_year.tsv")
ic(len(df_paper_pc2s_year))
df_paper_pc2s_year = df_paper_pc2s_year.groupby(['magid', 'patent']).first().reset_index()
ic(len(df_paper_pc2s_year))
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
        ax_c.set_xlabel("paper year", fontsize=70)
        ax_c.tick_params(labelsize=70)

plot_idx = 0

X_year = [i for i in range (start, end)]

for conf, paperyear_map in paperyear_map_conf.items():
    Y_papercnt = [0] * span
    Y_citedpapercnt = [0] * span
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
            Y_citedpapercnt[i-start] = len(citedpaper_map[str(i)])
        if str(i) in citedpaper_map.keys():
            Y_citedportion[i-start] = len(citedpaper_map[str(i)]) / Y_papercnt[i-start]
    axes[plot_idx, 0].plot(X_year,Y_papercnt, 'o-', label='paper number', color='r', linewidth = 10, markersize=20)
    # axes[plot_idx, 0].plot(X_year,Y_citingpatentcnt, 'o-', label='patent_citation', color='g', linewidth = 10, markersize=20)
    axes[plot_idx, 0].plot(X_year,Y_citedpapercnt, 'o-', label='cited paper number', color='g', linewidth = 10, markersize=20)
    axes[plot_idx, 0].set_title('{}'.format(conf.upper().replace("UBI", "UbiComp")), fontsize=90)
    axes[plot_idx, 0].legend(loc = 'upper left', prop={'size': 100})
    axes[plot_idx, 1].plot(X_year,Y_citedportion, 'o-', label='cited ratio', color='b', linewidth = 10, markersize=20)
    axes[plot_idx, 1].set_title('{}'.format(conf.upper().replace("UBI", "UbiComp")), fontsize=90)
    axes[plot_idx, 1].legend(loc = 'upper left', prop={'size': 100})
    plot_idx += 1
save_png_idx += 1
plt.savefig('../final_paper_report_figure/fig_{}.png'.format(save_png_idx))
fig = plt.figure()
# plt.legend(loc = 'upper left')

# %%
# single point visualization
from scipy import stats
fig = plt.figure(figsize=(30,100))
axes = fig.subplots(nrows=4)

for ax_c in axes:
    ax_c.set_xlabel("paper citation", fontsize=70)
    ax_c.set_ylabel("patent citation", fontsize=70)
    ax_c.tick_params(labelsize=70)

plot_idx = 0

ic(len(single_citingpaper_map_conf['CHI']))
for conf, paperyear_map in paperyear_map_conf.items():
    citingpatent_map = single_citingpatent_map_conf[conf]
    citingpaper_map = single_citingpaper_map_conf[conf]
    Y_citingpatentcnt = [0] * max(len(citingpatent_map), len(citingpaper_map))
    Y_citingpapercnt = [0] * max(len(citingpatent_map), len(citingpaper_map))
    idx = 0
    for key, val in citingpatent_map.items():
        Y_citingpatentcnt[idx] = len(val)
        if key in citingpaper_map:
            Y_citingpapercnt[idx] = len(citingpaper_map[key])
        else:
            Y_citingpapercnt[idx] = 0
        idx += 1
    print(stats.pearsonr(Y_citingpapercnt, Y_citingpatentcnt))
    axes[plot_idx].plot(Y_citingpapercnt,Y_citingpatentcnt,'o',color='r',markersize=30)
    axes[plot_idx].set_title('{}'.format(conf.upper().replace("UBI", "UbiComp")), fontsize=90)
    axes[plot_idx].set_xscale("log")
    plot_idx += 1
save_png_idx = 7

plt.savefig('../final_paper_report_figure/fig_{}.png'.format(save_png_idx))
fig = plt.figure()

# %%
# single point visualization
from scipy import stats
fig = plt.figure(figsize=(30,100))
axes = fig.subplots(nrows=4)

for ax_c in axes:
    ax_c.set_xlabel("paper citation", fontsize=70)
    ax_c.set_ylabel("patent citation", fontsize=70)
    ax_c.tick_params(labelsize=70)

plot_idx = 0

ic(len(single_citingpaper_map_conf['CHI']))
for conf, paperyear_map in paperyear_map_conf.items():
    citingpatent_map = single_citingpatent_map_conf[conf]
    citingpaper_map = single_citingpaper_map_conf[conf]
    Y_citingpatentcnt = [0] * max(len(citingpatent_map), len(citingpaper_map))
    Y_citingpapercnt = [0] * max(len(citingpatent_map), len(citingpaper_map))
    idx = 0
    for key, val in citingpatent_map.items():
        Y_citingpatentcnt[idx] = len(val)
        if key in citingpaper_map:
            Y_citingpapercnt[idx] = len(citingpaper_map[key])
        else:
            Y_citingpapercnt[idx] = 0
        idx += 1
    print(stats.pearsonr(Y_citingpapercnt, Y_citingpatentcnt))
    axes[plot_idx].plot(Y_citingpapercnt,Y_citingpatentcnt,'o',color='r',markersize=30)
    axes[plot_idx].set_title('{}'.format(conf.upper().replace("UBI", "UbiComp")), fontsize=90)
    axes[plot_idx].set_yscale("log")
    plot_idx += 1
save_png_idx = 7

plt.savefig('../final_paper_report_figure/testylog_fig_{}.png'.format(save_png_idx))
fig = plt.figure()

df_patent_paper_year = pd.read_csv("../dataAug10/mergeversiondata/df_patent_paper_year.tsv")
df_patent_paper_year = df_patent_paper_year.drop_duplicates()
df_patent_paper_year = df_patent_paper_year.groupby(["magid", "patent_id"]).first().reset_index()

df_patent_paper_year = df_patent_paper_year.replace("UBI", "UbiComp")
# %%
# related patents over year
df_temp = df_patent_paper_year.groupby(['conf_id','patent_id','patent_year']).agg('count').reset_index()
df_temp = df_temp[['conf_id','patent_id','patent_year']]
df_temp = df_temp.groupby(['conf_id','patent_year']).agg('count').reset_index()


df_temp = df_temp[(df_temp['patent_year']>1985) & (df_temp['patent_year']<2020)]
df_temp = df_temp.sort_values(by=['conf_id'])
plt_ = sns.pointplot(x="patent_year", y="patent_id", hue="conf_id", data=df_temp)
plt.ylabel('Number of patents',fontsize = 20)
plt.title('Number of patents by years',fontsize = 20)
plt.xticks(fontsize = 18)
plt.yticks(fontsize = 20)
plt.legend(fontsize =15)
plt.xlabel('Year', fontsize =20)
for ind, label in enumerate(plt_.get_xticklabels()):
    if ind % 5 == 0:  # every 10th label is kept
        label.set_visible(True)
    else:
        label.set_visible(False)
save_png_idx += 1
plt.savefig('../final_paper_report_figure/fig_{}.png'.format(save_png_idx), bbox_inches = "tight")
fig = plt.figure()

# the average lag of science that influence patent
df_temp = df_patent_paper_year[df_patent_paper_year['patent_year']>1985]
df_temp = df_temp.sort_values(by=['conf_id'])
plt_ = sns.pointplot(x="patent_year", y="patent_paper_lag", hue="conf_id", data=df_temp)
plt.ylabel('Time difference (Year)',fontsize = 20)
plt.title('The average time lag of the paper\n cited by patents in year X',fontsize = 20)
plt.xticks(rotation=45, fontsize = 20)
plt.yticks(fontsize = 20)
plt.ylim(0, 30)
plt.legend(fontsize =15)
plt.xlabel('patent year', fontsize =20)
for ind, label in enumerate(plt_.get_xticklabels()):
    if ind % 5 == 0:  # every 10th label is kept
        label.set_visible(True)
    else:
        label.set_visible(False)
# plt.savefig('../final_paper_report_figure/fig_{}.png'.format(save_png_idx))
plt.savefig('../final_paper_report_figure/fig_12a.png', bbox_inches = "tight")
fig = plt.figure()

# the median lag of science that influence patent
df_temp = df_patent_paper_year[df_patent_paper_year['patent_year']>1985]
df_temp = df_temp.sort_values(by=['conf_id'])
plt_ = sns.pointplot(x="patent_year", y="patent_paper_lag", hue="conf_id", data=df_temp, estimator=np.median)
plt.ylabel('Time difference (Year)',fontsize = 20)
plt.title('The median time lag of the paper\n cited by patents in year X',fontsize = 20)
plt.xticks(rotation=45, fontsize = 20)
plt.yticks(fontsize = 20)
plt.ylim(0, 30)
plt.legend(fontsize =15)
plt.xlabel('patent year', fontsize =20)
for ind, label in enumerate(plt_.get_xticklabels()):
    if ind % 5 == 0:  # every 10th label is kept
        label.set_visible(True)
    else:
        label.set_visible(False)
plt.savefig('../final_paper_report_figure/fig_12c.png', bbox_inches = "tight")
fig = plt.figure()


# # # %%
# The time lag of the most recent paper cited by patents in year X
df_temp = df_patent_paper_year.groupby(['patent_id','patent_year','conf_id'])['patent_paper_lag'].agg('min').reset_index()
df_temp = df_temp[df_temp['patent_year']>1985]
df_temp = df_temp.sort_values(by=['conf_id'])
plt_ = sns.pointplot(x="patent_year", y="patent_paper_lag", hue="conf_id", data=df_temp)
plt.ylabel('Time difference (Year)',fontsize = 20)
plt.title('The time lag of the most recent paper\n cited by patents in year X',fontsize = 20)
plt.xticks(rotation=45, fontsize = 20)
plt.yticks(fontsize = 20)
plt.ylim(0, 30)
plt.legend(fontsize =15)
plt.xlabel('patent year', fontsize =20)
for ind, label in enumerate(plt_.get_xticklabels()):
    if ind % 5 == 0:  # every 10th label is kept
        label.set_visible(True)
    else:
        label.set_visible(False)
plt.savefig('../final_paper_report_figure/fig_12b.png', bbox_inches = "tight")
fig = plt.figure()