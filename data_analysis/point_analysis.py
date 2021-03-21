import pandas as pd
import matplotlib.pyplot as plt

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

citingpatent_map_conf = {}
citedpaper_map_conf = {}
for conf, df in ori_citingpatent_conf.items():
    citingpatent_map = {}
    citedpaper_map = {}
    inv_paperyear_map = inv_paperyear_map_conf[conf]
    for row in df.iterrows():
        paperid = str(row[1]).split(',')[0].split('\n')[0].split()[1] # paperid
        patentid = str(row[1]).split(',')[0].split('\n')[1].split()[1] # patentid
        # paperyear
        paperyear = inv_paperyear_map[paperid]
        if paperyear not in citingpatent_map.keys():
            citingpatent_map[paperyear] = []
        if paperyear not in citedpaper_map.keys():
            citedpaper_map[paperyear] = []  
        citingpatent_map[paperyear].append(patentid)
        # unique cited paper this year
        if paperid not in citedpaper_map[paperyear]:
            citedpaper_map[paperyear].append(paperid)
    citingpatent_map_conf[conf] = citingpatent_map
    citedpaper_map_conf[conf] = citedpaper_map

# citing paper
for item in conf_key:
    df = pd.read_csv('../new_extract_papercitations/papercited_{}.tsv'.format(item), usecols=[1,2])
    ori_citingpaper_conf[item] = df

citingpaper_map_conf = {}
for conf, df in ori_citingpaper_conf.items():
    citingpaper_map = {}
    inv_paperyear_map = inv_paperyear_map_conf[conf]
    for row in df.iterrows():
        citing_paperid = str(row[1]).split(',')[0].split('\n')[0].split()[1]
        cited_paperid = str(row[1]).split(',')[0].split('\n')[1].split()[1]
        # paperyear
        paperyear = inv_paperyear_map[cited_paperid]
        if paperyear not in citingpaper_map.keys():
            citingpaper_map[paperyear] = []
        citingpaper_map[paperyear].append(citing_paperid)
    citingpaper_map_conf[conf] = citingpaper_map

X_year = [i for i in range (1950, 2021)]

for conf, paperyear_map in paperyear_map_conf.items():
    Y_citingpatentcnt = [0] * 71
    Y_citingpapercnt = [0] * 71

    citingpatent_map = citingpatent_map_conf[conf]
    citingpaper_map = citingpaper_map_conf[conf]
    for i in range (1950, 2021):
        if str(i) in citingpatent_map.keys():
            Y_citingpatentcnt[i-1950] = len(citingpatent_map[str(i)])    
        if str(i) in citingpaper_map.keys():
            Y_citingpapercnt[i-1950] = len(citingpaper_map[str(i)])

    plt.plot(Y_citingpapercnt,Y_citingpatentcnt,'o',color='r')
    plt.title('conference_{}'.format(conf))
    plt.savefig('point_{}.png'.format(conf))
    plt.close()
    # plt.plot(X_year,Y_citedportion,color='b')
    # plt.title('conference_{}'.format(conf))
    # plt.savefig('analysis_portion_{}.png'.format(conf))