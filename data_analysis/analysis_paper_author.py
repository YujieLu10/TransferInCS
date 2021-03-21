import pandas as pd
import matplotlib.pyplot as plt

conf_key = ['CHI', 'CSCW', 'UBI', 'UIST']
ori_paperyear_conf = {}
ori_citingpatent_conf = {}
ori_author_conf = {}

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

# author
for item in conf_key:
    df = pd.read_csv('../paperauthororder_extracted/paperauthororder_{}.tsv'.format(item), usecols=[1,2])
    ori_author_conf[item] = df

cited_author_map_conf = {}
notcited_author_map_conf = {}
for conf, df in ori_author_conf.items():
    inv_paperyear_map = inv_paperyear_map_conf[conf]
    cited_author_map = {}
    notcited_author_map = {}
    cited_paper_list = citedpaper_list_conf[conf]
    for row in df.iterrows():
        paperid = str(row[1]).split(',')[0].split('\n')[0].split()[1]
        authorid = str(row[1]).split(',')[0].split('\n')[1].split()[1]
        paperyear = inv_paperyear_map[paperid]
        if paperid in cited_paper_list:
            if paperyear not in cited_author_map.keys():
                cited_author_map[paperyear] = []
            if authorid not in cited_author_map[paperyear]:
                cited_author_map[paperyear].append(authorid)
        else:
            if paperyear not in notcited_author_map.keys():
                notcited_author_map[paperyear] = []
            if authorid not in notcited_author_map[paperyear]:
                notcited_author_map[paperyear].append(authorid)
    cited_author_map_conf[conf] = cited_author_map
    notcited_author_map_conf[conf] = notcited_author_map

X_year = [i for i in range (1950, 2021)]

for conf, paperyear_map in paperyear_map_conf.items():
    Y_citedpaper_authorcnt = [0] * 71
    Y_notcitedpaper_authorcnt = [0] * 71

    cited_author_map = cited_author_map_conf[conf]
    notcited_author_map = notcited_author_map_conf[conf]
    for i in range (1950, 2021):
        if str(i) in cited_author_map.keys():
            Y_citedpaper_authorcnt[i-1950] = len(cited_author_map[str(i)])    
        if str(i) in notcited_author_map.keys():
            Y_notcitedpaper_authorcnt[i-1950] = len(notcited_author_map[str(i)])    

    plt.plot(X_year,Y_citedpaper_authorcnt,color='r')
    plt.plot(X_year,Y_notcitedpaper_authorcnt,color='g')
    plt.title('conference_{}'.format(conf))
    plt.savefig('comparison_analysis_{}.png'.format(conf))
    plt.close()