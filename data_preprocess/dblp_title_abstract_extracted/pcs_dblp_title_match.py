# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import pandas as pd

## merge microsoft's dataset
# conference_id = pd.read_csv("conferenceidname.tsv", sep = "\t")
# paper_conference = pd.read_csv("paperconferenceid.tsv", sep = "\t")
# paper_author_aff = pd.read_csv("paperauthoridaffiliationname.tsv", sep = "\t")

# hci = paper_conference[(paper_conference['conferenceid'] == 1171345118) | 
#                        (paper_conference['conferenceid'] == 1166315290) |
#                        (paper_conference['conferenceid'] == 1163450153) |
#                        (paper_conference['conferenceid'] == 1195049314)]


# hci_inf = pd.merge(hci, paper_author_aff, on='paperid', how='inner')
# paper_title = pd.read_csv("papertitle.tsv", sep = "\t")
# hci_title = pd.merge(hci_inf, paper_title, on='paperid', how='inner')
# TODO:load hci_tilte from each extracted file
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

hci_title_all = hci_tilte_CHI + hci_tilte_CSCW + hci_tilte_UIST + hci_tilte_IMCL + hci_tilte_UBI
# hci_title_all['papertitle'] = [title.encode('utf-8').strip().lower() for title in hci_title_all['papertitle']]

print("finished merging microsoft's dataset")

## read dallas's dataset
import json
paper = []
for line in open('dblp_papers_with_s2_abstracts.jsonlist', 'r'):
    paper.append(json.loads(line))
df = pd.DataFrame(paper)
# papers_map = {"papers_CHI":df[(df['dblp_venue'] == 'CHI')], "papers_CSCW":df[(df['dblp_venue'] == 'CSCW')], "papers_UIST":df[(df['dblp_venue'] == 'UIST')], "papers_IMCL":df[(df['dblp_venue'] == 'IMCL')],"papers_UBI":df[(df['dblp_venue'] == 'UbiComp')]}
# print(df['dblp_venue'])
papers = df[(df['dblp_venue'] == 'CHI')| (df['dblp_venue'] == 'CSCW') | 
            (df['dblp_venue'] == 'UIST') | (df['dblp_venue'] == 'IMCL') |
            (df['dblp_venue'] == 'UbiComp')]

# for key, item in papers_map.items():
#     item = item[['dblp_authors_stand','dblp_title', 'dblp_venue', 'dblp_year', 's2_abstract']]
#     item['papertitle'] = [title.encode('utf-8').strip().lower() for title in item['dblp_title']]

# papers = df[(df['dblp_venue'] == 'CHI')| (df['dblp_venue'] == 'CSCW') | 
#             (df['dblp_venue'] == 'UIST') | (df['dblp_venue'] == 'IMWUT') |
#            (df['dblp_venue'] == 'UbiComp')]

# papers = papers[['dblp_authors_stand','dblp_title', 'dblp_venue', 'dblp_year', 's2_abstract']]
papers = papers[['dblp_title', 'dblp_venue']]
papers['papertitle'] = [title.encode('utf-8').strip().lower() for title in papers['dblp_title']]

papers.to_csv('extract_dblp_venue.tsv')
print(papers)

paper_id = {}
# hci_title = hci_tilte_CHI
# hci_title_list = [hci_tilte_CHI, hci_tilte_CSCW, hci_tilte_UIST, hci_tilte_UBI]

for ind in hci_title_all.index:
    if hci_title_all['papertitle'][ind] not in paper_id:
        paper_id[hci_title_all['papertitle'][ind]] = hci_title_all['paperid'][ind]
        # print(hci_title_all['paperid'][ind])
    else:
        continue
# paper_aff = {} #the dictionary that saves papertitle: [affiliations]
# for ind in hci_title.index:
#     if hci_title['papertitle'][ind] not in paper_aff:
#         paper_aff[hci_title['papertitle'][ind]] = []
#         paper_aff[hci_title['papertitle'][ind]].append(hci_title['affiliationame'][ind])
#     else:
#         paper_aff[hci_title['papertitle'][ind]].append(hci_title['affiliationame'][ind])

print("finished reading dallas's dataset")

## match the affiliations
from fuzzywuzzy import process

# matched_paper = []
# affiliations = []

#matched = 'Technology heirlooms?: considerations fo passing down and inheriting digital materials.'
#print(papers['papertitle'].iloc[0])
#highest = process.extractOne(str(papers['papertitle'].iloc[0]), hci_title['papertitle'])
#print(highest)

success_match = 0
f = open("HCI_matched_title.txt", "w")
for ind in papers.index:
    print(papers['papertitle'][ind])
    #print(hci_title['papertitle'])
    highest = process.extractOne(papers['papertitle'][ind], hci_title_all['papertitle'])
    # f.write(papers['papertitle'][ind])
    # f.write("\t")
    print(highest)
    try:
        if highest[1] >= 90:
            success_match += 1
            print("success match: ",success_match)
            # print(ind,papers['papertitle'][ind],highest[0],paper_aff[highest[0]])
            #print(paper_id[highest[0]])
            f.write(paper_id[highest[0]])
            f.write("\t")
            f.write(highest[0])
            f.write("\t") 
            f.write(papers['papertitle'][ind])
            f.write("\t")            
            # f.write(paper_aff[highest[0]])
        else:
            print("score < 90", ind, papers['papertitle'][ind])
            # f.write("na")
            # f.write("\t")
            # f.write("na")
            # f.write("\t") 
            # f.write("na")
    except:
        print("something goes wrong", ind, papers['papertitle'][ind])
        # f.write("na")
        # f.write("\t")
        # f.write("na")
        # f.write("\t") 
        # f.write("na")

    f.write("\n")

#f.close()
