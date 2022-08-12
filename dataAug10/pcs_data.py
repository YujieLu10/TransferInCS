#------------ paper year -------------# data source:/data/pcsdata/selected_MAG_metadata/paperyear.tsv
from itertools import chain
import pandas as pd

import argparse
from icecream import ic

parser = argparse.ArgumentParser(description='PCS')
parser.add_argument('--extract', default="NA", help='type')
args = parser.parse_args()

# data_HCI = list(chain(*pd.read_csv('../dataAug10/HCI_paperids.tsv',sep=',').values.tolist()))
data_HCI = pd.read_csv('../dataAug10/HCI_paperids.tsv',sep='\t')
data_HCI = data_HCI.drop_duplicates()
data_HCI.head(10)
conf_name_map = {1163450153:'CHI', 1195049314:'CSCW', 1171345118:'UBI', 1166315290:'UIST'}
if args.extract == "paperyear":
    results = {'result_CHI':[], 'result_UBI':[], 'result_CSCW':[], 'result_UIST':[]}
    ori_file = open('../dataAug10/paperyear.tsv')
    conf_name_map = {1163450153:'CHI', 1195049314:'CSCW', 1171345118:'UBI', 1166315290:'UIST'}
    # conf_name_map could also load by category
    # data_category = pd.read_csv('../dataAug10/category.tsv',sep=',')
    # data_category = data_category.loc[data_category['category']=="AI"]
    # for row in data_category.iterrows():
    #     conf_name_map[row[0]] = row[1]

    iter_f = iter(ori_file)
    first_line = True
    for row in iter_f:
        if first_line:
            first_line = False
            continue
        paperid_str = str(row).split()[0] # paperid
        paperrow_str = str(row).split() # paper row
        paperid = int(paperid_str)
        if paperid in data_HCI['paper_id'].values:
            results['result_{}'.format(conf_name_map[int(data_HCI.loc[data_HCI['paper_id']==paperid]['conf_id'].values)])].append(list(paperrow_str))
    for name, result in results.items():
        result_pd = pd.DataFrame(data=result, columns=['paperid', 'year'])
        result_pd.to_csv('paperyear_' + str(name) + '.tsv')
    print(">>> done")
elif args.extract == "papertitle":
    #------------ paper titles -------------# data source: /data4/pcs/papertitle.tsv
    import os
    from itertools import chain
    import pandas as pd

    results_title = {'result_CHI':[], 'result_UBI':[], 'result_CSCW':[], 'result_UIST':[]}
    ori_pd = pd.read_csv('../dataAug10/papertitle.tsv', skiprows=1)
    pd.set_option("display.max_colwidth", 100000)

    for row in ori_pd.iterrows():
        paperid_str = str(row[1]).split('\\t')[1].split()[1] # paperid
        paper_title = str(row[1]).split('\\t')[2].split('\n')[0]
        paperrow_str = [paperid_str, paper_title]
        paperid = int(paperid_str)
        if paperid in data_HCI['paper_id'].values:
            results['result_{}'.format(conf_name_map[int(data_HCI.loc[data_HCI['paper_id']==paperid]['conf_id'].values)])].append(list(paperrow_str))
            
    for name, result in results_title.items():
        result_pd = pd.DataFrame(data=result, columns=['paperid', 'title'])
        result_pd.to_csv('papertitle_' + str(name) + '.tsv')
    print(">>> done")
elif args.extract == "paperauthororder":
    #------------ paper author order -------------#
    from itertools import chain
    import pandas as pd
    from icecream import ic

    results_author = {'result_CHI':[], 'result_UBI':[], 'result_CSCW':[], 'result_UIST':[]}
    ori_paperauthor = pd.read_csv('../dataAug10/paperauthororder.tsv', sep='\t')
    for conf_name in ["CHI", "CSCW", "UbiComp", "UIST"]:
        ori_conf = pd.read_csv('../dataAug10/{}_paperids.tsv'.format(conf_name),sep='\t')
        conf_paperauthor = ori_conf.merge(ori_paperauthor, left_on='paper_id', right_on="paperid")
        conf_paperauthor = conf_paperauthor.drop_duplicates().drop(columns=['paper_id'])
        conf_paperauthor.to_csv('paperauthororder_' + str(conf_name) + '.tsv')
    # for row in ori_paperauthor.iterrows():
    #     paperid_str = str(row[1]).split('    ')[1].split('\\t')[0] # paperid
    #     paperrow_str = str(row[1]).split('    ')[1].split('\n')[0].split('\\t') # paper row
    #     paperid = int(paperid_str)

    #     if paperid in data_HCI['paper_id'].values:
    #         results_author['result_{}'.format(conf_name_map[int(data_HCI.loc[data_HCI['paper_id']==paperid]['conf_id'].values)])].append(list(paperrow_str))

    # for name, result in results_author.items():
    #     result_pd = pd.DataFrame(data=result, columns=['paperid', 'authorid', 'authororder'])
    #     result_pd.to_csv('paperauthororder_' + str(name) + '.tsv')
    print(">>> done")
