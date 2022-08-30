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
    
with open('citingpaper_map_conf.pickle', 'rb') as handle:
    citingpaper_map_conf = pickle.load(handle)
    
with open('single_citingpaper_map_conf.pickle', 'rb') as handle:
    single_citingpaper_map_conf = pickle.load(handle)
    
with open('single_citingpatent_map_conf.pickle', 'rb') as handle:
    single_citingpatent_map_conf = pickle.load(handle)

ic(len(citedpaper_map_conf['CHI']))

ori_paperyear_conf = {}
ori_citingpatent_conf = {}


df_paper_year = pd.read_csv("df_paper_year.tsv")
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
# start = 1980
# end = 2019
# span = end - start
# fig = plt.figure(figsize=(100,100))
# axes = fig.subplots(nrows=4, ncols=2)
# for ax in axes:
#     ax[0].set_ylabel("number", fontsize=70)
#     ax[1].set_ylabel("ratio", fontsize=70)
#     for ax_c in ax:
#         ax_c.set_xlabel("paper_year", fontsize=70)
#         ax_c.tick_params(labelsize=70)

# plot_idx = 0

# X_year = [i for i in range (start, end)]

# for conf, paperyear_map in paperyear_map_conf.items():
#     Y_papercnt = [0] * span
#     Y_citingpatentcnt = [0] * span
#     Y_citedportion = [0.0] * span

#     citingpatent_map = citingpatent_map_conf[conf]
#     citedpaper_map = citedpaper_map_conf[conf]
#     for i in range (start, end):
#         if str(i) in paperyear_map.keys():
#             Y_papercnt[i-start] = len(paperyear_map[str(i)])
#         if str(i) in citingpatent_map.keys():
#             Y_citingpatentcnt[i-start] = len(citingpatent_map[str(i)])    
#         if str(i) in citedpaper_map.keys():
#             Y_citedportion[i-start] = len(citedpaper_map[str(i)]) / Y_papercnt[i-start]
#     axes[plot_idx, 0].plot(X_year,Y_papercnt, 'o-', label='paper_number', color='r', linewidth = 10, markersize=20)
#     axes[plot_idx, 0].plot(X_year,Y_citingpatentcnt, 'o-', label='patent_citation', color='g', linewidth = 10, markersize=20)
#     axes[plot_idx, 0].set_title('conference_{}'.format(conf), fontsize=90)
#     axes[plot_idx, 0].legend(loc = 'upper left', prop={'size': 100})
#     axes[plot_idx, 1].plot(X_year,Y_citedportion, 'o-', label='cited_ratio', color='b', linewidth = 10, markersize=20)
#     axes[plot_idx, 1].set_title('conference_{}'.format(conf), fontsize=90)
#     axes[plot_idx, 1].legend(loc = 'upper left', prop={'size': 100})
#     plot_idx += 1
# save_png_idx += 1
# plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# fig = plt.figure()
# # plt.legend(loc = 'upper left')

# # %%
with open('citedpaper_list_conf.pickle', 'rb') as handle:
    citedpaper_list_conf = pickle.load(handle)
    
with open('cited_author_map_conf.pickle', 'rb') as handle:
    cited_author_map_conf = pickle.load(handle)
    ic(len(cited_author_map_conf["CHI"]))    
with open('notcited_author_map_conf.pickle', 'rb') as handle:
    notcited_author_map_conf = pickle.load(handle)

# # %%
# # Visualization
# start = 1980
# end = 2019
# span = end - start
# fig = plt.figure(figsize=(100,100))
# axes = fig.subplots(nrows=4)

# for ax_c in axes:
#     ax_c.set_xlabel("paper_year", fontsize=70)
#     ax_c.set_ylabel("author_number", fontsize=70)
#     ax_c.tick_params(labelsize=70)

# plot_idx = 0

# X_year = [i for i in range (start, end)]

# for conf, paperyear_map in paperyear_map_conf.items():
#     Y_citedpaper_authorcnt = [0] * span
#     Y_notcitedpaper_authorcnt = [0] * span

#     cited_author_map = cited_author_map_conf[conf]
#     notcited_author_map = notcited_author_map_conf[conf]
#     for i in range (start, end):
#         if str(i) in cited_author_map.keys():
#             Y_citedpaper_authorcnt[i-start] = len(cited_author_map[str(i)])    
#         if str(i) in notcited_author_map.keys():
#             Y_notcitedpaper_authorcnt[i-start] = len(notcited_author_map[str(i)])    

#     axes[plot_idx].plot(X_year,Y_citedpaper_authorcnt, 'o-', label='citedpaper_authornumber', color='r', linewidth = 10)
#     axes[plot_idx].legend(loc = 'upper left', prop={'size': 100})
#     axes[plot_idx].plot(X_year,Y_notcitedpaper_authorcnt, 'o-', label='notcitedpaper_authornumber', color='g', linewidth = 10)
#     axes[plot_idx].set_title('conference_{}'.format(conf), fontsize=90)
#     axes[plot_idx].legend(loc = 'upper left', prop={'size': 100})
#     plot_idx += 1
# save_png_idx += 1
# plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# fig = plt.figure()

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
plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# fig = plt.figure()

# # %
ori_citingpaper_conf = {}
df_paper_cited = pd.read_csv("df_paper_cited.tsv")
ic(len(df_paper_cited))
for conf_name,conf_id in conf_key.items():
    ori_citingpaper_conf[conf_name] = df_paper_cited.loc[df_paper_cited['conf_id']==conf_id]
# #------------ analyze VIS4 -------------#


# # %%
# with open('cited_paper_map_conf.pickle', 'rb') as handle:
#     cited_paper_map_conf = pickle.load(handle)
    
# with open('notcited_paper_map_conf.pickle', 'rb') as handle:
#     notcited_paper_map_conf = pickle.load(handle)
    
# # Number of papers transferred to patents by year
# start = 1980
# end = 2019
# span = end - start
# font = {'size'   : 18}
# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
# plt.xlim([start,end])
# plt.xlabel('Year', fontsize = 18)
# plt.ylabel('Number of transfers', fontsize = 18)
# plt.title('Number of papers transferred to patents by year', fontsize = 18)

