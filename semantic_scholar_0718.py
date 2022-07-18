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
hci_poaperids_df = pd.read_csv('HCI_paperids.tsv', sep='\t')
result = []
ic(hci_poaperids_df.size)
count = 0
write_head = True
for index, line in tqdm(hci_poaperids_df[start_idx:].iterrows()):
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
        count += 0
        # ic(paper_response.json())
        if paper_response.json().get("message", "") == "Too Many Requests":
            result_pd = pd.DataFrame(data=result, columns=['mag_id', 'paperid', 'externalIds', 'url', 'title', 'abstract', 'venue', 'year', 'referenceCount', 'citationCount', 'influentialCitationCount', 'isOpenAccess', 'fieldsOfStudy', 's2FieldsOfStudy', 'publicationTypes', 'publicationDate', 'journal', 'authors'])
            result_pd.to_csv('paperinformation_' + str(conf_name) + '.tsv', mode='a', header=write_head, index=False, encoding='utf-8')
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
result_pd.to_csv('paperinformation_' + str(conf_name) + '.tsv', mode='a', header=write_head, index=False, encoding='utf-8')
write_head = False
ic(count)
# hci_poaperids_df = pd.read_csv('/Users/yujie/Desktop/Project/TransferInCS/paperinformation_HCI.tsv', sep=',')
# for index, line in hci_poaperids_df.iterrows():
#     ic(line)

# https://api.semanticscholar.org/graph/v1/paper/MAG:2244265604/authors?fields=name,affiliations,paperCount,citationCount