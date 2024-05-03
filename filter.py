import pandas as pd
HCI_filter_df_paperid = pd.read_csv('filtered_HCI_papers.csv', sep=',')
white_list = HCI_filter_df_paperid['mag_id'].tolist()

# df_paper_year = pd.read_csv("data_analysis/df_paper_year.tsv")
# df_patent_paper_year = pd.read_csv("data_analysis/df_patent_paper_year.tsv")
# df_paper_pc2s_year = pd.read_csv("data_analysis/df_paper_pc2s_year.tsv")
# df_patent_paper_year = pd.read_csv("data_analysis_no_researcher/df_patent_paper_year.tsv")
# df_paper_pc2s_year = pd.read_csv("data_analysis_no_researcher/df_paper_pc2s_year_no_researcher.tsv")
# df_patent_paper_year = pd.read_csv("data_analysis_non_self_cite/df_patent_paper_year.tsv")
# df_paper_pc2s_year = pd.read_csv("data_analysis_non_self_cite/df_paper_pc2s_year_non_self_cite.tsv")
df_patent_paper_year = pd.read_csv("data_analysis_sigchi/df_patent_paper_year.tsv")
df_paper_pc2s_year = pd.read_csv("data_analysis_sigchi/df_paper_pc2s_year_non_self_cite.tsv")

# df_paper_year = df_paper_year[df_paper_year.paper_id.isin(white_list)]
df_patent_paper_year = df_patent_paper_year[df_patent_paper_year.magid.isin(white_list)]
df_paper_pc2s_year = df_paper_pc2s_year[df_paper_pc2s_year.magid.isin(white_list)]


# df_paper_year.to_csv("data_analysis/df_paper_year_filtered.tsv")
# df_patent_paper_year.to_csv("data_analysis/df_patent_paper_year_filtered.tsv")
# df_paper_pc2s_year.to_csv("data_analysis/df_paper_pc2s_year_filtered.tsv")
# df_patent_paper_year.to_csv("data_analysis_no_researcher/df_patent_paper_year_filtered.tsv")
# df_paper_pc2s_year.to_csv("data_analysis_no_researcher/df_paper_pc2s_year_no_researcher_filtered.tsv")
# df_patent_paper_year.to_csv("data_analysis_non_self_cite/df_patent_paper_year_filtered.tsv")
# df_paper_pc2s_year.to_csv("data_analysis_non_self_cite/df_paper_pc2s_year_non_self_cite_filtered.tsv")
df_patent_paper_year.to_csv("data_analysis_sigchi/df_patent_paper_year_filtered.tsv")
df_paper_pc2s_year.to_csv("data_analysis_sigchi/df_paper_pc2s_year_non_self_cite_filtered.tsv")