# color_list = ['red', 'blue', 'green', 'cyan']
# idx = 0
# for conf, paperyear_map in paperyear_map_conf.items():
#     cited_paper_map = cited_paper_map_conf[conf]
#     Y_citedpaper_cnt= [0] * span
#     for i in range (start, end):
#         if str(i) in cited_paper_map.keys():
#             Y_citedpaper_cnt[i-start] = len(cited_paper_map[str(i)])
#     plt.plot(X_year, Y_citedpaper_cnt, 'o-', label = conf, color = color_list[idx], linewidth = 2)
#     idx += 1

# plt.legend(loc = 'upper left')
# plt.rc('font', **font)
# # plt.show()
# save_png_idx += 1
# plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# fig = plt.figure()

# # %%
# # proportion of papers transferred to patents by year
# # Number of papers transferred to patents by year
# start = 1980
# end = 2019
# span = end - start
# font = {'size'   : 18}
# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
# plt.xlim([start,end])
# plt.xlabel('Year', fontsize = 18)
# plt.ylabel('Number of transfers', fontsize = 18)
# plt.title('Number of papers transferred to patents by year', fontsize = 18)

# color_list = ['red', 'blue', 'green', 'cyan']
# idx = 0
# for conf, paperyear_map in paperyear_map_conf.items():
#     cited_paper_map = cited_paper_map_conf[conf]
#     Y_citedpaper_cnt= [0] * span
#     for i in range (start, end):
#         if str(i) in cited_paper_map.keys():
#             Y_citedpaper_cnt[i-start] = len(cited_paper_map[str(i)])
#     plt.plot(X_year, Y_citedpaper_cnt, 'o-', label = conf, color = color_list[idx], linewidth = 2)
#     idx += 1

# plt.legend(loc = 'upper left')
# plt.rc('font', **font)
# # plt.show()
# save_png_idx += 1
# plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# fig = plt.figure()
# font = {'size'   : 18}
# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
# plt.xlim([start,end])
# plt.xlabel('Year', fontsize = 18)
# plt.ylabel('Proportion of transfers', fontsize = 18)
# plt.title('Proportion of papers transferred to patents by year', fontsize = 18)

# color_list = ['red', 'blue', 'green', 'cyan']
# idx = 0
# for conf, paperyear_map in paperyear_map_conf.items():
#     cited_paper_map = cited_paper_map_conf[conf]
#     notcited_paper_map = notcited_paper_map_conf[conf]
#     paper_map = cited_paper_map_conf[conf]
#     # ic(notcited_paper_map.keys(), cited_paper_map.keys())
#     Y_citedpaper_cnt = [0] * span
#     for i in range (start, end):
#         if str(i) in cited_paper_map.keys():
#             if str(i) in notcited_paper_map.keys():
#                 Y_citedpaper_cnt[i-start] = len(cited_paper_map[str(i)]) / (len(cited_paper_map[str(i)]) + len(notcited_paper_map[str(i)]))
#             else:
#                 Y_citedpaper_cnt[i-start] = 1
#     plt.plot(X_year, Y_citedpaper_cnt, 'o-', label = conf, color = color_list[idx], linewidth = 2)
#     idx += 1

# plt.legend(loc = 'upper left')
# plt.rc('font', **font)
# # plt.show()
# save_png_idx += 1
# plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# fig = plt.figure()

# # %%
# # visualization
# start = 1980
# end = 2019
# span = end - start
# X_year = [i for i in range (start, end)]
# fig = plt.figure(figsize=(100,100))
# axes = fig.subplots(nrows=4)

# for ax_c in axes:
#     ax_c.set_xlabel("paper_citation", fontsize=70)
#     ax_c.set_ylabel("paper_citation_std", fontsize=70)
#     ax_c.tick_params(labelsize=70)

# plot_idx = 0
# for conf, paperyear_map in paperyear_map_conf.items():
#     Y_citedpaper_citation_std = [0.0] * span
#     Y_notcitedpaper_citation_std = [0.0] * span
#     Y_citedpaper_citation_cnt= [0] * span
#     Y_notcitedpaper_citation_cnt = [0] * span
#     cited_totalcitation = 0
#     notcited_totalcitation = 0

#     cited_citingpaper_map = cited_citingpaper_map_conf[conf]
#     notcited_citingpaper_map = notcited_citingpaper_map_conf[conf]
#     cited_paper_map = cited_paper_map_conf[conf]
#     notcited_paper_map = notcited_paper_map_conf[conf]
#     for i in range (start, end):
#         if str(i) in cited_citingpaper_map.keys():
#             Y_citedpaper_citation_cnt[i-start] = len(cited_citingpaper_map[str(i)])
#             cited_totalcitation += len(cited_citingpaper_map[str(i)])
#         if str(i) in notcited_citingpaper_map.keys():
#             Y_notcitedpaper_citation_cnt[i-start] = len(notcited_citingpaper_map[str(i)])
#             notcited_totalcitation += len(notcited_citingpaper_map[str(i)])

#     for i in range (start, end):
#         if str(i) in cited_paper_map.keys():
#             citing_list = []
#             for key,val in cited_paper_map[str(i)].items():
#                 citing_list.append(len(val))
#             # print(">>> cited conf{} list{}".format(conf, citing_list))
#             Y_citedpaper_citation_std[i-start] = np.std(citing_list)
#         if str(i) in notcited_paper_map.keys():
#             citing_list = []
#             for key,val in notcited_paper_map[str(i)].items():
#                 citing_list.append(len(val))
#             # print(">>> notcited conf{} list{}".format(conf, citing_list))
#             Y_notcitedpaper_citation_std[i-start] = np.std(citing_list)

#     axes[plot_idx].plot(Y_citedpaper_citation_cnt,Y_citedpaper_citation_std,'o',label='citedpaper_citation',color='r',markersize=30)
#     axes[plot_idx].legend(loc = 'upper left', prop={'size': 100})
#     axes[plot_idx].plot(Y_notcitedpaper_citation_cnt,Y_notcitedpaper_citation_std,'o',label='notcitedpaper_citation',color='g',markersize=30)
#     axes[plot_idx].legend(loc = 'upper left', prop={'size': 100})
#     axes[plot_idx].set_title('vis4_conference_{}'.format(conf), fontsize=90)
#     plot_idx += 1
# save_png_idx += 1
# plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# fig = plt.figure()


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
    axes[plot_idx].set_title('conference_{}'.format(conf), fontsize=90)
    plot_idx += 1
