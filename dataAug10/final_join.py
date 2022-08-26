import argparse
from itertools import chain
import pandas as pd
import os
import argparse
from icecream import ic

parser = argparse.ArgumentParser(description='final_join')
parser.add_argument('--citation_per_record', action='store_true', default=False,
                    help='disables CUDA training')
args = parser.parse_args()

citation_per_record = args.citation_per_record
# paper per record: paper_patent_all_info.tsv
# citation per record
import collections
HCI_ori_paper_pd = pd.read_csv('data4analysis/paper_patent_all_info_{}_per_record.tsv'.format("citation" if citation_per_record else "paper"))
ic(collections.Counter(HCI_ori_paper_pd['year']==2020), collections.Counter(HCI_ori_paper_pd['year']==2017))
print(len(HCI_ori_paper_pd))
HCI_affiliation_pd = pd.read_csv('mergeversiondata/HCI_paper_authorid_affiliation.tsv', sep='\t')
HCI_affiliation_pd = HCI_affiliation_pd.rename(columns={"paperid":"aff_paperid", "Affiliation": "aff_affiliations", "authorid": "aff_authorids"})
HCI_ori_paper_pd = HCI_ori_paper_pd.merge(HCI_affiliation_pd, left_on='mag_id', right_on='aff_paperid', how='left')

HCI_ori_paper_pd = HCI_ori_paper_pd.drop_duplicates()
if citation_per_record:
    # do not use patent_id to drop duplicates here!
    HCI_ori_paper_pd = HCI_ori_paper_pd.groupby(['mag_id', 'patent']).first().reset_index()
else:
    HCI_ori_paper_pd = HCI_ori_paper_pd.groupby('mag_id').first().reset_index()
print(len(HCI_ori_paper_pd))
ic(collections.Counter(HCI_ori_paper_pd['year']==2020), collections.Counter(HCI_ori_paper_pd['year']==2017))
HCI_ori_paper_pd.to_csv("data4analysis/final_all_HCI_info_{}_per_record.tsv".format("citation" if citation_per_record else "paper"), index=False)