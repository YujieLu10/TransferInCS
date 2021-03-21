import pandas as pd
import matplotlib.pyplot as plt

conf_key = ['CHI', 'CSCW', 'UBI', 'UIST']
ori_paperyear_conf = {}
ori_citingpatent_conf = {}

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


X_year = [i for i in range (1950, 2021)]

for conf, paperyear_map in paperyear_map_conf.items():
    Y_papercnt = [0] * 71
    Y_citingpatentcnt = [0] * 71
    Y_citedportion = [0.0] * 71

    citingpatent_map = citingpatent_map_conf[conf]
    citedpaper_map = citedpaper_map_conf[conf]
    for i in range (1950, 2021):
        if str(i) in paperyear_map.keys():
            Y_papercnt[i-1950] = len(paperyear_map[str(i)])
        if str(i) in citingpatent_map.keys():
            Y_citingpatentcnt[i-1950] = len(citingpatent_map[str(i)])    
        if str(i) in citedpaper_map.keys():
            Y_citedportion[i-1950] = len(citedpaper_map[str(i)]) / Y_papercnt[i-1950]
    plt.plot(X_year,Y_papercnt,color='r')
    plt.plot(X_year,Y_citingpatentcnt,color='g')
    plt.title('conference_{}'.format(conf))
    plt.savefig('analysis_{}.png'.format(conf))
    plt.close()
    plt.plot(X_year,Y_citedportion,color='b')
    plt.title('conference_{}'.format(conf))
    plt.savefig('analysis_portion_{}.png'.format(conf))