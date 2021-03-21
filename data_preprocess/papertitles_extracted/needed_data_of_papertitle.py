import os
from itertools import chain
import pandas as pd
data_CHI = list(chain(*pd.read_csv('extracted_paperids/CHI_paperids.tsv',sep='\t',usecols=[0]).values.tolist()))
data_UBI = list(chain(*pd.read_csv('extracted_paperids/UbiComp_paperids.tsv', sep='\t', usecols=[0]).values.tolist()))
data_CSCW = list(chain(*pd.read_csv('extracted_paperids/CSCW_paperids.tsv', sep='\t', usecols=[0]).values.tolist()))
data_IMCL = list(chain(*pd.read_csv('extracted_paperids/IMCL_paperids.tsv', sep='\t', usecols=[0]).values.tolist()))
data_UIST = list(chain(*pd.read_csv('extracted_paperids/UIST_paperids.tsv', sep='\t', usecols=[0]).values.tolist()))
#paper_list = data_CHI + data_UBI + data_CSCW + data_IMCL + data_UIST
#paper_list = list(chain(*paper_list))
#print(data_CHI)
result_CHI, result_UBI, result_CSCW, result_IMCL, result_UIST = [], [], [], [], []
files = os.listdir("/data1/mag_data/splited_papertitle")
cnt = 0
for file in files:
    cnt = 0
    print(file)
    #paper_citation_file = pd.read_csv(os.path.join("/data1/mag_data/splited_papercitations",file), nrows=10) 
    title_file = open(os.path.join("/data1/mag_data/splited_papertitle", file))
    iter_f = iter(title_file)
    for row in iter_f:
        if file == "split_papertitle_0.tsv" and cnt == 0:
            cnt += 1
            print(">>>")
            continue
        cnt += 1
        if cnt % 100000 == 0:
            print(cnt)
        paperid_str = str(row).split()[0].split(',')[1] # paperid
        #print(citing_paperid_str)
        paperrow_str = str(row).split(',')[1].split() # paper row
        #print(paperrow_str)
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
result_pd = pd.DataFrame(data=result_CHI, columns=['paperid', 'title'])
result_pd.to_csv('papertitle_CHI.tsv')
result_pd = pd.DataFrame(data=result_UBI, columns=['paperid', 'title'])
result_pd.to_csv('papertitle_UBI.tsv')
result_pd = pd.DataFrame(data=result_CSCW, columns=['paperid', 'title'])
result_pd.to_csv('papertitle_CSCW.tsv')
result_pd = pd.DataFrame(data=result_IMCL, columns=['paperid', 'title'])
result_pd.to_csv('papertitle_IMCL.tsv')
result_pd = pd.DataFrame(data=result_UIST, columns=['paperid', 'title'])
result_pd.to_csv('papertitle_UIST.tsv')
