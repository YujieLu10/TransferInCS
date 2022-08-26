import pandas as pd


def get_confid(x):
    if str(x) == "1163450153": return "CHI"
    if str(x) == "1195049314": return "CSCW"
    if str(x) == "1171345118": return "UBI"
    if str(x) == "1166315290": return "UIST"
    return x
    
df = pd.read_csv('mergeversiondata/patent_information_HCI.tsv')["conf_id"].apply(get_confid)
df.to_csv('mergeversiondata/patent_information_HCI.tsv')
# HCI_papercitationscience_pd["patent"] = HCI_papercitationscience_pd["patent"].apply(get_patentid)
