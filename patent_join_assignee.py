#------------ patent year -------------# data source:/patentsview/patent.tsv
from itertools import chain
import pandas as pd
import os

HCI_ori_pd = pd.read_csv('patent_year_inventor.tsv')
patent_assignee_pd = pd.read_csv('patent_assignee.tsv',sep='\t')
# merge ori_conf_pd_map
HCI_ori_pd = HCI_ori_pd[['patent_id']]
HCI_ori_pd = HCI_ori_pd.drop_duplicates()
HCI_ori_pd = HCI_ori_pd.merge(patent_assignee_pd, left_on='patent_id', right_on='patent_id')
print(HCI_ori_pd.head(5))
HCI_ori_pd.to_csv('patent_assignee_HCI.tsv')