save_png_idx += 1
plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
fig = plt.figure()

# # %%
# import matplotlib.pyplot as plt
# import seaborn as sns
# # old_df_patent_year = pd.read_csv('../dataAug10/mergeversiondata/patent_year_inventor_HCI_oldmerge.tsv')[["patent_id","date","conf_id"]]
# # new_df_patent_year = pd.read_csv('../dataAug10/mergeversiondata/patent_year_inventor_new.tsv')[["patent_id","date","conf_id"]]
# # df_patent_year = pd.read_csv('../dataAug10/mergeversiondata/patent_year_inventor_HCI.tsv')[["patent_id","date","conf_id"]]
# # def get_conf_name(x):
# #     if str(x) == "1163450153": return "CHI"
# #     if str(x) == "1195049314": return "CSCW"
# #     if str(x) == "1166315290": return "UIST"
# #     if str(x) == "1171345118": return "UBI"
# #     return x
# # df_patent_year = df_patent_year.append(old_df_patent_year, ignore_index=True)
# # df_patent_year = df_patent_year.append(new_df_patent_year, ignore_index=True)
# # df_patent_year = df_patent_year.apply(get_conf_name).drop_duplicates()
# # df_patent_year['patent_year'] = pd.DatetimeIndex(df_patent_year['date']).year
# # df_patent_year['patent_id'] = df_patent_year['patent_id'].apply(str)
# # df_paper_pc2s_year = df_paper_pc2s_year.drop(columns=["conf_id"])
# # # df_patent_paper_year = df_patent_year.merge(df_paper_pc2s_year,left_on='patent_id',right_on='patent')
# # df_patent_paper_year = df_paper_pc2s_year.merge(df_patent_year,left_on='patent',right_on='patent_id')
# # df_patent_paper_year['patent_paper_lag'] = df_patent_paper_year['patent_year'] - df_patent_paper_year['year']
# # df_patent_paper_year = df_patent_paper_year.drop_duplicates()
# # df_patent_paper_year = df_patent_paper_year.groupby(["magid", "patent_id"]).first().reset_index()
# import pandas as pd
# df_patent_paper_year = pd.read_csv("../dataAug10/mergeversiondata/df_patent_paper_year.tsv")
# df_patent_paper_year.head(3)

# # %%
# # related patents over year
# df_temp = df_patent_paper_year.groupby(['conf_id','patent_id','patent_year']).agg('count').reset_index()
# df_temp = df_temp[['conf_id','patent_id','patent_year']]
# df_temp = df_temp.groupby(['conf_id','patent_year']).agg('count').reset_index()


# df_temp = df_temp[(df_temp['patent_year']>1985) & (df_temp['patent_year']<2020)]
# plt_ = sns.pointplot(x="patent_year", y="patent_id", hue="conf_id", data=df_temp)
# plt.ylabel('Number of patents',fontsize = 20)
# plt.title('Number of patents by years',fontsize = 20)
# plt.xticks(fontsize = 18)
# plt.yticks(fontsize = 20)
# plt.legend(fontsize =15)
# plt.xlabel('Year', fontsize =20)
# for ind, label in enumerate(plt_.get_xticklabels()):
#     if ind % 5 == 0:  # every 10th label is kept
#         label.set_visible(True)
#     else:
#         label.set_visible(False)
# save_png_idx += 1
# plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# fig = plt.figure()
# # %%
# # df_patent_paper_year.head(2)
# # df_patent_paper_year.loc[df_patent_paper_year["year"]==2019]
# # df_paper_pc2s_year.loc[df_paper_pc2s_year["year"]==2019]
# # len(paperyear_map_conf["CHI"]['2019'])
# # df_paper_pc2s_year

# # %%
# # related patents over year
# # df_temp = df_patent_paper_year.groupby(['conf_id','magid','year']).agg('count').reset_index()
# # df_temp = df_temp[['conf_id','magid','year']]
# # df_temp = df_temp.groupby(['conf_id','year']).agg('count').reset_index()
# df_temp = df_patent_paper_year.groupby(['conf_id','magid','patent_year']).agg('count').reset_index()
# df_temp = df_temp[['conf_id','magid','patent_year']]
# df_temp = df_temp.groupby(['conf_id','patent_year']).agg('count').reset_index()


# df_temp = df_temp[(df_temp['patent_year']>1985) & (df_temp['patent_year']<2020)]
# plt_ = sns.pointplot(x="patent_year", y="magid", hue="conf_id", data=df_temp)
# plt.ylabel('Number of papers',fontsize = 20)
# plt.title('Number of papers by citing patent years',fontsize = 20)
# plt.xticks(fontsize = 18)
# plt.yticks(fontsize = 20)
# plt.legend(fontsize = 15)
# plt.xlabel('Year', fontsize = 20)
# for ind, label in enumerate(plt_.get_xticklabels()):
#     if ind % 5 == 0:  # every 10th label is kept
#         label.set_visible(True)
#     else:
#         label.set_visible(False)
# save_png_idx += 1
# plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# fig = plt.figure()
# # %%
# # related patents over year
# df_temp = df_patent_paper_year.groupby(['patent_id','patent_year']).agg('count').reset_index()
# df_temp = df_temp[['patent_id','patent_year']]
# df_temp = df_temp.groupby(['patent_year']).agg('count').reset_index()


# df_temp = df_temp[df_temp['patent_year']>1985]
# plt_ = sns.pointplot(x="patent_year", y="patent_id", data=df_temp)
# plt.ylabel('Number of patents',fontsize = 20)
# plt.title('Number of patents by years',fontsize = 20)
# plt.xticks(fontsize = 18)
# plt.yticks(fontsize = 20)
# #plt.legend(fontsize =15)
# plt.xlabel('Year', fontsize =20)
# for ind, label in enumerate(plt_.get_xticklabels()):
#     if ind % 5 == 0:  # every 10th label is kept
#         label.set_visible(True)
#     else:
#         label.set_visible(False)
# save_png_idx += 1
# plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# fig = plt.figure()
# # %%
# import numpy as np
# subfield_list = ['HCI']
# df_category = pd.read_csv("../data/category.tsv")
# transfer_year = []
# for subfield in subfield_list:
#     df_temp = df_patent_paper_year[df_patent_paper_year['conf_id'].isin(df_category.loc[df_category['subfield']==subfield]['conf_name'].tolist())]
#     print("sunfield {} mean papaer to patent transfer time: {}".format(subfield, np.mean(list(df_temp['patent_paper_lag']))))
#     print("sunfield {} median papaer to patent transfer time: {}".format(subfield, np.median(list(df_temp['patent_paper_lag']))))
#     transfer_year.append(np.mean(list(df_temp['patent_paper_lag'])))

