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
ori_paperauthor = pd.read_csv('paperauthororder.tsv')
for row in ori_paperauthor.iterrows():
    cnt += 1
    if cnt == 1:
        print(">>>")
        continue
    if cnt % 100000 == 0:
        print(cnt)
    paperid_str = str(row[1]).split('    ')[1].split('\\t')[0] # paperid
    paperrow_str = str(row[1]).split('    ')[1].split('\n')[0].split('\\t') # paper row
    paperid = int(paperid_str)
    #paperid = 2025981437
    #print(paperrow_str)
    if paperid in data_CHI:
        #print(paperid)
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
result_pd = pd.DataFrame(data=result_CHI, columns=['paperid', 'authorid', 'authororder'])
result_pd.to_csv('paperauthororder_CHI.tsv')
result_pd = pd.DataFrame(data=result_UBI, columns=['paperid', 'authorid', 'authororder'])
result_pd.to_csv('paperauthororder_UBI.tsv')
result_pd = pd.DataFrame(data=result_CSCW, columns=['paperid', 'authorid', 'authororder'])
result_pd.to_csv('paperauthororder_CSCW.tsv')
result_pd = pd.DataFrame(data=result_IMCL, columns=['paperid', 'authorid', 'authororder'])
result_pd.to_csv('paperauthororder_IMCL.tsv')
result_pd = pd.DataFrame(data=result_UIST, columns=['paperid', 'authorid', 'authororder'])
result_pd.to_csv('paperauthororder_UIST.tsv')
