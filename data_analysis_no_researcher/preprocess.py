import string
import pandas as pd
import pickle
from icecream import ic

conf_key = {'CHI':1163450153, 'CSCW':1195049314, 'UBI':1171345118, 'UIST':1166315290}

ori_paperyear_conf = {}
ori_citingpatent_conf = {}


patent_id_no_researcher = pd.read_csv("patent_id_no_researcher.csv")
patent_id_no_researcher["patent"] = patent_id_no_researcher["patent"].astype(str)
df_paper_year = pd.read_csv("df_paper_year.tsv")
df_paper_pc2s_year = pd.read_csv("df_paper_pc2s_year.tsv")
df_paper_pc2s_year["patent"] = df_paper_pc2s_year["patent"].astype(str)
ic(len(df_paper_pc2s_year))
df_paper_pc2s_year = df_paper_pc2s_year.merge(patent_id_no_researcher, left_on='patent', right_on='patent')
df_paper_pc2s_year = df_paper_pc2s_year.drop_duplicates()
ic(len(df_paper_pc2s_year))
df_paper_pc2s_year.to_csv("df_paper_pc2s_year_no_researcher.tsv")

for conf_name,conf_id in conf_key.items():
    ori_paperyear_conf[conf_name] = df_paper_year.loc[df_paper_year['conf_id']==conf_id]
    ori_citingpatent_conf[conf_name] = df_paper_pc2s_year.loc[df_paper_pc2s_year['conf_id']==conf_id]
# #------------ analyze paper author -------------#
# ori_author_conf = {}
# # author
# df_paper_author = pd.read_csv("df_paper_author.tsv")
# for conf_name,conf_id in conf_key.items():
#     ori_author_conf[conf_name] = df_paper_author.loc[df_paper_author['conf_id']==conf_id]

# # %%
# citedpaper_list_conf = {}
# for conf, df in ori_citingpatent_conf.items():
#     citedpaper_list = []
#     for row in df.iterrows():
#         paperid = str(row[1]).split(',')[0].split('\n')[5].split()[1] # paperid
#         # patentid = str(row[1]).split(',')[0].split('\n')[1].split()[1] # patentid
#         citedpaper_list.append(paperid)
#     citedpaper_list_conf[conf] = citedpaper_list

# with open('citedpaper_list_conf.pickle', 'wb') as handle:
#     pickle.dump(citedpaper_list_conf, handle, protocol=pickle.HIGHEST_PROTOCOL)

# with open('inv_paperyear_map_conf.pickle', 'rb') as handle:
#     inv_paperyear_map_conf = pickle.load(handle)
    
# cited_author_map_conf = {}
# notcited_author_map_conf = {}
# for conf, df in ori_author_conf.items():
#     inv_paperyear_map = inv_paperyear_map_conf[conf]
#     cited_author_map = {}
#     notcited_author_map = {}
#     cited_paper_list = citedpaper_list_conf[conf]
#     for row in df.iterrows():
#         paperid = str(row[1]).split(',')[0].split('\n')[1].split()[1]
#         authorid = str(row[1]).split(',')[0].split('\n')[2].split()[1]
#         if paperid not in inv_paperyear_map.keys(): continue
#         paperyear = inv_paperyear_map[paperid]
#         if paperid in cited_paper_list:
#             if paperyear not in cited_author_map.keys():
#                 cited_author_map[paperyear] = []
#             if authorid not in cited_author_map[paperyear]:
#                 cited_author_map[paperyear].append(authorid)
#         else:
#             if paperyear not in notcited_author_map.keys():
#                 notcited_author_map[paperyear] = []
#             if authorid not in notcited_author_map[paperyear]:
#                 notcited_author_map[paperyear].append(authorid)
#     cited_author_map_conf[conf] = cited_author_map
#     notcited_author_map_conf[conf] = notcited_author_map
# print(">>> author map construction done")

# with open('cited_author_map_conf.pickle', 'wb') as handle:
#     pickle.dump(cited_author_map_conf, handle, protocol=pickle.HIGHEST_PROTOCOL)

