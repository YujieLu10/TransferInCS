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
# paper per record: paper_patent_all_info.tsv
# citation per record
HCI_ori_paper_pd = pd.read_csv('data4analysis/paper_patent_all_info_{}_per_record.tsv'.format("citation" if citation_per_record else "paper"))
print(len(HCI_ori_paper_pd))
HCI_affiliation_pd = pd.read_csv('HCI_paper_authorid_affiliation.tsv', sep='\t')
HCI_affiliation_pd = HCI_affiliation_pd.rename(columns={"paperid":"aff_paperid", "Affiliation": "aff_affiliations", "authorid": "aff_authorids"})
HCI_ori_paper_pd = HCI_ori_paper_pd.merge(HCI_affiliation_pd, left_on='mag_id', right_on='aff_paperid')

HCI_ori_paper_pd = HCI_ori_paper_pd.drop_duplicates()
if citation_per_record:
    HCI_ori_paper_pd = HCI_ori_paper_pd.groupby(['mag_id', 'patent']).first().reset_index()
else:
    HCI_ori_paper_pd = HCI_ori_paper_pd.groupby('mag_id').first().reset_index()
print(len(HCI_ori_paper_pd))
HCI_ori_paper_pd.to_csv("data4analysis/final_all_HCI_info_{}_per_record.tsv".format("citation" if citation_per_record else "paper"), index=False)