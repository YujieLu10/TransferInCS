import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from icecream import ic
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

save_png_idx = 0
# conf_key = {'CHI':1163450153, 'CSCW':1195049314, 'UIST':1166315290, 'UbiComp':1171345118}

# with open('paperyear_map_conf.pickle', 'rb') as handle:
#     paperyear_map_conf = pickle.load(handle)

# with open('inv_paperyear_map_conf.pickle', 'rb') as handle:
#     inv_paperyear_map_conf = pickle.load(handle)
    
# with open('citingpatent_map_conf.pickle', 'rb') as handle:
#     citingpatent_map_conf = pickle.load(handle)
    
# with open('citedpaper_map_conf.pickle', 'rb') as handle:
#     citedpaper_map_conf = pickle.load(handle)
    
# with open('citingpaper_map_conf.pickle', 'rb') as handle:
#     citingpaper_map_conf = pickle.load(handle)
    
# with open('single_citingpaper_map_conf.pickle', 'rb') as handle:
#     single_citingpaper_map_conf = pickle.load(handle)
    
# with open('single_citingpatent_map_conf.pickle', 'rb') as handle:
#     single_citingpatent_map_conf = pickle.load(handle)

# with open('citedpaper_list_conf.pickle', 'rb') as handle:
#     citedpaper_list_conf = pickle.load(handle)

# ic(len(citedpaper_map_conf['CHI']))
# ic(len(paperyear_map_conf['CHI']))


# # plt.savefig('../final_paper_report_figure/fig_{}.png'.format(save_png_idx))

# # ===================
# data_HCI = pd.read_csv('sigchi_paperids.tsv',sep='\t')
# conf_paper_list = data_HCI['paperid'].tolist()

# data_pcs = pd.read_csv('pcs_mag_doi_pmid.tsv',sep='\t')

# data_pcs = data_pcs.loc[data_pcs["magid"].isin(conf_paper_list)]

# ic(len(data_pcs)) # 42822458; 83792
# # data_pcs = data_pcs[(data_pcs["wherefound"] == "bodyonly") | (data_pcs["wherefound"] == "both")]
# # ic(len(data_pcs)) # 17523031; 3859
# data_pcs = data_pcs.groupby(["patent"]).first().reset_index()
# data_pcs = data_pcs.drop_duplicates()
# ic(len(data_pcs)) # 3022924; 1344
# # # ===================
# data_pcs.to_csv("df_patent_paper_year_sigchi_allpatent.tsv")

# ===================
data_HCI = pd.read_csv('sigchi_paperids.tsv',sep='\t')
conf_paper_list = data_HCI['paperid'].tolist()

data_pcs = pd.read_csv('pcs_mag_doi_pmid.tsv',sep='\t')

data_pcs = data_pcs.loc[data_pcs["magid"].isin(conf_paper_list)]

ic(len(data_pcs)) # 42822458; 83792
data_pcs = data_pcs.drop_duplicates()
# # ===================
data_pcs.to_csv("df_patent_paper_year_sigchi_all.tsv")

# # ==========
# data_HCI = pd.read_csv('sigchi_paperids.tsv',sep='\t')
# data_HCI = pd.read_csv('HCI_paperids.tsv',sep='\t')
# conf_paper_list = data_HCI['paperid'].tolist()

# data_pcs = pd.read_csv('pcs_mag_doi_pmid.tsv',sep='\t')

# data_pcs = data_pcs.loc[data_pcs["magid"].isin(conf_paper_list)]
# data_pcs.to_csv("df_patent_paper_year_hci_all.tsv")
# # ==========

# df_patent_year = pd.read_csv('../dataAug10/rawdata/patent_year_inventor.tsv')[['date', 'patent_id']]
# df_patent_year['patent_year'] = pd.DatetimeIndex(df_patent_year['date']).year
# df_patent_year['patent_id'] = df_patent_year['patent_id'].astype(str)

# df_patent_paper_year = pd.read_csv("df_patent_paper_year_sigchi_allpatent.tsv") #pd.read_csv("df_patent_paper_year_filtered.tsv")
# df_patent_paper_year = df_patent_paper_year.drop_duplicates()

# def get_patentid(x):
#     x = x[x.index("-")+1:]
#     if "-" in x:
#         return x[:x.index("-")]
#     else:
#         return x
    
# df_patent_paper_year['patent'] = df_patent_paper_year['patent'].apply(get_patentid)
# df_patent_paper_year['patent'] = df_patent_paper_year['patent'].astype(str)

# df_patent_paper_year = df_patent_paper_year.merge(df_patent_year, left_on='patent', right_on='patent_id')
# df_patent_paper_year = df_patent_paper_year.drop_duplicates()
# ic(len(df_patent_paper_year))
# # %%
# # related patents over year
# df_patent_paper_year['conf_id'] = "SIGCHI"
# df_temp = df_patent_paper_year.groupby(['conf_id', 'patent_id','patent_year']).agg('count').reset_index()
# df_temp = df_temp[['conf_id', 'patent_id','patent_year']]
# df_temp = df_temp.groupby(['conf_id', 'patent_year']).agg('count').reset_index()

# # df_temp = df_temp[(df_temp['patent_year']!=2001)]
# df_temp = df_temp[(df_temp['patent_year']>=1989) & (df_temp['patent_year']<=2018)]
# # hue="conf_id",

# plt_ = sns.lineplot(x="patent_year", y="patent_id", hue="conf_id", data=df_temp, palette="Accent")
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
# plt.savefig('fig_{}.png'.format(save_png_idx), bbox_inches = "tight")
# fig = plt.figure()