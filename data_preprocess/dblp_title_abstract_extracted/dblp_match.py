# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import pandas as pd

for conf_name in ['CHI', 'CSCW', 'UBI', 'UIST']:
    hci_tilte = pd.read_csv("../papertitles_extracted/papertitle_{}.tsv".format(conf_name), sep = ",")

    hci_tilte['papertitle'] = [title.encode('utf-8').strip().lower() for title in hci_tilte['title']]

    from fuzzywuzzy import process

    # matched = 'Technology heirlooms?: considerations fo passing down and inheriting digital materials.'
    # print(papers['papertitle'].iloc[0])
    # highest = process.extractOne(str(papers['papertitle'].iloc[0]), hci_title['papertitle'])
    # print(highest)

    result = []
    with open('dblp_{}_title.tsv'.format(conf_name), "r") as title_f:
        for line in title_f:
            paper_idx = line[0:line.index(',')]
            paper_title = line[line.index(',') + 1:]
            highest = process.extractOne(paper_title, hci_tilte['papertitle'])
            print(highest)
            try:
                output = [highest[0], highest[1], highest[2], paper_idx]
                result.append(list(output))
            except:
                print(">>> error")
        result_pd = pd.DataFrame(data=result, columns=['papertitle', 'score', 'paperidx', 'dblppaperidx'])
        result_pd.to_csv('matched_{}.tsv'.format(conf_name))
