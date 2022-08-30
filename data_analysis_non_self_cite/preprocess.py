import pandas as pd
import pickle
from icecream import ic

conf_key = {'CHI':1163450153, 'CSCW':1195049314, 'UBI':1171345118, 'UIST':1166315290}

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
ic(df_paper_pc2s_year.head(2))
df_paper_pc2s_year = df_paper_pc2s_year.drop_duplicates()

for conf_name,conf_id in conf_key.items():
    ori_paperyear_conf[conf_name] = df_paper_year.loc[df_paper_year['conf_id']==conf_id]
    ori_citingpatent_conf[conf_name] = df_paper_pc2s_year.loc[df_paper_pc2s_year['conf_id']==conf_id]
#------------ analyze paper author -------------#
ori_author_conf = {}
# author
df_paper_author = pd.read_csv("df_paper_author.tsv")
for conf_name,conf_id in conf_key.items():
    ori_author_conf[conf_name] = df_paper_author.loc[df_paper_author['conf_id']==conf_id]

paperyear_map_conf = {}
inv_paperyear_map_conf = {}
for conf, df in ori_paperyear_conf.items():
    paperyear_map = {}
    inv_paperyear_map = {}
    for row in df.iterrows():
        paperid = str(row[1]).split(',')[0].split('\n')[1].split()[1] # paperid
        paperyear = str(row[1]).split(',')[0].split('\n')[2].split()[1] # paperyear 
        # ic(paperid, paperyear)
        if paperyear not in paperyear_map.keys():
            paperyear_map[paperyear] = []    
        if paperid not in paperyear_map[paperyear]:
            paperyear_map[paperyear].append(paperid)
        inv_paperyear_map[paperid] = paperyear
    paperyear_map_conf[conf] = paperyear_map
    inv_paperyear_map_conf[conf] = inv_paperyear_map
print(">>> done paper year map construction")

citingpatent_map_conf = {}
citedpaper_map_conf = {}
for conf, df in ori_citingpatent_conf.items():
    citingpatent_map = {}
    citedpaper_map = {}
    inv_paperyear_map = inv_paperyear_map_conf[conf]
    for row in df.iterrows():
        paperid = str(row[1]).split(',')[0].split('\n')[0].split()[1] # paperid
        patentid = str(row[1]).split(',')[0].split('\n')[1].split()[1] # patentid
        # paperyear
        if paperid not in inv_paperyear_map.keys(): continue
        paperyear = inv_paperyear_map[paperid]
        if paperyear not in citingpatent_map.keys():
            citingpatent_map[paperyear] = []
        if paperyear not in citedpaper_map.keys():
            citedpaper_map[paperyear] = []  
        citingpatent_map[paperyear].append(patentid)
        # unique cited paper this year
        if paperid not in citedpaper_map[paperyear]:
            citedpaper_map[paperyear].append(paperid)
    citingpatent_map_conf[conf] = citingpatent_map
    citedpaper_map_conf[conf] = citedpaper_map
print(">>> done citing data")


with open('paperyear_map_conf.pickle', 'wb') as handle:
    pickle.dump(paperyear_map_conf, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('inv_paperyear_map_conf.pickle', 'wb') as handle:
    pickle.dump(inv_paperyear_map_conf, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
with open('citingpatent_map_conf.pickle', 'wb') as handle:
    pickle.dump(citingpatent_map_conf, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
with open('citedpaper_map_conf.pickle', 'wb') as handle:
    pickle.dump(citedpaper_map_conf, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
