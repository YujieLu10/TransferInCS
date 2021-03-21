from itertools import chain
import pandas as pd
data_CHI = pd.read_csv('/data1/mag_data/extracted_paperids/CHI_paperids.tsv',sep='\t',usecols=[0]).values.tolist()
data_UBI = pd.read_csv('/data1/mag_data/extracted_paperids/UbiComp_paperids.tsv', sep='\t', usecols=[0]).values.tolist()
data_CSCW = pd.read_csv('/data1/mag_data/extracted_paperids/CSCW_paperids.tsv', sep='\t', usecols=[0]).values.tolist()
data_IMCL = pd.read_csv('/data1/mag_data/extracted_paperids/IMCL_paperids.tsv', sep='\t', usecols=[0]).values.tolist()
data_UIST = pd.read_csv('/data1/mag_data/extracted_paperids/UIST_paperids.tsv', sep='\t', usecols=[0]).values.tolist()
data_CHI = list(chain(*data_CHI))
data_UBI = list(chain(*data_UBI))
data_CSCW = list(chain(*data_CSCW))
data_IMCL = list(chain(*data_IMCL))
data_UIST = list(chain(*data_UIST))
results = {'result_CHI':[], 'result_UBI':[], 'result_CSCW':[], 'result_IMCL':[], 'result_UIST':[]}
ori_file = open('/data/pcsdata/pcs.tsv')
iter_f = iter(ori_file)
first_line = True
for row in iter_f:
    if first_line:
        first_line = False
        continue
    paperrow_str = str(row).split() # paper row
    paperid_str = paperrow_str[2]
    paperid = int(paperid_str)
    if paperid in data_CHI:
        results['result_CHI'].append(list(paperrow_str))
    elif paperid in data_UBI:
        results['result_UBI'].append(list(paperrow_str))
    elif paperid in data_CSCW:
        results['result_CSCW'].append(list(paperrow_str))
    elif paperid in data_IMCL:
        results['result_IMCL'].append(list(paperrow_str))
    elif paperid in data_UIST:
        results['result_UIST'].append(list(paperrow_str))
for name, result in results.items():
    result_pd = pd.DataFrame(data=result, columns=['reftype', 'confscore', 'paperid', 'patent'])
    result_pd.to_csv('papercitationscience_' + str(name) + '.tsv')
