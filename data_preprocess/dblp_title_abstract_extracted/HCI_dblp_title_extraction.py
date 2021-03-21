# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import pandas as pd

import json
paper = []
for line in open('dblp_papers_with_s2_abstracts.jsonlist', 'r'):
    paper.append(json.loads(line))
df = pd.DataFrame(paper)

papers = df[(df['dblp_venue'] == 'CHI')| (df['dblp_venue'] == 'CSCW') | 
            (df['dblp_venue'] == 'UIST') | (df['dblp_venue'] == 'IMCL') |
            (df['dblp_venue'] == 'UbiComp')]

papers_CHI = df[(df['dblp_venue'] == 'CHI')]
papers_CSCW = df[(df['dblp_venue'] == 'CSCW')]
papers_UIST = df[(df['dblp_venue'] == 'UIST')]
papers_IMCL = df[(df['dblp_venue'] == 'IMCL')]
papers_UBI = df[(df['dblp_venue'] == 'UbiComp')]

papers_CHI = papers_CHI[['dblp_title', 'dblp_venue', 's2_abstract']]
papers_CHI['papertitle'] = [title.encode('utf-8').strip().lower() for title in papers_CHI['dblp_title']]

papers_CSCW = papers_CSCW[['dblp_title', 'dblp_venue', 's2_abstract']]
papers_CSCW['papertitle'] = [title.encode('utf-8').strip().lower() for title in papers_CSCW['dblp_title']]

papers_UIST = papers_UIST[['dblp_title', 'dblp_venue', 's2_abstract']]
papers_UIST['papertitle'] = [title.encode('utf-8').strip().lower() for title in papers_UIST['dblp_title']]

papers_IMCL = papers_IMCL[['dblp_title', 'dblp_venue', 's2_abstract']]
papers_IMCL['papertitle'] = [title.encode('utf-8').strip().lower() for title in papers_IMCL['dblp_title']]

papers_UBI = papers_UBI[['dblp_title', 'dblp_venue', 's2_abstract']]
papers_UBI['papertitle'] = [title.encode('utf-8').strip().lower() for title in papers_UBI['dblp_title']]

papers_CHI['papertitle'].to_csv('dblp_CHI_title.tsv')
papers_CSCW['papertitle'].to_csv('dblp_CSCW_title.tsv')
papers_UIST['papertitle'].to_csv('dblp_UIST_title.tsv')
papers_IMCL['papertitle'].to_csv('dblp_IMCL_title.tsv')
papers_UBI['papertitle'].to_csv('dblp_UBI_title.tsv')

papers_CHI['s2_abstract'].to_csv('dblp_CHI_abstract.tsv')
papers_CSCW['s2_abstract'].to_csv('dblp_CSCW_abstract.tsv')
papers_UIST['s2_abstract'].to_csv('dblp_UIST_abstract.tsv')
papers_IMCL['s2_abstract'].to_csv('dblp_IMCL_abstract.tsv')
papers_UBI['s2_abstract'].to_csv('dblp_UBI_abstract.tsv')