# with open('notcited_author_map_conf.pickle', 'wb') as handle:
#     pickle.dump(notcited_author_map_conf, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
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
with open('inv_paperyear_map_conf.pickle', 'rb') as handle:
    inv_paperyear_map_conf = pickle.load(handle)
df_paperid = pd.read_csv('../dataAug10/mergeversiondata/HCI_paperids.tsv', sep='\t')
df_paperid = df_paperid.drop_duplicates()
# #------------ analyze paper point -------------#
# ori_citingpaper_conf = {}

# df_cited = pd.read_csv('../dataAug10/mergeversiondata/papercited.tsv', usecols=[1,2])
# for conf in ["CHI", "CSCW", "UbiComp", "UIST"]:
#     new_df = pd.read_csv('../dataAug10/mergeversiondata/papercited_{}.tsv'.format(conf), usecols=[3,4])
#     df_cited = df_cited.append(new_df, ignore_index=True)

# df_paper_cited = df_cited.merge(df_paperid, left_on='citedpaperid', right_on='paper_id')
# df_paper_cited = df_paper_cited.drop_duplicates()
# df_paper_cited.to_csv("df_paper_cited.tsv")
# ic(len(df_paper_cited))
# # df_paper_cited.head(3)
# # citing paper
# for conf_name,conf_id in conf_key.items():
#     ori_citingpaper_conf[conf_name] = df_paper_cited.loc[df_paper_cited['conf_id']==conf_id]

ori_citingpaper_conf = {}
df_cited = pd.read_csv('../dataAug10/mergeversiondata/papercited.tsv', usecols=[1,2])
for conf in ["CHI", "CSCW", "UbiComp", "UIST"]:
    new_df = pd.read_csv('../dataAug10/mergeversiondata/papercited_{}.tsv'.format(conf), usecols=[3,4])
    df_cited = df_cited.append(new_df, ignore_index=True)

df_paper_cited = df_cited.merge(df_paperid, left_on='citedpaperid', right_on='paper_id')
df_paper_cited = df_paper_cited.drop_duplicates()
df_paper_cited.to_csv("df_paper_cited.tsv")
# df_paper_cited = pd.read_csv("df_paper_cited.tsv")
ic(len(df_paper_cited))
for conf_name,conf_id in conf_key.items():
    ori_citingpaper_conf[conf_name] = df_paper_cited.loc[df_paper_cited['conf_id']==conf_id]

# %%
citingpaper_map_conf = {}
for conf, df in ori_citingpaper_conf.items():
    citingpaper_map = {}
    inv_paperyear_map = inv_paperyear_map_conf[conf]
    count = 0
    for row in df.iterrows():
        citing_paperid = str(row[1]).split(',')[0].split('\n')[1].split()[1]
        cited_paperid = str(row[1]).split(',')[0].split('\n')[2].split()[1]
        # paperyear
        if cited_paperid not in inv_paperyear_map.keys():
            count += 1
            continue
        paperyear = inv_paperyear_map[cited_paperid]
        if paperyear not in citingpaper_map.keys():
            citingpaper_map[paperyear] = []
        citingpaper_map[paperyear].append(citing_paperid)
    citingpaper_map_conf[conf] = citingpaper_map
    ic(len(citingpaper_map_conf[conf]))
print(">>> citing paper map construction done; count {}".format(count))

with open('citingpaper_map_conf.pickle', 'wb') as handle:
    pickle.dump(citingpaper_map_conf, handle, protocol=pickle.HIGHEST_PROTOCOL)

# % ====
ori_citingpaper_conf = {}
df_paper_cited = pd.read_csv("df_paper_cited.tsv")
ic(len(df_paper_cited))
for conf_name,conf_id in conf_key.items():
    ori_citingpaper_conf[conf_name] = df_paper_cited.loc[df_paper_cited['conf_id']==conf_id]

with open('citedpaper_list_conf.pickle', 'rb') as handle:
    citedpaper_list_conf = pickle.load(handle)
cited_citingpaper_map_conf = {}
notcited_citingpaper_map_conf = {}

cited_paper_map_conf = {}
notcited_paper_map_conf = {}