# # %%
# conf_list = ['CHI','CSCW','UBI','UIST']
# df_category = pd.read_csv("../data/category.tsv")
# transfer_year = []
# for conf in conf_list:
#     df_temp = df_patent_paper_year[df_patent_paper_year['conf_id']==conf]
#     print("conference {} mean papaer to patent transfer time: {}".format(conf, np.mean(list(df_temp['patent_paper_lag']))))
#     print("conference {} median papaer to patent transfer time: {}".format(conf, np.median(list(df_temp['patent_paper_lag']))))
#     transfer_year.append(np.mean(list(df_temp['patent_paper_lag'])))

# # # %%
# # # the average lag of science that influence patent
# # sns.pointplot(x="conf_id", y="patent_paper_lag", data=df_patent_paper_year, order = ['CHI','CSCW','UBI','UIST'], join=False)
# # plt.ylabel('Time difference (Year)',fontsize = 20)
# # plt.title('Average influence lags between patent and paper',fontsize = 20)
# # plt.xticks(fontsize = 20)
# # plt.yticks(fontsize = 20)
# # plt.xlabel('')
# # save_png_idx += 1
# # plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# # fig = plt.figure()
# # %%
# # the averaged number of years before first patent citation (facet, paper from different years): NA

# # the average lag of science that influence patent
# df_temp = df_patent_paper_year[df_patent_paper_year['patent_year']>1985]
# plt_ = sns.pointplot(x="patent_year", y="patent_paper_lag", hue="conf_id", data=df_temp)
# plt.ylabel('Time difference (Year)',fontsize = 20)
# plt.title('The average time lag of the paper\n cited by patents in year X',fontsize = 20)
# plt.xticks(rotation=45, fontsize = 20)
# plt.yticks(fontsize = 20)
# plt.ylim(0, 50)
# plt.legend(fontsize =15)
# plt.xlabel('patent year', fontsize =20)
# for ind, label in enumerate(plt_.get_xticklabels()):
#     if ind % 5 == 0:  # every 10th label is kept
#         label.set_visible(True)
#     else:
#         label.set_visible(False)
# save_png_idx += 1
# plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# fig = plt.figure()

# # the median lag of science that influence patent
# df_temp = df_patent_paper_year[df_patent_paper_year['patent_year']>1985]
# plt_ = sns.pointplot(x="patent_year", y="patent_paper_lag", hue="conf_id", data=df_temp, estimator=np.median)
# plt.ylabel('Time difference (Year)',fontsize = 20)
# plt.title('The median time lag of the paper\n cited by patents in year X',fontsize = 20)
# plt.xticks(rotation=45, fontsize = 20)
# plt.yticks(fontsize = 20)
# plt.ylim(0, 50)
# plt.legend(fontsize =15)
# plt.xlabel('patent year', fontsize =20)
# for ind, label in enumerate(plt_.get_xticklabels()):
#     if ind % 5 == 0:  # every 10th label is kept
#         label.set_visible(True)
#     else:
#         label.set_visible(False)
# save_png_idx += 1
# plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# fig = plt.figure()

# # %%
# # the average lag of patent that cite papers in year X
# df_temp = df_patent_paper_year.sort_values('year', ascending = False).reset_index(drop=True)
# df_temp = df_temp[df_temp['year']>1977]
# plt_ = sns.pointplot(x="year", y="patent_paper_lag", hue="conf_id", data=df_temp)
# plt.ylabel('Time difference (Year)',fontsize = 20)
# plt.title('The average time lag of patent\n that cite papers in year X',fontsize = 20)
# plt.xticks(rotation=90)
# plt.xticks(rotation=45, fontsize = 20)
# plt.legend(fontsize =15)
# plt.xlabel('paper year', fontsize =15)
# plt.yticks(fontsize = 20)
# for ind, label in enumerate(plt_.get_xticklabels()):
#     if ind % 5 == 0:  # every 10th label is kept
#         label.set_visible(True)
#     else:
#         label.set_visible(False)
# save_png_idx += 1
# plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# fig = plt.figure()

# # the median lag of patent that cite papers in year X
# df_temp = df_patent_paper_year.sort_values('year', ascending = False).reset_index(drop=True)
# df_temp = df_temp[df_temp['year']>1977]
# plt_ = sns.pointplot(x="year", y="patent_paper_lag", hue="conf_id", data=df_temp, estimator=np.median)
# plt.ylabel('Time difference (Year)',fontsize = 20)
# plt.title('The median time lag of patent\n that cite papers in year X',fontsize = 20)
# plt.xticks(rotation=90)
# plt.xticks(rotation=45, fontsize = 20)
# plt.legend(fontsize =15)
# plt.xlabel('paper year', fontsize =15)
# plt.yticks(fontsize = 20)
# for ind, label in enumerate(plt_.get_xticklabels()):
#     if ind % 5 == 0:  # every 10th label is kept
#         label.set_visible(True)
#     else:
#         label.set_visible(False)
# save_png_idx += 1
# plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# fig = plt.figure()

# # %%
# # Average influence lags between patent and paper
# sns.pointplot(x="conf_id", y="patent_paper_lag", data=df_patent_paper_year, join=False)
# plt.ylabel('Time difference (Year)',fontsize = 20)
# plt.title('Average influence lags between patent and paper',fontsize = 20)
# plt.xticks(fontsize = 20)
# plt.yticks(fontsize = 20)
# plt.xlabel('')
# save_png_idx += 1
# plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# fig = plt.figure()

# # Median influence lags between patent and paper
# sns.pointplot(x="conf_id", y="patent_paper_lag", data=df_patent_paper_year, join=False, estimator=np.median)
# plt.ylabel('Time difference (Year)',fontsize = 20)
# plt.title('Median influence lags between patent and paper',fontsize = 20)
# plt.xticks(fontsize = 20)
# plt.yticks(fontsize = 20)
# plt.xlabel('')
# save_png_idx += 1
# plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# fig = plt.figure()

