import os
import pandas as pd

CHI_pd = pd.read_csv("papercitations_CHI.tsv", sep=',')
CSCW_pd = pd.read_csv("papercitations_CSCW.tsv", sep=',')
UIST_pd = pd.read_csv("papercitations_UIST.tsv", sep=',')
UBI_pd = pd.read_csv("papercitations_UBI.tsv", sep=',')

CHI_pcs_pd = pd.read_csv("../papercitation2science_extracted/papercitationscience_result_CHI.tsv", sep=',')
CSCW_pcs_pd = pd.read_csv("../papercitation2science_extracted/papercitationscience_result_CSCW.tsv", sep=',')
UIST_pcs_pd = pd.read_csv("../papercitation2science_extracted/papercitationscience_result_UIST.tsv", sep=',')
UBI_pcs_pd = pd.read_csv("../papercitation2science_extracted/papercitationscience_result_UBI.tsv", sep=',')
pcs_pd_list = [CHI_pcs_pd, CSCW_pcs_pd, UIST_pcs_pd, UBI_pcs_pd]
pd_list = [CHI_pd, CSCW_pd, UIST_pd, UBI_pd]

for idx in range(4):
    citation_pd = pd_list[idx]
    cited_paper_num = {}
    cited_patent_num = {}
    for row in citation_pd.iterrows():
        citing_paperid_str = str(row).split()[5] # paperid
        cited_paperid_str = str(row).split()[7]
        if cited_paperid_str in cited_paper_num.keys():
            cited_paper_num[cited_paperid_str] += 1
        else:
            cited_paper_num[cited_paperid_str] = 1
    result = []
    paperid_list = []
    # print(cited_paper_num)
    pcs_pd = pcs_pd_list[idx]
    for row in pcs_pd.iterrows():
        paperid = str(row).split()[9]
        patentid = str(row).split()[11]
        paperid_list.append(paperid)
        if paperid in cited_patent_num.keys():
            cited_patent_num[paperid] += 1
        else:
            cited_patent_num[paperid] = 1
    for k, v in cited_paper_num.items():
        if k not in cited_patent_num.keys():
            cited_patent_num[k] = 0                
        result.append(list([k, str(cited_paper_num[k]), str(cited_patent_num[k])]))
    result_pd = pd.DataFrame(data=result, columns=['paperid', 'citedbypapers', 'citedbypatents'])
    result_pd.to_csv('popular_transferred_paper{}.tsv'.format(idx))
