import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from icecream import ic
import pickle
import seaborn as sns

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

import pandas as pd
df_patent_paper_year = pd.read_csv("../dataAug10/mergeversiondata/df_patent_paper_year.tsv")

df_temp = df_patent_paper_year.groupby(['conf_id','patent_id','patent_year']).agg('count').reset_index()
df_temp = df_temp[['conf_id','patent_id','patent_year']]
df_temp = df_temp.groupby(['conf_id','patent_year']).agg('count').reset_index()

# df_temp2 = df_patent_paper_year.groupby(['conf_id','magid','year']).agg('count').reset_index()
# df_temp2 = df_temp2[['conf_id','magid','year']]
# df_temp2 = df_temp2.groupby(['conf_id','year']).agg('count').reset_index()

def get_conf_name(x):
    if str(x) == "1163450153": return "CHI"
    if str(x) == "1195049314": return "CSCW"
    if str(x) == "1166315290": return "UIST"
    if str(x) == "1171345118": return "UBI"
    return x


df_paper_year = df_paper_year.replace(1163450153, "CHI_papers").replace(1195049314, "CSCW_papers").replace(1166315290, "UIST_papers").replace(1171345118, "UBI_papers")
for conf_name in ["CHI", "CSCW", "UIST", "UBI"]:
    df_temp_paper = df_paper_year[df_paper_year["conf_id"] == conf_name+"_papers"].groupby(['conf_id','paper_id','year']).agg('count').reset_index()
    df_temp_paper = df_temp_paper[['conf_id','paper_id','year']]
    df_temp_paper = df_temp_paper.groupby(['conf_id','year']).agg('count').reset_index()
    

    df_temp = df_patent_paper_year.groupby(['conf_id','patent_id','patent_year']).agg('count').reset_index()
    df_temp = df_temp[['conf_id','patent_id','patent_year']]
    df_temp = df_temp.groupby(['conf_id','patent_year']).agg('count').reset_index()
    df_temp = df_temp[df_temp["conf_id"] == conf_name][(df_temp['patent_year']>=1985) & (df_temp['patent_year']<2020)]
    # df_temp2 = df_temp2[(df_temp2['year']>=1985) & (df_temp2['year']<=2020)]
    df_temp_paper = df_temp_paper[(df_temp_paper['year']>=1985) & (df_temp_paper['year']<2020)]
    plt_ = sns.pointplot(x="patent_year", y="patent_id", hue="conf_id", data=df_temp)
    # plt_ = sns.pointplot(x="year", y="magid", hue="conf_id", data=df_temp2, markers="*")
    plt_ = sns.pointplot(x="year", y="paper_id", hue="conf_id", data=df_temp_paper, markers="*")
    plt.ylabel('Number of patents/papers',fontsize = 20)
    plt.title('Number of patents/papers by years',fontsize = 20)
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
    plt.savefig('../slides_report_figure/{}_fig_{}.png'.format(conf_name, save_png_idx))
    fig = plt.figure()