elif args.extract == "affiliation":
    #------------ paper affiliations -------------#
    import os
    from itertools import chain
    import pandas as pd

    results_affiliation = {'result_CHI':[], 'result_UBI':[], 'result_CSCW':[], 'result_UIST':[]}
    ori_pd = pd.read_csv('../dataAug10/paperauthoridaffiliationname.tsv', sep='\t', skiprows=1)
    pd.set_option("display.max_colwidth", 100000)

    for row in ori_pd.iterrows():
        paperid_str = str(row[1]).split('\n')[0].split()[1]
        authorid = str(row[1]).split('\n')[1].split()[1]
        affiliationname = str(row[1]).split('\n')[2].split()[1]
        paperrow_str = [paperid_str, authorid, affiliationname]
        paperid = int(paperid_str)

        if paperid in data_HCI['paper_id'].values:
            results_affiliation['result_{}'.format(conf_name_map[int(data_HCI.loc[data_HCI['paper_id']==paperid]['conf_id'].values)])].append(list(paperrow_str))

    for name, result in results_affiliation.items():
        result_pd = pd.DataFrame(data=result, columns=['paperid', 'authorid', 'affiliationname'])
        result_pd.to_csv('authoraffname_' + str(name) + '.tsv')
    print(">>> done")
elif args.extract == "papercitations":
    #------------ paper citations -------------# data source: /data4/pcs/papercitations
    import os
    from itertools import chain
    import pandas as pd

    results_citing = {'result_CHI':[], 'result_UBI':[], 'result_CSCW':[], 'result_UIST':[]}
    results_cited = {'result_CHI':[], 'result_UBI':[], 'result_CSCW':[], 'result_UIST':[]}

    ori_papercitations = pd.read_csv('../dataAug10/papercitations/papercitations.tsv', sep='\t')
    for conf_name in ["CHI", "CSCW", "UbiComp", "UIST"]:
        ori_conf = pd.read_csv('../dataAug10/{}_paperids.tsv'.format(conf_name),sep='\t')
        conf_papercitations_citing = ori_conf.merge(ori_papercitations, left_on="paper_id", right_on="citingpaperid")
        conf_papercitations_citing = conf_papercitations_citing.drop_duplicates()
        conf_papercitations_citing.to_csv('paperciting_' + str(conf_name) + '.tsv')

        conf_papercitations_cited = ori_conf.merge(ori_papercitations, left_on="paper_id", right_on="citedpaperid")
        conf_papercitations_cited = conf_papercitations_cited.drop_duplicates()
        conf_papercitations_cited.to_csv('papercited_' + str(conf_name) + '.tsv')
    # all citation raw file are listed in papercitations directory
    # files = os.listdir("../dataAug10/papercitations")
    # for file in files:
    #     firstline = True
    #     paper_citation_file = open(os.path.join("../dataAug10/papercitations", file))
    #     iter_f = iter(paper_citation_file)
    #     for row in iter_f:
    #         if firstline:
    #             firstline = False
    #             continue
    #         if len(str(row).split()) < 2:
    #             continue
    #         citing_paperid_str = str(row).split()[0] # citingpaperid
    #         cited_paperid_str = str(row).split()[1]
    #         paperrow_str = [citing_paperid_str, cited_paperid_str]
    #         paperid = int(citing_paperid_str)
    #         paperid2 = int(cited_paperid_str)
    #         if paperid in data_HCI['paper_id'].values:
    #             results_citing['result_{}'.format(conf_name_map[int(data_HCI.loc[data_HCI['paper_id']==paperid]['conf_id'].values)])].append(list(paperrow_str))

    #         if paperid2 in data_HCI['paper_id'].values:
    #             results_cited['result_{}'.format(conf_name_map[int(data_HCI.loc[data_HCI['paper_id']==paperid2]['conf_id'].values)])].append(list(paperrow_str))

    # for name, result in results_citing.items():
    #     result_pd = pd.DataFrame(data=result, columns=['citingpaperid', 'citedpaperid'])
    #     result_pd.to_csv('paperciting_' + str(name) + '.tsv')

    # for name, result in results_cited.items():
    #     result_pd = pd.DataFrame(data=result, columns=['citingpaperid', 'citedpaperid'])
    #     result_pd.to_csv('papercited_' + str(name) + '.tsv')

    print(">>> done")
