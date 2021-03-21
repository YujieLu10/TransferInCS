from itertools import chain
import pandas as pd
data_CHI = list(chain(*pd.read_csv('extracted_paperids/CHI_paperids.tsv',sep='\t',usecols=[0]).values.tolist()))
data_UBI = list(chain(*pd.read_csv('extracted_paperids/UbiComp_paperids.tsv', sep='\t', usecols=[0]).values.tolist()))
data_CSCW = list(chain(*pd.read_csv('extracted_paperids/CSCW_paperids.tsv', sep='\t', usecols=[0]).values.tolist()))
data_IMCL = list(chain(*pd.read_csv('extracted_paperids/IMCL_paperids.tsv', sep='\t', usecols=[0]).values.tolist()))
data_UIST = list(chain(*pd.read_csv('extracted_paperids/UIST_paperids.tsv', sep='\t', usecols=[0]).values.tolist()))
#paper_list = data_CHI + data_UBI + data_CSCW + data_IMCL + data_UIST
#paper_list = list(chain(*paper_list))
results = {'result_CHI':[], 'result_UBI':[], 'result_CSCW':[], 'result_IMCL':[], 'result_UIST':[]}
#result_CHI, result_UBI, result_CSCW, result_IMCL, result_UIST = [], [], [], [], []
#ori_pd = pd.read_csv('/data/pcsdata/selected_MAG_metadata/paperyear.tsv',skiprows=1,nrows=2)
ori_file = open('/data/pcsdata/selected_MAG_metadata/paperyear.tsv')
iter_f = iter(ori_file)
first_line = True
cnt = 0
for row in iter_f:
    if first_line:
        first_line = False
        continue
    cnt += 1
    if cnt % 100000 == 0:
        print(cnt)
    paperid_str = str(row).split()[0] # paperid
    paperrow_str = str(row).split() # paper row
    paperid = int(paperid_str)
    #print(paperid)
    #print(paperrow_str)
    #paperid = 2025981437
    if paperid in data_CHI:
        #print(paperrow_str)
        results['result_CHI'].append(list(paperrow_str))
    elif paperid in data_UBI:
        results['result_UBI'].append(list(paperrow_str))
    elif paperid in data_CSCW:
        results['result_CSCW'].append(list(paperrow_str))
    elif paperid in data_IMCL:
        results['result_IMCL'].append(list(paperrow_str))
    elif paperid in data_UIST:
        results['result_UIST'].append(list(paperrow_str))
#outfile.write(result)
for name, result in results.items():
    result_pd = pd.DataFrame(data=result, columns=['paperid', 'year'])
    result_pd.to_csv('paperyear_' + str(name) + '.tsv')
#result_pd = pd.DataFrame(data=result_CHI, columns=['paperid', 'authorid', 'authororder'])
#result_pd.to_csv('paperauthororder_CHI.tsv')
#result_pd = pd.DataFrame(data=result_UBI, columns=['paperid', 'authorid', 'authororder'])
#result_pd.to_csv('paperauthororder_UBI.tsv')
#result_pd = pd.DataFrame(data=result_CSCW, columns=['paperid', 'authorid', 'authororder'])
#result_pd.to_csv('paperauthororder_CSCW.tsv')
#result_pd = pd.DataFrame(data=result_IMCL, columns=['paperid', 'authorid', 'authororder'])
#result_pd.to_csv('paperauthororder_IMCL.tsv')
#result_pd = pd.DataFrame(data=result_UIST, columns=['paperid', 'authorid', 'authororder'])
#result_pd.to_csv('paperauthororder_UIST.tsv')
