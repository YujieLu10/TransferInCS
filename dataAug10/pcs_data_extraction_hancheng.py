#------------ paper year -------------# data source:/data/pcsdata/selected_MAG_metadata/paperyear.tsv
from itertools import chain
import pandas as pd
# data_HCI = list(chain(*pd.read_csv('../data/HCI_paperids.tsv',sep=',').values.tolist()))
data_HCI = pd.read_csv('HCI_paperids.tsv',sep='\t')
data_HCI.head(10)
conf_name_map = {1163450153:'CHI', 1195049314:'CSCW', 1171345118:'UBI', 1166315290:'UIST'}

## faster implementation for detecting author affiliation at paper level
f = open('paperauthoridaffiliationname.tsv')
paper_author_affiliation = {}
paper_author_id = {}
line = f.readline()
while line:
    paperid = line.split('\t')[0]
    authorid = line.split('\t')[1]
    affiliation = line.split('\t')[2][:-1]
    if paperid not in paper_author_affiliation:
        paper_author_id[paperid] = [authorid]
        paper_author_affiliation[paperid] = [affiliation]
    else:
        paper_author_id[paperid].append(authorid)
        paper_author_affiliation[paperid].append(affiliation)
    line = f.readline()
## get author affiliation, id level information related to hci conferences
Paperid = []
Affiliation = []
AuthorId = []
for paperid in data_HCI['paper_id']:
    paperid = str(paperid)
    try:
        
        Affiliation.append(paper_author_affiliation[paperid])
        AuthorId.append(paper_author_id[paperid])
        Paperid.append(paperid)
    except:
        pass
df = pd.DataFrame({'paperid':Paperid, 'authorid':AuthorId,'Affiliation':Affiliation})
df.to_csv('HCI_paper_authorid_affiliation.tsv',sep='\t', index=False,encoding='utf-8')