elif args.extract == "pcs":
    #------------ paper citations science -------------# data source: /data/pcsdata/pcs.tsv
    from itertools import chain
    import pandas as pd
    pcs_pd = pd.read_csv('../dataAug10/pcs_mag_doi_pmid.tsv', sep='\t')
    for conf_name in ["CHI", "CSCW", "UbiComp", "UIST"]:
        HCI_filter_df_paperid = pd.read_csv('/local/home/yujielu/project/TransferInCS/dataAug10/{}_paperids.tsv'.format(conf_name), sep='\t')
        conf_paper_list = HCI_filter_df_paperid['paper_id'].tolist()
        conf_pd = pcs_pd.loc[pcs_pd["magid"].isin(conf_paper_list)]
        conf_pd.to_csv('papercitationscience_' + conf_name + '.tsv', index=False)
    
    # results_pcs = {'result_CHI':[], 'result_UBI':[], 'result_CSCW':[], 'result_UIST':[]}
    # ori_file = open('../dataAug10/pcs.tsv')
    # ori_file = open('../dataAug10/pcs_mag_doi_pmid.tsv')
    # iter_f = iter(ori_file)
    # first_line = True
    # for row in iter_f:
    #     if first_line:
    #         first_line = False
    #         continue
    #     paperrow_str = str(row).split() # paper row
    #     paperid_str = paperrow_str[2]
    #     paperid = int(paperid_str)
    #     if paperid in data_HCI['paper_id'].values:
    #         results_pcs['result_{}'.format(conf_name_map[int(data_HCI.loc[data_HCI['paper_id']==paperid]['conf_id'].values)])].append(list(paperrow_str))

    # for name, result in results_pcs.items():
    #     result_pd = pd.DataFrame(data=result, columns=['reftype', 'confscore', 'paperid', 'patent', 'uspto', 'wherefound', 'doi', 'pmid', 'diff_month', 'selfciteconf_avg', 'selfciteconf_avgno0', 'selfciteconf_max'])
    #     result_pd.to_csv('papercitationscience_' + str(name) + '.tsv')
elif args.extract == "inventor":
    #------------ patent inventors -------------# data source:pcs/patent_dblpdata/patent_inventor.tsv
    from itertools import chain
    import pandas as pd
    patent_data_HCI = pd.read_csv('../dataAug10/papercitationscience_result.tsv',sep='\t')
    patent_data_HCI = patent_data_HCI.merge(data_HCI, left_index=True, right_index=True)
    patent_data_HCI.head(5)
    results_inventors = {'result_CHI':[], 'result_UBI':[], 'result_CSCW':[], 'result_UIST':[]}

    ori_patentinventors = pd.read_csv('../dataAug10/patent_inventor.tsv',skiprows=1)
    for row in ori_patentinventors.iterrows():
        patent_id = str(row[1]).split('    ')[1].split('\\t')[0]
        patentinventors_row = str(row[1]).replace("\"","").split('    ')[1].split('\n')[0].split('\\t')

        if paperid in data_HCI['paper_id'].values:
            results_inventors['result_{}'.format(conf_name_map[int(patent_data_HCI.loc[patent_data_HCI['paper_id']==paperid]['conf_id'].values)])].append(list(patentinventors_row))
            
    for name, result in results_inventors.items():
        result_pd = pd.DataFrame(data=result, columns=['patent_id', 'inventor_id', 'location_id'])
        result_pd.to_csv('patentinventors_' + str(name) + '.tsv')
    print(">>> done")
elif args.extract == "abstract":
    #------------ patent abstract -------------# data source: /data4/pcs/abstract/brf_sum_text.tsv
    from itertools import chain
    import pandas as pd
    results_abstract = {'result_CHI':[], 'result_UBI':[], 'result_CSCW':[], 'result_UIST':[]}

    ori_patent_abstract = pd.read_csv('../dataAug10/brf_sum_text.tsv', sep='\t', skiprows=1)
    pd.set_option("display.max_colwidth", 100000)
    for row in ori_patent_abstract.iterrows():
        uuid = str(row[1]).split('\n')[0].split()[1].strip("\n")
        patent_id = str(row[1]).split('\n')[1].split()[1].strip("\n")
        abstract = str(row[1]).split('\n')[2].split('         ')[1]
        patent_abstract_row = [uuid, patent_id, abstract]
        
        if paperid in data_HCI['paper_id'].values:
            results_abstract['result_{}'.format(conf_name_map[int(patent_data_HCI.loc[patent_data_HCI['paper_id']==paperid]['conf_id'].values)])].append(list(patent_abstract_row))

    for name, result in results_inventors.items():
        result_pd = pd.DataFrame(data=result, columns=['uuid', 'patent_id', 'abstract'])
        result_pd.to_csv('patent_abstract_' + str(name) + '.tsv')
    print(">>> done")
elif args.extract == "paperyearinventor":
    #------------ patent year -------------# data source:/patentsview/patent.tsv
    from itertools import chain
    import pandas as pd
    import os

    HCI_ori_pd = None
    for path,directory,files in os.walk('../dataAug10/patentinventors/'):
        # here, we have conf_id name of CHI, CSCW, UBI, UIST
        for file in files:
            ori_pd = pd.read_csv(os.path.join(path, file))
            conf_id = file[file.index('_') + 1:-4]
            # add conf_id property to patent data
            ori_pd['conf_id'] = conf_id
            if HCI_ori_pd is None:
                HCI_ori_pd = ori_pd
            else:
                HCI_ori_pd = pd.concat([HCI_ori_pd, ori_pd],axis=0)
    # extract patent year data
    print("start load")
    patent_pd = pd.read_csv('patent.tsv',sep='\t')
    # merge ori_conf_pd_map
    print("start merge")
    HCI_ori_pd = HCI_ori_pd.merge(patent_pd, left_on='patent_id', right_on='id')
    HCI_ori_pd.to_csv('patent_year_inventor.tsv')
    HCI_ori_pd.head(5)