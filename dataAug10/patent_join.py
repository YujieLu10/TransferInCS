#------------ patent year -------------# data source:/patentsview/patent.tsv
from itertools import chain
import pandas as pd
import os

HCI_ori_pd = pd.read_csv('rawdata/patent_year_inventor.tsv')
patent_assignee_pd = pd.read_csv('rawdata/patent_assignee.tsv',sep='\t')
# merge ori_conf_pd_map
HCI_ori_pd = HCI_ori_pd[['patent_id']]
HCI_ori_pd = HCI_ori_pd.drop_duplicates()
HCI_ori_pd = HCI_ori_pd.merge(patent_assignee_pd, left_on='patent_id', right_on='patent_id')
print(HCI_ori_pd.head(5))
HCI_ori_pd.to_csv('patent_assignee_HCI.tsv')

#------------ patent year -------------# data source:/patentsview/patent.tsv
from itertools import chain
import pandas as pd
import os

HCI_ori_pd = pd.read_csv('rawdata/patent_year_inventor.tsv')
patent_inventor_pd = pd.read_csv('rawdata/patent_inventor.tsv',sep='\t')
# merge ori_conf_pd_map
HCI_ori_pd = HCI_ori_pd[['patent_id', 'conf_id', 'id', 'type', 'number', 'country', 'date', 'abstract', 'title', 'kind', 'num_claims', 'filename', 'withdrawn']]
HCI_ori_pd.head(5)
HCI_ori_pd = HCI_ori_pd.drop_duplicates()
HCI_ori_pd = HCI_ori_pd.merge(patent_inventor_pd, left_on='patent_id', right_on='patent_id')
HCI_ori_pd.head(5)
HCI_ori_pd.to_csv('patent_year_inventor_HCI.tsv')


# join inventor and assignee id
patent_year_inventor_HCI_pd = pd.read_csv('patent_year_inventor_HCI.tsv')
patent_assignee_HCI_pd = pd.read_csv('patent_assignee_HCI.tsv')
# merge ori_conf_pd_map
patent_year_inventor_HCI_pd = patent_year_inventor_HCI_pd.merge(patent_assignee_HCI_pd, left_on='patent_id', right_on='patent_id')
patent_year_inventor_HCI_pd.to_csv('patent_inventor_assignee_id_HCI.tsv')

# join all information
patent_inventor_assignee_id_HCI = pd.read_csv('patent_inventor_assignee_id_HCI.tsv')
assignee_pd = pd.read_csv('rawdata/assignee.tsv', sep='\t')
assignee_pd = assignee_pd.rename(columns={"id":"ori_assignee_id", "name_first": "assignee_name_first", "name_last": "assignee_name_last"})
inventor_pd = pd.read_csv('rawdata/inventor.tsv', sep='\t')
inventor_pd = inventor_pd.rename(columns={"id":"ori_inventor_id", "name_first": "inventor_name_first", "name_last": "inventor_name_last"})
patent_inventor_assignee_id_HCI = patent_inventor_assignee_id_HCI.merge(assignee_pd, left_on='assignee_id', right_on='ori_assignee_id')
print(patent_inventor_assignee_id_HCI.head(5))
patent_inventor_assignee_id_HCI = patent_inventor_assignee_id_HCI.merge(inventor_pd, left_on='inventor_id', right_on='ori_inventor_id')
print(patent_inventor_assignee_id_HCI.head(5))
patent_inventor_assignee_id_HCI.to_csv('patent_information_HCI.tsv')