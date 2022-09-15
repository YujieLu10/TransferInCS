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
fig = plt.figure(figsize=(100,100), constrained_layout=True)
fig.tight_layout()
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
    Y_citedpapercnt = np.array(Y_citedpapercnt).astype(float)
    Y_citedportion = np.array(Y_citedportion).astype(float)
    if conf == "CHI":
        Y_papercnt[[4, 7]] = -np.inf
        Y_citedpapercnt[[4, 7]] = -np.inf
        Y_citedportion[[4, 7]] = -np.inf
    if conf == "CSCW":
        Y_papercnt[[5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]] = -np.inf
        Y_citedpapercnt[[5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]] = -np.inf
        Y_citedportion[[5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]] = -np.inf
    if conf == "UBI":
        Y_papercnt[[37]] = -np.inf
        Y_citedpapercnt[[37]] = -np.inf
        Y_citedportion[[37]] = -np.inf
    Y_citedpapercnt = np.array(Y_citedpapercnt).astype(float)
    # Y_citedpapercnt[ Y_citedpapercnt<=3 ] = -np.inf
    Y_citedportion = np.array(Y_citedportion).astype(float)
    s1mask = np.isfinite(Y_papercnt)
    s2mask = np.logical_and(s1mask, np.isfinite(Y_citedpapercnt))
    s3mask = np.logical_and(s1mask, s2mask)
    # ic(conf, s1mask, s2mask, s3mask, X_year)
    axes[plot_idx, 0].plot(X_year[s1mask].astype(int),Y_papercnt[s1mask].astype(int), 'o-', label='Published', color='r', linewidth = 20, markersize=30)
    # axes[plot_idx, 0].plot(X_year,Y_citingpatentcnt, 'o-', label='patent_citation', color='g', linewidth = 10, markersize=20)
    axes[plot_idx, 0].plot(X_year[s2mask].astype(int),Y_citedpapercnt[s2mask].astype(int), 'o-', label='Published and later cited by patents', color='b', linewidth = 20, markersize=30)
    axes[plot_idx, 0].set_title('{}'.format(conf.upper().replace("UBI", "UbiComp")), fontsize=120)
    axes[plot_idx, 0].legend(loc = 'upper left', prop={'size': 100})
    axes[plot_idx, 1].plot(X_year[s3mask].astype(int),Y_citedportion[s3mask], 'o-', label='Percent of published papers later cited by patents', color='black', linewidth = 20, markersize=30)
    axes[plot_idx, 1].set_ylim([0,100])
    axes[plot_idx, 1].set_title('{}'.format(conf.upper().replace("UBI", "UbiComp")), fontsize=120)
    axes[plot_idx, 1].legend(loc = 'upper left', prop={'size': 100})
    plot_idx += 1
save_png_idx += 1
plt.savefig('../final_paper_report_figure/fig_{}.png'.format(save_png_idx))
fig = plt.figure()
# plt.legend(loc = 'upper left')

# # %%
# # single point visualization
# from scipy import stats
# # fig = plt.figure(figsize=(30,100))
# # axes = fig.subplots(nrows=4)

# # for ax_c in axes:
# #     ax_c.set_xlabel("paper citation", fontsize=70)
# #     ax_c.set_ylabel("patent citation", fontsize=70)
# #     ax_c.tick_params(labelsize=70)

# # plot_idx = 0

# ic(len(single_citingpaper_map_conf['CHI']))
# import math
# for conf in ["CHI", "CSCW", "UIST", "UBI"]:
#     paperyear_map = paperyear_map_conf[conf]
#     citingpatent_map = single_citingpatent_map_conf[conf]
#     citingpaper_map = single_citingpaper_map_conf[conf]
#     Y_citingpatentcnt = [0] * max(len(citingpatent_map), len(citingpaper_map))
#     Y_citingpapercnt = [0] * max(len(citingpatent_map), len(citingpaper_map))
#     idx = 0
#     for key, val in citingpatent_map.items():
#         Y_citingpatentcnt[idx] = len(val)
#         if key in citingpaper_map:
#             Y_citingpapercnt[idx] = math.log(len(citingpaper_map[key]))
#         else:
#             Y_citingpapercnt[idx] = math.log(0.0001)
#         idx += 1
#     print(stats.pearsonr(Y_citingpapercnt, Y_citingpatentcnt))
#     # print(stats.ttest_ind(Y_citingpapercnt, Y_citingpatentcnt))
    
# #     axes[plot_idx].plot(Y_citingpapercnt,Y_citingpatentcnt,'o',color='r',markersize=30)
# #     axes[plot_idx].set_title('{}'.format(conf.upper().replace("UBI", "UbiComp")), fontsize=90)
# #     axes[plot_idx].set_xscale("log")
# #     plot_idx += 1
# # save_png_idx = 7

# # plt.savefig('../final_paper_report_figure/fig_{}.png'.format(save_png_idx))


