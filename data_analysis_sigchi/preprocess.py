import string
import pandas as pd
import pickle
from icecream import ic

conf_key = {'CHI':1163450153, 'CSCW':1195049314, 'UBI':1171345118, 'UIST':1166315290}

ori_paperyear_conf = {}
ori_citingpatent_conf = {}


# patent_id_no_researcher = pd.read_csv("patent_id_no_researcher.csv")
# patent_id_no_researcher["patent"] = patent_id_no_researcher["patent"].astype(str)
# df_paper_year = pd.read_csv("df_paper_year.tsv")
# df_paper_pc2s_year = pd.read_csv("df_paper_pc2s_year.tsv")
# df_paper_pc2s_year["patent"] = df_paper_pc2s_year["patent"].astype(str)
# ic(len(df_paper_pc2s_year))
# df_paper_pc2s_year = df_paper_pc2s_year.merge(patent_id_no_researcher, left_on='patent', right_on='patent')
# df_paper_pc2s_year = df_paper_pc2s_year.drop_duplicates()
# ic(len(df_paper_pc2s_year))
# df_paper_pc2s_year.to_csv("df_paper_pc2s_year_no_researcher.tsv")

df_patent_paper_year = pd.read_csv("../dataAug10/mergeversiondata/df_patent_paper_year.tsv")
df_patent_paper_year["patent_id"] = df_patent_paper_year["patent_id"].astype(str)
df_patent_paper_year = df_patent_paper_year.merge(patent_id_no_researcher, left_on='patent_id', right_on='patent')
df_patent_paper_year.to_csv("df_patent_paper_year.tsv")
