import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

conf_key = {'CHI':1163450153, 'CSCW':1195049314, 'UBI':1171345118, 'UIST':1166315290}

ori_paperyear_conf = {}
ori_citingpatent_conf = {}

# join paperid with paperyear and papercitation2science
# df_year = pd.read_csv('../dataAug10/paperyear_result.tsv', usecols=[1,2])
df_year = pd.read_csv('../dataAug10/mergeversiondata/paperyear_result.tsv')
for conf in ["CHI", "CSCW", "UBI", "UIST"]:
    new_df = pd.read_csv('../dataAug10/mergeversiondata/paperyear_result_{}.tsv'.format(conf))
    df_year = df_year.append(new_df, ignore_index=True)
df_year = df_year.drop_duplicates()

df_paperid = pd.read_csv('../dataAug10/mergeversiondata/HCI_paperids.tsv', sep='\t')
df_paperid = df_paperid.drop_duplicates()
df_paperid.head(4)

df_paper_year = df_year.merge(df_paperid, left_on='paperid', right_on='paper_id')
df_paper_year = df_paper_year.drop_duplicates()[['paper_id', 'year', 'conf_id']]
df_paper_year.head(4)

# df_papercitation2science = pd.read_csv('../data/papercitationscience_result.tsv', usecols=[3,4])
df_papercitation2science = pd.read_csv('../dataAug10/mergeversiondata/papercitationscience.tsv')
for conf in ["CHI", "CSCW", "UbiComp", "UIST"]:
    new_df = pd.read_csv('../dataAug10/mergeversiondata/papercitationscience_{}.tsv'.format(conf))[["reftype","confscore","magid","patent"]]
    df_papercitation2science = df_papercitation2science.append(new_df, ignore_index=True)
def get_patentid(x):
    if '-' not in x: return x
    x = x[x.index('-')+1:]
    if '-' in x: return x[:x.index('-')]
    else: return x
df_papercitation2science["patent"] = df_papercitation2science["patent"].astype(str)
df_papercitation2science["patent"] = df_papercitation2science["patent"].apply(get_patentid)
df_papercitation2science = df_papercitation2science.drop_duplicates()
df_papercitation2science.head(3)

df_paper_pc2s_year = df_papercitation2science.merge(df_paper_year, left_on='magid', right_on='paper_id')
df_paper_pc2s_year = df_paper_pc2s_year.drop_duplicates().drop(columns=['paper_id']) #.drop(columns=['confid_y', 'paperid']).rename(columns={"confid_x":"confid"})
df_paper_pc2s_year.head(5)

import seaborn as sns
old_df_patent_year = pd.read_csv('../dataAug10/mergeversiondata/patent_year_inventor_HCI_oldmerge.tsv')[["patent_id","date","conf_id"]]
new_df_patent_year = pd.read_csv('../dataAug10/mergeversiondata/patent_year_inventor_new.tsv')[["patent_id","date","conf_id"]]
df_patent_year = pd.read_csv('../dataAug10/mergeversiondata/patent_year_inventor_HCI.tsv')[["patent_id","date","conf_id"]]
def get_conf_name(x):
    if str(x) == "1163450153": return "CHI"
    if str(x) == "1195049314": return "CSCW"
    if str(x) == "1166315290": return "UIST"
    if str(x) == "1171345118": return "UBI"
    return x
df_patent_year = df_patent_year.append(old_df_patent_year, ignore_index=True)
df_patent_year = df_patent_year.append(new_df_patent_year, ignore_index=True)
df_patent_year = df_patent_year.apply(get_conf_name).drop_duplicates()
df_patent_year['patent_year'] = pd.DatetimeIndex(df_patent_year['date']).year
df_patent_year['patent_id'] = df_patent_year['patent_id'].apply(str)
df_paper_pc2s_year = df_paper_pc2s_year.drop(columns=["conf_id"])
df_patent_paper_year = df_patent_year.merge(df_paper_pc2s_year,left_on='patent_id',right_on='patent')
# df_patent_paper_year = df_paper_pc2s_year.merge(df_patent_year,left_on='patent',right_on='patent_id')
df_patent_paper_year['patent_paper_lag'] = df_patent_paper_year['patent_year'] - df_patent_paper_year['year']
df_patent_paper_year = df_patent_paper_year.drop_duplicates()
df_patent_paper_year = df_patent_paper_year.groupby(["magid", "patent_id"]).first().reset_index()
df_patent_paper_year.to_csv("../dataAug10/mergeversiondata/df_patent_paper_year.tsv")
# df_patent_paper_year.head(3)