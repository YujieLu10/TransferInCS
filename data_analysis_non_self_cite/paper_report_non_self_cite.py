import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from icecream import ic
import pickle
import seaborn as sns

save_png_idx = 0
conf_key = {'CHI':1163450153, 'CSCW':1195049314, 'UBI':1171345118, 'UIST':1166315290}

import pandas as pd
df_patent_paper_year = pd.read_csv("../dataAug10/mergeversiondata/df_patent_paper_year.tsv")

with open('paperyear_map_conf.pickle', 'rb') as handle:
    paperyear_map_conf = pickle.load(handle)

with open('inv_paperyear_map_conf.pickle', 'rb') as handle:
    inv_paperyear_map_conf = pickle.load(handle)
    
with open('citingpatent_map_conf.pickle', 'rb') as handle:
    citingpatent_map_conf = pickle.load(handle)
    ic(len(citingpatent_map_conf['CHI']))
    
with open('citedpaper_map_conf.pickle', 'rb') as handle:
    citedpaper_map_conf = pickle.load(handle)

with open('citingpaper_map_conf.pickle', 'rb') as handle:
    citingpaper_map_conf = pickle.load(handle)
    
with open('single_citingpaper_map_conf.pickle', 'rb') as handle:
    single_citingpaper_map_conf = pickle.load(handle)
    
with open('single_citingpatent_map_conf.pickle', 'rb') as handle:
    single_citingpatent_map_conf = pickle.load(handle)
    
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
plt.savefig('../paper_report_figure_no_selfcite/fig_{}.png'.format(save_png_idx))
fig = plt.figure()

# %%
# point visualization
start = 1980
end = 2019
span = end - start
fig = plt.figure(figsize=(100,100))
axes = fig.subplots(nrows=4)

for ax_c in axes:
    ax_c.set_xlabel("paper_citation", fontsize=70)
    ax_c.set_ylabel("patent_citation", fontsize=70)
    ax_c.tick_params(labelsize=70)

plot_idx = 0

X_year = [i for i in range (start, end)]

for conf, paperyear_map in paperyear_map_conf.items():
    Y_citingpatentcnt = [0] * span
    Y_citingpapercnt = [0] * span

    citingpatent_map = citingpatent_map_conf[conf]
    citingpaper_map = citingpaper_map_conf[conf]
    for i in range (start, end):
        if str(i) in citingpatent_map.keys():
            Y_citingpatentcnt[i-start] = len(citingpatent_map[str(i)])    
        if str(i) in citingpaper_map.keys():
            Y_citingpapercnt[i-start] = len(citingpaper_map[str(i)])

    axes[plot_idx].plot(Y_citingpapercnt,Y_citingpatentcnt,'o',color='r',markersize=30)
    axes[plot_idx].set_title('conference_{}'.format(conf), fontsize=90)
    plot_idx += 1
save_png_idx += 1
plt.savefig('../paper_report_figure_no_selfcite/fig_{}.png'.format(save_png_idx))
fig = plt.figure()

# %%
# single point visualization
from scipy import stats
fig = plt.figure(figsize=(100,100))
axes = fig.subplots(nrows=4)

for ax_c in axes:
    ax_c.set_xlabel("paper_citation", fontsize=70)
    ax_c.set_ylabel("patent_citation", fontsize=70)
    ax_c.tick_params(labelsize=70)

plot_idx = 0

ic(len(single_citingpatent_map_conf['CHI']))
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
    # ic(Y_citingpapercnt, Y_citingpatentcnt)
    ic(stats.pearsonr(Y_citingpapercnt, Y_citingpatentcnt))
    axes[plot_idx].plot(Y_citingpapercnt,Y_citingpatentcnt,'o',color='r',markersize=30)
    axes[plot_idx].set_title('conference_{}'.format(conf), fontsize=90)
    plot_idx += 1
save_png_idx += 1
plt.savefig('../paper_report_figure_no_selfcite/fig_{}.png'.format(save_png_idx))
fig = plt.figure()

# the average lag of science that influence patent
df_temp = df_patent_paper_year[df_patent_paper_year['patent_year']>1985]
plt_ = sns.pointplot(x="patent_year", y="patent_paper_lag", hue="conf_id", data=df_temp)
plt.ylabel('Time difference (Year)',fontsize = 20)
plt.title('The average time lag of the paper\n cited by patents in year X',fontsize = 20)
plt.xticks(rotation=45, fontsize = 20)
plt.yticks(fontsize = 20)
plt.ylim(0, 50)
plt.legend(fontsize =15)
plt.xlabel('patent year', fontsize =20)
for ind, label in enumerate(plt_.get_xticklabels()):
    if ind % 5 == 0:  # every 10th label is kept
        label.set_visible(True)
    else:
        label.set_visible(False)
save_png_idx += 1
plt.savefig('../paper_report_figure_no_selfcite/fig_{}.png'.format(save_png_idx))
fig = plt.figure()

# the median lag of science that influence patent
df_temp = df_patent_paper_year[df_patent_paper_year['patent_year']>1985]
plt_ = sns.pointplot(x="patent_year", y="patent_paper_lag", hue="conf_id", data=df_temp, estimator=np.median)
plt.ylabel('Time difference (Year)',fontsize = 20)
plt.title('The median time lag of the paper\n cited by patents in year X',fontsize = 20)
plt.xticks(rotation=45, fontsize = 20)
plt.yticks(fontsize = 20)
plt.ylim(0, 50)
plt.legend(fontsize =15)
plt.xlabel('patent year', fontsize =20)
for ind, label in enumerate(plt_.get_xticklabels()):
    if ind % 5 == 0:  # every 10th label is kept
        label.set_visible(True)
    else:
        label.set_visible(False)
save_png_idx += 1
plt.savefig('../paper_report_figure_no_selfcite/fig_{}.png'.format(save_png_idx))
fig = plt.figure()

# %%
# The time lag of the most recent paper cited by patents in year X
df_temp = df_patent_paper_year.groupby(['patent_id','patent_year','conf_id'])['patent_paper_lag'].agg('min').reset_index()
df_temp = df_temp[df_temp['patent_year']>1985]
plt_ = sns.pointplot(x="patent_year", y="patent_paper_lag", hue="conf_id", data=df_temp)
plt.ylabel('Time difference (Year)',fontsize = 20)
plt.title('The time lag of the most recent paper\n cited by patents in year X',fontsize = 20)
plt.xticks(rotation=45, fontsize = 20)
plt.yticks(fontsize = 20)
plt.ylim(0, 50)
plt.legend(fontsize =15)
plt.xlabel('patent year', fontsize =20)
for ind, label in enumerate(plt_.get_xticklabels()):
    if ind % 5 == 0:  # every 10th label is kept
        label.set_visible(True)
    else:
        label.set_visible(False)
save_png_idx += 1
plt.savefig('../paper_report_figure_no_selfcite/fig_{}.png'.format(save_png_idx))
fig = plt.figure()

# %%
# related patents over year
df_temp = df_patent_paper_year.groupby(['conf_id','patent_id','patent_year']).agg('count').reset_index()
df_temp = df_temp[['conf_id','patent_id','patent_year']]
df_temp = df_temp.groupby(['conf_id','patent_year']).agg('count').reset_index()


df_temp = df_temp[(df_temp['patent_year']>1985) & (df_temp['patent_year']<2020)]
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
plt.savefig('../paper_report_figure_no_selfcite/fig_{}.png'.format(save_png_idx))
fig = plt.figure()