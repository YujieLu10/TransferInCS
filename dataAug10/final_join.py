import argparse
from itertools import chain
import pandas as pd
import os
import argparse

parser = argparse.ArgumentParser(description='final_join')
parser.add_argument('--citation_per_record', action='store_true', default=False,
                    help='disables CUDA training')
args = parser.parse_args()

citation_per_record = args.citation_per_record
# HCI_ori_paper_pd = pd.read_csv('paperinformation_HCI.tsv')
HCI_patent_pd = pd.read_csv('patent_information_HCI.tsv')
HCI_papercitationscience_pd = pd.read_csv('papercitationscience_CHI.tsv')
for conf in ["CSCW", "UbiComp", "UIST"]:
    new_df = pd.read_csv('papercitationscience_{}.tsv'.format(conf))
    HCI_papercitationscience_pd = HCI_papercitationscience_pd.append(new_df, ignore_index=True)
HCI_papercitationscience_pd = HCI_papercitationscience_pd.drop_duplicates()

# HCI_papercitationscience_pd = HCI_papercitationscience_pd[['paperid','patent']]
HCI_patent_pd = HCI_patent_pd[['patent_id', 'country', 'date', 'abstract', 'title', 'kind', 'num_claims', 'withdrawn', 'inventor_id', 'inventor_name_first', 'inventor_name_last', 'male_flag', 'attribution_status', 'assignee_id', 'assignee_name_first', 'assignee_name_last', 'organization']]

def get_patentid(x):
    x = x[x.index('-')+1:]
    if '-' in x: return x[:x.index('-')]
    else: return x
    
HCI_patent_pd["patent_id"] = HCI_patent_pd["patent_id"].astype(str)
HCI_papercitationscience_pd["patent"] = HCI_papercitationscience_pd["patent"].astype(str)
HCI_papercitationscience_pd["patent"] = HCI_papercitationscience_pd["patent"].apply(get_patentid)
# HCI_ori_paper_pd.head(5)
# from icecream import ic
# HCI_ori_paper_pd["patents"] = ""
# # HCI_ori_paper_pd = HCI_ori_pd.merge(patent_assignee_pd, left_on='paperid', right_on='paperid')
# # from icecream import ic
# for index, row in HCI_ori_paper_pd.iterrows():
#     citing_patent_id = HCI_papercitationscience_pd.loc[HCI_papercitationscience_pd['magid']==row['mag_id'], 'patent']
#     if not citing_patent_id.empty:
#         patent_information_dict = {}
#         for patent_id in citing_patent_id.values:
#             # ic(patent_id)
#             # ic(HCI_patent_pd.loc[HCI_patent_pd['patent_id']==9589072])
#             patent_information_dict[patent_id] = {}
#             patent_information_dict[patent_id]["patent_info"] = HCI_patent_pd.loc[HCI_patent_pd['patent_id']==str(patent_id),['country', 'date', 'abstract', 'title', 'kind', 'num_claims', 'withdrawn', 'assignee_id', 'assignee_name_first', 'assignee_name_last', 'organization']].to_dict('record')
#             inventor_part = HCI_patent_pd.loc[HCI_patent_pd['patent_id']==str(patent_id), ['inventor_id', 'inventor_name_first', 'inventor_name_last', 'male_flag', 'attribution_status']].to_dict('record')
#             patent_information_dict[patent_id]["inventors"] = inventor_part
#         # ic(patent_information_dict)
#         HCI_ori_paper_pd.at[index,'patents'] = patent_information_dict
# HCI_ori_paper_pd.to_csv('data4analysis/paper_patent_all_info_{}_per_record.tsv'.format("citation" if citation_per_record else "paper"), index=False)
from itertools import chain
import pandas as pd
import os

# paper per record: paper_patent_all_info.tsv
# citation per record
HCI_all_pd = pd.read_csv('data4analysis/paper_patent_all_info_{}_per_record.tsv'.format("citation" if citation_per_record else "paper"))
HCI_affiliation_pd = pd.read_csv('HCI_paper_authorid_affiliation.tsv', sep='\t')
HCI_affiliation_pd = HCI_affiliation_pd.rename(columns={"paperid":"aff_paperid", "Affiliation": "aff_affiliations", "authorid": "aff_authorids"})
HCI_all_pd = HCI_all_pd.merge(HCI_affiliation_pd, left_on='mag_id', right_on='aff_paperid')
HCI_all_pd.to_csv("data4analysis/final_all_HCI_info_{}_per_record.tsv".format("citation" if citation_per_record else "paper"), index=False)