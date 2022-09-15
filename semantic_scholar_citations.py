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
cur_result_pd = pd.read_csv('paper_academia_peak_HCI.tsv', sep=',')
cur_result_pd = cur_result_pd.drop_duplicates()
history_list = cur_result_pd['mag_id'].tolist()
# # ic(cur_result_pd['mag_id'].tolist()[:10])

hci_poaperids_df = pd.read_csv('dataAug10/mergeversiondata/HCI_paperids.tsv', sep='\t')
hci_poaperids_df = hci_poaperids_df.drop_duplicates()
# '/Users/yujie/Desktop/Project/TransferInCS/paperinformation_HCI.tsv'
result = []
# ic(cur_result_pd.size, hci_poaperids_df.size)
write_head = False
new_hci_poaperids_df = hci_poaperids_df.loc[~hci_poaperids_df["paper_id"].isin(history_list)]
# start again id: 2079191613
def most_common(lst):
    return max(set(lst), key=lst.count)

for index, line in tqdm(new_hci_poaperids_df.iterrows()):
    # if line[0] in white_list: continue
    mag_id = line[0]
    query = "https://api.semanticscholar.org/graph/v1/paper/MAG:{}?fields=year,citations.year".format(mag_id)
    paper_response = requests.get(query)
    # ic(paper_response.json()["citations"])
    try:
        try:
            cite_list = paper_response.json()["citations"]
        except:
            result.append([mag_id, paper_response.json()["year"], -1, -1])
        peak_year_list = []
        for item in cite_list:
            peak_year_list.append(item["year"])
        if not len(peak_year_list):
            # non-paper-cited
            result.append([mag_id, paper_response.json()["year"], -1, -1])
            continue
        peak_year = most_common(peak_year_list)
        peak_year_lag = peak_year - paper_response.json()["year"]

        result.append([mag_id, paper_response.json()["year"], peak_year, peak_year_lag])
    except:
        if paper_response.json().get("message", "") == "Too Many Requests":
            result_pd = pd.DataFrame(data=result, columns=['mag_id', 'year', 'peak_year', 'peak_year_lag'])
            result_pd.to_csv('paper_academia_peak_' + str(conf_name) + '.tsv', mode='a', header=write_head, index=False, encoding='utf-8')
            
            write_head = False
            result = []
            while paper_response.json().get("message", "") == "Too Many Requests":
                time.sleep(180)
                ic()
                paper_response = requests.get(query)
            try:
                result.append([mag_id, paper_response.json()["year"], peak_year, peak_year_lag])
            except:
                result.append([mag_id, "", "", ""])
        else:
            result.append([mag_id, "", "", ""])
result_pd = pd.DataFrame(data=result, columns=['mag_id', 'year', 'peak_year', 'peak_year_lag'])
result_pd.to_csv('paper_academia_peak_' + str(conf_name) + '.tsv', mode='a', header=write_head, index=False, encoding='utf-8')
write_head = False