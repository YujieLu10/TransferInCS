import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from icecream import ic
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

save_png_idx = 0
conf_key = {'CHI':1163450153, 'CSCW':1195049314, 'UIST':1166315290, 'UbiComp':1171345118}

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

ic(len(citedpaper_map_conf['CHI']))
ic(len(paperyear_map_conf['CHI']))
# %%
# Visualization
start = 1980
end = 2019
span = end - start
fig = plt.figure(figsize=(180,180))
axes = fig.subplots(nrows=4, ncols=2)
for ax in axes:
    ax[0].set_ylabel("Number of Papers", fontsize=100)
    ax[1].set_ylabel("Percent (%)", fontsize=100)
    for ax_c in ax:
        ax_c.set_xlabel("Year", fontsize=100)
        ax_c.tick_params(labelsize=100)

plot_idx = 0

X_year = [i for i in range (start, end)]
# ic(paperyear_map_conf["UBI"][2017])
for conf in ["CHI", "CSCW", "UIST", "UBI"]:
    paperyear_map = paperyear_map_conf[conf]
    Y_papercnt = [0] * span
    Y_citedpapercnt = [0] * span
    Y_citingpatentcnt = [0] * span
    Y_citedportion = [0.0] * span

    citingpatent_map = citingpatent_map_conf[conf]
    citedpaper_map = citedpaper_map_conf[conf]
    
    for i in range (start, end):
        if i in paperyear_map.keys():
            Y_papercnt[i-start] = len(paperyear_map[i])
        if i in citingpatent_map.keys():
            Y_citingpatentcnt[i-start] = len(citingpatent_map[i])    
        if i in citedpaper_map.keys():
            Y_citedpapercnt[i-start] = len(citedpaper_map[i])
        if i in citedpaper_map.keys():
            Y_citedportion[i-start] = len(citedpaper_map[i]) / Y_papercnt[i-start] * 100
    # Y_papercnt = np.array(Y_papercnt).astype(float)
    # Y_papercnt[ Y_papercnt<=30 ] = np.nan
    # filled_Y_papercnt = pd.Series(Y_papercnt).fillna(method='ffill')
    
    # Y_citedpapercnt = np.array(Y_citedpapercnt).astype(float)
    # Y_citedpapercnt[ Y_citedpapercnt<=10 ] = np.nan
    # filled_Y_citedpapercnt = pd.Series(Y_citedpapercnt).fillna(method='ffill')
    
    # Y_citedportion = np.array(Y_citedportion).astype(float)
    # Y_citedportion[ Y_citedportion<=0.001 ] = np.nan
    # filled_Y_citedportion = pd.Series(Y_citedportion).fillna(method='ffill')
    X_year = np.array(X_year).astype(float)
    Y_papercnt = np.array(Y_papercnt).astype(float)
    if conf == "CSCW":
        Y_papercnt[[5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]] = None#-np.inf
    if conf == "UBI":
        Y_papercnt[[37]] = None#-np.inf
    # Y_citedpapercnt = np.array(Y_citedpapercnt).astype(float)
    # # Y_citedpapercnt[ Y_citedpapercnt<=3 ] = -np.inf
    # Y_citedportion = np.array(Y_citedportion).astype(float)
    # s1mask = np.isfinite(Y_papercnt)
    # s2mask = np.logical_and(s1mask, np.isfinite(Y_citedpapercnt))
    # s3mask = np.logical_and(s1mask, s2mask)

    axes[plot_idx, 0] = sns.lineplot(x=X_year, y=Y_papercnt, label='Published')
    # axes[plot_idx, 0].plot(X_year[s1mask].astype(int),Y_papercnt[s1mask].astype(int), 'o-', label='Published', color='r', linewidth = 10, markersize=20)
    # axes[plot_idx, 0].plot(X_year,Y_citingpatentcnt, 'o-', label='patent_citation', color='g', linewidth = 10, markersize=20)
    axes[plot_idx, 0] = sns.lineplot(x=X_year, y=Y_citedpapercnt, label='Published and later cited by patents')
    # axes[plot_idx, 0].plot(X_year[s2mask].astype(int),Y_citedpapercnt[s2mask].astype(int), 'o-', label='Published and later cited by patents', color='b', linewidth = 10, markersize=20)
    axes[plot_idx, 0].set_title('{}'.format(conf.upper().replace("UBI", "UbiComp")), fontsize=120)
    axes[plot_idx, 0].legend(loc = 'upper left', prop={'size': 100})
    # axes[plot_idx, 1].plot(X_year[s3mask].astype(int),Y_citedportion[s3mask], 'o-', label='Percent of published papers later cited by patents', color='black', linewidth = 10, markersize=20)
    axes[plot_idx, 1] = sns.lineplot(x=X_year, y=Y_citedportion, label='Percent of published papers later cited by patents')
    axes[plot_idx, 1].set_ylim([0,100])
    axes[plot_idx, 1].set_title('{}'.format(conf.upper().replace("UBI", "UbiComp")), fontsize=120)
    axes[plot_idx, 1].legend(loc = 'upper left', prop={'size': 100})
    plot_idx += 1
save_png_idx += 1
plt.savefig('new_fig_{}.png'.format(save_png_idx))
fig = plt.figure()