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
cnt = 0
#print(data_CHI)
result_CHI, result_UBI, result_CSCW, result_IMCL, result_UIST = [], [], [], [], []
files = os.listdir("/data1/mag_data/splited_papercitations")
for file in files:
    print(file)
    cnt = 0
    #paper_citation_file = pd.read_csv(os.path.join("/data1/mag_data/splited_papercitations",file), nrows=10) 
    paper_citation_file = open(os.path.join("/data1/mag_data/splited_papercitations", file))
    iter_f = iter(paper_citation_file)
    for row in iter_f:
        cnt += 1
        if cnt == 1 and file == "splited_papercitations_0.tsv":
            print(">>>")
            continue
        citing_paperid_str = str(row).split()[0].split(',')[1] # paperid
        cited_paperid_str = str(row).split()[1]
        #print(citing_paperid_str)
        #print(cited_paperid_str)
        paperrow_str = str(row).split(',')[1].split() # paper row
        #print(paperrow_str)
        paperid = int(citing_paperid_str)
        paperid2 = int(cited_paperid_str)
        if paperid in data_CHI or paperid2 in data_CHI:
            result_CHI.append(list(paperrow_str))
        elif paperid in data_UBI or paperid2 in data_UBI:
            result_UBI.append(list(paperrow_str))
        elif paperid in data_CSCW or paperid2 in data_CSCW:
            result_CSCW.append(list(paperrow_str))
        elif paperid in data_IMCL or paperid2 in data_IMCL:
            result_IMCL.append(list(paperrow_str))
        elif paperid in data_UIST or paperid2 in data_UIST:
            result_UIST.append(list(paperrow_str))
    #outfile.write(result)
    result_pd = pd.DataFrame(data=result_CHI, columns=['citingpaperid', 'citedpaperid'])
    result_pd.to_csv('papercitations_CHI.tsv')
    result_pd = pd.DataFrame(data=result_UBI, columns=['citingpaperid', 'citedpaperid'])
    result_pd.to_csv('papercitations_UBI.tsv')
    result_pd = pd.DataFrame(data=result_CSCW, columns=['citingpaperid', 'citedpaperid'])
    result_pd.to_csv('papercitations_CSCW.tsv')
    result_pd = pd.DataFrame(data=result_IMCL, columns=['citingpaperid', 'citedpaperid'])
    result_pd.to_csv('papercitations_IMCL.tsv')
    result_pd = pd.DataFrame(data=result_UIST, columns=['citingpaperid', 'citedpaperid'])
    result_pd.to_csv('papercitations_UIST.tsv')
