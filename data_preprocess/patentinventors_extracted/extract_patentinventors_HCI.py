from itertools import chain
import pandas as pd
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
ori_patentinventors = pd.read_csv('/data/home/yujielu/project/pcs/patent_dblpdata/patent_inventor.tsv')
for row in ori_patentinventors.iterrows():
    cnt += 1
    if cnt == 1:
        print(">>>")
        continue
    if cnt % 100000 == 0:
        print(cnt)
    # print(row)
    patent_id = str(row[1]).split('    ')[1].split('\\t')[0]
    # print(patent_id)
    patentinventors_row = str(row[1]).replace("\"","").split('    ')[1].split('\n')[0].split('\\t')
    # print(patentinventors_row)
    # paperid_str = str(row[1]).split('    ')[1].split('\\t')[0] # paperid
    # paperrow_str = str(row[1]).split('    ')[1].split('\n')[0].split('\\t') # paper row
    # paperid = int(paperid_str)
    #paperid = 2025981437
    # print(patentinventors_row)
    if patent_id in data_CHI:
        #print(paperid)
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
