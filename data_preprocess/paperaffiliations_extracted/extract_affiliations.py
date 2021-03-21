import os
from itertools import chain
import pandas as pd
data_CHI = list(chain(*pd.read_csv('../paperauthororder_extracted/paperauthororder_CHI.tsv',sep='\t',usecols=[0]).values.tolist()))
data_UBI = list(chain(*pd.read_csv('../paperauthororder_extracted/paperauthororder_UBI.tsv', sep='\t', usecols=[0]).values.tolist()))
data_CSCW = list(chain(*pd.read_csv('../paperauthororder_extracted/paperauthororder_CSCW.tsv', sep='\t', usecols=[0]).values.tolist()))
data_IMCL = list(chain(*pd.read_csv('../paperauthororder_extracted/paperauthororder_IMCL.tsv', sep='\t', usecols=[0]).values.tolist()))
data_UIST = list(chain(*pd.read_csv('../paperauthororder_extracted/paperauthororder_UIST.tsv', sep='\t', usecols=[0]).values.tolist()))
#paper_list = data_CHI + data_UBI + data_CSCW + data_IMCL + data_UIST
#paper_list = list(chain(*paper_list))
# print(data_CHI)
result_CHI, result_UBI, result_CSCW, result_IMCL, result_UIST = [], [], [], [], []
# ori_file = open("/data4/pcs/papertitle.tsv", nrows=100)
ori_pd = pd.read_csv('paperauthoridaffiliationname.tsv', sep='\t')
pd.set_option("display.max_colwidth", 100000)
# iter_f = iter(ori_file)
first_line = True
cnt = 0
for row in ori_pd.iterrows():
    if first_line == True:
        first_line = False
        print(">>>")
        continue
    cnt += 1
    if cnt % 100000 == 0:
        print(cnt)
    
    paperid_str = str(row[1]).split('\n')[0].split()[1]
    authorid = str(row[1]).split('\n')[1].split()[1]
    affiliationname = str(row[1]).split('\n')[2].split()[1]

    paperrow_str = [paperid_str, authorid, affiliationname]
    # print(paperrow_str)
    paperid = int(paperid_str)
    if paperid in data_CHI:
        result_CHI.append(list(paperrow_str))
    elif paperid in data_UBI:
        result_UBI.append(list(paperrow_str))
    elif paperid in data_CSCW:
        result_CSCW.append(list(paperrow_str))
    elif paperid in data_IMCL:
        result_IMCL.append(list(paperrow_str))
    elif paperid in data_UIST:
        result_UIST.append(list(paperrow_str))
#outfile.write(result)
result_pd = pd.DataFrame(data=result_CHI, columns=['paperid', 'authorid', 'affiliationname'])
result_pd.to_csv('authoraffname_CHI.tsv')
result_pd = pd.DataFrame(data=result_UBI, columns=['paperid', 'authorid', 'affiliationname'])
result_pd.to_csv('authoraffname_UBI.tsv')
result_pd = pd.DataFrame(data=result_CSCW, columns=['paperid', 'authorid', 'affiliationname'])
result_pd.to_csv('authoraffname_CSCW.tsv')
result_pd = pd.DataFrame(data=result_IMCL, columns=['paperid', 'authorid', 'affiliationname'])
result_pd.to_csv('authoraffname_IMCL.tsv')
result_pd = pd.DataFrame(data=result_UIST, columns=['paperid', 'authorid', 'affiliationname'])
result_pd.to_csv('authoraffname_UIST.tsv')
