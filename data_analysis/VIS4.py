import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

conf_key = ['CHI', 'CSCW', 'UBI', 'UIST']
ori_paperyear_conf = {}
ori_citingpatent_conf = {}
ori_citingpaper_conf = {}

for item in conf_key:
    df = pd.read_csv('../paperyear_extracted/paperyear_result_{}.tsv'.format(item), usecols=[1,2])
    ori_paperyear_conf[item] = df

paperyear_map_conf = {}
inv_paperyear_map_conf = {}
for conf, df in ori_paperyear_conf.items():
    paperyear_map = {}
    inv_paperyear_map = {}
    for row in df.iterrows():
        paperid = str(row[1]).split(',')[0].split('\n')[0].split()[1] # paperid
        paperyear = str(row[1]).split(',')[0].split('\n')[1].split()[1] # paperyear 
        if paperyear not in paperyear_map.keys():
            paperyear_map[paperyear] = []    
        if paperid not in paperyear_map[paperyear]:
            paperyear_map[paperyear].append(paperid)
        inv_paperyear_map[paperid] = paperyear
    paperyear_map_conf[conf] = paperyear_map
    inv_paperyear_map_conf[conf] = inv_paperyear_map

# citing patent
for item in conf_key:
    df = pd.read_csv('../papercitation2science_extracted/papercitationscience_result_{}.tsv'.format(item), usecols=[3,4])
    ori_citingpatent_conf[item] = df

citedpaper_list_conf = {}
for conf, df in ori_citingpatent_conf.items():
    citedpaper_list = []
    for row in df.iterrows():
        paperid = str(row[1]).split(',')[0].split('\n')[0].split()[1] # paperid
        # patentid = str(row[1]).split(',')[0].split('\n')[1].split()[1] # patentid
        citedpaper_list.append(paperid)
    citedpaper_list_conf[conf] = citedpaper_list

# citing paper
for item in conf_key:
    df = pd.read_csv('../new_extract_papercitations/papercited_{}.tsv'.format(item), usecols=[1,2])
    ori_citingpaper_conf[item] = df

cited_citingpaper_map_conf = {}
notcited_citingpaper_map_conf = {}

cited_paper_map_conf = {}
notcited_paper_map_conf = {}

for conf, df in ori_citingpaper_conf.items():
    cited_citingpaper_map = {}
    notcited_citingpaper_map = {}
    cited_paper_map = {}
    notcited_paper_map = {}
    cited_paper_list = citedpaper_list_conf[conf]
    inv_paperyear_map = inv_paperyear_map_conf[conf]
    for row in df.iterrows():
        citing_paperid = str(row[1]).split(',')[0].split('\n')[0].split()[1]
        cited_paperid = str(row[1]).split(',')[0].split('\n')[1].split()[1]
        # paperyear
        paperyear = inv_paperyear_map[cited_paperid]
        if cited_paperid in cited_paper_list:
            if paperyear not in cited_citingpaper_map.keys():
                cited_citingpaper_map[paperyear] = []
            if paperyear not in cited_paper_map.keys():
                cited_paper_map[paperyear] = {}
            if cited_paperid not in cited_paper_map[paperyear].keys():
                cited_paper_map[paperyear][cited_paperid] = []
            if citing_paperid not in cited_paper_map[paperyear][cited_paperid]:
                cited_paper_map[paperyear][cited_paperid].append(citing_paperid)
            # if citing_paperid not in cited_citingpaper_map[paperyear]:
            cited_citingpaper_map[paperyear].append(citing_paperid)
        else:
            if paperyear not in notcited_citingpaper_map.keys():
                notcited_citingpaper_map[paperyear] = []
            if paperyear not in notcited_paper_map.keys():
                notcited_paper_map[paperyear] = {}
            if cited_paperid not in notcited_paper_map[paperyear].keys():
                notcited_paper_map[paperyear][cited_paperid] = []
            if citing_paperid not in notcited_paper_map[paperyear][cited_paperid]:
                notcited_paper_map[paperyear][cited_paperid].append(citing_paperid)
            # if citing_paperid not in notcited_citingpaper_map[paperyear]:
            notcited_citingpaper_map[paperyear].append(citing_paperid)
    cited_citingpaper_map_conf[conf] = cited_citingpaper_map
    notcited_citingpaper_map_conf[conf] = notcited_citingpaper_map
    cited_paper_map_conf[conf] = cited_paper_map
    notcited_paper_map_conf[conf] = notcited_paper_map
    
X_year = [i for i in range (1950, 2021)]

for conf, paperyear_map in paperyear_map_conf.items():
    Y_citedpaper_citation_std = [0.0] * 71
    Y_notcitedpaper_citation_std = [0.0] * 71
    Y_citedpaper_citation_cnt= [0] * 71
    Y_notcitedpaper_citation_cnt = [0] * 71
    cited_totalcitation = 0
    notcited_totalcitation = 0

    cited_citingpaper_map = cited_citingpaper_map_conf[conf]
    notcited_citingpaper_map = notcited_citingpaper_map_conf[conf]
    cited_paper_map = cited_paper_map_conf[conf]
    notcited_paper_map = notcited_paper_map_conf[conf]
    for i in range (1950, 2021):
        if str(i) in cited_citingpaper_map.keys():
            Y_citedpaper_citation_cnt[i-1950] = len(cited_citingpaper_map[str(i)])
            cited_totalcitation += len(cited_citingpaper_map[str(i)])
        if str(i) in notcited_citingpaper_map.keys():
            Y_notcitedpaper_citation_cnt[i-1950] = len(notcited_citingpaper_map[str(i)])
            notcited_totalcitation += len(notcited_citingpaper_map[str(i)])

    for i in range (1950, 2021):
        if str(i) in cited_paper_map.keys():
            citing_list = []
            for key,val in cited_paper_map[str(i)].items():
                citing_list.append(len(val))
            # print(">>> cited conf{} list{}".format(conf, citing_list))
            Y_citedpaper_citation_std[i-1950] = np.std(citing_list)
        if str(i) in notcited_paper_map.keys():
            citing_list = []
            for key,val in notcited_paper_map[str(i)].items():
                citing_list.append(len(val))
            # print(">>> notcited conf{} list{}".format(conf, citing_list))
            Y_notcitedpaper_citation_std[i-1950] = np.std(citing_list)

    plt.plot(Y_citedpaper_citation_cnt,Y_citedpaper_citation_std,'o',color='r')
    plt.plot(Y_notcitedpaper_citation_cnt,Y_notcitedpaper_citation_std,'o',color='g')
    plt.title('vis4_conference_{}'.format(conf))
    plt.savefig('vis4_analysis_{}.png'.format(conf))
    plt.close()