# # %%
# # Average transfer lags (grouped by patents)
# df_temp = df_patent_paper_year.groupby(['patent_id','patent_year','conf_id'])['patent_paper_lag'].agg('min').reset_index()
# sns.pointplot(x="conf_id", y="patent_paper_lag", data=df_temp, order = ['CHI','CSCW','UBI','UIST'], join=False)
# plt.ylabel('Time difference (Year)',fontsize = 20)
# plt.title('Average transfer lags (grouped by patents)',fontsize = 20)
# plt.xticks(fontsize = 20)
# plt.yticks(fontsize = 20)
# plt.xlabel('')
# save_png_idx += 1
# plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# fig = plt.figure()
# # Median transfer lags (grouped by patents)
# df_temp = df_patent_paper_year.groupby(['patent_id','patent_year','conf_id'])['patent_paper_lag'].agg('min').reset_index()
# sns.pointplot(x="conf_id", y="patent_paper_lag", data=df_temp, order = ['CHI','CSCW','UBI','UIST'], join=False, estimator=np.median)
# plt.ylabel('Time difference (Year)',fontsize = 20)
# plt.title('Median transfer lags (grouped by patents)',fontsize = 20)
# plt.xticks(fontsize = 20)
# plt.yticks(fontsize = 20)
# plt.xlabel('')
# save_png_idx += 1
# plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# fig = plt.figure()
# # %%
# # Average transfer lags (grouped by papers)
# df_temp = df_patent_paper_year.groupby(['magid','patent_year','conf_id'])['patent_paper_lag'].agg('min').reset_index()
# sns.pointplot(x="conf_id", y="patent_paper_lag", data=df_temp, order = ['CHI','CSCW','UBI','UIST'], join=False)
# plt.ylabel('Time difference (Year)',fontsize = 20)
# plt.title('Average transfer lags (grouped by papers)',fontsize = 20)
# plt.xticks(fontsize = 20)
# plt.yticks(fontsize = 20)
# plt.xlabel('')
# save_png_idx += 1
# plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# fig = plt.figure()
# # Median transfer lags (grouped by papers)
# df_temp = df_patent_paper_year.groupby(['magid','patent_year','conf_id'])['patent_paper_lag'].agg('min').reset_index()
# sns.pointplot(x="conf_id", y="patent_paper_lag", data=df_temp, order = ['CHI','CSCW','UBI','UIST'], join=False, estimator=np.median)
# plt.ylabel('Time difference (Year)',fontsize = 20)
# plt.title('Median transfer lags (grouped by papers)',fontsize = 20)
# plt.xticks(fontsize = 20)
# plt.yticks(fontsize = 20)
# plt.xlabel('')
# save_png_idx += 1
# plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# fig = plt.figure()

# # %%
# # The time lag of the most recent paper cited by patents in year X
# df_temp = df_patent_paper_year.groupby(['patent_id','patent_year','conf_id'])['patent_paper_lag'].agg('min').reset_index()
# df_temp = df_temp[df_temp['patent_year']>1985]
# plt_ = sns.pointplot(x="patent_year", y="patent_paper_lag", hue="conf_id", data=df_temp)
# plt.ylabel('Time difference (Year)',fontsize = 20)
# plt.title('The time lag of the most recent paper\n cited by patents in year X',fontsize = 20)
# plt.xticks(rotation=45, fontsize = 20)
# plt.yticks(fontsize = 20)
# plt.ylim(0, 50)
# plt.legend(fontsize =15)
# plt.xlabel('patent year', fontsize =20)
# for ind, label in enumerate(plt_.get_xticklabels()):
#     if ind % 5 == 0:  # every 10th label is kept
#         label.set_visible(True)
#     else:
#         label.set_visible(False)
# save_png_idx += 1
# plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# fig = plt.figure()
# # %%
# # the first patent that adopts a paper
# df_temp = df_patent_paper_year.groupby(['magid','year',"conf_id"])['patent_paper_lag'].agg('min').reset_index()
# df_temp = df_temp[df_temp['year']>1977]
# plt_ = sns.pointplot(x="year", y="patent_paper_lag", hue="conf_id", data=df_temp)
# plt.ylabel('Time difference (Year)',fontsize = 20)
# plt.title('The time lag of the first patent\n that cite papers in year X',fontsize = 20)
# plt.xticks(rotation=45, fontsize = 20)
# plt.legend(fontsize =15)
# plt.xlabel('paper year', fontsize =15)
# plt.yticks(fontsize = 20)
# for ind, label in enumerate(plt_.get_xticklabels()):
#     if ind % 5 == 0:  # every 10th label is kept
#         label.set_visible(True)
#     else:
#         label.set_visible(False)
# save_png_idx += 1
# plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# fig = plt.figure()
# # %%
# ## Plot aggregate average times a paper gets transferred to patents 
# ## Only consider papers that get transferred
# font = {'size'   : 18}
# patent_CHI_year = pd.DataFrame({'count': df_patent_paper_year.loc[df_patent_paper_year['conf_id']=="CHI"].groupby(['year','magid'])['patent_id'].count()}).reset_index()
# patent_CSCW_year = pd.DataFrame({'count': df_patent_paper_year.loc[df_patent_paper_year['conf_id']=="CSCW"].groupby(['year','magid'])['patent_id'].count()}).reset_index()
# patent_UBI_year = pd.DataFrame({'count': df_patent_paper_year.loc[df_patent_paper_year['conf_id']=="UBI"].groupby(['year','magid'])['patent_id'].count()}).reset_index()
# patent_UIST_year = pd.DataFrame({'count': df_patent_paper_year.loc[df_patent_paper_year['conf_id']=="UIST"].groupby(['year','magid'])['patent_id'].count()}).reset_index()
# f_CHI = patent_CHI_year['count'].sum()/len(patent_CHI_year[patent_CHI_year['count']>0])
# f_CSCW = patent_CSCW_year['count'].sum()/len(patent_CSCW_year[patent_CSCW_year['count']>0])
# f_UBI = patent_UBI_year['count'].sum()/len(patent_UBI_year[patent_UBI_year['count']>0])
# f_UIST = patent_UIST_year['count'].sum()/len(patent_UIST_year[patent_UIST_year['count']>0])

