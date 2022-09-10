import pandas as pd
from icecream import ic

ori = pd.read_csv("data_analysis/df_paper_pc2s_year.tsv")
ori = ori.groupby(["patent"]).first().reset_index()
ori = ori.drop_duplicates()
ic(ori["patent"].count())
nr = pd.read_csv("data_analysis_no_researcher/patent_id_no_researcher.csv")
nr["patent"] = nr["patent"].astype(str)
nr = nr.groupby(["patent"]).first().reset_index()
nr = ori.merge(nr, left_on='patent', right_on='patent')
nr = nr.drop_duplicates()
ic(nr["patent"].count())
ns = pd.read_csv("data_analysis_non_self_cite/non_self_cite_patent_mag.tsv")
ns = ori.merge(ns, left_on=['magid', 'patent'], right_on=['magid', 'patent'])
ns = ns.groupby(['magid', 'patent']).first().reset_index()
# ns = ns.groupby(["patent"]).first().reset_index()
ic(ns["patent"].count())