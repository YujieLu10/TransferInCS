from itertools import chain
import pandas as pd
import os

data_CHI = list(chain(*pd.read_csv('/data/home/yujielu/project/pcs/papercitation2science_extracted/papercitationscience_result_CHI.tsv',sep=',',usecols=[4]).values.tolist()))
data_UBI = list(chain(*pd.read_csv('/data/home/yujielu/project/pcs/papercitation2science_extracted/papercitationscience_result_UBI.tsv', sep=',',usecols=[4]).values.tolist()))
data_CSCW = list(chain(*pd.read_csv('/data/home/yujielu/project/pcs/papercitation2science_extracted/papercitationscience_result_CSCW.tsv', sep=',',usecols=[4]).values.tolist()))
data_IMCL = list(chain(*pd.read_csv('/data/home/yujielu/project/pcs/papercitation2science_extracted/papercitationscience_result_IMCL.tsv', sep=',',usecols=[4]).values.tolist()))
data_UIST = list(chain(*pd.read_csv('/data/home/yujielu/project/pcs/papercitation2science_extracted/papercitationscience_result_UIST.tsv', sep=',',usecols=[4]).values.tolist()))
#paper_list = data_CHI + data_UBI + data_CSCW + data_IMCL + data_UIST
#paper_list = list(chain(*paper_list))
cnt = 0
# print(data_CHI)
result_CHI, result_UBI, result_CSCW, result_IMCL, result_UIST = [], [], [], [], []

files = os.listdir('old')
for file in files:
    print(file)
    cnt = 0
    old_file = open(os.path.join("/data/home/yujielu/project/pcs/patentinventors_extracted/old", file))
    iter_f = iter(old_file)
    for row in iter_f:
        cnt += 1
        if cnt == 1:
            print(">>>")
            continue
        if cnt % 100000 == 0:
            print(cnt)
        patent_id = str(row).split(',')[1]
        inventor_id = str(row).split(',')[2]
        location_id = str(row).split(',')[3].split("\"")[0].strip()
        patentinventors_row = [patent_id, inventor_id, location_id]

        if patent_id in data_CHI:
            result_CHI.append(list(patentinventors_row))
        if patent_id in data_UBI:
            result_UBI.append(list(patentinventors_row))
        if patent_id in data_CSCW:
            result_CSCW.append(list(patentinventors_row))
        if patent_id in data_IMCL:
            result_IMCL.append(list(patentinventors_row))
        if patent_id in data_UIST:
            result_UIST.append(list(patentinventors_row))

#outfile.write(result)
result_pd = pd.DataFrame(data=result_CHI, columns=['patent_id', 'inventor_id', 'location_id'])
result_pd.to_csv('patentinventors_CHI.tsv')
result_pd = pd.DataFrame(data=result_UBI, columns=['patent_id', 'inventor_id', 'location_id'])
result_pd.to_csv('patentinventors_UBI.tsv')
result_pd = pd.DataFrame(data=result_CSCW, columns=['patent_id', 'inventor_id', 'location_id'])
result_pd.to_csv('patentinventors_CSCW.tsv')
result_pd = pd.DataFrame(data=result_IMCL, columns=['patent_id', 'inventor_id', 'location_id'])
result_pd.to_csv('patentinventors_IMCL.tsv')
result_pd = pd.DataFrame(data=result_UIST, columns=['patent_id', 'inventor_id', 'location_id'])
result_pd.to_csv('patentinventors_UIST.tsv')