# prop = [f_CHI, f_CSCW, f_UBI, f_UIST]
# bars = ('CHI', 'CSCW', 'UBI', 'UIST')
# plt.bar(bars, prop, color=['red', 'blue', 'green', 'cyan'])
# plt.title('Average frequency a paper appears in patent', fontsize=18)
# plt.ylabel('Frequency', fontsize=18)
# plt.rc('font', **font)

# save_png_idx += 1
# plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# fig = plt.figure()
# # %%
# ## Plot aggregate average number of times a paper gets transferred to patents per year 
# f_CHI_year = patent_CHI_year[patent_CHI_year['count']>0].groupby('year')['count'].sum()/ patent_CHI_year[patent_CHI_year['count']>0].groupby('year')['count'].count()
# f_CSCW_year = patent_CSCW_year[patent_CSCW_year['count']>0].groupby('year')['count'].sum()/ patent_CSCW_year[patent_CSCW_year['count']>0].groupby('year')['count'].count()
# f_UBI_year = patent_UBI_year[patent_UBI_year['count']>0].groupby('year')['count'].sum()/ patent_UBI_year[patent_UBI_year['count']>0].groupby('year')['count'].count()
# f_UIST_year = patent_UIST_year[patent_UIST_year['count']>0].groupby('year')['count'].sum()/ patent_UIST_year[patent_UIST_year['count']>0].groupby('year')['count'].count()

# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
# plt.xlim([1960,2020])
# plt.xlabel('Year', fontsize = 18)
# plt.ylabel('Frequency', fontsize = 18)
# plt.title('Average frequency of papers transferred to patents by year(paper year)', fontsize = 18)
# plt.plot(f_CHI_year.index, f_CHI_year, 'o-', label = 'CHI', color = 'red', linewidth = 3)
# plt.plot(f_CSCW_year.index, f_CSCW_year, 'o-', label = 'CSCW', color = 'blue', linewidth = 3)
# plt.plot(f_UBI_year.index, f_UBI_year, 'o-', label = 'UBI', color = 'green', linewidth = 3)
# plt.plot(f_UIST_year.index, f_UIST_year, 'o-', label = 'UIST', color = 'cyan', linewidth = 3)
# plt.legend(loc = 'upper left')
# plt.rc('font', **font)
# # plt.show()
# save_png_idx += 1
# plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# fig = plt.figure()

# # %%
# patent_CHI_freq = patent_CHI_year
# sns.distplot(patent_CHI_freq['count'],kde=False)
# plt.yscale('log')
# plt.xlabel('Citation count', fontsize = 18)
# plt.ylabel('Number of papers', fontsize = 18)
# plt.title('Distribution of CHI paper transfer frequency')
# save_png_idx += 1
# plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# fig = plt.figure()
# # %%
# patent_CSCW_freq = patent_CSCW_year
# sns.distplot(patent_CSCW_freq['count'],kde=False)
# plt.yscale('log')
# plt.xlabel('Citation count', fontsize = 18)
# plt.ylabel('Number of papers', fontsize = 18)
# plt.title('Distribution of CSCW paper transfer frequency')
# save_png_idx += 1
# plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# fig = plt.figure()
# # %%
# patent_UBI_freq = patent_UBI_year
# sns.distplot(patent_UBI_freq['count'],kde=False)
# plt.yscale('log')
# plt.xlabel('Citation count', fontsize = 18)
# plt.ylabel('Number of papers', fontsize = 18)
# plt.title('Distribution of UBI paper transfer frequency')
# save_png_idx += 1
# plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# fig = plt.figure()
# # %%
# patent_UIST_freq = patent_UIST_year
# sns.distplot(patent_UIST_freq['count'],kde=False)
# plt.yscale('log')
# plt.xlabel('Citation count', fontsize = 18)
# plt.ylabel('Number of papers', fontsize = 18)
# plt.title('Distribution of UIST paper transfer frequency')
# save_png_idx += 1
# plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# fig = plt.figure()


# # %%
# from string import ascii_letters
# import numpy as np
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import palettable

# year_data = np.random.random((31,31))
# accu_year_data = np.random.random((31,31))
# for year_x in range(1989,2020):
#     for year_y in range(1989,2020):
#         df_x = df_patent_paper_year[(df_patent_paper_year['patent_year'] == year_x)].drop_duplicates(['magid'])
#         df_y = df_patent_paper_year[(df_patent_paper_year['patent_year'] == year_y)].drop_duplicates(['magid'])
#         df_intersected = pd.merge(df_x, df_y, on=['magid'], how='inner')
#         dup_cnt = df_intersected.shape[0]
#         x_cnt = df_x.shape[0]
#         y_cnt = df_y.shape[0]
#         year_data[year_x-1989][year_y-1989] = dup_cnt / x_cnt if x_cnt > 0 else 0
        
#         accu_df_x = df_patent_paper_year[(df_patent_paper_year['patent_year'] == year_x)].drop_duplicates(['magid'])
#         accu_df_y = df_patent_paper_year[(df_patent_paper_year['patent_year'] <= year_y)].drop_duplicates(['magid'])
#         accu_df_intersected = pd.merge(accu_df_x, accu_df_y, on=['magid'], how='inner')
#         accu_dup_cnt = accu_df_intersected.shape[0]
#         accu_x_cnt = accu_df_x.shape[0]
#         accu_y_cnt = accu_df_y.shape[0]
#         accu_year_data[year_x-1989][year_y-1989] = accu_dup_cnt / accu_x_cnt if accu_x_cnt > 0 else 0

# x_tick=[year for year in range(1989,2020)]
# y_tick=[year for year in range(1989,2020)]
# dcorr=pd.DataFrame(year_data,index=y_tick,columns=x_tick)