# df_patent_paper_year = pd.read_csv("df_patent_paper_year_filtered.tsv")
# df_patent_paper_year = df_patent_paper_year.drop_duplicates()
# df_patent_paper_year = df_patent_paper_year.groupby(["magid", "patent_id"]).first().reset_index()

# df_patent_paper_year = df_patent_paper_year.replace("UBI", "UbiComp")

# # the median lag of science that influence patent
# df_temp = df_patent_paper_year[df_patent_paper_year['patent_year']>1985].groupby(['patent_id','patent_year','conf_id'])['patent_paper_lag'].agg('median').reset_index()
# # df_temp = df_temp.groupby(["patent_year"])["patent_paper_lag"].median().reset_index()
# # df_temp = df_temp.groupby(['patent_year'])['patent_paper_lag'].agg('median').reset_index()
# df_temp = df_temp.sort_values(by=['conf_id'])
# df_temp = df_temp[(df_temp["conf_id"] != "UbiComp") | (df_temp["patent_year"] >= 2005 )]
# plt_ = sns.lineplot(x="patent_year", y="patent_paper_lag", hue="conf_id", data=df_temp)
# plt.ylabel('Time difference (Year)',fontsize = 20)
# plt.title('The median time lag of the paper\n cited by patents in year X',fontsize = 20)
# # plt.xticks(rotation=45, fontsize = 20)
# plt.yticks([0,5,10,15,20],fontsize = 20)
# plt.ylim(0, 20)
# plt.legend(fontsize =15, loc = 'upper left')
# plt.xlabel('Year', fontsize =20)
# # for ind, label in enumerate(plt_.get_xticklabels()):
# #     if ind % 5 == 0:  # every 10th label is kept
# #         label.set_visible(True)
# #     else:
# #         label.set_visible(False)
# plt.savefig('../final_paper_report_figure/fig_12c.png', bbox_inches = "tight")
# fig = plt.figure()


# # # # %%
# # The time lag of the most recent paper cited by patents in year X
# # df_temp = df_patent_paper_year.groupby(['patent_id','patent_year','conf_id'])['patent_paper_lag'].agg('min').reset_index()
# df_temp = df_patent_paper_year[df_patent_paper_year['patent_year']>1985].groupby(['patent_id','patent_year','conf_id'])['patent_paper_lag'].agg('min').reset_index()
# df_temp = df_temp[df_temp['patent_year']>=1990]
# df_temp = df_temp.sort_values(by=['conf_id'])
# df_temp = df_temp[(df_temp["conf_id"] != "UbiComp") | (df_temp["patent_year"] >= 2005 )]
# plt_ = sns.lineplot(x="patent_year", y="patent_paper_lag", hue="conf_id", data=df_temp)
# plt.ylabel('Time difference (Year)',fontsize = 20)
# plt.title('The time lag of the most recent paper\n cited by patents in year X',fontsize = 20)
# # plt.xticks(rotation=45, fontsize = 20)
# plt.yticks([0,5,10,15,20],fontsize = 20)
# plt.ylim(0, 20)
# plt.legend(fontsize =15, loc = 'upper left')
# plt.xlabel('Year', fontsize =20)
# # for ind, label in enumerate(plt_.get_xticklabels()):
# #     if ind % 5 == 0:  # every 10th label is kept
# #         label.set_visible(True)
# #     else:
# #         label.set_visible(False)
# plt.savefig('../final_paper_report_figure/fig_12b.png', bbox_inches = "tight")
# fig = plt.figure()


# # %%
# # related patents over year
# df_temp = df_patent_paper_year.groupby(['conf_id','patent_id','patent_year']).agg('count').reset_index()
# df_temp = df_temp[['conf_id','patent_id','patent_year']]
# df_temp = df_temp.groupby(['conf_id','patent_year']).agg('count').reset_index()

# df_temp = df_temp[(df_temp['patent_year']!=2001)|(df_temp['conf_id']!="UbiComp")]
# df_temp = df_temp[(df_temp['patent_year']>=1989) & (df_temp['patent_year']<=2018)]
# plt_ = sns.lineplot(x="patent_year", y="patent_id", hue="conf_id", data=df_temp)
# plt.ylabel('Number of patents',fontsize = 20)
# plt.title('Patents Citing HCI Research',fontsize = 20)
# # plt.xticks(fontsize = 18)
# plt.yticks(fontsize = 20)
# plt.legend(fontsize =15, loc = 'upper left')
# plt.xlabel('Year', fontsize =20)
# # for ind, label in enumerate(plt_.get_xticklabels()):
# #     if ind % 5 == 0:  # every 10th label is kept
# #         label.set_visible(True)
# #     else:
# #         label.set_visible(False)
# save_png_idx = 8
# plt.savefig('../final_paper_report_figure/fig_{}.png'.format(save_png_idx), bbox_inches = "tight")
# fig = plt.figure()