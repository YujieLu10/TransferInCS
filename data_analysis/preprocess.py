import pandas as pd
import pickle
from icecream import ic

conf_key = {'CHI':1163450153, 'CSCW':1195049314, 'UBI':1171345118, 'UIST':1166315290}

ori_paperyear_conf = {}
ori_citingpatent_conf = {}


df_paper_year = pd.read_csv("df_paper_year.tsv")
df_paper_pc2s_year = pd.read_csv("df_paper_pc2s_year.tsv")

for conf_name,conf_id in conf_key.items():
    ori_paperyear_conf[conf_name] = df_paper_year.loc[df_paper_year['conf_id']==conf_id]
    ori_citingpatent_conf[conf_name] = df_paper_pc2s_year.loc[df_paper_pc2s_year['conf_id']==conf_id]
#------------ analyze paper author -------------#
ori_author_conf = {}
# author
df_paper_author = pd.read_csv("df_paper_author.tsv")
for conf_name,conf_id in conf_key.items():
    ori_author_conf[conf_name] = df_paper_author.loc[df_paper_author['conf_id']==conf_id]

# %%
citedpaper_list_conf = {}
for conf, df in ori_citingpatent_conf.items():
    citedpaper_list = []
    for row in df.iterrows():
        paperid = str(row[1]).split(',')[0].split('\n')[5].split()[1] # paperid
        # patentid = str(row[1]).split(',')[0].split('\n')[1].split()[1] # patentid
        citedpaper_list.append(paperid)
    citedpaper_list_conf[conf] = citedpaper_list

with open('citedpaper_list_conf.pickle', 'wb') as handle:
    pickle.dump(citedpaper_list_conf, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('inv_paperyear_map_conf.pickle', 'rb') as handle:
    inv_paperyear_map_conf = pickle.load(handle)
    
cited_author_map_conf = {}
notcited_author_map_conf = {}
for conf, df in ori_author_conf.items():
    inv_paperyear_map = inv_paperyear_map_conf[conf]
    cited_author_map = {}
    notcited_author_map = {}
    cited_paper_list = citedpaper_list_conf[conf]
    for row in df.iterrows():
        paperid = str(row[1]).split(',')[0].split('\n')[1].split()[1]
        authorid = str(row[1]).split(',')[0].split('\n')[2].split()[1]
        if paperid not in inv_paperyear_map.keys(): continue
        paperyear = inv_paperyear_map[paperid]
        if paperid in cited_paper_list:
            if paperyear not in cited_author_map.keys():
                cited_author_map[paperyear] = []
            if authorid not in cited_author_map[paperyear]:
                cited_author_map[paperyear].append(authorid)
        else:
            if paperyear not in notcited_author_map.keys():
                notcited_author_map[paperyear] = []
            if authorid not in notcited_author_map[paperyear]:
                notcited_author_map[paperyear].append(authorid)
    cited_author_map_conf[conf] = cited_author_map
    notcited_author_map_conf[conf] = notcited_author_map
print(">>> author map construction done")

with open('cited_author_map_conf.pickle', 'wb') as handle:
    pickle.dump(cited_author_map_conf, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('notcited_author_map_conf.pickle', 'wb') as handle:
    pickle.dump(notcited_author_map_conf, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
# paperyear_map_conf = {}
# inv_paperyear_map_conf = {}
# for conf, df in ori_paperyear_conf.items():
#     paperyear_map = {}
#     inv_paperyear_map = {}
#     for row in df.iterrows():
#         paperid = str(row[1]).split(',')[0].split('\n')[1].split()[1] # paperid
#         paperyear = str(row[1]).split(',')[0].split('\n')[2].split()[1] # paperyear 
#         if paperyear not in paperyear_map.keys():
#             paperyear_map[paperyear] = []    
#         if paperid not in paperyear_map[paperyear]:
#             paperyear_map[paperyear].append(paperid)
#         inv_paperyear_map[paperid] = paperyear
#     paperyear_map_conf[conf] = paperyear_map
#     inv_paperyear_map_conf[conf] = inv_paperyear_map
# print(">>> done paper year map construction")


# citingpatent_map_conf = {}
# citedpaper_map_conf = {}
# for conf, df in ori_citingpatent_conf.items():
#     citingpatent_map = {}
#     citedpaper_map = {}
#     inv_paperyear_map = inv_paperyear_map_conf[conf]
#     for row in df.iterrows():
#         paperid = str(row[1]).split(',')[0].split('\n')[5].split()[1] # paperid
#         patentid = str(row[1]).split(',')[0].split('\n')[6].split()[1] # patentid
#         # paperyear
#         if paperid not in inv_paperyear_map.keys(): continue
#         paperyear = inv_paperyear_map[paperid]
#         if paperyear not in citingpatent_map.keys():
#             citingpatent_map[paperyear] = []
#         if paperyear not in citedpaper_map.keys():
#             citedpaper_map[paperyear] = []  
#         citingpatent_map[paperyear].append(patentid)
#         # unique cited paper this year
#         if paperid not in citedpaper_map[paperyear]:
#             citedpaper_map[paperyear].append(paperid)
#     citingpatent_map_conf[conf] = citingpatent_map
#     citedpaper_map_conf[conf] = citedpaper_map
# print(">>> done citing data")


# with open('paperyear_map_conf.pickle', 'wb') as handle:
#     pickle.dump(paperyear_map_conf, handle, protocol=pickle.HIGHEST_PROTOCOL)

# with open('inv_paperyear_map_conf.pickle', 'wb') as handle:
#     pickle.dump(inv_paperyear_map_conf, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
# with open('citingpatent_map_conf.pickle', 'wb') as handle:
#     pickle.dump(citingpatent_map_conf, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
# with open('citedpaper_map_conf.pickle', 'wb') as handle:
#     pickle.dump(citedpaper_map_conf, handle, protocol=pickle.HIGHEST_PROTOCOL)
    

# df_author = pd.read_csv('../dataAug10/mergeversiondata/paperauthororder.tsv', usecols=[1,2])
# df_author = df_author.drop_duplicates()

# df_paperid = pd.read_csv('../dataAug10/mergeversiondata/HCI_paperids.tsv', sep='\t')
# df_paperid = df_paperid.drop_duplicates()

# df_paper_author = df_author.merge(df_paperid, left_on='paperid', right_on='paper_id')
# df_paper_author.to_csv("df_paper_author.tsv")