# plt.figure(figsize=(11, 9),dpi=100)
# sns.heatmap(data=dcorr,
#             vmax=1, 
#             cmap=palettable.cmocean.diverging.Curl_10.mpl_colors,
#             annot=True,#图中数字文本显示
#             fmt=".2f",#格式化输出图中数字，即保留小数位数等
#             annot_kws={'size':5,'weight':'normal', 'color':'#253D24'},#数字属性设置，例如字号、磅值、颜色            
#            )
# save_png_idx += 1
# plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# fig = plt.figure()
# accu_dcorr=pd.DataFrame(accu_year_data,index=y_tick,columns=x_tick)
# plt.figure(figsize=(11, 9),dpi=100)
# sns.heatmap(data=accu_dcorr,
#             vmax=1, 
#             cmap=palettable.cmocean.diverging.Curl_10.mpl_colors,
#             annot=True,
#             fmt=".2f",
#             annot_kws={'size':5,'weight':'normal', 'color':'#253D24'},
#             mask=np.triu(np.ones_like(dcorr,dtype=np.bool))#显示对脚线下面部分图，accumulative时，对角线上方皆为0
#            )
# save_png_idx += 1
# plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# fig = plt.figure()
# # %%
# from string import ascii_letters
# import numpy as np
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import palettable

# year_data = np.random.random((31,31))
# accu_year_data = np.random.random((31,31))
# for conf_id in ['CHI', 'CSCW', 'UBI', 'UIST']:
#     df_conf = df_patent_paper_year[(df_patent_paper_year['conf_id'] == conf_id)]
#     for year_x in range(1989,2020):
#         for year_y in range(1989,2020):
#             df_x = df_conf[(df_conf['patent_year'] == year_x)].drop_duplicates(['magid'])
#             df_y = df_conf[(df_conf['patent_year'] == year_y)].drop_duplicates(['magid'])
#             df_intersected = pd.merge(df_x, df_y, on=['magid'], how='inner')
#             dup_cnt = df_intersected.shape[0]
#             x_cnt = df_x.shape[0]
#             y_cnt = df_y.shape[0]
#             year_data[year_x-1989][year_y-1989] = dup_cnt / x_cnt if x_cnt > 0 else 0
            
#             accu_df_x = df_conf[(df_conf['patent_year'] == year_x)].drop_duplicates(['magid'])
#             accu_df_y = df_conf[(df_conf['patent_year'] <= year_y)].drop_duplicates(['magid'])
#             accu_df_intersected = pd.merge(accu_df_x, accu_df_y, on=['magid'], how='inner')
#             accu_dup_cnt = accu_df_intersected.shape[0]
#             accu_x_cnt = accu_df_x.shape[0]
#             accu_y_cnt = accu_df_y.shape[0]
#             accu_year_data[year_x-1989][year_y-1989] = accu_dup_cnt / accu_x_cnt if accu_x_cnt > 0 else 0

#     x_tick=[year for year in range(1989,2020)]
#     y_tick=[year for year in range(1989,2020)]
#     dcorr=pd.DataFrame(year_data,index=y_tick,columns=x_tick)

#     plt.figure(figsize=(11, 9),dpi=100)
#     plt.title("overlap map conf by venue {}".format(conf_id))
#     sns.heatmap(data=dcorr,
#                 vmax=1, 
#                 cmap=palettable.cmocean.diverging.Curl_10.mpl_colors,
#                 annot=True,#图中数字文本显示
#                 fmt=".2f",#格式化输出图中数字，即保留小数位数等
#                 annot_kws={'size':5,'weight':'normal', 'color':'#253D24'},#数字属性设置，例如字号、磅值、颜色            
#                )
#     plt.title("overlap map conf accumulate by venue {}".format(conf_id))

#     accu_dcorr=pd.DataFrame(accu_year_data,index=y_tick,columns=x_tick)
#     plt.figure(figsize=(11, 9),dpi=100)
#     sns.heatmap(data=accu_dcorr,
#                 vmax=1, 
#                 cmap=palettable.cmocean.diverging.Curl_10.mpl_colors,
#                 annot=True,
#                 fmt=".2f",
#                 annot_kws={'size':5,'weight':'normal', 'color':'#253D24'},
#                 mask=np.triu(np.ones_like(dcorr,dtype=np.bool))#显示对脚线下面部分图，accumulative时，对角线上方皆为0
#                )
# save_png_idx += 1
# plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# fig = plt.figure()
# # %%
# ## Plot aggregate average number of times a paper gets transferred to patents per year
# patent_CHI_year = pd.DataFrame({'count': df_patent_paper_year.loc[df_patent_paper_year['conf_id']=="CHI"].groupby(['patent_paper_lag','magid'])['patent_id'].count()}).reset_index()
# patent_CSCW_year = pd.DataFrame({'count': df_patent_paper_year.loc[df_patent_paper_year['conf_id']=="CSCW"].groupby(['patent_paper_lag','magid'])['patent_id'].count()}).reset_index()
# patent_UBI_year = pd.DataFrame({'count': df_patent_paper_year.loc[df_patent_paper_year['conf_id']=="UBI"].groupby(['patent_paper_lag','magid'])['patent_id'].count()}).reset_index()
# patent_UIST_year = pd.DataFrame({'count': df_patent_paper_year.loc[df_patent_paper_year['conf_id']=="UIST"].groupby(['patent_paper_lag','magid'])['patent_id'].count()}).reset_index()

# f_CHI_year = patent_CHI_year[patent_CHI_year['count']>0].groupby('patent_paper_lag')['count'].sum()/ patent_CHI_year[patent_CHI_year['count']>0]['count'].sum()
# f_CSCW_year = patent_CSCW_year[patent_CSCW_year['count']>0].groupby('patent_paper_lag')['count'].sum()/ patent_CSCW_year[patent_CSCW_year['count']>0]['count'].sum()
# f_UBI_year = patent_UBI_year[patent_UBI_year['count']>0].groupby('patent_paper_lag')['count'].sum()/ patent_UBI_year[patent_UBI_year['count']>0]['count'].sum()
# f_UIST_year = patent_UIST_year[patent_UIST_year['count']>0].groupby('patent_paper_lag')['count'].sum()/ patent_UIST_year[patent_UIST_year['count']>0]['count'].sum()

# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
# plt.xlim([0,40])
# plt.xlabel('Paper Age', fontsize = 18)
# plt.ylabel('Frequency', fontsize = 18)
# plt.title('Average frequency of papers transferred to patents by age(paper age)', fontsize = 18)
# plt.plot(f_CHI_year.index, f_CHI_year, 'o-', label = 'CHI', color = 'red', linewidth = 3)
# plt.plot(f_CSCW_year.index, f_CSCW_year, 'o-', label = 'CSCW', color = 'blue', linewidth = 3)
# plt.plot(f_UBI_year.index, f_UBI_year, 'o-', label = 'UBI', color = 'green', linewidth = 3)
# plt.plot(f_UIST_year.index, f_UIST_year, 'o-', label = 'UIST', color = 'cyan', linewidth = 3)
# plt.legend(loc = 'upper left')
# plt.rc('font', **font)
# # plt.show()
# save_png_idx += 1
# plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# fig = plt.figure()