for conf, df in ori_citingpaper_conf.items():
    cited_citingpaper_map = {}
    notcited_citingpaper_map = {}
    cited_paper_map = {}
    notcited_paper_map = {}
    cited_paper_list = citedpaper_list_conf[conf]
    inv_paperyear_map = inv_paperyear_map_conf[conf]
    for row in df.iterrows():
        citing_paperid = str(row[1]).split(',')[0].split('\n')[0].split()[1]
        cited_paperid = str(row[1]).split(',')[0].split('\n')[1].split()[1]
        # paperyear
        if cited_paperid not in inv_paperyear_map.keys(): continue
        paperyear = inv_paperyear_map[cited_paperid]
        if cited_paperid in cited_paper_list:
            if paperyear not in cited_citingpaper_map.keys():
                cited_citingpaper_map[paperyear] = []
            if paperyear not in cited_paper_map.keys():
                cited_paper_map[paperyear] = {}
            if cited_paperid not in cited_paper_map[paperyear].keys():
                cited_paper_map[paperyear][cited_paperid] = []
            if citing_paperid not in cited_paper_map[paperyear][cited_paperid]:
                cited_paper_map[paperyear][cited_paperid].append(citing_paperid)
            # if citing_paperid not in cited_citingpaper_map[paperyear]:
            cited_citingpaper_map[paperyear].append(citing_paperid)
        else:
            if paperyear not in notcited_citingpaper_map.keys():
                notcited_citingpaper_map[paperyear] = []
            if paperyear not in notcited_paper_map.keys():
                notcited_paper_map[paperyear] = {}
            if cited_paperid not in notcited_paper_map[paperyear].keys():
                notcited_paper_map[paperyear][cited_paperid] = []
            if citing_paperid not in notcited_paper_map[paperyear][cited_paperid]:
                notcited_paper_map[paperyear][cited_paperid].append(citing_paperid)
            # if citing_paperid not in notcited_citingpaper_map[paperyear]:
            notcited_citingpaper_map[paperyear].append(citing_paperid)
    cited_citingpaper_map_conf[conf] = cited_citingpaper_map
    notcited_citingpaper_map_conf[conf] = notcited_citingpaper_map
    cited_paper_map_conf[conf] = cited_paper_map
    notcited_paper_map_conf[conf] = notcited_paper_map
print(">>> cited paper map construction done")

with open('cited_paper_map_conf.pickle', 'wb') as handle:
    pickle.dump(cited_paper_map_conf, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open('notcited_paper_map_conf.pickle', 'wb') as handle:
    pickle.dump(notcited_paper_map_conf, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
    
# # %%
# # TODO: apply get_patentid
single_citingpaper_map_conf = {}
for conf, df in ori_citingpaper_conf.items():
    single_citingpaper_map = {}
    for row in df.iterrows():
        citing_paperid = str(row[1]).split(',')[0].split('\n')[1].split()[1]
        cited_paperid = str(row[1]).split(',')[0].split('\n')[2].split()[1]
        if cited_paperid not in single_citingpaper_map.keys():
            single_citingpaper_map[cited_paperid] = []
        if citing_paperid not in single_citingpaper_map[cited_paperid]:
            single_citingpaper_map[cited_paperid].append(citing_paperid)
    single_citingpaper_map_conf[conf] = single_citingpaper_map
print(">>> single citing paper map construction done")

# %%
# TODO: apply get_patentid
single_citingpatent_map_conf = {}
for conf, df in ori_citingpatent_conf.items():
    single_citingpatent_map = {}
    for row in df.iterrows():
        paperid = str(row[1]).split(',')[0].split('\n')[5].split()[1] # paperid
        patentid = str(row[1]).split(',')[0].split('\n')[6].split()[1] # patentid

        if paperid not in single_citingpatent_map.keys():
            single_citingpatent_map[paperid] = []
        if patentid not in single_citingpatent_map[paperid]:
            single_citingpatent_map[paperid].append(patentid)

    single_citingpatent_map_conf[conf] = single_citingpatent_map
print(">>> done single citing data")
with open('single_citingpaper_map_conf.pickle', 'wb') as handle:
    pickle.dump(single_citingpaper_map_conf, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open('single_citingpatent_map_conf.pickle', 'wb') as handle:
    pickle.dump(single_citingpatent_map_conf, handle, protocol=pickle.HIGHEST_PROTOCOL)