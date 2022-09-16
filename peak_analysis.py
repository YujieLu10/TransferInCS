import pandas as pd
from icecream import ic
# hci_paperids_df = pd.read_csv('data_analysis/df_paper_pc2s_year_filtered.tsv', sep=',')
# hci_paperids_df = hci_paperids_df.groupby(["magid"]).first().reset_index()
# hci_paperids_df = hci_paperids_df.drop_duplicates()

# df_patent_paper_year = pd.read_csv("data_analysis/df_patent_paper_year_filtered.tsv")
# df_patent_paper_year = df_patent_paper_year.drop_duplicates()
# df_patent_paper_year = df_patent_paper_year.groupby(["magid", "patent_id"]).first().reset_index()
# # df_temp = df_patent_paper_year[df_patent_paper_year['patent_year']>1985].groupby(['patent_id','patent_year','conf_id'])['patent_paper_lag'].agg('min').reset_index()
# df_temp = df_patent_paper_year[df_patent_paper_year['year']>1985].groupby(['magid','year','conf_id'])['patent_paper_lag'].agg('min').reset_index()

# df_peak_year = pd.read_csv("df_citedpaper_peakyear_filtered.tsv")
# df_peak_year = df_peak_year.loc[df_peak_year["mag_id"].isin(df_temp["magid"].to_list())]
# ic(len(df_peak_year))
# df_temp = df_temp.drop_duplicates()
# df_temp = df_temp.groupby(["magid"]).first().reset_index()
# df_temp = df_temp.loc[df_temp["magid"].isin(df_peak_year["mag_id"].to_list())]
# ic(len(df_temp))

# df_ttest = df_peak_year.merge(df_temp, left_on="mag_id", right_on="magid")
df_ttest = pd.read_csv("df_ttest.tsv")
df_ttest = df_ttest.loc[df_ttest["peak_year_lag"]>=0]
ic(len(df_ttest))
most_recent_lag_list = df_ttest["patent_paper_lag"].to_list()
peak_lag_list = df_ttest["peak_year_lag"].to_list()
import scipy.stats as stats
# ic(most_recent_lag_list[:10], peak_lag_list[:10])
import numpy as np
ic(np.asarray(most_recent_lag_list).mean())
ic(np.asarray(peak_lag_list).mean())
ic(stats.ttest_rel(most_recent_lag_list, peak_lag_list))