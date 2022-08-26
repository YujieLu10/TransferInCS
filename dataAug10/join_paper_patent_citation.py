from itertools import chain
import pandas as pd
import os
import json
from icecream import ic
    
record_per_citation = True
old_HCI_ori_paper_pd = pd.read_csv('paperinformation_HCI.tsv', sep=',')
HCI_ori_paper_pd = pd.read_csv('mergeversiondata/paperinformation_HCI.tsv', sep=',')
tmp_HCI_ori_paper_pd = pd.read_csv('mergeversiondata/tmp.tsv', error_bad_lines=False)
HCI_ori_paper_pd = HCI_ori_paper_pd.append(old_HCI_ori_paper_pd, ignore_index=True)
HCI_ori_paper_pd = HCI_ori_paper_pd.append(tmp_HCI_ori_paper_pd, ignore_index=True)

HCI_ori_paper_pd = HCI_ori_paper_pd.drop_duplicates()
print(len(HCI_ori_paper_pd))
HCI_patent_pd = pd.read_csv('mergeversiondata/patent_information_HCI.tsv')
HCI_patent_pd = HCI_patent_pd.drop_duplicates()
HCI_patent_pd
HCI_patent_pd = HCI_patent_pd[['patent_id', 'country', 'date', 'abstract', 'title', 'kind', 'num_claims', 'withdrawn', 'inventor_id', 'inventor_name_first', 'inventor_name_last', 'male_flag', 'attribution_status', 'assignee_id', 'assignee_name_first', 'assignee_name_last', 'organization']]
# HCI_papercitationscience_pd = pd.read_csv('data/papercitationscience_result.tsv')
# HCI_papercitationscience_pd = HCI_papercitationscience_pd[['paperid','patent']]
HCI_papercitationscience_pd = pd.read_csv('mergeversiondata/papercitationscience.tsv')
for conf in ["CHI","CSCW", "UbiComp", "UIST"]:
    new_df = pd.read_csv('mergeversiondata/papercitationscience_{}.tsv'.format(conf))
    HCI_papercitationscience_pd = HCI_papercitationscience_pd.append(new_df, ignore_index=True)
HCI_papercitationscience_pd = HCI_papercitationscience_pd.drop_duplicates()

def get_patentid(x):
    if not "-" in x: return x
    x = x[x.index('-')+1:]
    if '-' in x: return x[:x.index('-')]
    else: return x
    
HCI_patent_pd = HCI_patent_pd.drop_duplicates()
# HCI_patent_pd = HCI_patent_pd.groupby('patent_id').first().reset_index()
print(HCI_patent_pd.head(3))
HCI_patent_pd["patent_id"] = HCI_patent_pd["patent_id"].astype(str)
HCI_papercitationscience_pd["patent"] = HCI_papercitationscience_pd["patent"].astype(str)
HCI_papercitationscience_pd["patent"] = HCI_papercitationscience_pd["patent"].apply(get_patentid)
    
if record_per_citation:
    # ic(HCI_papercitationscience_pd["patent"].tolist())
    # ic(HCI_papercitationscience_pd.dtypes, HCI_patent_pd.dtypes)
    # HCI_ori_paper_pd["paperid"] = HCI_ori_paper_pd["paperid"].astype(int)
    HCI_merge_pd = HCI_papercitationscience_pd.merge(HCI_ori_paper_pd, left_on='magid', right_on='mag_id')
    # ic(HCI_merge_pd.head(5))
    HCI_merge_pd = HCI_merge_pd.merge(HCI_patent_pd, left_on='patent', right_on='patent_id')
    
    ic(HCI_merge_pd.head(5))
    HCI_merge_pd = HCI_merge_pd.drop_duplicates()
    # HCI_merge_pd = HCI_merge_pd.groupby('magid').first()
    HCI_merge_pd.to_csv('data4analysis/paper_patent_all_info_citation_per_record.tsv', index=False)   
else:
    HCI_ori_paper_pd["patents"] = ""
    # HCI_ori_paper_pd = HCI_ori_pd.merge(patent_assignee_pd, left_on='paperid', right_on='paperid')
    # from icecream import ic
    for index, row in HCI_ori_paper_pd.iterrows():
        citing_patent_id = HCI_papercitationscience_pd.loc[HCI_papercitationscience_pd['magid']==row['mag_id'], 'patent']
        if not citing_patent_id.empty:
            patent_information_dict = {}
            count = 0
            for patent_id in citing_patent_id.values:
                count += 1
                # ic(patent_id)
                # ic(HCI_patent_pd.loc[HCI_patent_pd['patent_id']==9589072])
                # ic(HCI_patent_pd.loc[HCI_patent_pd['patent_id']==int(patent_id), ['inventor_id', 'inventor_name_first', 'inventor_name_last', 'male_flag', 'attribution_status']])
                try:
                    patent_information_dict[patent_id] = {}
                    patent_information_dict[patent_id]["patent_info"] = HCI_patent_pd.loc[HCI_patent_pd['patent_id']==int(patent_id),['country', 'date', 'abstract', 'title', 'kind', 'num_claims', 'withdrawn', 'assignee_id', 'assignee_name_first', 'assignee_name_last', 'organization']].drop_duplicates().to_json(orient="records")
                    inventor_part = HCI_patent_pd.loc[HCI_patent_pd['patent_id']==int(patent_id), ['inventor_id', 'inventor_name_first', 'inventor_name_last', 'male_flag', 'attribution_status']].drop_duplicates().to_json(orient="records")
                    patent_information_dict[patent_id]["inventors"] = inventor_part
                    patent_information_dict[patent_id] = json.dumps(patent_information_dict[patent_id])
                    # ic(json.loads(inventor_part))                
                except:
                    continue
            
            HCI_ori_paper_pd.at[index,'patents'] = json.dumps(patent_information_dict)
    HCI_ori_paper_pd = HCI_ori_paper_pd.drop_duplicates()
    # HCI_ori_paper_pd = HCI_ori_paper_pd.groupby('magid').first()
    HCI_ori_paper_pd.to_csv('data4analysis/paper_patent_all_info.tsv', index=False)    