# # %%
# ## Plot aggregate average number of times a paper gets transferred to patents per year
# patent_CHI_year = pd.DataFrame({'count': df_patent_paper_year.loc[df_patent_paper_year['conf_id']=="CHI"].groupby(['patent_paper_lag','magid'])['patent_id'].count()}).reset_index()
# patent_CSCW_year = pd.DataFrame({'count': df_patent_paper_year.loc[df_patent_paper_year['conf_id']=="CSCW"].groupby(['patent_paper_lag','magid'])['patent_id'].count()}).reset_index()
# patent_UBI_year = pd.DataFrame({'count': df_patent_paper_year.loc[df_patent_paper_year['conf_id']=="UBI"].groupby(['patent_paper_lag','magid'])['patent_id'].count()}).reset_index()
# patent_UIST_year = pd.DataFrame({'count': df_patent_paper_year.loc[df_patent_paper_year['conf_id']=="UIST"].groupby(['patent_paper_lag','magid'])['patent_id'].count()}).reset_index()

# f_CHI_year = patent_CHI_year[patent_CHI_year['count']>0].groupby(['patent_paper_lag'])['count'].sum()/ patent_CHI_year[patent_CHI_year['count']>0].groupby(['patent_paper_lag'])['count'].count()
# f_CSCW_year = patent_CSCW_year[patent_CSCW_year['count']>0].groupby('patent_paper_lag')['count'].sum()/ patent_CSCW_year[patent_CSCW_year['count']>0].groupby('patent_paper_lag')['count'].count()
# f_UBI_year = patent_UBI_year[patent_UBI_year['count']>0].groupby('patent_paper_lag')['count'].sum()/ patent_UBI_year[patent_UBI_year['count']>0].groupby('patent_paper_lag')['count'].count()
# f_UIST_year = patent_UIST_year[patent_UIST_year['count']>0].groupby('patent_paper_lag')['count'].sum()/ patent_UIST_year[patent_UIST_year['count']>0].groupby('patent_paper_lag')['count'].count()

# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
# plt.xlim([0,40])
# plt.xlabel('Paper Age', fontsize = 18)
# plt.ylabel('Frequency', fontsize = 18)
# plt.title('Average patent impact of papers transferred to patents by age(paper age)', fontsize = 18)
# plt.plot(f_CHI_year.index, f_CHI_year, 'o-', label = 'CHI', color = 'red', linewidth = 3)
# plt.plot(f_CSCW_year.index, f_CSCW_year, 'o-', label = 'CSCW', color = 'blue', linewidth = 3)
# plt.plot(f_UBI_year.index, f_UBI_year, 'o-', label = 'UBI', color = 'green', linewidth = 3)
# plt.plot(f_UIST_year.index, f_UIST_year, 'o-', label = 'UIST', color = 'cyan', linewidth = 3)
# plt.legend(loc = 'upper left')
# plt.rc('font', **font)
# # plt.show()
# save_png_idx += 1
# plt.savefig('../paper_report_figure/fig_{}.png'.format(save_png_idx))
# fig = plt.figure()


# # %%
# #------------ analyze popular transferred paper -------------#

# CHI_pd = pd.read_csv("../dataAug10/mergeversiondata/paperciting_CHI.tsv", sep=',')
# CSCW_pd = pd.read_csv("../dataAug10/mergeversiondata/paperciting_CSCW.tsv", sep=',')
# UIST_pd = pd.read_csv("../dataAug10/mergeversiondata/paperciting_UIST.tsv", sep=',')
# UBI_pd = pd.read_csv("../dataAug10/mergeversiondata/paperciting_UbiComp.tsv", sep=',')

# CHI_pcs_pd = pd.read_csv("../dataAug10/mergeversiondata/papercitationscience_CHI.tsv", sep=',')
# CSCW_pcs_pd = pd.read_csv("../dataAug10/mergeversiondata/papercitationscience_CSCW.tsv", sep=',')
# UIST_pcs_pd = pd.read_csv("../dataAug10/mergeversiondata/papercitationscience_UIST.tsv", sep=',')
# UBI_pcs_pd = pd.read_csv("../dataAug10/mergeversiondata/papercitationscience_UbiComp.tsv", sep=',')
# pcs_pd_list = [CHI_pcs_pd, CSCW_pcs_pd, UIST_pcs_pd, UBI_pcs_pd]
# pd_list = [CHI_pd, CSCW_pd, UIST_pd, UBI_pd]

# for idx in range(4):
#     citation_pd = pd_list[idx]
#     cited_paper_num = {}
#     cited_patent_num = {}
#     for row in citation_pd.iterrows():
#         # citing_paperid_str = str(row["citingpaperid"])
#         # cited_paperid_str = str(row["citedpaperid"])
#         citing_paperid_str = str(row).split()[3] # paperid
#         cited_paperid_str = str(row).split()[4]
#         if cited_paperid_str in cited_paper_num.keys():
#             cited_paper_num[cited_paperid_str] += 1
#         else:
#             cited_paper_num[cited_paperid_str] = 1
#     result = []
#     paperid_list = []
#     # print(cited_paper_num)
#     pcs_pd = pcs_pd_list[idx]
#     for row in pcs_pd.iterrows():
#         paperid = str(row).split()[9]
#         patentid = str(row).split()[11]
#         paperid_list.append(paperid)
#         if paperid in cited_patent_num.keys():
#             cited_patent_num[paperid] += 1
#         else:
#             cited_patent_num[paperid] = 1
#     for k, v in cited_paper_num.items():
#         if k not in cited_patent_num.keys():
#             cited_patent_num[k] = 0                
#         result.append(list([k, str(cited_paper_num[k]), str(cited_patent_num[k])]))
#     result_pd = pd.DataFrame(data=result, columns=['magid', 'citedbypapers', 'citedbypatents'])
#     result_pd.to_csv('popular_transferred_paper{}.tsv'.format(idx))

# # %%
