# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import pandas as pd

hci_tilte_CHI = pd.read_csv("../papertitles_extracted/papertitle_CHI.tsv", sep = ",")
hci_tilte_CSCW = pd.read_csv("../papertitles_extracted/papertitle_CSCW.tsv", sep = ",")
hci_tilte_UIST = pd.read_csv("../papertitles_extracted/papertitle_UIST.tsv", sep = ",")
hci_tilte_IMCL = pd.read_csv("../papertitles_extracted/papertitle_IMCL.tsv", sep = ",")
hci_tilte_UBI = pd.read_csv("../papertitles_extracted/papertitle_UBI.tsv", sep = ",")

hci_tilte_CHI['papertitle'] = [title.encode('utf-8').strip().lower() for title in hci_tilte_CHI['title']]
hci_tilte_CSCW['papertitle'] = [title.encode('utf-8').strip().lower() for title in hci_tilte_CSCW['title']]
hci_tilte_UIST['papertitle'] = [title.encode('utf-8').strip().lower() for title in hci_tilte_UIST['title']]
hci_tilte_IMCL['papertitle'] = [title.encode('utf-8').strip().lower() for title in hci_tilte_IMCL['title']]
hci_tilte_UBI['papertitle'] = [title.encode('utf-8').strip().lower() for title in hci_tilte_UBI['title']]

from fuzzywuzzy import process

# matched = 'Technology heirlooms?: considerations fo passing down and inheriting digital materials.'
# print(papers['papertitle'].iloc[0])
# highest = process.extractOne(str(papers['papertitle'].iloc[0]), hci_title['papertitle'])
# print(highest)

success_match = 0
result_CHI = []
with open('dblp_CHI_title.tsv', "r") as chi_title_f:
    for line in chi_title_f:
        paper_idx = line[0:line.index(',')]
        paper_title = line[line.index(',') + 1:]
        highest = process.extractOne(paper_title, hci_tilte_CHI['papertitle'])
        try:
            output = [highest[0], highest[1], highest[2]]
            result_CHI.append(list(output))
        except:
            print(">>> error")
    result_pd = pd.DataFrame(data=result_CHI, columns=['papertitle', 'score', 'paperidx'])
    result_pd.to_csv('matched_CHI.tsv')

result_CSCW = []
with open('dblp_CSCW_title.tsv', "r") as cscw_title_f:
    for line in cscw_title_f:
        paper_idx = line[0:line.index(',')]
        paper_title = line[line.index(',') + 1:]
        highest = process.extractOne(paper_title, hci_tilte_CSCW['papertitle'])
        try:
            output = [highest[0], highest[1], highest[2]]
            result_CSCW.append(list(output))
        except:
            print(">>> error")
    result_pd = pd.DataFrame(data=result_CSCW, columns=['papertitle', 'score', 'paperidx'])
    result_pd.to_csv('matched_CSCW.tsv')

# result_UIST = []
# with open('dblp_UIST_title.tsv', "r") as uist_title_f:
#     for line in uist_title_f:
#         paper_idx = line[0:line.index(',')]
#         paper_title = line[line.index(',') + 1:]
#         highest = process.extractOne(paper_title, hci_tilte_UIST['papertitle'])
#         try:
#             output = [highest[0], highest[1], highest[2]]
#             result_UIST.append(list(output))
#         except:
#             print(">>> error")
#     result_pd = pd.DataFrame(data=result_UIST, columns=['papertitle', 'score', 'paperidx'])
#     result_pd.to_csv('matched_CSCW.tsv')

# result_IMCL = []
# with open('dblp_IMCL_title.tsv', "r") as imcl_title_f:
#     for line in imcl_title_f:
#         paper_idx = line[0:line.index(',')]
#         paper_title = line[line.index(',') + 1:]
#         highest = process.extractOne(paper_title, hci_tilte_IMCL['papertitle'])
#         try:
#             output = [highest[0], highest[1], highest[2]]
#             result_IMCL.append(list(output))
#         except:
#             print(">>> error")
#     result_pd = pd.DataFrame(data=result_IMCL, columns=['papertitle', 'score', 'paperidx'])
#     result_pd.to_csv('matched_IMCL.tsv') 

# result_UBI = []
# with open('dblp_UBI_title.tsv', "r") as ubi_title_f:
#     for line in ubi_title_f:
#         paper_idx = line[0:line.index(',')]
#         paper_title = line[line.index(',') + 1:]
#         highest = process.extractOne(paper_title, hci_tilte_UBI['papertitle'])
#         try:
#             output = [highest[0], highest[1], highest[2]]
#             result_UBI.append(list(output))
#         except:
#             print(">>> error")
#     result_pd = pd.DataFrame(data=result_UBI, columns=['papertitle', 'score', 'paperidx'])
#     result_pd.to_csv('matched_UBI.tsv')        
