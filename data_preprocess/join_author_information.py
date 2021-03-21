from itertools import chain
import pandas as pd

ori_paperauthor = pd.read_csv('/data/pcs/paperauthororder.tsv', delimiter="\t", encoding='unicode_escape')
ori_authoridname = pd.read_csv('/data/pcs/authoridname_raw.tsv', delimiter="\t", encoding='unicode_escape')
# ori_papercitations = pd.read_csv('/data/pcs/papercitations.tsv', delimiter="\t", encoding='unicode_escape')
# ori_paperyear = pd.read_csv('/data/pcs/paperyear.tsv', error_bad_lines=False, skiprows=1, nrows=100)

paperyear_map = {} 
paper_by_year = [0] * 401
citation_by_year = [0] * 401

ori_file = open('/data/pcs/paperyear.tsv')
iter_f = iter(ori_file)
first_line = True
cnt = 0
for row in iter_f:
    cnt += 1
    if first_line:
        first_line = False
        continue
    paperid = str(row).split()[0] # paperid
    paperyear = str(row).split()[1]
    
    if paperyear not in paperyear_map.keys():
        paperyear_map[paperyear] = []    
    paperyear_map[paperyear].append(paperid)
    if cnt == 100:
        break

resultf = open("author_popularity.txt", "w")
# no user if they do not exist in paperauhor_order.tsv
print(">>> start iter authorid")
for author_row in ori_authoridname.iterrows():
    #authorid_raw = str(author_row[1]).split('\\t')[1].split("    ")[1]
    authorid_raw = str(author_row[1]).split('\n')[1].split("    ")[1]
    # TODO:sort by autorid
    current_paperlist = []
    # current_citinglist = []
    cnt = 0
    for paper_row in ori_paperauthor.iterrows():
        cnt += 1
        authorid = str(paper_row[1]).split('\n')[1].split()[1]
        if authorid == authorid_raw:
            paperid = str(paper_row[1]).split('\n')[0].split()[1]
            current_paperlist.append(paperid)
        if cnt == len(ori_paperauthor):
            # find citing paper list
            # for citation_row in ori_papercitations.iterrows():
            # citing_paperid = str(citation_row[1]).split('\n')[0].split()[1]
            # cited_paperid = str(citation_row[1]).split('\n')[1].split()[1]
            #     if cited_paperid in current_paperlist:
            #         current_citinglist.append(citing_paperid)
            # find year
            for year, paper_list in paperyear_map.items():
                paper_by_year[int(year) - 1800] += len([i for i in current_paperlist if i in paper_list])
                # citation_by_year[int(year) - 1800] += len([i for i in current_citinglist if i in paper_list])
            # write author paper_by_year vector
            resultf.write(authorid_raw + '\t')
            resultf.write(','.join([str(elem) for elem in paper_by_year]))
            resultf.write('\t' + ','.join([str(elem) for elem in citation_by_year]))
            resultf.write('\n')
            # initializing for next author
            paper_by_year = [0] * 401
            citation_by_year = [0] * 401
            current_paperlist = []
            # current_citinglist = []
