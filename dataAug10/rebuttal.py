# 1. @hancheng conference id list (SIGCHI https://sigchi.org/conferences/upcoming-conferences/) @yujie paper cited by patent percentage 7678/57385 13.37%
#------------ paper year -------------# data source:/data/pcsdata/selected_MAG_metadata/paperyear.tsv
# from itertools import chain
# import pandas as pd

# import argparse
# from icecream import ic

# parser = argparse.ArgumentParser(description='PCS')
# parser.add_argument('--extract', default="NA", help='type')
# args = parser.parse_args()

# # data_HCI = list(chain(*pd.read_csv('../dataAug10/HCI_paperids.tsv',sep=',').values.tolist()))
# data_HCI = pd.read_csv('sigchi_paperids.tsv',sep='\t')
# # data_HCI = pd.read_csv('HCI_paperids.tsv',sep='\t')
# # data_HCI = data_HCI.drop_duplicates()
# data_HCI = data_HCI.groupby(["paperid"]).first().reset_index()
# data_HCI = data_HCI.drop_duplicates()
# # data_HCI.head(10)
# conf_paper_list = data_HCI['paperid'].tolist()
# print(len(data_HCI))
# from itertools import chain
# import pandas as pd
# pcs_pd = pd.read_csv('pcs_mag_doi_pmid.tsv', sep='\t')
# for conf_name in ["SIGCHI"]:
#     # HCI_filter_df_paperid = pd.read_csv('/local/home/yujielu/project/TransferInCS/dataAug10/{}_paperids.tsv'.format(conf_name), sep='\t')
#     # conf_paper_list = data_HCI['paperid'].tolist()
#     conf_pd = pcs_pd.loc[pcs_pd["magid"].isin(conf_paper_list)]
#     conf_pd.to_csv('papercitationscience_' + conf_name + '.tsv', index=False)
# print(len(conf_pd))
# conf_pd = conf_pd.groupby(["magid"]).first().reset_index()
# conf_pd = conf_pd.drop_duplicates()
# print(len(conf_pd))

# paper-wise both+bodyonly / all paper 1. all 2. sigchi venues

import pandas as pd
from icecream import ic
data_HCI = pd.read_csv('sigchi_paperids.tsv',sep='\t')
conf_paper_list = data_HCI['paperid'].tolist()

data_pcs = pd.read_csv('pcs_mag_doi_pmid.tsv',sep='\t')

data_pcs = data_pcs.loc[data_pcs["magid"].isin(conf_paper_list)]

ic(len(data_pcs)) # 42822458; 83792
data_pcs = data_pcs[(data_pcs["wherefound"] == "bodyonly") | (data_pcs["wherefound"] == "both")]
ic(len(data_pcs)) # 17523031; 3859
data_pcs = data_pcs.groupby(["magid"]).first().reset_index()
data_pcs = data_pcs.drop_duplicates()
ic(len(data_pcs)) # 3022924; 1344

# 1. all: 3022924/204728475 = 1.47%
# 2. sigchi: 1344/57386 = 2.34%