# https://api.semanticscholar.org/graph/v1/paper/MAG:2014544908?fields=title,abstract,year,authors,venue
from urllib import response
from icecream import ic
import requests
import csv
import pandas as pd
from tqdm import tqdm
import time

start_idx = 0
conf_name = "HCI"
cur_result_pd = pd.read_csv('mergeversiondata/paperinformation_HCI.tsv', sep=',')
cur_result_pd = cur_result_pd.drop_duplicates()
white_list = cur_result_pd['mag_id'].tolist()
# ic(cur_result_pd['mag_id'].tolist()[:10])

hci_poaperids_df = pd.read_csv('mergeversiondata/HCI_paperids.tsv', sep='\t')
hci_poaperids_df = hci_poaperids_df.drop_duplicates()
# '/Users/yujie/Desktop/Project/TransferInCS/paperinformation_HCI.tsv'
result = []
ic(cur_result_pd.size, hci_poaperids_df.size)
count = 0
write_head = False
new_hci_poaperids_df = hci_poaperids_df.loc[~hci_poaperids_df["paper_id"].isin(white_list)]
ic(new_hci_poaperids_df.size)
# start again id: 2079191613
for index, line in tqdm(new_hci_poaperids_df.iterrows()):
    # if line[0] in white_list: continue
    mag_id = line[0]
    query = "https://api.semanticscholar.org/graph/v1/paper/MAG:{}?fields=paperId,externalIds,url,title,abstract,venue,year,referenceCount,citationCount,influentialCitationCount,isOpenAccess,fieldsOfStudy,s2FieldsOfStudy,publicationTypes,publicationDate,journal,authors".format(mag_id)
    paper_response = requests.get(query)
    # ic(paper_response.json())
    author_query = "https://api.semanticscholar.org/graph/v1/paper/MAG:{}/authors?fields=name,affiliations,paperCount,citationCount,url,homepage".format(mag_id)
    author_response = requests.get(author_query)
    # ic(author_response.json())
    try:
        result.append([mag_id, paper_response.json()["paperId"], paper_response.json()["externalIds"], paper_response.json()["url"],  paper_response.json()["title"].strip(), paper_response.json()["abstract"].replace("\n", "").replace(" \n \n", "") if paper_response.json()["abstract"] else "", paper_response.json()["venue"], paper_response.json()["year"], paper_response.json()["referenceCount"], paper_response.json()["citationCount"], paper_response.json()["influentialCitationCount"], paper_response.json()["isOpenAccess"], paper_response.json()["fieldsOfStudy"], paper_response.json()["s2FieldsOfStudy"], paper_response.json()["publicationTypes"], paper_response.json()["publicationDate"], paper_response.json()["journal"], author_response.json()])
    except:
        count += 1
        # ic(paper_response.json())
        if paper_response.json().get("message", "") == "Too Many Requests":
            result_pd = pd.DataFrame(data=result, columns=['mag_id', 'paperid', 'externalIds', 'url', 'title', 'abstract', 'venue', 'year', 'referenceCount', 'citationCount', 'influentialCitationCount', 'isOpenAccess', 'fieldsOfStudy', 's2FieldsOfStudy', 'publicationTypes', 'publicationDate', 'journal', 'authors'])
            result_pd.to_csv('mergeversiondata/paperinformation_' + str(conf_name) + '.tsv', mode='a', header=write_head, index=False, encoding='utf-8')
            write_head = False
            result = []
            while paper_response.json().get("message", "") == "Too Many Requests":
                time.sleep(180)
                ic()
                paper_response = requests.get(query)
            try:
                result.append([mag_id, paper_response.json()["paperId"], paper_response.json()["externalIds"], paper_response.json()["url"],  paper_response.json()["title"].strip(), paper_response.json()["abstract"].replace("\n", "").replace(" \n \n", "") if paper_response.json()["abstract"] else "", paper_response.json()["venue"], paper_response.json()["year"], paper_response.json()["referenceCount"], paper_response.json()["citationCount"], paper_response.json()["influentialCitationCount"], paper_response.json()["isOpenAccess"], paper_response.json()["fieldsOfStudy"], paper_response.json()["s2FieldsOfStudy"], paper_response.json()["publicationTypes"], paper_response.json()["publicationDate"], paper_response.json()["journal"], author_response])
            except:
                result.append([mag_id, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""])
        else:
            result.append([mag_id, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""])
result_pd = pd.DataFrame(data=result, columns=['mag_id', 'paperid', 'externalIds', 'url', 'title', 'abstract', 'venue', 'year', 'referenceCount', 'citationCount', 'influentialCitationCount', 'isOpenAccess', 'fieldsOfStudy', 's2FieldsOfStudy', 'publicationTypes', 'publicationDate', 'journal', 'authors'])
result_pd = result_pd.drop_duplicates()
result_pd.to_csv('mergeversiondata/paperinformation_' + str(conf_name) + '.tsv', mode='a', header=write_head, index=False, encoding='utf-8')
write_head = False
ic(count)
# hci_poaperids_df = pd.read_csv('/Users/yujie/Desktop/Project/TransferInCS/paperinformation_HCI.tsv', sep=',')
# for index, line in hci_poaperids_df.iterrows():
#     ic(line)

# https://api.semanticscholar.org/graph/v1/paper/MAG:2244265604/authors?fields=name,affiliations,paperCount,citationCount