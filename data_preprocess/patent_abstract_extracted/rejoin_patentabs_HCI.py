from itertools import chain
import pandas as pd
import os
data_CHI = list(chain(*pd.read_csv('/data/home/yujielu/project/pcs/papercitation2science_extracted/papercitationscience_result_CHI.tsv',sep=',',usecols=[4]).values.tolist()))
data_UBI = list(chain(*pd.read_csv('/data/home/yujielu/project/pcs/papercitation2science_extracted/papercitationscience_result_UBI.tsv', sep=',',usecols=[4]).values.tolist()))
data_CSCW = list(chain(*pd.read_csv('/data/home/yujielu/project/pcs/papercitation2science_extracted/papercitationscience_result_CSCW.tsv', sep=',',usecols=[4]).values.tolist()))
data_IMCL = list(chain(*pd.read_csv('/data/home/yujielu/project/pcs/papercitation2science_extracted/papercitationscience_result_IMCL.tsv', sep=',',usecols=[4]).values.tolist()))
data_UIST = list(chain(*pd.read_csv('/data/home/yujielu/project/pcs/papercitation2science_extracted/papercitationscience_result_UIST.tsv', sep=',',usecols=[4]).values.tolist()))

cnt = 0
result_CHI, result_UBI, result_CSCW, result_IMCL, result_UIST = [], [], [], [], []

# ori_patent_abstract = pd.read_csv('/data4/pcs/abstract/brf_sum_text.tsv', sep='\t')
# pd.set_option("display.max_colwidth", 100000)
files = os.listdir('old')
for file in files:
    print(file)
    cnt = 0
    old_file = open(os.path.join("/data/home/yujielu/project/pcs/patent_abstract_extracted/old", file))
    iter_f = iter(old_file)
    for row in iter_f:
        cnt += 1
        if cnt == 1:
            print(">>>")
            continue
        if cnt % 100000 == 0:
            print(cnt)
        uuid = str(row).split(',')[1]
        patent_id = str(row).split(',')[2]
        abstract = ""
        if len(str(row).split('\"')) > 1:
            abstract = str(row).split('\"')[1]
        patent_abstract_row = [uuid, patent_id, abstract]
        if patent_id in data_CHI:
            result_CHI.append(list(patent_abstract_row))
        if patent_id in data_UBI:
            result_UBI.append(list(patent_abstract_row))
        if patent_id in data_CSCW:
            result_CSCW.append(list(patent_abstract_row))
        if patent_id in data_IMCL:
            result_IMCL.append(list(patent_abstract_row))
        if patent_id in data_UIST:
            result_UIST.append(list(patent_abstract_row))
result_pd = pd.DataFrame(data=result_CHI, columns=['uuid', 'patent_id', 'abstract'])
result_pd.to_csv('new_patent_abstract_CHI.tsv')
result_pd = pd.DataFrame(data=result_UBI, columns=['uuid', 'patent_id', 'abstract'])
result_pd.to_csv('new_patent_abstract_UBI.tsv')
result_pd = pd.DataFrame(data=result_CSCW, columns=['uuid', 'patent_id', 'abstract'])
result_pd.to_csv('new_patent_abstract_CSCW.tsv')
result_pd = pd.DataFrame(data=result_IMCL, columns=['uuid', 'patent_id', 'abstract'])
result_pd.to_csv('new_patent_abstract_IMCL.tsv')
result_pd = pd.DataFrame(data=result_UIST, columns=['uuid', 'patent_id', 'abstract'])
result_pd.to_csv('new_patent_abstract_UIST.tsv')
